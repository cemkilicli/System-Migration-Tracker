from django.shortcuts import render
from django.views.generic import TemplateView
from . models import MigrationSteps, MigrationPhase
from collections import defaultdict


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'
    
    

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        
        comp = defaultdict(dict)

        for phase in MigrationPhase.objects.all():
            
            
            
            total_values = phase.migration_steps.values('migration_step_status').count()
            total_completed = phase.migration_steps.values('migration_step_status').filter(migration_step_status__status__contains='Completed').count()
            total_started = phase.migration_steps.values('migration_step_status').filter(migration_step_status__status__contains='In Progress').count()
            
            if total_completed == 0:
                complition_percent = 0
            else:
                complition_percent = total_completed / total_values * 100
            
            comp[phase]['phase_complition_percent'] = complition_percent
            
            if complition_percent == 0:
    
                if total_started == 0:
                    comp[phase]['phase_status'] = 'Not Started'
                    comp[phase]['phase_status_color'] = 'badge-secondary'
                    comp[phase]['phase_status_progress_bar'] = 'progress-bar progress-bar-striped progress-bar-animated bg-secondary'
                else:
                    comp[phase]['phase_status'] = 'In Progress'
                    comp[phase]['phase_status_color'] = 'progress-bar-striped progress-bar-animated badge-primary'
                    comp[phase]['phase_status_progress_bar'] = 'progress-bar progress-bar-striped progress-bar-animated'
                    
            elif complition_percent > 0 and complition_percent < 100:
                comp[phase]['phase_status'] = 'In Progress'
                comp[phase]['phase_status_color'] = 'progress-bar-striped progress-bar-animated badge-primary'
                comp[phase]['phase_status_progress_bar'] = 'progress-bar progress-bar-striped progress-bar-animated'
            else:
                comp[phase]['phase_status'] = 'Completed'
                comp[phase]['phase_status_color'] = 'badge-success'
                comp[phase]['phase_status_progress_bar'] = 'progress-bar bg-success'
                    
       

           
            
        comp.default_factory = None
        
        print(comp)

        contex['migration_phases'] = comp
        
        return contex


