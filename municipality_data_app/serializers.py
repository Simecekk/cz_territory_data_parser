from rest_framework import serializers
from municipality_data_app.models import Obec, Orp, Pou

class PouSerializer(serializers.ModelSerializer):
    obec = serializers.SerializerMethodField()
    orp = serializers.SerializerMethodField()

    class Meta:
        model = Pou
        fields = '__all__'

    def get_obec(self, obj):
        obec = obj.spravni_obec_kod
        serializer = ObecSerializer(obec)
        return serializer.data

    def get_orp(self, obj):
        orp = obj.orp_kod
        serializer = OrpSerializer(orp)
        return serializer.data

class OrpSerializer(serializers.ModelSerializer):
    obec = serializers.SerializerMethodField()

    class Meta:
        model = Orp
        fields = '__all__'

    def get_obec(self, obj):
        obec = obj.spravni_obec_kod
        serializer = ObecSerializer(obec)
        return serializer.data


class ObecSerializer(serializers.ModelSerializer):

    class Meta:
        model = Obec
        fields = '__all__' 