from django.urls import path
from todolist_app import views

urlpatterns = [
    path('todolist', views.todolist, name = 'todolist'),
    path('todolist/delete/<task_id>', views.delete_task, name = 'delete_task' ),
    path('todolist/edit/<task_id>', views.edit_task, name = 'edit_task'),
    path('todolist/mark_task/<task_id>', views.mark_task, name = 'mark_task'),
    

]
