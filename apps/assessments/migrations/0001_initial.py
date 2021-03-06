# Generated by Django 2.2.2 on 2019-06-15 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entities', '0002_auto_20190615_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.URLField()),
                ('description', models.TextField()),
                ('rules', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessments', to='entities.Job')),
            ],
        ),
    ]
