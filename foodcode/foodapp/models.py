from django.db import models
from django.db.models import *

class FoodCategory():

    name_ru = CharField(verbose_name="Название на русском", max_length=255)
    name_en = CharField(verbose_name="Название на английском", max_length=255)
    name_ch = CharField(verbose_name="Название на китайском", max_length=255)

    order_id = SmallIntegerField(default=10, blank=True, null=True)


    def __str__(self):
        return self.name_ru
    

    class Meta:
        verbose_name = "Раздел меню"
        verbose_name_plural = "Разделы меню"
        ordering = ('name_ru', 'order_id')