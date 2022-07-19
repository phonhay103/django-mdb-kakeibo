# Generated by Django 3.2.8 on 2022-07-19 04:45

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
            name='AssetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリ名')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリ名')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリ名')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('amount', models.IntegerField(verbose_name='金額')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.paymentcategory', verbose_name='カテゴリ')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('amount', models.IntegerField(verbose_name='金額')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.incomecategory', verbose_name='カテゴリ')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('amount', models.BigIntegerField(verbose_name='資産額')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.assetcategory', verbose_name='カテゴリ')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]