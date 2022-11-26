
from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic import TemplateView
# from web.views import ContributeView

app_name='web'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('projects/cio4good', views.CIO4GoodView.as_view(), name='cio4good'),
    path('projects/chetah', views.ChetahView.as_view(), name='chetah'),
    path('api/chetah/v1/<str:query>', views.chetah_search)
]