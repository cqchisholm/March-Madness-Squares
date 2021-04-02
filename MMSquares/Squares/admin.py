from django.contrib import admin

from .models import SquaresCSV, WinningNumbers, LosingNumbers

admin.site.register(SquaresCSV)
admin.site.register(WinningNumbers)
admin.site.register(LosingNumbers)