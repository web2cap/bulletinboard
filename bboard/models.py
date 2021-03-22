from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Товар')
    content = models.TextField(null=True,

                               # разрешить пустое значение
                               blank=True,
                               verbose_name='Описание',
                               help_text='Короткое и ясное описание')
    price = models.FloatField(null=True, blank=True,
                              verbose_name='Цена')
    published = models.DateTimeField(
                                     # занести текущее время
                                     auto_now_add=True,
                                     # индекс о полю
                                     db_index=True,
                                     verbose_name='Опубликовано')
    # связь между моделями БД внешний ключ, первое имя связи
    rubric = models.ForeignKey('Rubric',
                               null=True,
                               on_delete=models.PROTECT,  # защита от удаления
                               verbose_name='Рубрика')
    class Meta:
        # Множествееное число
        verbose_name_plural = 'Объявления'
        # единственное число
        verbose_name = 'Объявление'
        # сортировка по 2 полям
        ordering = ['-published', 'title']
        # уникальная в пределах таблицы комбинация значений
        unique_together = (
            ('title', 'published'),
            ('title', 'price', 'rubric'),
        )


class Rubric(models.Model):
    name = models.CharField(max_length=20,  # максимальная длинна
                            db_index=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

