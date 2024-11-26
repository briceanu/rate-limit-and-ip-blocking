from django.urls import path
from . import views


urlpatterns = [
    path('list_create',views.PostCarAPI.as_view(),name='list_create')
]