from django.contrib.auth.models import User
from django.db import models

TiffinTypes = (
    ('BREAKFAST', 'BREAKFAST'),
    ('LUNCH', 'LUNCH'),
    ('DINNER', 'DINNER')
)

Rating = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNum = models.CharField(max_length=10)

    def __str__(self):
        return self.user.get_full_name()


class Kitchen(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breakFast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)
    rating = models.CharField(
        max_length=1,
        choices=Rating,
        default='5'
    )
    address = models.CharField(max_length=500)
    photo1 = models.ImageField(upload_to='kitchen_clicks', blank='True')
    photo2 = models.ImageField(upload_to='kitchen_clicks', blank='True')
    photo3 = models.ImageField(upload_to='kitchen_clicks', blank='True')

    def __str__(self):
        return self.name


class Tiffin(models.Model):
    tiffinType = models.CharField(
        max_length=20,
        choices=TiffinTypes,
        default='LUNCH'
    )
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.name