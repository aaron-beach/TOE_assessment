# Generated by Django 3.0.3 on 2020-02-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trick', models.CharField(choices=[('SI', 'Sit'), ('FT', 'Fetch'), ('ST', 'Stay'), ('RO', 'Roll Over'), ('NA', 'It is okay. My pup was stubborn too')], default='NA', max_length=2)),
                ('daily_walk', models.NullBooleanField()),
                ('age', models.PositiveIntegerField()),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='DemoModel',
        ),
    ]