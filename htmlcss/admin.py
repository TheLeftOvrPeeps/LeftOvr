from django.contrib import admin
from .models import Customer
from .models import Restaurant
from .models import Meals
from .models import slots

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Meals)
admin.site.register(slots)