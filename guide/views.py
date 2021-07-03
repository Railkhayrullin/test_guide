from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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
    """Получение элементов заданного справочника указанной версии"""
    queryset = GuideElement.objects.all()
    serializer_class = GuideElementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = GuideElementFilter
    filterset_fields = ('guide', 'version')


class GuideActualElementView(APIView):
    """Получение элементов заданного справочника текущей версии"""
    def get(self, request, guide):
        if GuideElement.objects.filter(guide__name=guide).exists():
            guide = GuideElement.objects.filter(guide__name=guide).latest('guide__date')
            serializer = GuideElementSerializer(guide)
            return Response(serializer.data)
        else:
            return Response({'Element Not Found': 'No such element'}, status=status.HTTP_404_NOT_FOUND)


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
        'guide', 'date', 'version', 'code', 'value'
    )
