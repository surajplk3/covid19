from django.db import models

# Create your models here.

class covid_ind(models.Model):
      confirmed = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_confirmed = models.IntegerField(null = True, db_index = True, blank = True)
      active = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_active = models.IntegerField(null = True, db_index = True, blank = True)
      recovered = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_recovered = models.IntegerField(null = True, db_index = True, blank = True)
      deaths = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_deaths = models.IntegerField(null = True, db_index = True, blank = True)
      
class covid_data_anal(models.Model):
      
      daily_confirm = models.ImageField(upload_to = 'graphs', blank = True)
      monthly_confirm = models.ImageField(upload_to = 'graphs', blank = True)
      daily_recov = models.ImageField(upload_to = 'graphs', blank = True)
      daily_decease = models.ImageField(upload_to = 'graphs', blank = True)
      daily_hospitalize = models.ImageField(upload_to = 'graphs', blank = True)
      age_distribution = models.ImageField(upload_to = 'graphs', blank = True)
      