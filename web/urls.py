
from django.urls import path
from django.contrib import admin
from . import views

app_name='web'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('projects/cio4good', views.CIO4GoodView.as_view(), name='cio4good'),
    path('projects/chetah', views.ChetahView.as_view(), name='chetah'),
    path('projects/simex', views.SimexView.as_view(), name='simex'),
    path('api/chetah/v1/<str:query>', views.chetah_search, name='chetah_v1_api')
]