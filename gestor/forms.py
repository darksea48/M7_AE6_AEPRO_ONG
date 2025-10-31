from django import forms
from .models import Voluntario, Evento
from datetime import date

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
        fields = ['titulo', 'descripcion', 'fecha']
        labels = {
            'titulo': 'Titulo del evento',
            'descripcion': 'Descripcion del Evento',
            'fecha': 'Fecha',    
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise forms.ValidationError("La fecha del evento no puede ser en el pasado.")
        return fecha