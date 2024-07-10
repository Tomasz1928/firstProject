from toDoList.models import Task


def get_all_data_from_DB():
    task_list = []
    tasks = Task.objects.all()
    for task in tasks:
        task_list.append({'name': task.name, 'description': task.description, 'id': task.id})

    return task_list


def get_element_by_id(ids):
     task = Task.objects.get(id=ids)
     return {'name': task.name, 'description': task.description, 'id': task.id}


def add_record_to_DB(name, description):
    new_task = Task(name=name, description=description)
    new_task.save()


def remove_record_from_DB(ids):
    task = Task.objects.get(id=ids)
    task.delete()


def update_record_in_DB(ids, **kwargs):
    task = Task.objects.get(id=int(ids))
    if 'name' in kwargs != '':
        task.name = kwargs['name']
    if 'description' in kwargs != '':
        task.description = kwargs['description']
    task.save()


