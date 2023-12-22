from django.urls import  path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('welcome/',views.welcome,name='welcome'),
    path('forms/',views.form,name='form'),
    path('logout/',views.logout,name='logout'),
    path('branches/',views.getbranches,name='branches'),
    path('success/',views.success,name='success'),

]