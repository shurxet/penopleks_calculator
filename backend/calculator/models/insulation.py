from django.db import models
from calculator.models import BaseModel


class Variety(BaseModel):
    title = models.CharField(
        verbose_name='Название вида плиты утеплителя',
        null=True, blank=True,
        default=None,
        help_text='В данном поле задаётся название листа утеплителя, то есть значение. Пример: Текст текст 00мм',
        max_length=100
    )
    sheet_area = models.FloatField(
        verbose_name='Площадь листа (м2)',
        null=True, blank=True,
        default=None,
        help_text='В данном поле задаётся площадь (м2) листа утеплителя, то есть значение. Пример: 0.00000000000',
        max_length=100
    )
    sheet_volume = models.FloatField(
        verbose_name='Oбъём листа (м3)',
        null=True, blank=True,
        default=None,
        help_text='В данном поле задаётся объём (м3) листа утеплителя, то есть значение. Пример: 0.00000000000',
        max_length=100
    )
    sheets_package = models.IntegerField(
        verbose_name='Количество листов в упаковке',
        null=True, blank=True,
        default=None,
        help_text='В данном поле задаётся объём (м3) листа утеплителя, то есть значение. Пример: 0.00000000000',
    )

    class Meta:
        verbose_name = 'Вид плиты утеплителя'
        verbose_name_plural = 'Виды плит утеплителей'

    def __str__(self):
        return self.title


class Insulation(BaseModel):
    title = models.CharField(
        verbose_name='Название Утеплителя',
        null=True, blank=True,
        default=None,
        help_text='В данном поле задаётся название листа утеплителя, то есть значение. Пример: Текст текст 00мм',
        max_length=100
    )
    subspecies = models.ManyToManyField(
        Variety,
        verbose_name='Вид Утеплителя',
        related_name='insulations',
        default=None,
        help_text='В данном поле, из списка выберается вид утеплителя созданный в модели Variety (Вид плиты утеплителя)'
                  'Если в списке нет доступных или подходящих видов утеплителя, то создайте необходимый новый вид в'
                  'модели Variety (Вид плиты утеплителя)',
        max_length=100
    )

    class Meta:
        verbose_name = 'Утеплитель'
        verbose_name_plural = 'Утеплители'

    def __str__(self):
        return self.title
