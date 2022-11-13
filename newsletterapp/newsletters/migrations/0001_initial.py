# Generated by Django 4.1.3 on 2022-11-13 18:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('file', models.FileField(upload_to='newsletterapp/newsletters/media/newsletters', validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])])),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('email', models.EmailField(max_length=254)),
                ('subscribed', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TopicSusbscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('subscribed', models.BooleanField(default=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletters.recipient')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletters.topic')),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.AddField(
            model_name='recipient',
            name='topics',
            field=models.ManyToManyField(through='newsletters.TopicSusbscription', to='newsletters.topic'),
        ),
        migrations.CreateModel(
            name='NewsLetterItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletters.newsletter')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletters.recipient')),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.AddField(
            model_name='newsletter',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletters.topic'),
        ),
    ]
