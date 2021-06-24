from rest_framework import serializers

from guide.models import Guide, GuideElement


class GuideSerializer(serializers.ModelSerializer):
    """Список справочников"""
    class Meta:
        model = Guide
        fields = '__all__'


class GuideElementSerializer(serializers.ModelSerializer):
    """Список элементов справочника"""
    # Для того, чтобы у guide выводилось поле "name" а не id поля, прописываем параметр guide
    guide = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = GuideElement
        fields = '__all__'
