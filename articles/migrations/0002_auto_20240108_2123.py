# Generated by Django 3.1.14 on 2024-01-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]