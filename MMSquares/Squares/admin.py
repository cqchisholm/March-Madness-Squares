from django.contrib import admin

from .models import RoundAmounts, SquaresCSV, Players, WinningNumbers, LosingNumbers

admin.site.register(SquaresCSV)
admin.site.register(Players)
admin.site.register(WinningNumbers)
admin.site.register(LosingNumbers)
admin.site.register(RoundAmounts)