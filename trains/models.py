from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, #Удаляет из других таблиц все записи о поезде, если удалили город например в который он шёл
                                  related_name='from_city_set',
                                  verbose_name='Из какого города'
                                  )
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, #Удаляет из других таблиц все записи о поезде, если удалили город например в который он шёл
                                related_name='to_city_set',
                                verbose_name='В какой город'
                                )

    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']  #Сортировка по времени в пути
