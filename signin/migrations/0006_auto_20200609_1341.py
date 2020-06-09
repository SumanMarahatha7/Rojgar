# Generated by Django 3.0.6 on 2020-06-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0005_auto_20200609_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='category',
            field=models.CharField(choices=[('P&T', 'Programming & Technology'), ('G&D', 'Graphics & Design'), ('DM', 'Digital Marketing'), ('W&T', 'Writing & Translation'), ('DE', 'Data Entry'), ('V&M', 'Video & Animation'), ('M&A', 'Music & Audio'), ('B&I', 'Business & Investment'), ('CS', 'Consulting Service'), ('M&P', 'Medical & Pharma'), ('AH', 'Architect Designs'), ('LI', 'Lifestyle'), ('AUD', 'Audit & Taxation'), ('QA', 'Quality Assurance'), ('ENG', 'Engineering Consultancy'), ('OM', 'Organization Management'), ('RP', 'Repair & Technical Support'), ('E&T', 'Education & Teaching')], default='E&T', max_length=40),
        ),
    ]
