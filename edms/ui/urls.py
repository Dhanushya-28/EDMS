from django.urls import path
from .views import *

urlpatterns = [   
    path('home/',home_view,name='home_view'),
    path('about/',about_view, name='about_view'),
    path('contact/',contact_view, name='contact_view'),
    path('register/',register_view,name ='register_view'),
    path('',login_view,name ='login_view'),
    path('view/',view_view, name="view_view"),
    path('add/',employee_form, name="employee_form"),
    path('edit/<int:id>/',edit_employee, name="edit_employee"),
    path('delete/<int:id>/',delete_employee, name="delete_employee")
]