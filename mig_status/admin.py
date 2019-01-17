from django.contrib import admin
from .models import MigrationPhase, MigrationSteps, Team, TeamMemebers, TeamType, Status, Todo, TeamAdmin, MigrationStepsAdmin, MigrationPhaseAdmin

# Register your models here.

admin.site.register(MigrationPhase, MigrationPhaseAdmin)
admin.site.register(MigrationSteps, MigrationStepsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMemebers)
admin.site.register(TeamType)
admin.site.register(Status)
admin.site.register(Todo)
