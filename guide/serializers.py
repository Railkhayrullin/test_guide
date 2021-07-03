from rest_framework import serializers

from guide.models import Guide, GuideElement


class GuideSerializer(serializers.ModelSerializer):
    """Список справочников"""
    class Meta:
        model = Guide
        fields = '__all__'


class GuideElementSerializer(serializers.ModelSerializer):
    """Список элементов справочника"""
    # Для того, чтобы у справочника выводилось поле "name" а не id поля, прописываем параметр guide
    # Для удобства получаем поле с версией справочника - "guide_version"
    guide = serializers.SlugRelatedField(slug_field='name', read_only=True)
    guide_version = serializers.CharField(source='guide.version', read_only=True)

    class Meta:
        model = GuideElement
        fields = ('id', 'guide', 'guide_version', 'element_code', 'element_value')
