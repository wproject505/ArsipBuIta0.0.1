# Generated by Django 4.1.6 on 2023-12-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajuan', '0010_alter_danamasuk_uraian'),
    ]

    operations = [
        migrations.AddField(
            model_name='danamasuk',
            name='nomer_dana_masuk',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
