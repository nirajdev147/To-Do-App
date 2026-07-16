from django.contrib import admin
from .models import Task, Category

# This makes your custom tables visible in the admin panel
admin.site.register(Task)
admin.site.register(Category)
