from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def fiitPage(request):
    return render(request, 'main/fiitPage.html')


def kbPage(request):
    return render(request, 'main/kbPage.html')


def ivtPage(request):
    return render(request, 'main/ivtPage.html')


def piPage(request):
    return render(request, 'main/piPage.html')


def moaisPage(request):
    return render(request, 'main/moaisPage.html')


def siPage(request):
    return render(request, 'main/siPage.html')


def ish(request):
    return render(request, 'main/ish.html')



def pedPage(request):
    return render(request, 'main/pedPage.html')

