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

### INDEX ###
def index(request):
    # сортировка перенесена в moderls -> Meta class
    #bbs = Bb.objects.order_by('-published')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


### RUBRIC ###
from .models import Rubric

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context= {'bbs': bbs, 'rubrics': rubrics,
              'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

### ADD FORM ###
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BbForm

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


