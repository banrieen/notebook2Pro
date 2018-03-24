# -*- coding: UTF-8 -*-

'''
Created on 2018年3月22日

@author: lizhen
'''
from django.urls import path
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        ]
