# Generated by Django 2.2.4 on 2021-06-04 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_pc_app', '0006_product_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='productorder',
            field=models.ManyToManyField(through='build_pc_app.cart', to='build_pc_app.product'),
        ),
        migrations.CreateModel(
            name='postimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='build_pc_app.product')),
            ],
        ),
    ]
