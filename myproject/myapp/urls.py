from django.urls import path
from .views import add_employee, get_all_employees, get_employee_by_id, update_employee, delete_employee,add_user,get_user

urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('get_all_user/', get_user, name='get_all_user'),
    path('add_employee/', add_employee, name='add_employee'),
    path('get_all_employees/', get_all_employees, name='get_all_employees'),
    path('get_employee_by_id/<int:pk>/', get_employee_by_id, name='get_employee_by_id'),
    path('update_employee/<int:pk>/', update_employee, name='update_employee'),
    path('delete_employee/<int:pk>/', delete_employee, name='delete_employee'),
]