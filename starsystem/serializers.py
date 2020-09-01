from rest_framework import serializers

from .models import Planet, Star


class PlanetSerializer(serializers.Serializer):
    star = serializers.CharField(max_length=100, required=True)
    name = serializers.CharField(max_length=100, required=True)
    order_from_star = serializers.IntegerField()
    has_atmosphere = serializers.BooleanField(required=False, allow_null=True)
    has_water = serializers.BooleanField(required=False, allow_null=True)

    def create(self, validated_data):
        validated_data["star"] = Star.objects.get(pk=validated_data["star"])
        return Star.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_from_star = validated_data.get(
            "order_from_star", instance.order_from_star
        )
        instance.save()
        return instance

    def validate(self, data):
        if Star.objects.filter(name=data["star"]).exists():
            star = Star.objects.get(pk=data["star"])
            if star.planets.filter(order_from_star=data["order_from_star"]).exists():
                raise serializers.ValidationError(
                    "dont put two planets on same orbit, you fool"
                )
        else:
            raise serializers.ValidationError("no star found :(")
        return data


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = "__all__"

    def create(self, validated_data):
        self.is_valid()
