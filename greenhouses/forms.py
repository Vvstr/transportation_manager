from django import forms
from .models import Crop, Greenhouse, SowingSchedule, IrrigationSchedule, FertilizationSchedule, HarvestSchedule, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class GreenhouseForm(forms.ModelForm):
    class Meta:
        model = Greenhouse
        fields = ['name', 'crop_type', 'owner']


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'green_house']


class SowingScheduleForm(forms.ModelForm):
    class Meta:
        model = SowingSchedule
        fields = ['planned_date', 'actual_date', 'resources_used']
        widgets = {
            'planned_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'actual_date': forms.DateInput(attrs={'class': 'datepicker'})
        }


class IrrigationScheduleForm(forms.ModelForm):
    class Meta:
        model = IrrigationSchedule
        fields = ['planned_date', 'actual_date', 'resources_used']
        widgets = {
            'planned_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'actual_date': forms.DateInput(attrs={'class': 'datepicker'})
        }


class FertilizationScheduleForm(forms.ModelForm):
    class Meta:
        model = FertilizationSchedule
        fields = ['planned_date', 'actual_date', 'resources_used']
        widgets = {
            'planned_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'actual_date': forms.DateInput(attrs={'class': 'datepicker'})
        }


class HarvestScheduleForm(forms.ModelForm):
    class Meta:
        model = HarvestSchedule
        fields = ['planned_date', 'actual_date', 'resources_used']
        widgets = {
            'planned_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'actual_date': forms.DateInput(attrs={'class': 'datepicker'})
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Введите корпоративную почту')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class LogInForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
