# Generated by Django 2.1 on 2018-08-20 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='coin',
            name='quantity',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=24),
        ),
        migrations.AddField(
            model_name='coin',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.User'),
        ),
    ]
