from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('add/',add_employee,name='add_employee'),
    path('list/',employees_list,name='employees_list'),
    path('edit/<int:id>/',edit_employee,name='edit_employee'),
    path('details/<int:id>/',employees_details,name='employees_details'),
    path('delete/<int:id>/',delete_employee,name='delete_employee'),
    path('AllDepartment/', all_department),
    path('createDepartment/',create_department)
]