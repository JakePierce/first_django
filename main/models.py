from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    abbrev = models.CharField(max_length=255, null=True, blank=True)
    pop = models.CharField(max_length=255, null=True, blank=True)
    state_map = models.ImageField(upload_to='state_map', null=True, blank=True)


    def __unicode__(self):
        return self.name


class StateCapital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    #state = models.ForeignKey('main.State', null=True, blank=True)
    #state = models.ManyToManyField('main.State', null=True, blank=True)
    state = models.OneToOneField('main.State', null=True, blank=True)

    def __unicode__(self):
        return self.name

class City(models.Model):
    zip_code = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(max_length=255, null=True, blank=True)
    lon = models.FloatField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey('main.State', null=True, blank=True)
    abbrev = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

    