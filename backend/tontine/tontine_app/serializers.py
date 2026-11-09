from rest_framework import serializers
from .models import Versement

class VersementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versement
        fields = ['id', 'description', 'montant', 'date_versement']
        read_only_fields = ['id', 'date_versement']  #* valeurs de ces champs sont générées automatiquement