# Generated manually for BookTracker book details.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_livro_favorito"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="ano",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="genero",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="livro",
            name="formato",
            field=models.CharField(
                choices=[
                    ("livro", "Livro"),
                    ("manga", "Manga"),
                    ("light_novel", "Light novel"),
                    ("manhwa", "Manhwa"),
                    ("manhua", "Manhua"),
                    ("hq", "HQ"),
                    ("outro", "Outro"),
                ],
                default="livro",
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name="livro",
            name="enredo",
            field=models.TextField(blank=True),
        ),
        migrations.RemoveField(
            model_name="livro",
            name="resenha",
        ),
    ]
