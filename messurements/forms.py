from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import extras

from .models import Pressure, Weight, UserProfile, Basic, Sleep, Exercise, Meal

class PressureForm(forms.ModelForm):

    class Meta:
        model = Pressure
        exclude = ('user', 'timestamp', 'comment' )

class WeightForm(forms.ModelForm):

    class Meta:
        model = Weight
        exclude = ('user', 'timestamp', '_bmi', 'comment')
 
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user', 'targetweight','timestamp')

class BasicForm(forms.ModelForm):
    birthdate = forms.DateField(widget=extras.SelectDateWidget(required = False, years = range(2014, 1930, -1)))
    
    class Meta:
        model = Basic
        exclude = ('user', 'timestamp')

    

class SleepForm(forms.ModelForm):

    class Meta:
        model = Sleep
        exclude = ('user', 'timestamp' )

class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        exclude = ('user', 'timestamp')
 
class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        exclude = ('user', 'timestamp')
