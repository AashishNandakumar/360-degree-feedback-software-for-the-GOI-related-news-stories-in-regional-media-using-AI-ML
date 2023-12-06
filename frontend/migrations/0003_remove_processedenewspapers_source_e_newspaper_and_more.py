# Generated by Django 5.0 on 2023-12-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_rename_websites_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processedenewspapers',
            name='source_e_newspaper',
        ),
        migrations.RemoveField(
            model_name='notificationslog',
            name='official_id',
        ),
        migrations.RemoveField(
            model_name='processedwebsites',
            name='source_website',
        ),
        migrations.RemoveField(
            model_name='processedyoutubevideos',
            name='source_video',
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='ENewspapers',
        ),
        migrations.DeleteModel(
            name='ProcessedENewspapers',
        ),
        migrations.DeleteModel(
            name='NotificationsLog',
        ),
        migrations.DeleteModel(
            name='PIBOfficials',
        ),
        migrations.DeleteModel(
            name='ProcessedWebsites',
        ),
        migrations.DeleteModel(
            name='ProcessedYouTubeVideos',
        ),
        migrations.DeleteModel(
            name='YouTubeVideos',
        ),
    ]