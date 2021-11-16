from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_delete

# Create your models here.
class QuanLyPhim(models.Model):
    maPhim = models.IntegerField(primary_key=True)
    tenPhim = models.CharField(max_length=50)
    biDanh = models.CharField(max_length=50)
    trailer = models.TextField()
    hinhAnh = models.FileField(upload_to='images')
    moTa = models.TextField()
    maNhom = models.TextField()
    ngayKhoiChieu = models.DateTimeField()
    danhGia = models.IntegerField()

    def __str__(self):
        return self.tenPhim


# LayThongTinHeThongRap
class LayThongTinHeThongRap(models.Model):
    maHeThongRap = models.CharField(max_length=50, primary_key=True)
    tenHeThongRap = models.CharField(max_length=50)
    biDanh = models.CharField(max_length=50)
    logo = models.FileField(upload_to='images')
    def __str__(self):
        return self.tenHeThongRap


# LayThongTinCumRap
# CumRap -------- 1---------Has ---------- N -----------Rap

class Rap(models.Model):
    maRap = models.CharField(max_length=50, primary_key=True)
    tenRap = models.CharField(max_length=50)
    def __str__(self):
        return self.maRap

class LayThongTinCumRap(models.Model):
    maCumRap = models.CharField(max_length=50, primary_key=True)
    tenCumRap = models.CharField(max_length=50)
    diaChi = models.CharField(max_length=50)
    danhSachRap = models.ManyToManyField(Rap)
    def __str__(self):
        return self.tenCumRap





# LayThongTinLichChieuPhim
class LayBuoiChieuPhim(models.Model):
    maLichChieu = models.CharField(max_length=50, primary_key=True)
    maRap =  models.ForeignKey(Rap, on_delete=CASCADE)
    ngayChieuGioChieu = models.DateTimeField()
    giaVe = models.IntegerField()
    thoiLuong = models.IntegerField()

class LayCumRapChieu(models.Model):
    maCumRap = models.ForeignKey(LayThongTinCumRap, on_delete=CASCADE)
    lichChieuPhim = models.ManyToManyField(LayBuoiChieuPhim)

class HeThongRapChieu(models.Model):
    maHeThongRap = models.ForeignKey(LayThongTinHeThongRap, on_delete=CASCADE)
    cumRapChieu = models.ManyToManyField(LayCumRapChieu)

class LayThongTinLichChieuPhim(models.Model):
    maPhim = models.ForeignKey(QuanLyPhim, on_delete=CASCADE)
    heThongRapChieu = models.ManyToManyField(HeThongRapChieu)
    def __str__(self):
        return self.maPhim