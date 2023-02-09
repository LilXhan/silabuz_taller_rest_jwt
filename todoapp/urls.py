from django.urls import path 
from rest_framework import routers

from . import api

router = routers.DefaultRouter()

router.register('todo', api.TodoViewSet, basename='todo')

urlpatterns = [
    path('todo/getAll/function/', api.todo_get_all, name='getAll_function'),
    path('todo/getAll/', api.TodoGetAll.as_view(), name='getAll'),
    path('todo/delAll/function/', api.todo_del_all, name='delAll_function'),
    path('todo/delAll/', api.TodoDelAll.as_view(), name='delAll'),
    path('todo/twoTasks/', api.GetTwoTasks.as_view(), name='getTwoTasks')
]

urlpatterns += router.urls