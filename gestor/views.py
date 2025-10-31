from django.shortcuts import render, redirect, get_object_or_404
from gestor.models import Voluntario, Evento
from gestor.formularios import VoluntarioForm, EventoForm

def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'lista_voluntarios.html', {'voluntarios': voluntarios})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm()
    return render(request, 'form_voluntario.html', {'form': form})

def editar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'voluntarios/form_voluntario.html', {'form': form})

def eliminar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('lista_voluntarios')
    return render(request, 'voluntarios/confirmar_eliminar.html', {'voluntario': voluntario})

# eventos.

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'form_evento.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'form_evento.html', {'form': form})

def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'confirmar_eliminar.html', {'evento': evento})