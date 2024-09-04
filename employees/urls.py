from django.urls import path

from employees.apps import EmployeesConfig
from employees.views import EmployeeListAPIView, EmployeeCreateAPIView, \
    EmployeeDestroyAPIView, EmployeeRetrieveAPIView, \
    EmployeeUpdateAPIView, EmployeeActiveTaskListAPIView

app_name = EmployeesConfig.name


urlpatterns = [
    path('', EmployeeListAPIView.as_view(), name='employee_list'),
    path('create/', EmployeeCreateAPIView.as_view(), name='employee_create'),
    path('<int:pk>/update/', EmployeeUpdateAPIView.as_view(), name='employee_update'),
    path('<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employee_view'),
    path('<int:pk>/delete/', EmployeeDestroyAPIView.as_view(), name='employee_delete'),
    path('active/', EmployeeActiveTaskListAPIView.as_view(), name='employee_list_active_task')
]
