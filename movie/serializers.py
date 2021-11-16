from django.db.models import fields
from rest_framework import serializers
from movie.models import LayBuoiChieuPhim, LayThongTinHeThongRap, QuanLyPhim, Rap, LayThongTinCumRap, LayCumRapChieu, HeThongRapChieu, LayThongTinLichChieuPhim


class QuanLyPhimSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuanLyPhim
        fields = ('__all__')

class LayThongTinHeThongRapSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayThongTinHeThongRap
        fields = ('__all__')

class RapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rap
        fields = ('__all__')

class LayThongTinCumRapSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayThongTinCumRap
        fields = ('__all__')

class LayBuoiChieuPhimSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayBuoiChieuPhim
        fields = ('__all__')

class LayCumRapChieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayCumRapChieu
        fields = ('__all__')
class HeThongRapChieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeThongRapChieu
        fields = ('__all__')

class LayThongTinLichChieuPhimSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayThongTinLichChieuPhim
        fields = ('__all__')