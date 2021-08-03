from django.urls.resolvers import URLPattern
from .views import say_hello_views, input_show_name_views,copy_names_views
from django.urls import path

urlpatterns=[
    path('/say_hello',say_hello_views),
    path('/input',input_show_name_views),
    path('/copy_names', copy_names_views),
] 
