from django.urls import path
from .views import GuideListView, GuideElementListView, GuideActualElementView, GuideElementValidation

urlpatterns = [
    path('guide/', GuideListView.as_view()),
    path('element/', GuideElementListView.as_view()),
    path('actual-element/<str:guide>', GuideActualElementView.as_view()),
    path('element-validation/', GuideElementValidation.as_view()),
]
