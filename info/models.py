import profile
from tabnanny import verbose
from turtle import update
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=20, verbose_name = 'Имя')
    greetings_1 = models.CharField(max_length=5, verbose_name = 'Приветствие 1')
    greetings_2 = models.CharField(max_length=8, verbose_name = 'Приветствие 2')
    image = models.ImageField(upload_to = 'pic/', verbose_name = 'Фото')
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница "Главная"'
        verbose_name_plural = 'Страницы "Главная"'

class About(models.Model):
    heading = models.CharField(max_length=50, verbose_name = 'Заголовок')
    career = models.CharField(max_length=20, verbose_name = 'Опыт работы')
    description = models.TextField(blank=False, verbose_name = 'Описание')
    profile_img = models.ImageField(upload_to='pic/', verbose_name = 'Фото')
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.career

    class Meta:
        verbose_name = 'Страница "Обо мне"'
        verbose_name_plural = 'Страницы "Обо мне"'

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete = models.CASCADE)
    social_name = models.CharField(max_length = 10)
    link = models.URLField(max_length = 200)

class Category(models.Model):
    name = models.CharField(max_length = 20)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    skill_name = models.CharField(max_length = 20)

class Portfolio(models.Model):
    image = models.ImageField(upload_to = 'pic/')
    link = models.URLField(max_length = 200)

    def __str___(self):
        return f'Portfolio{self.id}'

    class Meta:
        verbose_name = 'Мое портфолио'
        verbose_name_plural = 'Мои портфолио'











