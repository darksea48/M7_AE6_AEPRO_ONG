from django import forms
from .models import Voluntario, Evento



class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', 'email' , 'telefono']
        labels = {
            'nombre': 'Ingresa tu nombre',
            'email': 'Ingresa tu email',
            'telefono': 'Ingresa tu telefono',    
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento 
        field = ['titulo', 'descripcion', 'fecha']
        labels = {
            'titulo': 'Titulo del evento',
            'descripcion': 'Descripcion del Evento',
            'fecha': 'Fecha',    
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        }