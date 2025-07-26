from django.contrib import admin
from django.urls import path
from tasks.views import task_list, task_detail, task_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', task_list, name='task_list'),               
    path('tasks/<int:pk>/', task_detail, name='task_detail'),  
    path('tasks/create/', task_create, name='task_create'),    
]
