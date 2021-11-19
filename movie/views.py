from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, generics, filters

import movie.models
import movie.serializers
from PIL import Image

def secureImage(request, imagePath):
    response = HttpResponse(mimetype="image/jpg")
    img = Image.open(imagePath)
    img.save(response,'jpg')
    return response

# Create your views here.
class QuanLyPhimList(generics.ListAPIView):
    queryset = movie.models.Phim.objects.all()
    serializer_class = movie.serializers.PhimSerializer
    filterset_fields = ['maNhom', 'tenPhim']

class LayThongTinHeThongRapList(generics.ListAPIView):
    queryset = movie.models.HeThongRap.objects.all()
    serializer_class = movie.serializers.HeThongRapSerializer

class LayThongTinCumRapList(generics.ListAPIView):
    serializer_class = movie.serializers.CumRapSerializer

    def get_queryset(self):
        queryset = movie.models.CumRap.objects.all()
        maHeThongRap = self.request.query_params.get('maHeThongRap')
        if maHeThongRap is not None:
            queryset = queryset.filter(heThongRap__maHeThongRap=maHeThongRap)
        return queryset

#Lay Thong Tin Lich Chieu
class LayThongTinLichChieuPhimList(generics.ListAPIView):
    serializer_class = movie.serializers.LTTLCP

    def get_queryset(self):
        queryset = movie.models.lichChieuPhim.objects.all()
        maPhim = self.request.query_params.get('maPhim')
        if maPhim is not None:
            queryset = queryset.filter(phim__maPhim=maPhim)
        return queryset

class LayThongTinLichChieuHeThongRapList(generics.ListAPIView):
    serializer_class = movie.serializers.LTTLCHTR

    def get_queryset(self):
        queryset = movie.models.lichChieuPhim.objects.all()
        maNhom = self.request.query_params.get('maNhom')
        if maNhom is not None:
            queryset = queryset.filter(phim__maNhom=maNhom)
        return queryset