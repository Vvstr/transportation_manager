from django.shortcuts import render, redirect, get_object_or_404
from .models import Greenhouse, Crop, CustomUser
from .forms import GreenhouseForm, CropForm, SowingScheduleForm, IrrigationScheduleForm, FertilizationScheduleForm, \
    HarvestScheduleForm, SignUpForm, LogInForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate


def is_agronom(user):
    return user.groups.filter(name='Agronom').exists()


def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')


def index(request):
    greenhouses = Greenhouse.objects.all()
    unique_crops = Crop.objects.all().distinct()
    agronomist = request.user
    print(f"Greenhouses: {greenhouses}")
    print(f"Crops: {unique_crops}")  # Добавляем отладочную информацию
    return render(request, 'greenhouses/index.html', {'greenhouses': greenhouses,
                                                      'unique_crops': unique_crops,
                                                      'current_user': agronomist
                                                      })


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'greenhouses/signup.html', {'form': form})


def login_view(request):
    form = LogInForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    return render(request, 'greenhouses/login.html', {'form': form})


def agronomists(request):
    agronomists = CustomUser.objects.filter(groups__name='Agronom')
    print(f"Agronomists: {agronomists}")
    return render(request, 'greenhouses/agronomists.html', {'agronomists': agronomists})


def greenhouse_detail(request, pk):
    greenhouse = get_object_or_404(Greenhouse, pk=pk)
    crops = greenhouse.crops.all()
    return render(request, 'greenhouses/greenhouse_detail.html', {'greenhouse': greenhouse, 'crops': crops})


def crop_detail(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    greenhouse = crop.green_house
    can_edit = False

    if greenhouse and greenhouse.owner == request.user:
        can_edit = True

    sowing_schedules = crop.sowing_schedules.all()
    irrigation_schedules = crop.irrigation_schedules.all()
    fertilization_schedules = crop.fertilization_schedules.all()
    harvest_schedules = crop.harvest_schedules.all()
    context = {
        'crop': crop,
        'can_edit': can_edit,
        'sowing_schedules': sowing_schedules,
        'irrigation_schedules': irrigation_schedules,
        'fertilization_schedules': fertilization_schedules,
        'harvest_schedules': harvest_schedules,
    }

    return render(request, 'greenhouses/crop_detail.html', context)


@login_required
@user_passes_test(is_agronom)
def create_greenhouse(request):
    if request.method == 'POST':
        form = GreenhouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GreenhouseForm()
    return render(request, 'greenhouses/create_greenhouse.html', {'form': form})


@login_required
@user_passes_test(is_agronom)
def create_crop(request, greenhouse_pk):
    greenhouse = get_object_or_404(Greenhouse, pk=greenhouse_pk)
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.greenhouse = greenhouse
            crop.save()
            return redirect('greenhouse_detail', pk=greenhouse.pk)
    else:
        form = CropForm()
    return render(request, 'greenhouses/create_crop.html', {'form': form, 'greenhouse': greenhouse})


@login_required
def create_sowing_schedule(request, crop_pk):
    crop = get_object_or_404(Crop, pk=crop_pk)
    if not crop.green_house.owner == request.user:
        return redirect('crop_detail', pk=crop_pk)
    if request.method == 'POST':
        form = SowingScheduleForm(request.POST)
        if form.is_valid():
            sowing_schedule = form.save(commit=False)
            sowing_schedule.crop = crop
            sowing_schedule.save()
            return redirect('crop_detail', pk=crop.pk)
    else:
        form = SowingScheduleForm()
    return render(request, 'greenhouses/create_sowing_schedule.html', {'form': form, 'crop': crop})


@login_required
def create_irrigation_schedule(request, crop_pk):
    crop = get_object_or_404(Crop, pk=crop_pk)
    if not crop.green_house.owner == request.user:
        return redirect('crop_detail', pk=crop_pk)
    if request.method == 'POST':
        form = IrrigationScheduleForm(request.POST)
        if form.is_valid():
            irrigation_schedule = form.save(commit=False)
            irrigation_schedule.crop = crop
            irrigation_schedule.save()
            return redirect('crop_detail', pk=crop.pk)
    else:
        form = IrrigationScheduleForm()
    return render(request, 'greenhouses/create_irrigation_schedule.html', {'form': form, 'crop': crop})


@login_required
def create_fertilization_schedule(request, crop_pk):
    crop = get_object_or_404(Crop, pk=crop_pk)
    if not crop.green_house.owner == request.user:
        return redirect('crop_detail', pk=crop_pk)
    if request.method == 'POST':
        form = FertilizationScheduleForm(request.POST)
        if form.is_valid():
            fertilization_schedule = form.save(commit=False)
            fertilization_schedule.crop = crop
            fertilization_schedule.save()
            return redirect('crop_detail', pk=crop.pk)
    else:
        form = FertilizationScheduleForm()
    return render(request, 'greenhouses/create_fertilization_schedule.html', {'form': form, 'crop': crop})


@login_required
def create_harvest_schedule(request, crop_pk):
    crop = get_object_or_404(Crop, pk=crop_pk)
    if not crop.green_house.owner == request.user:
        return redirect('crop_detail', pk=crop_pk)
    if request.method == 'POST':
        form = HarvestScheduleForm(request.POST)
        if form.is_valid():
            harvest_schedule = form.save(commit=False)
            harvest_schedule.crop = crop
            harvest_schedule.save()
            return redirect('crop_detail', pk=crop.pk)
    else:
        form = HarvestScheduleForm()
    return render(request, 'greenhouses/create_harvest_schedule.html', {'form': form, 'crop': crop})


@login_required
def profile_view(request):
    return render(request, 'greenhouses/profile.html', {'user': request.user})
