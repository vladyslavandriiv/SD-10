# polls/urls.py
from django.urls import path
from .views import register_view

app_name = 'polls'   # рекомендовано, щоб уникнути колізій імен

urlpatterns = [
    path('register/', register_view, name='register'),
    # сюди пізніше можна додати інші маршрути з polls
]
