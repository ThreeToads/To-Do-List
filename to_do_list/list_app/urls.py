from django.contrib.auth.views import LoginView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from list_app.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='tokens_obtain_pair'),
    path('tasks/create', TaskCreateView.as_view(), name='task-create_new'),
    path('tasks/', TaskListView.as_view(), name='task-list-view'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail-view'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update-view'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete-view'),
]

