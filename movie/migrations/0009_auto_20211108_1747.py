# Generated by Django 3.2.9 on 2021-11-08 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20211108_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeThongRapChieu',
            fields=[
                ('maHeThongRap', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tenHeThongRap', models.CharField(max_length=50)),
                ('logo', models.FileField(blank=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='LayBuoiChieuPhim',
            fields=[
                ('maLichChieu', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tenRap', models.CharField(max_length=50)),
                ('ngayChieuGioChieu', models.DateTimeField()),
                ('giaVe', models.IntegerField()),
                ('thoiLuong', models.IntegerField()),
                ('maRap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.rap')),
            ],
        ),
        migrations.CreateModel(
            name='LayThongTinLichChieuPhim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenPhim', models.CharField(max_length=50)),
                ('biDanh', models.CharField(max_length=50)),
                ('trailer', models.TextField()),
                ('hinhAnh', models.FileField(blank=True, upload_to='images')),
                ('moTa', models.TextField()),
                ('maNhom', models.TextField()),
                ('ngayKhoiChieu', models.DateTimeField()),
                ('danhGia', models.IntegerField()),
                ('heThongRapChieu', models.ManyToManyField(to='movie.HeThongRapChieu')),
                ('maPhim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.quanlyphim')),
            ],
        ),
        migrations.CreateModel(
            name='LayCumRapChieu',
            fields=[
                ('maCumRap', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tenCumRap', models.CharField(max_length=50)),
                ('hinhanh', models.FileField(blank=True, upload_to='images')),
                ('lichChieuPhim', models.ManyToManyField(to='movie.LayBuoiChieuPhim')),
            ],
        ),
        migrations.AddField(
            model_name='hethongrapchieu',
            name='cumRapChieu',
            field=models.ManyToManyField(to='movie.LayCumRapChieu'),
        ),
    ]