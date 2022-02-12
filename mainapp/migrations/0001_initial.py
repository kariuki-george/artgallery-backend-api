# Generated by Django 4.0.1 on 2022-02-12 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artcategory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usercategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usercategory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phonenumber', models.IntegerField(default=400)),
                ('accesstoken', models.CharField(max_length=100)),
                ('refreshtoken', models.CharField(max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Novels', to='mainapp.usercategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=400)),
                ('imageurl', models.ImageField(upload_to='images')),
                ('pages', models.IntegerField(default=400)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Textbook', to='mainapp.artcategory')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designer', to='mainapp.user')),
            ],
        ),
    ]
