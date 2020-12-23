"""pts_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from django.conf import settings #GAMBI PRA TESTE
from django.conf.urls.static import static #GAMBI
from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet
from comentarios.api.viewsets import ComentarioViewSet
from localizacao.api.viewsets import LocalizacaoViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'localizacao', LocalizacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #GAMBI
