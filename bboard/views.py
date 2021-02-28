#from django.shortcuts import render

# Create your views here.
"""
from django.http import HttpResponse
from django.template import loader
from .models import Bb

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}

    #return HttpResponse(s, content_type='text/plain; charset=utf-8')
    return HttpResponse(template.render(context,request))
"""
from django.shortcuts import render
from .models import Bb

def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'bboard/index.html',{'bbs': bbs})
