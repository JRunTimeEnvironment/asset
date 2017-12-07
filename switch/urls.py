# -*- coding:utf-8 -*-
__author__ = 'jummy'

from django.conf.urls import url,include
from .views import shebei, dates,forms, warrantyDevice,Storage,Network,index,update,downloadfroms

urlpatterns=[
    #url(r'',index,name='index'),
    url(r'^dates',dates,name='dates'),
    url(r'^shebei',shebei,name='shebei'),
    url(r'^froms',forms,name='forms'),
    url(r'^warranty',warrantyDevice,name='warranty'),
    url(r'^storage',Storage,name='Storage'),
    url(r'^networl',Network,name='Network'),
    url(r'^update',update,name='update'),
    url(r'^downloadfroms',downloadfroms,name='downloadfroms'),
]


