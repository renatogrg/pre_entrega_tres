from django import forms


class CreacionCarroFormulario(forms.Form):
    modelo = forms.CharField(max_length=80)
    marca = forms.CharField(max_length=80)
    precio = forms.IntegerField()
    año_fabricacion = forms.IntegerField()
    
    
    
class BuscarCarro(forms.Form):
    modelo = forms.CharField(max_length=80, required=False)