# Generated by Django 2.2 on 2019-04-21 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('group', models.CharField(choices=[('MV', 'movies'), ('GA', 'games'), ('BO', 'books')], max_length=2)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
        ),
    ]