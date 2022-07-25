

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roommember',
            old_name='member_id',
            new_name='uid',
        ),
    ]
