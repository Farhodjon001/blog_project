from .views import blog_list_view
from django.urls import path
urlpatterns=[
    path("",blog_list_view,name='blog_list_view')
]