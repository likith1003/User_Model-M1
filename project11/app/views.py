from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.


def register(request):
    EUFO = UserForm()
    d = {'EUFO': EUFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        if UFDO.is_valid():
            UFDO.save()
            return HttpResponse('Done')
        return HttpResponse('Noooooooo')

    return render(request, 'register.html', d)