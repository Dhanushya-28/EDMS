from django.shortcuts import render, redirect
from .forms import EmployeeForm,RegisterForm
from django.http import HttpResponse
import requests 
from datetime import date


BACKEND_URL = "http://127.0.0.1:8080/"



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # You can handle form data here (e.g., save to the database)
            # For now, we just redirect to a success page
            payload = form.cleaned_data
            res = requests.post(BACKEND_URL+"register/", json=payload)
            if res.status_code == 201:
                return redirect("login_view")
            return HttpResponse(f"API Error: {res.text}", status=res.status_code)
        return HttpResponse(f"Form Error: {form.errors}")
        # return HttpResponse("Registration successful!")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        response = requests.post("http://127.0.0.1:8080/login/", json={'username': username, 'password': password})
        if response.status_code == 200:
            return redirect('home_view')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request,'login.html')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def view_view(request):
    requestObj = requests.get(BACKEND_URL+"list/")
    data = requestObj.json()
    return render(request, 'view.html', {"employeeList": data})


def employee_form(request):
    departmentChoices = get_departments(request)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.fields["departmentId"].choices = departmentChoices
        if form.is_valid():
            # You can handle form data here (e.g., save to the database)
            # For now, we just redirect to a success page
            payload = form.cleaned_data
            if isinstance(payload['dateOfJoin'], date):
                payload['dateOfJoin'] = payload['dateOfJoin'].isoformat() # convert from datetime.date(2019, 2, 27) into '2019-02-27'
            res = requests.post(BACKEND_URL+"add/", json=payload)
            if res.status_code == 201:
                return redirect("view_view")
            return HttpResponse(f"API Error: {res.text}", status=res.status_code)
        return HttpResponse(f"Form Error: {form.errors}")
        # return HttpResponse("Registration successful!")
    else:
        form = EmployeeForm()
        form.fields["departmentId"].choices = departmentChoices
    return render(request, 'forms.html', {'form': form})

def edit_employee(request, id):
    departmentChoices = get_departments(request)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.fields["departmentId"].choices = departmentChoices
        if form.is_valid():
            payload = form.cleaned_data
            if isinstance(payload['dateOfJoin'], date):
                payload['dateOfJoin'] = payload['dateOfJoin'].isoformat()
            res = requests.put(BACKEND_URL+f"edit/{id}/", json=payload)
            if res.status_code == 200:
                return redirect("view_view")
            return HttpResponse(f"API Error: {res.text}", status=res.status_code)
        return HttpResponse(f"Form Error: {form.errors}")
    else:
        requestObj =requests.get(BACKEND_URL+f"details/{id}/")
        jsonData = requestObj.json()
        form = EmployeeForm(initial=jsonData)
        print(departmentChoices)
        form.fields["departmentId"].choices = departmentChoices
        return render(request, "forms.html", {"form": form})

def delete_employee(request, id):
    if request.method == "POST":
        print(id)
        res = requests.delete(BACKEND_URL+f"delete/{id}/")
        if res.status_code == 200:
            return redirect('view_view')
        return HttpResponse(f"API Error: {res.text}")
    

def get_departments(request):
    requestObj = requests.get(f"http://127.0.0.1:8080/AllDepartment/")
    print(requestObj.json())
    if requestObj.status_code == 200:
        data = requestObj.json()
    else:
        data = []
    print(data)
    departmentChoices = []
    for item in data:
        departmentChoices.append((item["departmentId"], item["departmentName"]))
    return departmentChoices
    
def contact_view(request):
    return render(request, 'contact.html')





