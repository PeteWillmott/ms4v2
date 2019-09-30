# Generated by Django 2.2.5 on 2019-09-30 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('sale_status', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('era', models.CharField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='images')),
                ('start', models.DateTimeField(null=True, verbose_name='Auction starts')),
                ('finish', models.DateTimeField(null=True, verbose_name='Auction finishes')),
                ('reserve', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('increment', models.DecimalField(decimal_places=2, default=10, max_digits=10)),
                ('bid', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('last_bidder', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
