# Generated by Django 4.2.11 on 2024-04-10 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_question_answer_questionanswer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionanswer',
            old_name='qa_id',
            new_name='question_answer_id',
        ),
        migrations.RenameField(
            model_name='questionanswermessage',
            old_name='qa_id',
            new_name='question_answer_id',
        ),
        migrations.RenameField(
            model_name='questionanswermessage',
            old_name='qam_id',
            new_name='question_answer_message_id',
        ),
    ]
