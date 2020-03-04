from django.db import models

# Create your models here.
class SpaceObject(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Star(SpaceObject):
    TYPE_M = "M"
    TYPE_G = "G"
    STAR_TYPES = [(TYPE_M, "Red star"), (TYPE_G, "Yellow star")]
    star_type = models.CharField(choices=STAR_TYPES, default=TYPE_G, max_length=2)


class PlanetLike(SpaceObject):
    has_water = models.BooleanField(default=False)
    has_atmosphere = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Planet(PlanetLike):
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name="planets")
    order_from_star = models.IntegerField()
    distance_from_star = models.FloatField(null=True, blank=True)
