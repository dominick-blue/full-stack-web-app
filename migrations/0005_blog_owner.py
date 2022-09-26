# Generated by Django 4.0.6 on 2022-08-24 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('blogs', '0004_blog_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]