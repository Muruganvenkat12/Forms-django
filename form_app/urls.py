from django.urls import path

from form_app.views import register, success

urlpatterns = [
    path('', register, name='register'),
    path('success/', success, name='success')
]
