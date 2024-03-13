from django.urls import include, path
from .views import RoomDetailView, LightCalculation

urlpatterns = [
    path("room/<slug:id>", RoomDetailView.as_view()),
    path("light-calculator", LightCalculation.as_view())
]