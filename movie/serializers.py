from typing import List, OrderedDict
from django.db.models import fields
from rest_framework import serializers
import movie.models
from drf_writable_nested.serializers import WritableNestedModelSerializer

class PhimSerializer(serializers.ModelSerializer):
    ngayKhoiChieuFormat = serializers.DateTimeField(source = 'ngayKhoiChieu', format="%d/%m/%Y")
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

class maPhimFilterForLTTLCP(serializers.ListSerializer):
    def to_representation(self, data):
        maPhim = self.context['request'].query_params['maPhim']
        data = data.filter(phim__maPhim = maPhim)
        return super(maPhimFilterForLTTLCP, self).to_representation(data)

class lichChieuPhimSerializerForLTTLCP(serializers.ModelSerializer):
    maRap = serializers.ReadOnlyField(source='rap.maRap')
    tenRap = serializers.ReadOnlyField(source='rap.tenRap')

    class Meta:
        list_serializer_class = maPhimFilterForLTTLCP
        model = movie.models.lichChieuPhim
        fields = ['maLichChieu', 'maRap', 'tenRap', 'ngayChieuGioChieu', 'giaVe', 'thoiLuong']

class rapForLTTLCP(serializers.ModelSerializer):
    d = lichChieuPhimSerializerForLTTLCP(source = 'lichChieu', read_only = True, many = True)
    class Meta:
        model = movie.models.Rap
        fields = ['d']
    def to_representation(self, instance):
        return super().to_representation(instance)['d']

class cumRapChieuForLTTLCP(serializers.ModelSerializer):
    lichChieuPhim = rapForLTTLCP(source = 'rap', read_only = True, many = True)
    hinhAnh = serializers.IntegerField(default=None)
    
    class Meta:
        model = movie.models.CumRap
        fields = ['lichChieuPhim', 'maCumRap', 'tenCumRap', 'hinhAnh']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        newarr = []
        for d in data['lichChieuPhim']:
            newarr += d
        data['lichChieuPhim'] = newarr
        if (data['lichChieuPhim'] != []): return data

class heThongRapChieuForLTTLCP(serializers.ModelSerializer):
    cumRapChieu = cumRapChieuForLTTLCP(source = 'cumrap', read_only = True, many = True)

    class Meta:
        model = movie.models.HeThongRap
        fields = ['cumRapChieu', 'maHeThongRap', 'tenHeThongRap', 'logo']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        newdict = OrderedDict()
        for (key, value) in data.items():
            if (key == 'cumRapChieu'):
                newlist = OrderedDict()
                for d in value:
                    if (d is not None): 
                        newlist.update(d)
                if (newlist is List): value = newlist
                elif (newlist == {}): value = []
                else: value = [newlist]
            newdict.update({key: value})
        return newdict

class ListLichChieuTheoPhimSerializersForLTTLCHTR(serializers.ModelSerializer):
    maRap = serializers.ReadOnlyField(source='rap.maRap')
    tenRap = serializers.ReadOnlyField(source='rap.tenRap')
    maPhim = serializers.ReadOnlyField(source = 'phim.maPhim')
    tenPhim = serializers.ReadOnlyField(source = 'phim.tenPhim')
    hinhAnh = serializers.FileField(source = 'phim.hinhAnh')

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['maLichChieu', 'maRap', 'tenRap', 'ngayChieuGioChieu', 'giaVe', 'maPhim', 'tenPhim', 'hinhAnh']

class danhSachPhimSerializersforLTTLCHTR(serializers.ModelSerializer):
    lstLichChieuTheoPhim = ListLichChieuTheoPhimSerializersForLTTLCHTR(source = 'lichChieu', read_only = True, many = True)
    # maPhim = serializers.ReadOnlyField(source='phim.maPhim')
    # tenPhim = serializers.ReadOnlyField(source='phim.tenPhim')
    # hinhAnh = serializers.FileField(source='phim.hinhAnh')

    class Meta:
        model = movie.models.Rap
        fields = ['lstLichChieuTheoPhim']

    def to_representation(self, instance):
        return super().to_representation(instance)['lstLichChieuTheoPhim']

class listCumRapSerializersForLTTLCHTR(serializers.ModelSerializer):
    danhSachPhim = danhSachPhimSerializersforLTTLCHTR(source = 'rap', read_only = True, many = True)

    class Meta:
        model = movie.models.CumRap
        fields = ['danhSachPhim', 'maCumRap', 'tenCumRap', 'diaChi']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        newarr = []
        for d in data['danhSachPhim']:
            newarr += d
        data['danhSachPhim'] = newarr
        return data


class LTTLCHTR(serializers.ModelSerializer):
    lstCumRap = listCumRapSerializersForLTTLCHTR(source = 'cumrap', read_only = True, many = True)
    # maHeThongRap = serializers.ReadOnlyField(source='rap.cumRap.heThongRap.maHeThongRap')
    # tenHeThongRap = serializers.ReadOnlyField(source='rap.cumRap.heThongRap.tenHeThongRap')
    # logo = serializers.FileField(source='rap.cumRap.heThongRap.logo')
    maNhom = serializers.CharField(default='GP01')
    class Meta:
        model = movie.models.HeThongRap
        fields = ['lstCumRap', 'maHeThongRap', 'tenHeThongRap', 'logo', 'maNhom']

class thongTinPhimSerializerForLDSPV(WritableNestedModelSerializer):
    tenCumRap = serializers.ReadOnlyField(source = 'rap.cumRap.tenCumRap')
    tenRap = serializers.ReadOnlyField(source = 'rap.tenRap')
    diaChi = serializers.ReadOnlyField(source = 'rap.cumRap.diaChi')
    tenPhim = serializers.ReadOnlyField(source = 'phim.tenPhim')
    hinhAnh = serializers.FileField(source = 'phim.hinhAnh')
    ngayChieu = serializers.DateTimeField(source = 'ngayChieuGioChieu', format="%d/%m/%Y")
    gioChieu = serializers.DateTimeField(source = 'ngayChieuGioChieu', format="%H:%m")

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['maLichChieu', 'tenCumRap', 'tenRap', 'diaChi', 'tenPhim', 'hinhAnh', 'ngayChieu', 'gioChieu']

class danhSachGheSerializerForLDSPV(WritableNestedModelSerializer):
    class Meta:
        model = movie.models.Ghe
        fields = ['maGhe', 'tenGhe', 'loaiGhe', 'stt', 'giaVe', 'daDat', 'taiKhoanNguoiDat']

class LDSPV(WritableNestedModelSerializer):
    thongTinPhim = thongTinPhimSerializerForLDSPV(source = '*')
    danhSachGhe = danhSachGheSerializerForLDSPV(source = 'ghe', many = True)

    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['thongTinPhim', 'danhSachGhe']

class DatGhe(WritableNestedModelSerializer):
    danhSachGhe = danhSachGheSerializerForLDSPV(source = 'ghe', many = True)
    class Meta:
        model = movie.models.lichChieuPhim
        fields = ['maLichChieu', 'danhSachGhe']

class UserSerializerForDangKy(serializers.ModelSerializer):
    class Meta:
        model = movie.models.NguoiDung
        fields = '__all__'

class UserSerializerForDangNhap(serializers.ModelSerializer):
    class Meta:
        model = movie.models.NguoiDung
        fields = ['ID', 'email', 'soDt']