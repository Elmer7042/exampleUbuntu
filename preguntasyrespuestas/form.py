from django.forms import ModelForm
from preguntasyrespuestas.models import Pregunta

'''
class PreguntaForm(forms.Form):
    asunto = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(widget=forms.Textarea, required=True)
'''


class PreguntaForm(ModelForm):
    class Meta:
        model = Pregunta
        fields = '__all__'
