from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


from .models import Guide, GuideElement
from .serializers import GuideSerializer, GuideElementSerializer
from .filters import GuideFilter, GuideElementFilter, GuideElementValidationFilter


class GuideListView(generics.ListAPIView):
    """Получение списка всех справочников или справочников с актуальной датой"""
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = GuideFilter
    filterset_fields = ('date',)


class GuideElementListView(generics.ListAPIView):
    """Получение элементов заданного справочника текущей версии и указанной версии"""
    queryset = GuideElement.objects.all()
    serializer_class = GuideElementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = GuideElementFilter
    filterset_fields = ('guide', 'version')


class GuideElementValidation(generics.ListAPIView):
    """
    Валидация элементов заданного справочника
    текущей версии или по указанной версии
    """
    queryset = GuideElement.objects.all()
    serializer_class = GuideElementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = GuideElementValidationFilter
    filterset_fields = (
        'guide', 'guide_date', 'guide_version', 'element_code', 'element_value'
    )
