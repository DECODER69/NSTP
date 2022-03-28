# Generated by Django 4.0.1 on 2022-03-28 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='alphamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='bravomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='charliemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='cwts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='deltamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='echomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='foxtrotmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='golfmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='hotelmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='indiamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='julietmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='kilomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='limamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='extenduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platoon', models.CharField(blank=True, max_length=10, null=True)),
                ('lname', models.CharField(default='', max_length=20)),
                ('fname', models.CharField(default='', max_length=30)),
                ('minitial', models.CharField(default='', max_length=3)),
                ('address', models.CharField(default='', max_length=100)),
                ('cpnumber', models.DecimalField(decimal_places=0, default='', max_digits=11)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('gender', models.CharField(default='', max_length=6)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('bdate', models.CharField(default='', max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('grades', models.CharField(choices=[('PENDING', 'PENDING'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='PENDING', max_length=20)),
                ('section', models.CharField(default='', max_length=20)),
                ('field', models.CharField(default='', max_length=20)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('ENROLLED', 'ENROLLED')], default='PENDING', max_length=10)),
                ('cert_datereq', models.CharField(default='', max_length=20)),
                ('cert_document', models.CharField(default='', max_length=20)),
                ('cert_status', models.CharField(choices=[('PENDING', 'PENDING'), ('ENROLLED', 'ENROLLED')], default='PENDING', max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_email', models.EmailField(max_length=254, null=True)),
                ('cert_fullname', models.CharField(max_length=100)),
                ('cert_course', models.CharField(max_length=20)),
                ('cert_datereq', models.CharField(max_length=20)),
                ('cert_document', models.CharField(max_length=20)),
                ('cert_status', models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
