# Generated by Django 4.0 on 2022-02-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='watering',
            name='date',
            field=models.DateField(verbose_name='Watering Date'),
        ),
        migrations.AddField(
            model_name='plant',
            name='categories',
            field=models.ManyToManyField(to='main_app.Category'),
        ),
    ]
