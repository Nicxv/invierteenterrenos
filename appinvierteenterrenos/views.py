from django.shortcuts import render

# Create your views here.


def principal(request):
    return render(request, 'principal.html')

def terrenos(request):
    return render(request, 'terrenos.html')
def asesores(request):
    return render(request, 'asesores.html')
