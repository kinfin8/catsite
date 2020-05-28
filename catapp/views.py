from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .models import Breed
from .models import Cat
from .models import Human
from .models import Home
from .serializers import BreedSerializer
from .serializers import CatSerializer
from .serializers import HumanSerializer
from .serializers import HomeSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all().order_by('id')
    serializer_class = BreedSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('id')
    serializer_class = CatSerializer


class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all().order_by('id')
    serializer_class = HumanSerializer


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer