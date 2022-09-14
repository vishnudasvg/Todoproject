from django.urls import path
from . import views

urlpatterns = [
    path('task', views.task_view, name='task_view'),
    path('', views.task_view, name='task_view'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvtask/',views.TaskListview.as_view(),name='cbvtask')

]
