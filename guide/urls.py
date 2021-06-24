from django.urls import path
from .views import GuideListView, GuideElementListView, GuideElementValidation

urlpatterns = [
    path('guide/', GuideListView.as_view()),
    path('element/', GuideElementListView.as_view()),
    path('element-validation/', GuideElementValidation.as_view()),
]
