from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from localizacao.api.serializers import LocalizacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True) #tem o argumento pq é de muitos pra muitos
    localizacao = LocalizacaoSerializer()
    descricao_full = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id','nome','descricao','aprovado','foto','atracoes','comentario','avaliacao','localizacao', 'descricao_full')

    def get_descricao_full(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)