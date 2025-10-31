from django.shortcuts import render, redirect, get_object_or_404
from gestor.models import Voluntario, Evento
from gestor.forms import VoluntarioForm, EventoForm

def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'voluntarios_list.html', {'voluntarios': voluntarios})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voluntarios_list')
    else:
        form = VoluntarioForm()
    return render(request, 'voluntario_form.html', {'form': form})

def editar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('voluntarios_list')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'voluntario_form.html', {'form': form})

def eliminar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('voluntarios_list')
    return render(request, 'voluntario_confirm_delete.html', {'voluntario': voluntario})

# eventos.

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos_list.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos_list')
    else:
        form = EventoForm()
    return render(request, 'evento_form.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('eventos_list')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'evento_form.html', {'form': form})

def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('eventos_list')
    return render(request, 'evento_confirm_delete.html', {'evento': evento})