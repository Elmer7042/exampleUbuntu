from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from preguntasyrespuestas.form import PreguntaForm
from preguntasyrespuestas.models import Pregunta


def index(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'preguntasyrespuestas/index.html', {'preguntas': preguntas})


def pregunta_detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, 'preguntasyrespuestas/pregunta_detalle.html', {'pregunta': pregunta})


'''
def pregunta_crear(request):
    form = PreguntaForm()
    return render(request, 'preguntasyrespuestas/pregunta_crear.html', {'form': form})
'''


@login_required
def pregunta_crear(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            #pregunta = Pregunta(asunto=form.cleaned_data['asunto'], descripcion=form.cleaned_data['descripcion'], fecha_publicacion=timezone.now())
            #pregunta.save()
            return redirect('preguntas')
    else:
        form = PreguntaForm()
        return render(request, 'preguntasyrespuestas/pregunta_crear.html', {'form': form})


@login_required
def pregunta_editar(request,pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    if request.method == 'POST':
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('pregunta_detalle', pregunta_id)
    else:
        form = PreguntaForm(instance=pregunta)
        return render(request, 'preguntasyrespuestas/pregunta_editar.html', {'form': form})



