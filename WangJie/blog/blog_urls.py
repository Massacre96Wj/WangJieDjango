# -*- coding: UTF-8 -*-
"""
@Author ：WangJie
@Date   ：2020/12/3 21:36 
@Desc   ：
"""

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
]