from django.contrib import admin

from .models import Pizza, Sub, Platter, Pasta, Topping, Salad

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Platter)
admin.site.register(Pasta)
admin.site.register(Topping)
admin.site.register(Salad)
