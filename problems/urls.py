from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('<int:problem_id>/', views.editor, name='editor'),
    path('compile/', views.compile, name='compile'),
]