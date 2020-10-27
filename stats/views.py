from django.shortcuts import render

def index(request):
    context = {
        'total':total,
        'recuperados':total,
        'fallecidos':total,
        'actualizado':total,
        'pais':total,
    }


    return render(request, 'stats/index.html')

