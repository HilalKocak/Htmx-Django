from django.contrib import admin
from .models import User, DataFile, Dashboard, Charts
# Register your models here.


admin.site.register(User)
admin.site.register(DataFile)
admin.site.register(Dashboard)
admin.site.register(Charts)