from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.ForeignKey(User)
    height = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    targetweight =models.IntegerField(blank=True, null=True, 
                    verbose_name= _("Target weight (kg)"),
                    help_text=_("Weight you want to reach in full kg"))
    def __unicode__(self):
        return u'-'.join([self.user.username, unicode(self.id)])
class Basic (models.Model):
    user = models.ForeignKey(User)
    CATEGORY_CHOICES = (
            ('M','Male'),
            ('F','Female'),
            )
    gender = models.CharField(max_length = 1, choices = CATEGORY_CHOICES)
    #birthday = models.DateField()
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
class Sleep (models.Model):
    user = models.ForeignKey(User)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")

class Exercise (models.Model):
    user = models.ForeignKey(User)
    EXERCISE_CHOICES = (
            ('Badminton','Badminton'),
            ('Baseball','Baseball'),
            ('Basketball','Basketball'),
            ('jogging','jogging'),
            ('soccer','soccer'),
            ('rope skipping','rope skipping'),
            ('tennis','tennis'),   
            ('others','others'),
            )
    kind = models.CharField(max_length=10, choices=EXERCISE_CHOICES )
    how_long = models.CharField(max_length=10)
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")

class Meal (models.Model):
    user = models.ForeignKey(User)
    breakfast = models.CharField(max_length=250)
    how_much = models.CharField(max_length=10)
    lunch = models.CharField(max_length=250)
    how_much2 = models.CharField(max_length=10)
    dinner = models.CharField(max_length=250)
    how_much3 = models.CharField(max_length=10)
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
class Pressure (models.Model):
    user = models.ForeignKey(User)
    sys = models.FloatField(blank=False, null=False, verbose_name=_(u"systolic"))
    dia = models.FloatField(blank=False, null=False, verbose_name=_(u"diastolic"))
    pulse = models.IntegerField(blank=False, null=False, verbose_name=_(u"Pulse"))
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")

class Weight(models.Model):
    user = models.ForeignKey(User)
    weight = models.FloatField(blank=False, null=False, verbose_name=_(u"Weight"))
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    comment = models.TextField(blank=True, null=True)

    # Hidden fields
    # Remember to be also inserted into list of hidden fields on forms/views 
    #_bmi = models.FloatField(blank=True, null=True)

    #def bmi(self):
    #    height = UserProfile.objects.get(pk=self.user.id).height
    #    if height:
    #        bmi = self.weight / (height **2 ) * 10000
    #    return bmi
        
    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
