from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Planet, Star
from .serializers import PlanetSerializer, StarSerializer
from rest_framework.decorators import action
from rest_framework import status


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance.name

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pk = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {"pk": pk}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer

    @action(detail=True)
    def planets(self, request, *args, **kwargs):
        star = self.get_object()
        planets = Planet.objects.filter(star=star).order_by("order_from_star")
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def star_with_most_planets(self, request, *args, **kwargs):
        stars = Star.objects.all()
        leader = None
        with_score = 0
        for star in stars:
            planet_num = star.planets.count()
            if planet_num > with_score:
                leader = star
        serializer = StarSerializer(leader, many=False)
        return Response(serializer.data)


class RedPlanetViewSet(StarViewSet):
    queryset = Star.objects.filter(star_type="M")


# Create your views here.
