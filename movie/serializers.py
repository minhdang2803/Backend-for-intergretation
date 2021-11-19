from django.db.models import fields
from rest_framework import serializers
import movie.models

class PhimSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie.models.Phim
        fields = '__all__'

class HeThongRapSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie.models.HeThongRap
        fields = '__all__'

class RapSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie.models.Rap
        fields = ['maRap', 'tenRap']

class CumRapSerializer(serializers.ModelSerializer):
    danhSachRap = RapSerializer(source = 'rap', read_only = True, many = True)

    class Meta:
        model = movie.models.CumRap
        fields = ['maCumRap', 'tenCumRap', 'diaChi', 'danhSachRap']

class lichChieuPhimSerializerForLTTLCP(serializers.ModelSerializer):
    maRap = serializers.ReadOnlyField(source='rap.maRap')
    tenRap = serializers.ReadOnlyField(source='rap.tenRap')

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['maLichChieu', 'maRap', 'tenRap', 'ngayChieuGioChieu', 'giaVe', 'thoiLuong']

class cumRapChieuForLTTLCP(serializers.ModelSerializer):
    lichChieuPhim = lichChieuPhimSerializerForLTTLCP(source = '*', read_only = True)
    maCumRap = serializers.ReadOnlyField(source='rap.cumRap.maCumRap')
    tenCumRap = serializers.ReadOnlyField(source='rap.cumRap.tenCumRap')
    hinhAnh = serializers.IntegerField(default=None)
    
    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['lichChieuPhim', 'maCumRap', 'tenCumRap', 'hinhAnh']

class heThongRapChieuForLTTLCP(serializers.ModelSerializer):
    cumRapChieu = cumRapChieuForLTTLCP(source = '*', read_only = True)
    maHeThongRap = serializers.ReadOnlyField(source='rap.cumRap.heThongRap.maHeThongRap')
    tenHeThongRap = serializers.ReadOnlyField(source='rap.cumRap.heThongRap.tenHeThongRap')
    logo = serializers.FileField(source='rap.cumRap.heThongRap.logo')

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['cumRapChieu', 'maHeThongRap', 'tenHeThongRap', 'logo']

class LTTLCP(serializers.ModelSerializer):
    heThongRapChieu = heThongRapChieuForLTTLCP(source = '*', read_only = True)
    maPhim = serializers.ReadOnlyField(source='phim.maPhim')
    tenPhim = serializers.ReadOnlyField(source='phim.tenPhim')
    biDanh = serializers.ReadOnlyField(source='phim.biDanh')
    trailer = serializers.ReadOnlyField(source='phim.trailer')
    hinhAnh = serializers.FileField(source='phim.hinhAnh')
    moTa = serializers.ReadOnlyField(source='phim.moTa')
    maNhom = serializers.ReadOnlyField(source='phim.maNhom')
    ngayKhoiChieu = serializers.ReadOnlyField(source='phim.ngayKhoiChieu')
    danhGia = serializers.ReadOnlyField(source='phim.danhGia')

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['heThongRapChieu', 'maPhim', 'tenPhim', 'biDanh', 'trailer', 'hinhAnh', 'moTa', 'maNhom', 'ngayKhoiChieu', 'danhGia']


class ListLichChieuTheoPhimSerializersForLTTLCHTR(serializers.ModelSerializer):
    maRap = serializers.ReadOnlyField(source='rap.maRap')
    tenRap = serializers.ReadOnlyField(source='rap.tenRap')

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['maLichChieu', 'maRap', 'tenRap', 'ngayChieuGioChieu', 'giaVe']

class danhSachPhimSerializersforLTTLCHTR(serializers.ModelSerializer):
    lstLichChieuTheoPhim = ListLichChieuTheoPhimSerializersForLTTLCHTR(source = '*', read_only = True)
    maPhim = serializers.ReadOnlyField(source='phim.maPhim')
    tenPhim = serializers.ReadOnlyField(source='phim.tenPhim')
    hinhAnh = serializers.FileField(source='phim.hinhAnh')

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['lstLichChieuTheoPhim', 'maPhim', 'tenPhim', 'hinhAnh']

class listCumRapSerializersForLTTLCHTR(serializers.ModelSerializer):
    danhSachPhim = danhSachPhimSerializersforLTTLCHTR(source = '*', read_only = True)
    maCumRap = serializers.ReadOnlyField(source='rap.cumRap.maCumRap')
    tenCumRap = serializers.ReadOnlyField(source='rap.cumRap.tenCumRap')
    diaChi = serializers.ReadOnlyField(source='rap.cumRap.diaChi')

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['danhSachPhim', 'maCumRap', 'tenCumRap', 'diaChi']


class LTTLCHTR(serializers.ModelSerializer):
    lstCumRap = listCumRapSerializersForLTTLCHTR(source = '*', read_only = True)
    maHeThongRap = serializers.ReadOnlyField(source='rap.cumRap.heThongRap.maHeThongRap')
    tenHeThongRap = serializers.ReadOnlyField(source='rap.cumRap.heThongRap.tenHeThongRap')
    logo = serializers.FileField(source='rap.cumRap.heThongRap.logo')
    maNhom = serializers.ReadOnlyField(source='phim.maNhom')
    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['lstCumRap', 'maHeThongRap', 'tenHeThongRap','logo', 'maNhom']
