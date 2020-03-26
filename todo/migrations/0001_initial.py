# Generated by Django 2.2.4 on 2020-03-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_id', models.IntegerField(default=1)),
                ('content', models.CharField(max_length=500)),
                ('createtime', models.DateTimeField(verbose_name='publish time')),
                ('is_complete', models.IntegerField(default=1)),
            ],
        ),
    ]