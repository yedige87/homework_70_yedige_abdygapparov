from django.urls import path

from webapp.views.todos import ToDoDetail, ToDoUpdateView, ToDoCreateView, ToDoDeleteView, ProjectTasksView, \
    ProjectsView, ProjectCreateView, ProjectToDoCreateView, ProjectUpdateView, ProjectUsersUpdateView, \
    ProjectDeleteView, ProjectDetail
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo/add/', ToDoCreateView.as_view(), name='todo_add'),
    path('todo/<int:pk>', ToDoDetail.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/confirm_delete/', ToDoDeleteView.as_view(), name='confirm_delete'),
    path('project/<int:project_id>', ProjectTasksView.as_view(), name='project_detail'),
    path('projects/', ProjectsView.as_view(), name='projects_view'),
    path('project/add', ProjectCreateView.as_view(), name='project_add'),
    path('project/add/<int:pk>', ProjectToDoCreateView.as_view(), name='todo_project_add'),
    path('project/edit/<int:pk>', ProjectUpdateView.as_view(), name='project_edit'),
    path('project/users_update/<int:pk>', ProjectUsersUpdateView.as_view(), name='project_users'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/confirm_delete/', ProjectDeleteView.as_view(), name='project_confirm_delete'),
    path('project/view/<int:pk>', ProjectDetail.as_view(), name='project_view'),
]