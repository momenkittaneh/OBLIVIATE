# Generated by Django 2.2.4 on 2021-06-06 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_pc_app', '0015_auto_20210606_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='build_pc_app.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='login_reg_app.users'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prodpic', to='build_pc_app.product'),
        ),
    ]