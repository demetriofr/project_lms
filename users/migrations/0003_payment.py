# Generated by Django 4.2 on 2024-03-11 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_lesson'),
        ('users', '0002_alter_user_options_remove_user_username_user_avatar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_paid', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('sum_paid', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('payment_methode', models.CharField(choices=[('C', 'Наличные'), ('T', 'Перевод на счет')], max_length=1, verbose_name='метод оплаты',default='C')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.lesson', verbose_name='урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платёж',
                'verbose_name_plural': 'платёжи',
            },
        ),
    ]