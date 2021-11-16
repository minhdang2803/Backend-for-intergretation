from django.contrib import admin
from movie.models import HeThongRapChieu, LayThongTinCumRap, LayThongTinHeThongRap, QuanLyPhim, Rap,LayBuoiChieuPhim,LayCumRapChieu,LayThongTinLichChieuPhim

# Register your models here.
admin.site.register(QuanLyPhim)
admin.site.register(LayThongTinHeThongRap)
admin.site.register(Rap)
admin.site.register(LayThongTinCumRap)
admin.site.register(LayBuoiChieuPhim)
admin.site.register(LayCumRapChieu)
admin.site.register(HeThongRapChieu)
admin.site.register(LayThongTinLichChieuPhim)