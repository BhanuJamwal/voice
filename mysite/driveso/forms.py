from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from driveso.models import UserProfile

class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    #is_verified = forms.BooleanField(initial=False)
    
    class Meta:
        model = User
        fields = ('username', 
            'phone_number',
            'password1',
            'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.phone_number = self.cleaned_data['phone_number']
        #user.is_verified = False
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            
        return user




