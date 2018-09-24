from django.conf.urls import patterns, include, url
from basic_app import views

#template tagging
app_name = 'basic_app'


urlpatterns = patterns('',

    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
    url(r'^new_user_form/$', views.new_user_form, name='new_user_form'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^date_generator_form/$', views.date_generator_form, name='date_generator_form'),


)
