# Generated by Django 4.0.4 on 2022-05-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'bullet'), (2, 'food'), (3, 'travel'), (4, 'sport')], default=None),
            preserve_default=False,
        ),
    ]
