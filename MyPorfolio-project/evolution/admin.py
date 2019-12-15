from django.contrib import admin
from .models import Player, Section, Theme, Phase, PhaseTheme


# Register your models here.
admin.site.register(Player)
admin.site.register(Section)
admin.site.register(Phase)
admin.site.register(Theme)
admin.site.register(PhaseTheme)