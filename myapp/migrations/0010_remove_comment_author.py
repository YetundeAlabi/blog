# Generated by Django 4.2 on 2023-04-17 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_remove_post_comment_comment_author_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="author",
        ),
    ]