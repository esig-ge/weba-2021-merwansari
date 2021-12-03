from django.contrib import admin
from .models import Camp, Course, Module


# Register your models here.

admin.site.register(Course)
admin.site.register(Camp)
admin.site.register(Module)