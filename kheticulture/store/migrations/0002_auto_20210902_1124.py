# Generated by Django 3.2.7 on 2021-09-02 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='store.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='store.producttype'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='', help_text='Required', max_length=255, verbose_name='title'),
        ),
    ]