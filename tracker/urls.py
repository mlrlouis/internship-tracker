from django.urls import path
from . import views

urlpatterns = [
        path('', views.company_list, name='company_list'),
        path('delete/<int:application_id>', views.delete_application, name='delete_application'),
        path('edit/<int:application_id>', views.edit_application, name='edit_application')
]