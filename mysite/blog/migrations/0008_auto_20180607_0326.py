# Generated by Django 2.0.6 on 2018-06-07 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpage_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
