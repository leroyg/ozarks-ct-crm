# Generated by Django 3.1.7 on 2021-03-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.DateField(help_text='01-30-2001', null=True)),
                ('contact_phone', models.CharField(help_text='+14156665555', max_length=12, null=True)),
                ('sports_team', models.CharField(choices=[('WBB', "Women's Basketball"), ('MBB', "Men's Basketball"), ('BB', 'Baseball'), ('SB', 'Softball'), ('Shoot', 'Shooting Sports'), ('XC', 'Cross Country'), ('WSC', "Women's Soccer"), ('MSC', "Men's Soccer"), ('TNS', 'Tennis'), ('SD', 'Swimming & Diving'), ('TR', 'Track'), ('WWR', "Women's Wrestling"), ('MWR', "Men's Wrestling")], max_length=5, null=True)),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2, null=True)),
            ],
        ),
    ]