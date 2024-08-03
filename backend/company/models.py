from django.db import models

from user.models import BaseUser


# Create your models here.
#
class Company(models.Model):
    name = models.CharField("Название", max_length=50)
    rating = models.IntegerField("Рейтинг")
    image = models.ImageField("Изображение")
    applicant = models.BooleanField()
    pointsHave = models.IntegerField(default=0)
    employer = models.ForeignKey(BaseUser, models.CASCADE, "company", verbose_name="Создатель")


class Works(models.Model):
    company = models.ForeignKey(Company, models.CASCADE, related_name="works", verbose_name="Компания")
    title = models.CharField("Название", max_length=50)
    description = models.CharField("Описание", max_length=600)
    image = models.ImageField("Изображение")
    rating = models.IntegerField("Рейтинг")
    pointsToGive = models.IntegerField()
    timeToJob = models.IntegerField("Время сколько нужно отработать", default=1)


class TicketChoice(models.TextChoices):
    REJECTED = "rejected", "Отклонено"
    WAITING = "waiting", "Ожидание"
    APPROVED = "approved", "Принят"


class Ticket(models.Model):
    work = models.ForeignKey(Works, models.CASCADE, related_name="tickets", verbose_name="Вакансия")
    applicant = models.ForeignKey(BaseUser, models.CASCADE, related_name="tickets", verbose_name="Работник")
    status = models.CharField("Статус", max_length=15, choices=TicketChoice.choices, default=TicketChoice.WAITING)
