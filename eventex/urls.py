from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from eventex.core.views import home, speaker_detail, talk_list, cancela

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls',
                               namespace='subscriptions')),
    path('palestras/', talk_list, name='talk_list'),
    path('palestrantes/<slug>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
    path('cancela', cancela, name='cancela')
]
