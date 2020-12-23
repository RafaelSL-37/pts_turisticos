from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #filter_backends = (DjangoFilterBackend,) #caso queira colocar filtragem de um por um
    filter_fields = ('nome','descricao')