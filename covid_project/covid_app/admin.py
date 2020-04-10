from django.contrib import admin
from covid_app.models import covid_ind, covid_data_anal

# Register your models here.
admin.site.register(covid_ind)
admin.site.register(covid_data_anal)
