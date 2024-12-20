from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def func_prod(request):
    return render(request, 'func_prodact.html')


class Class_prod(TemplateView):
    template_name = 'class_prodact.html'
