from django.db import models

class Fruit(models.Model):
    """
    Модель для представления фруктов в магазине
    Поля:
    - name: Название фрукта (макс. 100 символов)
    - description: Описание характеристик
    - price: Цена за килограмм
    - created_at: Дата добавления в базу
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Введите название фрукта'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Опишите сорт и особенности'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Цена',
        help_text='Цена за 1 кг в рублях'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    def __str__(self):
        return f"{self.name} - {self.price}₽/кг"

    class Meta:
        verbose_name = 'Фрукт'
        verbose_name_plural = 'Фрукты'
        ordering = ['-created_at']