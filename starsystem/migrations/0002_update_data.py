from django.db import migrations

def fix_planets(apps, schema_editor):
    Planet = apps.get_model('starsystem', 'Planet')
    i = 0
    for planet in Planet.objects.all():
        planet.name = f'planet {i}'
        planet.save()


class Migration(migrations.Migration):

    dependencies = [
        ('starsystem', '0001_initial'),
    ],
    operations = [
        migrations.RunPython(fix_planets),
    ]