# Generated by Django 3.0.2 on 2020-01-16 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'actor',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(max_length=20)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_id', models.SmallIntegerField()),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('activebool', models.BooleanField()),
                ('create_date', models.DateField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Address')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('rental_duration', models.SmallIntegerField()),
                ('rental_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('length', models.SmallIntegerField(blank=True, null=True)),
                ('replacement_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.TextField(blank=True, null=True)),
                ('last_update', models.DateTimeField()),
                ('special_features', models.TextField(blank=True, null=True)),
                ('fulltext', models.TextField()),
            ],
            options={
                'db_table': 'film',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_id', models.SmallIntegerField()),
                ('last_update', models.DateTimeField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Film')),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('store_id', models.SmallIntegerField()),
                ('active', models.BooleanField()),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('last_update', models.DateTimeField()),
                ('picture', models.BinaryField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Address')),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('last_update', models.DateTimeField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Address')),
                ('manager_staff', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Staff')),
            ],
            options={
                'db_table': 'store',
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False)),
                ('rental_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Customer')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Inventory')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Staff')),
            ],
            options={
                'db_table': 'rental',
                'unique_together': {('rental_date', 'inventory', 'customer')},
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Customer')),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Rental')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Staff')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Language'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Country')),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.City'),
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('film', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rental.Film')),
                ('last_update', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Category')),
            ],
            options={
                'db_table': 'film_category',
                'unique_together': {('film', 'category')},
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('actor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rental.Actor')),
                ('last_update', models.DateTimeField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental.Film')),
            ],
            options={
                'db_table': 'film_actor',
                'unique_together': {('actor', 'film')},
            },
        ),
    ]
