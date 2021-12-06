from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_day>', views.get_todo_week_every_day_by_number),
    path('<str:sign_day>/', views.todo_week_every_day, name='week-name'),
]