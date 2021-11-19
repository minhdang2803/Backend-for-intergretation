"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from movie import views
from movie.models import HeThongRap
from . import settings
from project1.settings import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/QuanLyPhim/LayDanhSachPhim', views.QuanLyPhimList.as_view()),
    path('api/QuanLyRap/LayThongTinHeThongRap',views.LayThongTinHeThongRapList.as_view()), #Xem He Thong Rap
    path('api/QuanLyRap/LayThongTinCumRapTheoHeThong',views.LayThongTinCumRapList.as_view()),#Xem Cụm Rạp
    path('api/QuanLyRap/LayThongTinLichChieuPhim',views.LayThongTinLichChieuPhimList.as_view()), #Xem lịch chiếu
    path('api/QuanLyRap/LayThongTinLichChieuHeThongRap',views.LayThongTinLichChieuHeThongRapList.as_view()) #Xem phim
]