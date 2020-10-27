from django.shortcuts import render

def get_data(pais):
    #
    #
    #
    #


def index(request):
    user = #
    data = get_data(user.pais)
    context = {
        'confirmados': get_data(),
        'total': get_data()
    }
    return render(request, 'index.html', context)

