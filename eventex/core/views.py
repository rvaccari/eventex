from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from eventex.core.models import Speaker, Talk, Cancelado

home = ListView.as_view(template_name='index.html',
                        model=Speaker)

speaker_detail = DetailView.as_view(model=Speaker)

talk_list = ListView.as_view(model=Talk)


def cancela(request):
    Cancelado.objects.create(resposta=request.GET)
    Cancelado.objects.create(resposta=request.POST)
    return HttpResponse('ok')
