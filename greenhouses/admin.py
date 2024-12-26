from django.contrib import admin
from .models import SowingSchedule, FertilizationSchedule, IrrigationSchedule, HarvestSchedule, Greenhouse, Crop, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'green_house',)
    search_fields = ('name',)


@admin.register(Greenhouse)
class GreenhouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'crop_type',)
    search_fields = ('name',)


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


@admin.register(SowingSchedule)
class SowingScheduleAdmin(admin.ModelAdmin):
    list_display = ('crop', 'planned_date', 'actual_date', 'resources_used',)
    search_fields = ('crop',)


@admin.register(FertilizationSchedule)
class FertilizationScheduleAdmin(admin.ModelAdmin):
    list_display = ('crop', 'planned_date', 'actual_date', 'resources_used',)
    search_fields = ('crop',)


@admin.register(IrrigationSchedule)
class IrrigationScheduleAdmin(admin.ModelAdmin):
    list_display = ('crop', 'planned_date', 'actual_date', 'resources_used',)
    search_fields = ('crop',)


@admin.register(HarvestSchedule)
class HarvestScheduleAdmin(admin.ModelAdmin):
    list_display = ('crop', 'planned_date', 'actual_date', 'resources_used',)
    search_fields = ('crop',)
