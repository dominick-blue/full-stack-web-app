# Generated by Django 4.0.6 on 2022-07-21 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_tag_blog_vote_ratio_blog_vote_total_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_uuid',
            new_name='id',
        ),
    ]
