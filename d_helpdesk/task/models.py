from django.db import models


class Start_task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Задача')
    content = models.TextField(verbose_name='Описание задачи')
    created_dr = models.DateField(auto_now=True, verbose_name='Время создания')
    created_up = models.DateField(auto_now_add=True, verbose_name='Время изминения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Прикрепленное фото', blank=True)
    end_task = models.BooleanField(default=True, verbose_name='Завершить задачу?')

    def __str__(self):
        return self.title
