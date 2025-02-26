from django.shortcuts import render , redirect
from .models import Usuario
from .forms import UsuarioForm
# Create your views here.
def register_view(request):
    if request.method == 'GET':
        form = UsuarioForm()
        return render(request, 'usuarios/register.html', {'form': form})
    if request.method =='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:criar')
        
def list_view(request):
    usuarios = Usuario.objects.all()
    if usuarios:
        return render(request, 'usuarios/list.html', {'usuarios': usuarios})
    return render(request , 'usuarios/list.html')
