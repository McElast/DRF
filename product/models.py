from django.db import models


class Product(models.Model):
    MEASURE_UNITS = [
        ('p', 'шт.'),
        ('k', 'кг'),
        ('l', 'л')
    ]

    name = models.CharField(max_length=150, unique=True, blank=False, null=False, verbose_name='имя')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    measure = models.CharField(max_length=1, choices=MEASURE_UNITS, verbose_name='Единица измерения')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    date_mod = models.DateTimeField(auto_now=True, verbose_name='Дата')

    class Meta:
        ordering = ['-date_mod']

    def __str__(self):
        return f'{self.name} (Цена: {self.price} -- Количество: {self.quantity})'
