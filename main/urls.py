from django.urls import path, re_path

from . import views

app_name = 'main'

urlpatterns = [
    path('favicon.ico', views.PageNotFoundView.as_view(), name='404'),
    re_path(r'.*', views.IndexView.as_view(), name='index')
]
