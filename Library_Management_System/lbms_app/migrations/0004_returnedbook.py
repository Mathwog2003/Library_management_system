# Generated by Django 5.1.2 on 2024-10-15 07:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbms_app', '0003_rename_student_bookissue_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned_by', models.CharField(max_length=225)),
                ('return_date', models.DateField(default=django.utils.timezone.now)),
                ('book_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lbms_app.bookissue')),
            ],
        ),
    ]
