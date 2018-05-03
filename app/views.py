from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Carro
# Create your views here.

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano',
            'valor', 'data_cadastro']

def Cadastrar_Carro(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, 'carro_form',{'form':form})