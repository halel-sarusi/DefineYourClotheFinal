# Generated by Django 3.0.4 on 2020-07-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='dateCompleted',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='isImportant',
        ),
        migrations.AddField(
            model_name='todo',
            name='basket',
            field=models.CharField(choices=[('D', 'Dark'), ('LS', 'Ligth Soft'), ('DS', 'Dark Soft')], default='D', max_length=3),
        ),
        migrations.AddField(
            model_name='todo',
            name='color',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='todo',
            name='item_type',
            field=models.CharField(choices=[('SHI', 'Shirts'), ('P', 'Pants'), ('SK', 'Skirts'), ('D', 'Dresses'), ('SHO', 'Shoes')], default='D', max_length=3),
        ),
    ]
