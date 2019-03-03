from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # トップページにアクセスがあった場合、views.pyでindexアクションをお呼び出す。
]
