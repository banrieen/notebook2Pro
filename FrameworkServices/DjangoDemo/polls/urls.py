""" Polls URLconf 
# 将 URL 映射到 view
# 并在全局URLconf中指定 polls.urls
 """

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index')
]