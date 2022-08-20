from django.urls import path

from webhook import views

app_name = 'webhook'

urlpatterns = [
    path('', views.webhook, name='webhook'),
]
