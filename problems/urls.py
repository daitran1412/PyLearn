from django.urls import path
from . import views

urlpatterns = [
    path('<int:problem_id>/', views.editor, name='editor'),
    path('run/', views.run, name='run'),
]