from django.shortcuts import render, redirect
from toDoList import dbHelper

# Create your views here.

TASK = [{'name': 'task1', 'description': ' to jest task nr1', 'id': 1},
        {'name': 'task2', 'description': ' to jest task nr2', 'id': 2},
        {'name': 'task3', 'description': ' to jest task nr3', 'id': 3},
        {'name': 'task4', 'description': ' to jest task nr4', 'id': 4},
        {'name': 'task5', 'description': ' to jest task nr5', 'id': 5}]


def task_view(request):
    task = dbHelper.get_all_data_from_DB()
    return render(request, 'toDoList/main_task_view.html', {'task': task})


def task_details_view(request):
    task_ids = request.POST.getlist("task_ids")
    task_to_show = []
    for x in task_ids:
       task_to_show.append(dbHelper.get_element_by_id(int(x)))

    return render(request, 'toDoList/task_details_view.html', {'task': task_to_show})


def delete_task(request):
    task_ids = request.POST.getlist("task_ids")
    for x in task_ids:
        dbHelper.remove_record_from_DB(int(x))

    return redirect('main_task_views')


def create_task(request):
    data = request.POST
    dbHelper.add_record_to_DB(data['task_name'], data['task_description'])
    return redirect('main_task_views')


def update_task(request):
    data = request.POST
    print(data)
    dbHelper.update_record_in_DB(data["task_id"],name=data['new_task_name'], description=data['new_task_name'])
    return redirect('main_task_views')