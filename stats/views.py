from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    #context = {
    #    'total':total,
    #    'recuperados':total,
    #    'fallecidos':total,
    #   'actualizado':total,
    #    'pais':total,
    #}


    return render(request, 'stats/index.html')

