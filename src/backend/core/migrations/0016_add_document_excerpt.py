# Generated by Django 5.1.4 on 2024-12-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0015_set_path_on_existing_documents"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="excerpt",
            field=models.TextField(
                blank=True, max_length=300, null=True, verbose_name="excerpt"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices="(('en-us', 'English'), ('fr-fr', 'French'), ('de-de', 'German'))",
                default="en-us",
                help_text="The language in which the user wants to see the interface.",
                max_length=10,
                verbose_name="language",
            ),
        ),
    ]
