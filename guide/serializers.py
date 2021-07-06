from rest_framework import serializers

from guide.models import Guide, GuideElement


class GuideSerializer(serializers.ModelSerializer):
    """Список справочников"""

    class Meta:
        model = Guide
        fields = '__all__'


class GuideElementSerializer(serializers.ModelSerializer):
    """Список элементов справочника"""
    # Для того, чтобы у справочника выводилось поле "name" а не id поля, прописываем параметр guide.
    # Для понимания к какому справочнику относится элемент - добавил поля "guide_version" и "guide_date".
    guide = serializers.SlugRelatedField(slug_field='name', read_only=True)
    guide_version = serializers.CharField(source='guide.version', read_only=True)
    guide_date = serializers.DateField(source='guide.date', read_only=True)

    class Meta:
        model = GuideElement
        fields = (
            'id',
            'guide',
            'guide_version',
            'guide_date',
            'element_code',
            'element_value'
        )
