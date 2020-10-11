from django.contrib import admin
from cats.models import Cat,Breed

# Register your models here.
admin.site.register(Cat)
admin.site.register(Breed)