from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('tasks/<int:pk>/delete', views.TaskDelete.as_view(), name='task_delete')
]