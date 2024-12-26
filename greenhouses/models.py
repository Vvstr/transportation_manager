from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    group = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username


class Greenhouse(models.Model):
    name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, related_name='greenhouses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=100)
    green_house = models.ForeignKey(Greenhouse, related_name='crops', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BaseShedule(models.Model):
    planned_date = models.DateField()
    actual_date = models.DateField(null=True, blank=True)
    resources_used = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class SowingSchedule(BaseShedule):
    crop = models.ForeignKey(Crop, related_name='sowing_schedules', on_delete=models.CASCADE)

    def __str__(self):
        return f"Посев {self.crop.name} запланирован на дату {self.planned_date}"


class IrrigationSchedule(BaseShedule):
    crop = models.ForeignKey(Crop, related_name='irrigation_schedules', on_delete=models.CASCADE)

    def __str__(self):
        return f"Полив {self.crop.name} запланирован на дату {self.planned_date}"


class FertilizationSchedule(BaseShedule):
    crop = models.ForeignKey(Crop, related_name='fertilization_schedules', on_delete=models.CASCADE)

    def __str__(self):
        return f"Удобрение {self.crop.name} запланировано на дату {self.planned_date}"


class HarvestSchedule(BaseShedule):
    crop = models.ForeignKey(Crop, related_name='harvest_schedules', on_delete=models.CASCADE)

    def __str__(self):
        return f"Сбор урожая {self.crop.name} запланирован на дату {self.planned_date}"
