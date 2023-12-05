# Generated by Django 5.0 on 2023-12-05 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ENewspapers',
            fields=[
                ('e_newspaper_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_path', models.CharField(max_length=500)),
                ('raw_text', models.TextField()),
                ('scanned_at', models.DateTimeField(auto_now_add=True)),
                ('edition', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Source.e-newspaper',
            },
        ),
        migrations.CreateModel(
            name='PIBOfficials',
            fields=[
                ('official_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact_detail', models.JSONField()),
                ('department', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Notification.pib_official',
            },
        ),
        migrations.CreateModel(
            name='Websites',
            fields=[
                ('website_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=500)),
                ('raw_content', models.TextField()),
                ('scraped_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Source.website',
            },
        ),
        migrations.CreateModel(
            name='YouTubeVideos',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_url', models.CharField(max_length=500)),
                ('transcript', models.TextField()),
                ('downloaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Source.video',
            },
        ),
        migrations.CreateModel(
            name='NotificationsLog',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('sentiment', models.CharField(choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], max_length=10)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('official_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.pibofficials')),
            ],
            options={
                'db_table': 'Notification.notification_log',
            },
        ),
        migrations.CreateModel(
            name='ProcessedENewspapers',
            fields=[
                ('processed_e_newspaper_id', models.AutoField(primary_key=True, serialize=False)),
                ('processed_text', models.CharField(max_length=255)),
                ('sentiment', models.CharField(choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], max_length=10)),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
                ('source_e_newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.enewspapers')),
            ],
            options={
                'db_table': 'Processed_and_analyzed.processed_e_newspaper',
            },
        ),
        migrations.CreateModel(
            name='ProcessedWebsites',
            fields=[
                ('processed_website_id', models.AutoField(primary_key=True, serialize=False)),
                ('processed_content', models.TextField()),
                ('sentiment', models.CharField(choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], max_length=10)),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
                ('source_website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.websites')),
            ],
            options={
                'db_table': 'Processed_and_analyzed.processed_website',
            },
        ),
        migrations.CreateModel(
            name='ProcessedYouTubeVideos',
            fields=[
                ('processed_video_id', models.AutoField(primary_key=True, serialize=False)),
                ('sentiment', models.CharField(choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], max_length=10)),
                ('processed_transcript', models.TextField()),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
                ('source_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.youtubevideos')),
            ],
            options={
                'db_table': 'Processed_and_analyzed.processed_video',
            },
        ),
    ]
