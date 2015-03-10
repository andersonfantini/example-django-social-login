# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'login.views.login'),    
    url(r'^entrar/', 'login.views.login', name='login'),
    url(r'^home/', 'login.views.home', name='home'),
    url(r'^logout/', 'login.views.logout_user', name='logout'),    
    url(r'^cadastro/', 'login.views.criar_usuario', name='cadastro'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    
)
