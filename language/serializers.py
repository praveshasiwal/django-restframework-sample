from rest_framework import serializers
from .models import Language

class LanguageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Language
        fields = ('id', 'url', 'name', 'paradigm')