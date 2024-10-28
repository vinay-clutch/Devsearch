from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.Projects, name="Projects"),
    path("Projects/<str:pk>", views.project, name="Project"),
    path("create/", views.CreateProject, name="CreateProject"),
    path('update_project/<str:pk>',views.UpdateProject,name='update_project'),
    path('delete_project/<str:pk>',views.DeleteProject,name='delete_project'),
]
