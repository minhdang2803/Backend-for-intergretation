import collections
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
    queryset = movie.models.HeThongRap.objects.all()
    serializer_class = movie.serializers.heThongRapChieuForLTTLCP
    serializer_class_phim = movie.serializers.PhimSerializer

    def get_queryset_phim(self):
        queryset = movie.models.Phim.objects.all()
        maPhim = self.request.query_params.get('maPhim')
        if maPhim is not None:
            queryset = queryset.filter(maPhim=maPhim)
        return queryset

    def list(self, request, *args, **kwargs):
        heThongRap = self.serializer_class(self.get_queryset(), many = True, context={'request': request})
        phim = self.serializer_class_phim(self.get_queryset_phim(), many = True, context={'request': request})
        result = {'heThongRapChieu': heThongRap.data}
        for i in range(9):
            result.update(phim.data.pop())
        return Response(result)

class LayDanhSachPhongVe(generics.ListAPIView):
    queryset = movie.models.lichChieuPhim.objects.all()
    serializer_class = movie.serializers.LDSPV
    
    def get_queryset(self):
        queryset = movie.models.lichChieuPhim.objects.all()
        maLichChieu = self.request.query_params.get('maLichChieu') or self.request.query_params.get('MaLichChieu')
        if maLichChieu is not None:
            queryset = queryset.filter(maLichChieu=maLichChieu)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])

class DangNhap(generics.ListAPIView):
    queryset = movie.models.NguoiDung.objects.all()
    serializer_class = movie.serializers.UserSerializerForDangKy
    filterset_fields = ['taiKhoan', 'matKhau']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])

class DangKy(generics.CreateAPIView):
    queryset = movie.models.NguoiDung.objects.all()
    serializer_class = movie.serializers.UserSerializerForDangKy

class DatGhe(generics.UpdateAPIView):
    queryset = movie.models.lichChieuPhim.objects.all()
    serializer_class = movie.serializers.DatGhe
