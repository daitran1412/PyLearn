from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path("problems/", views.problems, name="problems"),
    path('problems/<int:problem_id>/', views.editor, name='editor'),
    path('problems/save/', views.save, name='save'),
    path('problems/run/', views.run, name='run'),
]
