from django.urls import path
from . import views as views


urlpatterns = [
    path('user_login/',views.user_login),

]
