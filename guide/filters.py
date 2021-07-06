from django_filters import rest_framework as filters
from datetime import date

from guide.models import GuideElement, Guide


class GuideFilter(filters.FilterSet):
    date = filters.DateFilter(method='date_filter')

    class Meta:
        model = Guide
        fields = ('date',)

    def date_filter(self, queryset, name, value):
        request_date = self.request.GET.get('date')
        filtered_qs = queryset.filter(date__lte=request_date) \
                              .order_by('name', '-date') \
                              .distinct('name')
        return filtered_qs


class GuideElementFilter(filters.FilterSet):
    guide = filters.CharFilter(method='guide_filter')
    version = filters.CharFilter(field_name='guide__version', lookup_expr='exact')

    class Meta:
        model = GuideElement
        fields = ('guide', 'version')

    def guide_filter(self, queryset, name, value):
        if self.request.GET.get('version'):
            guide = self.request.GET.get('guide')
            filtered_qs = queryset.filter(guide__name=guide)
            return filtered_qs
        else:
            current_date = date.today()
            guide = self.request.GET.get('guide')
            filtered_qs = queryset.filter(guide__name=guide, guide__date__lte=current_date) \
                                  .order_by('guide__name', '-guide__date') \
                                  .distinct('guide__name')
            return filtered_qs


class GuideElementValidationFilter(filters.FilterSet):
    guide = filters.CharFilter(field_name='guide__name', lookup_expr='exact')
    date = filters.CharFilter(field_name='guide__date', lookup_expr='contains')
    version = filters.CharFilter(field_name='guide__version', lookup_expr='exact')
    code = filters.CharFilter(field_name='element_code', lookup_expr='exact')
    value = filters.CharFilter(field_name='element_value', lookup_expr='contains')

    class Meta:
        model = GuideElement
        fields = (
            'guide',
            'date',
            'version',
            'code',
            'value'
        )
