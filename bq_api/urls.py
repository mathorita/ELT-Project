from django.urls import path
from api.views import YearCountView

urlpatterns = [
    path('year-counts/', YearCountView.as_view()),
]