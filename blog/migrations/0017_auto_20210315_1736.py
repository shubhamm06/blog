# Generated by Django 3.1.7 on 2021-03-15 12:06

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210315_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, default='fgh'),
            preserve_default=False,
        ),
    ]
