from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

app_name = 'rhymesapp'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('audio_list', views.audio_list, name='audio_list'),
    path('nurseryList', views.nurseryList, name='nurseryList'),
    path('account_information', views.infoView, name='account_information'),
    path('nurseryPage', views.nurseryPage, name='nurseryPage'),
    path('upgrade', views.upgrade, name='upgrade'),
    path('account_created', views.account_created, name='account_created'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^register/account_created/$', views.account_created, name='account_created'),
    path('email/', views.emailView, name='email'),
    url(r'^email/success/$', views.success, name='success'),
    url(r'^account_information/$', views.infoView, name='edit_profile'),
    url(r'^account_information/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^login/reset_password/$', PasswordResetView.as_view(), {'template_name': 'rhymesapp/reset_password.html'}, name='PasswordResetView'),
    url(r'^login/reset_password/done/$', PasswordResetDoneView.as_view(), name='PasswordResetDoneView'),
    url(r'^login/reset_password/confirm/$',PasswordResetConfirmView.as_view(), name='PasswordResetConfirmView'),

]
# (?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/

