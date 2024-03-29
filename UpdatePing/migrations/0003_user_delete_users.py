# Generated by Django 4.2.1 on 2023-05-29 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UpdatePing', '0002_alter_users_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=200)),
                ('games', models.ManyToManyField(related_name='user_games', to='UpdatePing.game')),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
