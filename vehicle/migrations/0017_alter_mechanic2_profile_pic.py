# Generated by Django 4.0.5 on 2022-07-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0016_alter_mechanic2_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic2',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic/MechanicProfilePic2/'),
        ),
    ]