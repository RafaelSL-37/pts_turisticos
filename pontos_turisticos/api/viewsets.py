from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('nome','descricao', 'localizacao__linha1')
    lookup_field = 'nome' #tem que ser unique, quando tem mais de um retorna erro
    '''
    ^ -> starts with
    = -> exact
    @ -> search
    $ -> regex
    '''

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id) #cria o queryset
        if nome:
            queryset = queryset.filter(nome__iexact=nome) #adiciona filtro, adiciona __iexact pra case sensitive
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
        #return PontoTuristico.objects.filter(aprovado=True)

'''
    def list(self, request, *args, **kwargs):
        pass
        #return Response({'teste': 123})

    def create(self, request, *args, **kwargs):
        pass
        #return Response({'Hello': request.data['nome']})
        #return super(PontoTuristicoViewSet, self).create(self, request, *args, **kwargs) #VOLTA METODO MAE

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass
'''