from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, generics, filters

from . models import LayThongTinHeThongRap, QuanLyPhim, Rap, LayThongTinCumRap
from . serializers import QuanLyPhimSerializer, LayThongTinHeThongRapSerializer, LayThongTinCumRapSerializer, RapSerializer
from PIL import Image

def secureImage(request, imagePath):
    response = HttpResponse(mimetype="image/jpg")
    img = Image.open(imagePath)
    img.save(response,'jpg')
    return response

# Create your views here.
class QuanLyPhimList(generics.ListAPIView):
    queryset = QuanLyPhim.objects.all()
    serializer_class = QuanLyPhimSerializer
    filterset_fields = ['maNhom', 'tenPhim']

class QuanLyPhimDelete(generics.DestroyAPIView):
    queryset = QuanLyPhim.objects.all()
    serializer_class = QuanLyPhimSerializer

class QuanLyPhimCreate(generics.CreateAPIView):
    queryset = QuanLyPhim.objects.all()
    serializer_class = QuanLyPhimSerializer

#! Lay thong tin he thong rap
class LayThongTinHeThongRapList(generics.ListAPIView):
    queryset = LayThongTinHeThongRap.objects.all()
    serializer_class = LayThongTinHeThongRapSerializer
    filterset_fields = ['maHeThongRap', 'tenHeThongRap']
    
class LayThongTinHeThongRapDelete(generics.DestroyAPIView):
    queryset = LayThongTinHeThongRap.objects.all()
    serializer_class = LayThongTinHeThongRapSerializer

class LayThongTinHeThongRapCreate(generics.CreateAPIView):
    queryset = LayThongTinHeThongRap.objects.all()
    serializer_class = LayThongTinHeThongRapSerializer

# !Lay thong tin cum rap
class RapList(generics.ListAPIView):
    queryset = Rap.objects.all()
    serializer_class = RapSerializer
    filterset_fields = ['maRap', 'tenRap']

class RapCreate(generics.CreateAPIView):
    queryset = Rap.objects.all()
    serializer_class = RapSerializer

class RapDelete(generics.DestroyAPIView):
    queryset = Rap.objects.all()
    serializer_class = RapSerializer

class LayThongTinCumRapList(generics.ListAPIView):
    queryset = LayThongTinCumRap.objects.all()
    serializer_class = LayThongTinCumRapSerializer
    filterset_fields = ['maCumRap', 'tenCumRap']

class LayThongTinCumRapCreate(generics.CreateAPIView):
    queryset = LayThongTinCumRap.objects.all()
    serializer_class = LayThongTinCumRapSerializer

class LayThongTinCumRapDelete(generics.DestroyAPIView):
    queryset = LayThongTinCumRap.objects.all()
    serializer_class = LayThongTinCumRapSerializer

#LayBuoiChieuPhim

class LayBuoiChieuPhimList(generics.ListAPIView):
    queryset = QuanLyPhim.objects.all()
    serializer_class = QuanLyPhimSerializer
    filterset_fields = ['maLichChieu','ngayChieuGioChieu']

#LayCumRapChieu

class LayCumRapchieuphimList(generics.ListAPIView):
    queryset = LayThongTinCumRap.objects.all()
    serializer_class = LayThongTinCumRapSerializer
    filterset_fields = ['maCumRap','lichChieuPhim']

#HeThongChieuPhim

class HeThongChieuPhimList(generics.ListAPIView):
    queryset = LayThongTinHeThongRap.objects.all()
    serializer_class = LayThongTinHeThongRapSerializer
    filterset_fields = ['maHeThongRap','cumRapChieu']
class HeThongChieuPhimCreate(generics.CreateAPIView):
    queryset = LayThongTinHeThongRap.objects.all()
    serializer_class = LayThongTinHeThongRapSerializer

class HeThongChieuPhimDelete(generics.DestroyAPIView):
    queryset = LayThongTinHeThongRap.objects.all()
    serializer_class = LayThongTinHeThongRapSerializer

#LayThongTinLichChieuPhim

class LayThongTinLichChieuPhimList(generics.ListAPIView):
    queryset = QuanLyPhim.objects.all()
    serializer_class = QuanLyPhimSerializer
    filterset_fields = ['maPhim','heThongRapChieu']
class LayThongTinLichChieuPhimCreate(generics.CreateAPIView):
    queryset = QuanLyPhim.objects.all()
    serializer_class = QuanLyPhimSerializer

class LayThongTinLichChieuPhimDelete(generics.DestroyAPIView):
    queryset = QuanLyPhim.objects.all()
    serializer_class = QuanLyPhimSerializer