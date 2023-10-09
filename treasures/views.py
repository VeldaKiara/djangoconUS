from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from treasures.models import Treasure
from treasures.serializers import TreasureSerializer

class TreasureListView(ListAPIView):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer

class TreasureDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer

class TreasureCreateView(CreateAPIView):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer