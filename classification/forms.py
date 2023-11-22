from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.forms.widgets import PasswordInput, TextInput
from .models import *
from django import forms 


class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']
class CompteForm(forms.ModelForm):
    class Meta:
        model= Compte
        fields=['roles']
class CreateCommentaire(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
    rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),required=True)
    class Meta:
        model=Commentaire  
        fields=['body','rate']  
        
    def __init__(self, user, *args, **kwargs):
        super(CreateCommentaire, self).__init__(*args, **kwargs) 
        
class UpdateMed(forms.ModelForm):

    class Meta:
        model=Medecin
        fields= '__all__' 
        exclude=['compte','note']   
    def __init__(self, user, *args, **kwargs):
        super(UpdateMed, self).__init__(*args, **kwargs)    
        compte=Compte.objects.get(user=user) 
        self=Medecin.objects.get(compte=compte)    
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['message','Name','email']