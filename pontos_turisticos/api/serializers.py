from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from localizacao.api.serializers import LocalizacaoSerializer
from localizacao.models import Localizacao

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True) #tem o argumento pq é de muitos pra muitos
    localizacao = LocalizacaoSerializer(read_only=True)
    descricao_full = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id','nome','descricao','aprovado','foto','atracoes','comentario','avaliacao','localizacao', 'descricao_full')
        read_only_fields = ('comentario', 'avaliacao')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data('atracoes')
        del validated_data['atracoes']
        localizacao = validated_data('localizacao')
        del validated_data['localizacao']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        loc = Localizacao.objects.create(**localizacao)
        ponto.localizacao = loc
        ponto.save()
        return ponto

    def get_descricao_full(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
