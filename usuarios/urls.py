from django.urls import path
from . import views
from .views import register_view
from django.http import HttpResponse

app_name = 'usuarios'

urlpatterns = [
    path('criar/', views.register_view , name='criar'),

]
