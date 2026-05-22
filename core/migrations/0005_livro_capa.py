# Generated manually for optional book cover uploads.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_acompanhamento_livro"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="capa",
            field=models.ImageField(blank=True, null=True, upload_to="capas/"),
        ),
    ]
