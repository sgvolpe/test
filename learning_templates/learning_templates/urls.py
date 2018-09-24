from django.conf.urls import patterns, include, url
from django.contrib import admin
from basic_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learning_templates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basic_app/', include('basic_app.urls')),
    url(r'^logout/', views.user_logout, name='user_logout'),
    url(r'^special/', views.special, name='special'),
)
