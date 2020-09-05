from django.forms import ModelForm
from testApp.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'jwt']





