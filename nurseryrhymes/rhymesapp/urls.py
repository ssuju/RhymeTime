from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'rhymesapp'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('audio_list', views.audio_list, name='audio_list'),
    path('account_information', views.account_information, name='account_information'),
    path('nurseryList', views.nurseryList, name='nurseryList'),
    path('nurseryPage', views.nurseryPage, name='nurseryPage'),
    path('register', views.register, name='register'),
    path('upgrade', views.upgrade, name='upgrade'),
    path('account_created', views.account_created, name='account_created'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^register/account_created/$', views.account_created, name='account_created'),
    path('email/', views.emailView, name='email'),
    url(r'^email/success/$', views.success, name='success'),
]


