# Generated by Django 2.2.4 on 2019-08-18 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsamuems', '0006_auto_20190817_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergenciasnippet',
            old_name='diagonostico',
            new_name='diagnostico',
        ),
    ]
