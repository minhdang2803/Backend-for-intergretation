from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_delete

# Create your models here.
class Phim(models.Model):
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

class HeThongRap(models.Model):
    maHeThongRap = models.CharField(max_length=50, primary_key=True)
    tenHeThongRap = models.CharField(max_length=50)
    biDanh = models.CharField(max_length=50)
    logo = models.FileField(upload_to='images')
    
    def __str__(self):
        return self.tenHeThongRap


class CumRap(models.Model):
    heThongRap = models.ForeignKey(HeThongRap, on_delete=CASCADE)
    maCumRap = models.CharField(max_length=50, primary_key=True)
    tenCumRap = models.CharField(max_length=50)
    diaChi = models.CharField(max_length=100)

    def __str__(self):
        return self.tenCumRap


class Rap(models.Model):
    cumRap = models.ForeignKey(CumRap, on_delete=CASCADE)
    maRap = models.IntegerField(primary_key=True)
    tenRap = models.CharField(max_length=10)

    def __str__(self):
        return self.cumRap.tenCumRap + " - " + self.tenRap

class lichChieuPhim(models.Model):
    rap = models.ForeignKey(Rap, on_delete=CASCADE)
    phim = models.ForeignKey(Phim, on_delete=CASCADE)
    maLichChieu = models.IntegerField(primary_key=True)
    ngayChieuGioChieu = models.DateTimeField()
    giaVe = models.IntegerField()
    thoiLuong = models.IntegerField()

    def __str__(self):
        return self.rap.__str__() + " - " + str(self.maLichChieu)

