from django.urls import path
from django.views.generic import TemplateView
from treasures.views import TreasureListView, TreasureDetailView, TreasureCreateView
app_name='treasures'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('treasures/', TreasureListView.as_view(), name='treasure-list'),
    path('treasures/<uuid:pk>/', TreasureDetailView.as_view(), name='treasure-detail'),
    path('treasures/create/', TreasureCreateView.as_view(), name='treasure-create'),
]