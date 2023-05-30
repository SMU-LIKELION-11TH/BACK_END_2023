# Generated by Django 4.2.1 on 2023-05-14 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='writer',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='author',
            new_name='writer',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(verbose_name='내용'),
        ),
    ]