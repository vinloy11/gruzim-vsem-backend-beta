from django.db import models
from datetime import date


class Category(models.Model):
    """ Категории """
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class User(models.Model):
    """ Пользователи """
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField()
    city = models.CharField("Город", max_length=50, default="Новосибирск")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Car(models.Model):
    """ Машина """
    name = models.CharField("Имя", max_length=100)
    carrying = models.PositiveSmallIntegerField("Грузоподъемность", default=0)
    length = models.PositiveSmallIntegerField('Длина')
    width = models.PositiveSmallIntegerField('Ширина')
    height = models.PositiveSmallIntegerField('Высота')
    payment = models.PositiveSmallIntegerField("Оплата")
    description = models.TextField("Описание")
    url = models.SlugField(max_length=130, unique=True)
    driver = models.ForeignKey(User, verbose_name="Водитель", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class Payment(models.Model):
    """ Способы оплаты """
    name = models.CharField("Способ оплаты", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"


class Order(models.Model):
    """ Заявка """
    title = models.CharField("Заголовок", max_length=100)
    from_address = models.CharField("Откуда", max_length=100)
    to_address = models.CharField("Куда", max_length=100)
    date = models.DateField("Дата перевозки", default=date.today)
    weight = models.PositiveSmallIntegerField('Вес')
    length = models.PositiveSmallIntegerField('Длина')
    width = models.PositiveSmallIntegerField('Ширина')
    height = models.PositiveSmallIntegerField('Высота')
    count = models.PositiveSmallIntegerField('Количество')
    payment = models.ForeignKey(Payment, verbose_name="Способ оплаты", on_delete=models.SET_NULL, null=True)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(User, verbose_name="Клиент", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Reviews(models.Model):
    """ Отзывы """
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    car = models.ForeignKey(Car, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.car}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
