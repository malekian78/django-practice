from celery import shared_task
from time import sleep
from todo.models import Task

@shared_task
def DeleteCompletedTask():
    completedTask = Task.objects.filter(complete=True)
    print(completedTask)
    sizeOfcompletedTask = len(completedTask)
    if sizeOfcompletedTask > 0:
        print("try to remove ({})".format(completedTask[sizeOfcompletedTask-1]))
        completedTask[sizeOfcompletedTask-1].delete()
        print("one completed Task was removed.")
    else:
        print("no completed task found.")

