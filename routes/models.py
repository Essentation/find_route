from django.db import models

from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Название маршрута')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, #Удаляет из других таблиц все записи о поезде, если удалили город например в который он шёл
                                  related_name='route_from_city_set',
                                  verbose_name='Из какого города'
                                  )
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, #Удаляет из других таблиц все записи о поезде, если удалили город например в который он шёл
                                related_name='route_to_city_set',
                                verbose_name='В какой город'
                                )
    trains = models.ManyToManyField(
        'trains.Train', verbose_name='Список поездов')

    def __str__(self):
        return f'Маршрут {self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_times']