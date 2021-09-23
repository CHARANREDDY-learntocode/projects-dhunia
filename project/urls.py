from django.urls import path

from .views import (ProjectListView, ProjectDetailView,
    ProjectCreateView, ProjectUpdateView, ProjectDestroyView,
    UserProjectListView, MyProjectListView,
)


urlpatterns = [
    path('project/', ProjectListView.as_view(), name='projects-all'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/delete/<int:pk>/', ProjectDestroyView.as_view(), name='project-delete'),
    path('project/my-projects/', MyProjectListView.as_view(), name='projects-self_projects'),
    path('project/<str:email>/', UserProjectListView.as_view(), name='projects-by_user'),
]