from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user,name="login_user"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('input_data',views.input_data,name="input_data"),
    path('show_data',views.show_data,name="show_data"),
    path('update/<int:id>',views.user_update,name="update"),
    path('delete/<id>',views.user_delete,name="delete"),
    path('input_ai_data',views.input_ai_data,name="input_ai_data"),

]

