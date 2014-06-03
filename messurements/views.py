from django.views.generic.base import View
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Avg
from django.contrib.auth.decorators import login_required


# Class based views to create a new dataset and Update one
from django.views.generic.edit import CreateView, UpdateView

# Current time
from django.utils.timezone import now

from messurements.models import Pressure, Weight, UserProfile, Basic, Sleep, Exercise, Meal
from messurements.forms import PressureForm, WeightForm, UserProfileForm, BasicForm, SleepForm, ExerciseForm, MealForm

########################################################################

class PressureListView(View):
    model = Pressure
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Pressure.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date','sys', 'dia','pulse')
             )

        return render(request, self.template_name, {'output': qs})
########################################################################

class UserProfileListView(View):
    model = UserProfile
    template_name = 'height_list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             UserProfile.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date', 'height')
             )

        return render(request, self.template_name, {'output': qs})
########################################################################

class BasicListView(View):
    model = Basic
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Basic.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date', 'gender', 'birthday')
             )

        return render(request, self.template_name, {'output': qs})
########################################################################

class SleepListView(View):
    model = Sleep
    template_name = 'sleep_list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Sleep.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date', 'start_time', 'end_time')
             )

        return render(request, self.template_name, {'output': qs})
########################################################################

class ExerciseListView(View):
    model = Exercise
    template_name = 'exercise_list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Exercise.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date', 'kind', 'how_long')
             )

        return render(request, self.template_name, {'output': qs})
########################################################################

class MealListView(View):
    model = Meal
    template_name = 'meal_list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Meal.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date', 'breakfast', 'how_much', 'lunch','how_much2', 'dinner', 'how_much3')
             )

        return render(request, self.template_name, {'output': qs})
########################################################################

class WeightListView(View):
    model = Weight
    template_name = 'weight_list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Weight.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date', 'weight')
             )
        return render(request, self.template_name, {'output': qs})

########################################################################

class WeightFormView(CreateView):
    model = Weight
    fields = ['weight']
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.timestamp = now()
        return super(WeightFormView, self).form_valid(form)

########################################################################

@login_required
def PressureWeightView(request):
    if request.method == 'POST':
       pressure_form = PressureForm(request.POST)
       weight_form = WeightForm(request.POST)
       userprofile_form = UserProfileForm(request.POST)
       basic_form = BasicForm(request.POST)
       sleep_form = SleepForm(request.POST)
       exercise_form = ExerciseForm(request.POST)
       meal_form = MealForm(request.POST)
       if all(form.is_valid() for form in [pressure_form, weight_form, userprofile_form, basic_form, sleep_form, exercise_form, meal_form]):
            record_time = now()
            #pressure = pressure_form.save(commit=False)
            #pressure.timestamp = record_time
            #pressure.user = request.user
            #pressure.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            sleep = sleep_form.save(commit=False)
            sleep.user = request.user
            sleep.timestamp = record_time
            sleep.start_time = sleep_form.save(commit=False)
            sleep.end_time = sleep_form.save(commit=False)
            sleep.save()
            exercise = exercise_form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            meal = meal_form.save(commit=False)
            meal.user = request.user
            meal.save()
            weight = weight_form.save(commit=False)
            weight.timestamp = record_time
            weight.user = request.user
            #weight._bmi = weight.bmi()
            weight.save()
            return redirect('user_dashboard')
    else:
        print "else"
        pressure_form = PressureForm()
        weight_form = WeightForm()
        userprofile_form = UserProfileForm()
        basic_form = BasicForm()
        sleep_form = SleepForm()
        exercise_form = ExerciseForm()
        meal_form = MealForm()
    context = {
        'pressure_form': pressure_form,
        'weight_form': weight_form,
        'userprofile_form': userprofile_form,
        'basic_form' : basic_form,
        'sleep_form' : sleep_form,
        'exercise_form' : exercise_form,
        'meal_form' : meal_form,
    }
    return render(request, 'messurements/messurement_form.html', context)
########################################################################

@login_required
def AllView(request):
    if request.method == 'POST':
       pressure_form = PressureForm(request.POST)
       weight_form = WeightForm(request.POST)
       userprofile_form = UserProfileForm(request.POST)
       basic_form = BasicForm(request.POST)
       sleep_form = SleepForm(request.POST)
       exercise_form = ExerciseForm(request.POST)
       meal_form = MealForm(request.POST)
       if all(form.is_valid() for form in [pressure_form, weight_form, userprofile_form, basic_form, sleep_form, exercise_form, meal_form]):
            record_time = now()
            basic = basic_form.save(commit=False)
            basic.user = request.user
            basic.gender = basic_form.save(commit=False)
            basic.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            pressure = pressure_form.save(commit=False)
            pressure.timestamp = record_time
            pressure.user = request.user
            pressure.save()
            sleep = sleep_form.save(commit=False)
            sleep.user = request.user
            sleep.timestamp = record_time
            sleep.start_time = sleep_form.save(commit=False)
            sleep.end_time = sleep_form.save(commit=False)
            sleep.save()
            exercise = exercise_form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            meal = meal_form.save(commit=False)
            meal.user = request.user
            meal.save()
            weight = weight_form.save(commit=False)
            weight.timestamp = record_time
            weight.user = request.user
            #weight._bmi = weight.bmi()
            weight.save()
            return redirect('user_dashboard')
    else:
        print "else"
        pressure_form = PressureForm()
        weight_form = WeightForm()
        userprofile_form = UserProfileForm()
        basic_form = BasicForm()
        sleep_form = SleepForm()
        exercise_form = ExerciseForm()
        meal_form = MealForm()
    context = {
        'pressure_form': pressure_form,
        'weight_form': weight_form,
        'userprofile_form': userprofile_form,
        'basic_form' : basic_form,
        'sleep_form' : sleep_form,
        'exercise_form' : exercise_form,
        'meal_form' : meal_form,
    }
    return render(request, 'messurements/all_form.html', context)