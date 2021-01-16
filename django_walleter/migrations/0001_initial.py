import django.db.models.deletion
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'deposit'), (2, 'withdraw')], db_index=True, verbose_name='Type')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Amount')),
                ('meta', jsonfield.fields.JSONField(null=True, verbose_name='Meta')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_id', models.PositiveIntegerField(db_index=True, verbose_name='Holder Id')),
                ('holder_type', models.CharField(db_index=True, max_length=255, verbose_name='Holder Type')),
                ('balance', models.DecimalField(decimal_places=3, default=0, max_digits=8, verbose_name='Balance')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='from_wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_wallet', to='django_walleter.Wallet'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='to_wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_wallet', to='django_walleter.Wallet'),
        ),
    ]
