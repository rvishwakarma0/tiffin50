# Generated by Django 3.2.2 on 2021-05-12 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breakFast', models.BooleanField(default=True)),
                ('lunch', models.BooleanField(default=True)),
                ('dinner', models.BooleanField(default=True)),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='5', max_length=1)),
                ('address', models.CharField(max_length=500)),
                ('photo1', models.ImageField(blank='True', upload_to='kitchen_clicks')),
                ('photo2', models.ImageField(blank='True', upload_to='kitchen_clicks')),
                ('photo3', models.ImageField(blank='True', upload_to='kitchen_clicks')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNum', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tiffin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiffinType', models.CharField(choices=[('BREAKFAST', 'BREAKFAST'), ('LUNCH', 'LUNCH'), ('DINNER', 'DINNER')], default='LUNCH', max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(max_length=1500)),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.kitchen')),
            ],
        ),
        migrations.AddField(
            model_name='kitchen',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor'),
        ),
    ]
