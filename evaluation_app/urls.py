from django.urls import path

from evaluation_app import views

# from evaluation_app import views

urlpatterns = [
    path('',views.front_page,name='front_page'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login_view',views.login_view,name='login_view'),
    path('user_reg',views.user_reg,name='user_reg'),
    path('publisher_reg',views.publisher_reg,name='publisher_reg'),
]