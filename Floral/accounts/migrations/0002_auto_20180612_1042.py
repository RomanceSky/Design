# Generated by Django 2.0.5 on 2018-06-12 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name=' Member card number Member')),
                ('printed_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='The name of the member card')),
                ('membership_type_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member type code')),
                ('membership_status_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member status code')),
                ('membership_photo', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member photo')),
                ('issue_date', models.DateTimeField(blank=True, null=True, verbose_name='Issue date')),
                ('effective_date', models.DateTimeField(blank=True, null=True, verbose_name='Effective Date')),
                ('expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='Expiry Date ')),
                ('printed', models.NullBooleanField(verbose_name='printed')),
                ('printed_date', models.DateTimeField(blank=True, null=True, verbose_name='Printed Date')),
                ('renewed_date', models.DateTimeField(blank=True, null=True, verbose_name='Renewed Date')),
                ('tmp_effective_date', models.DateTimeField(blank=True, null=True, verbose_name='Tmp Effective Date')),
                ('tmp_expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='Tmp Expiry Date')),
                ('tmp_membership_status_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Tmp Membership Status Code')),
                ('points_bal', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Points Bal')),
                ('total_points_bal', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Total_Points Bal')),
                ('holding_points', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Holding Points')),
                ('remarks', models.CharField(blank=True, max_length=64, null=True, verbose_name='Remarks')),
                ('membership_discount', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Membership Discount')),
                ('tier_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Tier Code')),
                ('tier_anniversary_start_date', models.DateTimeField(blank=True, null=True, verbose_name='Tier Anniversary Start Date')),
                ('tier_anniversary_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Tier Anniversary End Date')),
                ('loyalty_message', models.CharField(blank=True, max_length=64, null=True, verbose_name='Loyalty Message')),
                ('dollar_to_points_ratio', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Dollar to Points Ratio')),
                ('is_supplementary', models.NullBooleanField(verbose_name='Is Supplementary')),
                ('is_burn_supplementary', models.NullBooleanField(verbose_name='Is Burn Supplementary')),
                ('relation_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='Relation Id')),
                ('primary_card_no', models.CharField(blank=True, max_length=64, null=True, verbose_name='Primary Card No')),
                ('primary_relation_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='Primary Relation Id')),
                ('primary_card_expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='Primary Card Expiry Date ')),
                ('primary_card_effective_date', models.DateTimeField(blank=True, null=True, verbose_name='Primary Card Effective Date')),
                ('pts_holding_days', models.IntegerField(blank=True, null=True, verbose_name='Pts Holding Days')),
                ('current_net_spent', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Current Net Spent')),
                ('pass_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Pass Code')),
                ('stored_value_balance', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Stored Value Balance')),
                ('currency', models.CharField(blank=True, max_length=64, null=True, verbose_name='Currency')),
                ('last_visited_date', models.DateTimeField(blank=True, null=True, verbose_name='Last Visited Date')),
                ('last_visited_outlet', models.CharField(blank=True, max_length=64, null=True, verbose_name='Last Visited Outlet')),
                ('points_to_next_tier', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Points To Next Tier')),
                ('nett_to_next_tier', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Nett To Next Tier')),
                ('lucky_draw_conversion_pts_usage_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='Lucky Draw Conversion Pts Usage Type')),
                ('lucky_draw_conversion_rate', models.CharField(blank=True, max_length=64, null=True, verbose_name='Lucky Draw Conversion Rate')),
                ('spent_quota_increasement', models.FloatField(blank=True, max_length=32, null=True, verbose_name='Spent Quota Increasement')),
                ('spent_quota_increasement_expired_on', models.CharField(blank=True, max_length=64, null=True, verbose_name='spent_quota_increasement_expired_on')),
                ('pickup_date', models.DateTimeField(blank=True, null=True, verbose_name='pickup_date')),
                ('pickup_by', models.CharField(blank=True, max_length=64, null=True, verbose_name='pickup_by')),
                ('current_rcnett_spent', models.IntegerField(blank=True, null=True, verbose_name='current_rcnett_spent')),
                ('cmc_earned_points', models.FloatField(blank=True, max_length=32, null=True, verbose_name='cmc_earned_points')),
                ('crc_earned_points', models.IntegerField(blank=True, null=True, verbose_name='crc_earned_points')),
                ('current_tier_nett', models.FloatField(blank=True, max_length=32, null=True, verbose_name='current_tier_nett')),
                ('current_tier_amt', models.FloatField(blank=True, max_length=32, null=True, verbose_name='current_tier_amt')),
                ('bring_fwd_tier_nett', models.FloatField(blank=True, max_length=32, null=True, verbose_name='bring_fwd_tier_nett')),
                ('bring_fwd_tier_amt', models.FloatField(blank=True, max_length=32, null=True, verbose_name='bring_fwd_tier_amt')),
                ('bring_fwd_tier_expiry', models.CharField(blank=True, max_length=64, null=True, verbose_name='bring_fwd_tier_expiry')),
                ('bring_fwd_tier_start_date', models.DateTimeField(blank=True, null=True, verbose_name='bring_fwd_tier_start_date')),
                ('extended_tier_anniversary_end_date', models.DateTimeField(blank=True, null=True, verbose_name='extended_tier_anniversary_end_date')),
            ],
        ),
        migrations.CreateModel(
            name='InterestGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Interest Group name')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('individual_position', models.CharField(blank=True, max_length=64, null=True, verbose_name='Individual position')),
                ('salutation', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member salutation')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member name')),
                ('nric', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member NRIC')),
                ('passport', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member passport')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Member email')),
                ('gender', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member gender')),
                ('dob', models.DateTimeField(blank=True, null=True, verbose_name='Member birthday')),
                ('nationality', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member nationality')),
                ('block', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member block')),
                ('level', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member level')),
                ('unit', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member unit')),
                ('street', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member street')),
                ('building', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member building')),
                ('postal_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member postal_code')),
                ('country', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member country')),
                ('address1', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member address1')),
                ('address2', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member address2')),
                ('address3', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member address3')),
                ('contact_no', models.CharField(blank=True, max_length=64, null=True, verbose_name='contact_no')),
                ('mobile_no', models.CharField(max_length=64, unique=True, verbose_name='mobile_no')),
                ('fax_no', models.CharField(blank=True, max_length=64, null=True, verbose_name='fax_no')),
                ('referrer_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='referrer_code')),
                ('facebook_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='salutation')),
                ('facebook_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='facebook_name')),
                ('facebook_photo_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='facebook_photo_link')),
                ('facebook_token', models.CharField(blank=True, max_length=128, null=True, verbose_name='facebook_token')),
                ('facebook_token_expiry', models.CharField(blank=True, max_length=64, null=True, verbose_name='facebook_token_expiry')),
                ('full_photo_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='full_photo_name')),
                ('base64_photo_string', models.CharField(blank=True, max_length=256, null=True, verbose_name='base64_photo_string')),
                ('photo_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='photo_link')),
                ('race_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='race_code')),
                ('notify_post', models.NullBooleanField(max_length=64, verbose_name='notify_post')),
                ('notify_sms', models.NullBooleanField(max_length=64, verbose_name='notify_sms')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='last_name')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='join_date')),
                ('username', models.CharField(blank=True, max_length=64, null=True, verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('interestGroups', models.ManyToManyField(related_name='members', to='accounts.InterestGroup', verbose_name='Member interestGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_level', models.IntegerField(unique=True, verbose_name='Membership Level')),
                ('membership_name', models.CharField(max_length=32, unique=True, verbose_name='Membership Name')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'ADMIN'), (1, 'POS'), (2, 'MEMBER'), (3, 'ANONYMOUS')], help_text='0:admin,1:pos,2:member,3:anonymous', unique=True, verbose_name='Role name')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='accounts.Membership', verbose_name='Membership level'),
        ),
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='accounts.Role', verbose_name='role'),
        ),
        migrations.AddField(
            model_name='card',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='accounts.Member', verbose_name='Member'),
        ),
    ]
