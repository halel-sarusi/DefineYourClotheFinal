# Generated by Django 3.0.4 on 2020-07-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20200720_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='basket',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
