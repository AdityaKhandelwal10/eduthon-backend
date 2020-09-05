from django.forms import ModelForm
from indv.models import IndvTask

class IndvTaskForm(ModelForm):
    class Meta:
        model = IndvTask
        fields = '__all__'



