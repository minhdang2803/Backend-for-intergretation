from django.db import models
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save

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
    phim = models.ManyToManyField(Phim, related_name='cumRap')
    heThongRap = models.ForeignKey(HeThongRap, related_name='cumrap', on_delete=CASCADE)
    maCumRap = models.CharField(max_length=50, primary_key=True)
    tenCumRap = models.CharField(max_length=50)
    diaChi = models.CharField(max_length=100)

    def __str__(self):
        return self.tenCumRap

class Rap(models.Model):
    cumRap = models.ForeignKey(CumRap, related_name='rap', on_delete=CASCADE)
    maRap = models.IntegerField(primary_key=True)
    tenRap = models.CharField(max_length=10)

    def __str__(self):
        return self.cumRap.tenCumRap + " - " + self.tenRap

class lichChieuPhim(models.Model):
    rap = models.ForeignKey(Rap, related_name='lichChieu', on_delete=CASCADE)
    phim = models.ForeignKey(Phim, related_name='lichChieu', on_delete=CASCADE)
    maLichChieu = models.IntegerField(primary_key=True)
    ngayChieuGioChieu = models.DateTimeField()
    giaVe = models.IntegerField()
    thoiLuong = models.IntegerField()

    def __str__(self):
        return self.rap.__str__() + " - " + str(self.maLichChieu)

class Ghe(models.Model):
    lichChieu = models.ForeignKey(lichChieuPhim, related_name='ghe', on_delete=CASCADE)
    maGhe = models.AutoField(primary_key=True)
    tenGhe = models.CharField(max_length=4)
    loaiGhe = models.CharField(max_length=10)
    stt = models.CharField(max_length=4)
    giaVe = models.IntegerField()
    daDat = models.BooleanField()
    taiKhoanNguoiDat = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.lichChieu.__str__() + " - " + self.tenGhe

@receiver(post_save, sender=lichChieuPhim)
def make_ghe(sender, instance, created, **kwargs):
    if created:
        for i in range(160):
            if (35 <= i+1 <= 46 or 51 <= i+1 <= 62 or 67 <= i+1 <= 78 or 83 <= i+1 <= 94 or 99 <= i+1 <= 110 or 115 <= i+1 <= 126):
                Ghe.objects.create(
                    lichChieu = instance,
                    tenGhe = str(i+1),
                    loaiGhe = "Vip",
                    stt = str(i+1),
                    giaVe = instance.giaVe,
                    daDat = False,
                    taiKhoanNguoiDat = None
                )
            else:
                Ghe.objects.create(
                    lichChieu = instance,
                    tenGhe = str(i+1),
                    loaiGhe = "Thuong",
                    stt = str(i+1),
                    giaVe = instance.giaVe,
                    daDat = False,
                    taiKhoanNguoiDat = None
                )

class NguoiDung(models.Model):
    ID = models.AutoField(primary_key=True)
    taiKhoan = models.CharField(max_length=20)
    matKhau = models.CharField(max_length=32)
    email = models.EmailField()
    soDt = models.CharField(max_length=15)
    hoTen = models.CharField(max_length=50)

    class Meta:
        unique_together = ('ID', 'taiKhoan')

    def __str__(self):
        return self.hoTen