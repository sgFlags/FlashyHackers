#from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from MS.models import Group
#from bootstrap3_datetime.widgets import DateTimePicker

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class CreatePartialGroupForm(forms.ModelForm):
    name = forms.CharField(label = 'Group Name:', max_length=30, help_text='*Required. Only alphabets and numbers accepted')
    #admin_name = forms.CharField(label = 'Admin Name:', max_length=30, help_text='*Required.')
    class Meta:
        model = Group
        exclude = ['admin']
