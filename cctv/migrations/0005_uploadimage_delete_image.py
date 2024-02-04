# Generated by Django 5.0 on 2024-01-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0004_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='cctv/images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
