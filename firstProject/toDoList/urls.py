from django.urls import path

from toDoList import views

urlpatterns = [
    path('task/', views.task_view, name='main_task_views'),
    path('task/details/', views.task_details_view, name='task_details_view'),
    path('task/delete/', views.delete_task, name='delete_tasks'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/update/', views.update_task, name='update_task')
]