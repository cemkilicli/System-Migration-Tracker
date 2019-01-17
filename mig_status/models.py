from django.db import models
from django.contrib import admin


# Create your models here.

class TeamMemebers(models.Model):
	member_name = models.CharField(max_length=256)
	#member_email = models.EmailField(max_length=254, default="ets@etstur.com",  blank=True)
	#member_phone = models.IntegerField(blank=True)
	
	def __str__(self):
		return self.member_name
	
class TeamType(models.Model):
	team_type_name = models.CharField(max_length=256)
	
	def __str__(self):
		return self.team_type_name

class Team(models.Model):
	team_name = models.CharField(max_length=256)
	
	# ForeignKey Keys
	team_type = models.ForeignKey(TeamType, related_name='team_type', on_delete = models.CASCADE)
	
	def __str__(self):
		return self.team_name



	
class Status(models.Model):
	status = models.CharField(max_length=30)
	
	def __str__(self):
		return self.status


class MigrationSteps(models.Model):
	migration_step = models.CharField(max_length=512)
	migration_step_starts = models.TimeField(auto_now_add=False, default="00:00")
	migration_step_ends = models.TimeField(auto_now_add=False, default="00:00")
	
	# ForeignKey Keys
	step_migration_accountable = models.ForeignKey(TeamMemebers, related_name='step_migration_accountable', on_delete=models.CASCADE)
	step_migration_responsiable = models.ForeignKey(TeamMemebers, related_name='step_migration_responsiable', on_delete=models.CASCADE)
	migration_step_status = models.ForeignKey(Status, related_name='migration_step_status', on_delete=models.CASCADE, default=0)
	step_migration_consulted = models.ManyToManyField(TeamMemebers, related_name='step_migration_consulted', blank=True)
	step_migration_Informed = models.ManyToManyField(TeamMemebers, related_name='step_migration_Informed', blank=True)
	
	
	
	def __str__(self):
		return self.migration_step


class MigrationPhase(models.Model):
	migration_phase_name = models.CharField(max_length=256)
	migration_phase_description = models.CharField(max_length=1024)
	migration_steps = models.ManyToManyField(MigrationSteps, related_name='step_migration_phase')
	
	
	def __str__(self):
		return self.migration_phase_name


class Todo(models.Model):
	todo_name = models.CharField(max_length=512)
	
	def __str__(self):
		return self.todo_name
	
	
class TeamAdmin(admin.ModelAdmin):
	list_display = (
		'team_name',
		'team_type',
	)
	
class MigrationStepsAdmin(admin.ModelAdmin):
	list_display = (
		'migration_step',
		'migration_step_starts',
		'migration_step_ends',
		'step_migration_accountable',
		'step_migration_responsiable',
		'migration_step_status',


	)
	
class MigrationPhaseAdmin(admin.ModelAdmin):
	list_display = (
		'migration_phase_name',
		'migration_phase_description',
	)