# Generated by Django 4.2 on 2023-05-10 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_passport'),
        ('purchase', '0002_alter_purchase_date_alter_purchase_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='user.user'),
        ),
    ]