# Generated by Django 4.1 on 2023-11-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("icmp_cou", models.CharField(max_length=128)),
                ("tcp_cou", models.CharField(max_length=128)),
                ("udp_cou", models.CharField(max_length=128)),
                ("ip_cou", models.CharField(max_length=256)),
            ],
        ),
    ]