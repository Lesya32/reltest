from django.shortcuts import render
from .models import MPS


def index(request):
    # data = {'title': 'Главная страница',
    #        'massiv': ['som1', 'som2', 'som3'],
    #       'slovar': {
    #           'car': 'bmw',
    #           'age': 18,
    #           'hobby': 'nohobby'
    #      }
    #      }
    # return render(request, 'Otchet/index.html', data)

    #news = PacPolic.objects.get(ss = '002-003-362 49')
    news = MPS.objects.all()
    print(    news )
    #for e in PacPolic.objects.all()[:5]:
    #    print(e.ss)


    #b = PacPolic(ss='102-003-362 49', npp='2726')
    #b.save()

    #b = PacPolic.objects.get(ss='102-003-362 49')
    #b.npp_1 = '5'
    #b.save()

    return render(request, 'Otchet/index.html', {'news': news})
