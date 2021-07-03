from django_filters import rest_framework as filters

from guide.models import GuideElement, Guide


class GuideFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='contains')

    class Meta:
        model = Guide
        fields = ('date', )


class GuideElementFilter(filters.FilterSet):
    guide = filters.CharFilter(field_name='guide__name', lookup_expr='exact')
    version = filters.CharFilter(field_name='guide__version', lookup_expr='exact')

    class Meta:
        model = GuideElement
        fields = ('guide', 'version')


class GuideElementValidationFilter(filters.FilterSet):
    guide = filters.CharFilter(field_name='guide__name', lookup_expr='exact')
    date = filters.CharFilter(field_name='guide__date', lookup_expr='contains')
    version = filters.CharFilter(field_name='guide__version', lookup_expr='exact')
    code = filters.CharFilter(field_name='element_code', lookup_expr='exact')
    value = filters.CharFilter(field_name='element_value', lookup_expr='contains')

    class Meta:
        model = GuideElement
        fields = ('guide', 'date', 'version', 'code', 'value')
