from rest_framework.viewsets import ModelViewSet
from localizacao.models import Localizacao
from .serializers import LocalizacaoSerializer

class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer