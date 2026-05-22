# Generated manually for BookTracker reading activity.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_livro_detalhes_obra"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="enredo",
            new_name="sinopse",
        ),
        migrations.AddField(
            model_name="livro",
            name="pagina_atual",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="livro",
            name="total_paginas",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="resenha",
            field=models.TextField(blank=True),
        ),
    ]
