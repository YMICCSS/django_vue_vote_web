# Generated by Django 3.2.18 on 2023-04-14 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapi', '0004_alter_vote_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapi.item'),
        ),
    ]