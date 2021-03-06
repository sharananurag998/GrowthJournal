# Generated by Django 3.0.4 on 2020-03-21 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.TextField(null=True)),
                ('personal_goals', models.TextField(null=True)),
                ('professional_goals', models.TextField(null=True)),
                ('motivation', models.TextField(null=True)),
                ('happiness', models.TextField(null=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
