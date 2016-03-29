from django.contrib import admin

from .models import Team, Player


class PlayerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Info', 		{'fields': ['player_name', 'position', 'team', 'nationality', 'height', 'weight', 'age']}),
		('Stats', 	{'fields': ['appearances', 'goals', 'assists', 'fouls_per_game', 'yellow_cards', 'red_cards']}),
	]

	list_display = ('player_name', 'team')

	search_fields = ['player_name']

# Register your models here.

admin.site.register(Team)
# admin.site.register(Player)
admin.site.register(Player, PlayerAdmin)
# admin.site.register(Attacker)
# admin.site.register(Midfielder)
# admin.site.register(Defender)