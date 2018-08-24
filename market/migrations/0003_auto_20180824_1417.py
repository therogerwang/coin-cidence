# Generated by Django 2.1 on 2018-08-24 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20180820_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('usd_balance', models.DecimalField(decimal_places=2, max_digits=24)),
            ],
        ),
        migrations.AlterField(
            model_name='coin',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Balance'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]