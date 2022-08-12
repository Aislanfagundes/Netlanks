from django.http import HttpResponse


def home(request):
    return HttpResponse('Inicio de um sonho, esse site vai ser passa')

