from django.urls import path
from . import views as views

urlpatterns = [
    path('post_list1/',views.post_list1),
    path('post_list2/',views.post_list2),
    path('post_list3/',views.post_list3)
]
