# Generated by Django 4.2.4 on 2023-08-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='articles/')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(),
        ),
    ]