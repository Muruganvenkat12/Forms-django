from django.urls import path

from form_app.views import register

urlpatterns = [
    path('', register, name='register'),
]
