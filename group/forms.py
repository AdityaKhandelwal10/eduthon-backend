from django.forms import ModelForm
from group.models import TeamModel, GroupTasks

class TeamForm(ModelForm):
    class Meta:
        model = TeamModel
        fields = ['members', 'name']

class GroupTasksForm(ModelForm):
    class Meta:
        model = GroupTasks
        fields = ['task', 'team']
