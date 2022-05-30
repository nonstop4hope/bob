from django.http import HttpResponse


def result(request):
    return HttpResponse('ok')
