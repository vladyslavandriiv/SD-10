# mysite/urls.py
from django.contrib import admin
from django.urls import path, include           # <-- include має бути тут
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('polls/', include('polls.urls')),      # <-- Ось правильний запис
]
