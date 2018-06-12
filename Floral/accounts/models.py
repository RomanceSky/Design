from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _



from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class InterestGroup(models.Model):
    name = models.CharField(verbose_name='Interest Group name', max_length=32, unique=True)

class Role(models.Model):
    ADMIN, POS, MEMBER, ANONYMOUS = range(4)
    NAME_CHOICES = (
        (ADMIN, 'ADMIN'),
        (POS, 'POS'),
        (MEMBER, 'MEMBER'),
        (ANONYMOUS, 'ANONYMOUS'),
    )
    name = models.IntegerField(
        verbose_name="Role name",
        choices=NAME_CHOICES,
        help_text="0:admin,1:pos,2:member,3:anonymous",
        unique=True
    )

class Membership(models.Model):
    membership_level = models.IntegerField(verbose_name='Membership Level', unique=True)
    membership_name = models.CharField(verbose_name='Membership Name', max_length=32, unique=True)

class Member(AbstractBaseUser):
    USERNAME_FIELD = 'mobile_no'
    individual_position = models.CharField(verbose_name='Individual position', max_length=64, null=True, blank=True)
    membership = models.ForeignKey(verbose_name='Membership level', to='Membership', related_name='members', on_delete=models.CASCADE, null=True, blank=True)
    salutation = models.CharField(verbose_name='Member salutation', max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name='Member name', max_length=64, null=True, blank=True)
    nric = models.CharField(verbose_name='Member NRIC', max_length=64, null=True, blank=True)
    passport = models.CharField(verbose_name='Member passport', max_length=64, null=True, blank=True)
    email = models.EmailField(verbose_name='Member email', null=True, blank=True)
    gender = models.CharField(verbose_name='Member gender', max_length=64, null=True, blank=True)
    dob = models.DateTimeField(verbose_name='Member birthday', null=True, blank=True)
    nationality = models.CharField(verbose_name='Member nationality', max_length=64, null=True, blank=True)
    block = models.CharField(verbose_name='Member block', max_length=64, null=True, blank=True)
    level = models.CharField(verbose_name='Member level', max_length=64, null=True, blank=True)
    unit = models.CharField(verbose_name='Member unit', max_length=64, null=True, blank=True)
    street = models.CharField(verbose_name='Member street', max_length=64, null=True, blank=True)
    building = models.CharField(verbose_name='Member building', max_length=64, null=True, blank=True)
    postal_code = models.CharField(verbose_name='Member postal_code', max_length=64, null=True, blank=True)
    country = models.CharField(verbose_name='Member country', max_length=64, null=True, blank=True)
    address1 = models.CharField(verbose_name='Member address1', max_length=64, null=True, blank=True)
    address2 = models.CharField(verbose_name='Member address2', max_length=64, null=True, blank=True)
    address3 = models.CharField(verbose_name='Member address3', max_length=64, null=True, blank=True)
    contact_no = models.CharField(verbose_name='contact_no', max_length=64, null=True, blank=True)
    mobile_no = models.CharField(verbose_name='mobile_no', max_length=64, unique=True)
    fax_no = models.CharField(verbose_name='fax_no', max_length=64, null=True, blank=True)
    referrer_code = models.CharField(verbose_name='referrer_code', max_length=64, null=True, blank=True)
    facebook_id = models.CharField(verbose_name='salutation', max_length=64, null=True, blank=True)
    facebook_name = models.CharField(verbose_name='facebook_name', max_length=64, null=True, blank=True)
    facebook_photo_link = models.CharField(verbose_name='facebook_photo_link', max_length=128, null=True, blank=True)
    facebook_token = models.CharField(verbose_name='facebook_token', max_length=128, null=True, blank=True)
    facebook_token_expiry = models.CharField(verbose_name='facebook_token_expiry', max_length=64, null=True, blank=True)
    full_photo_name = models.CharField(verbose_name='full_photo_name', max_length=64, null=True, blank=True)
    base64_photo_string = models.CharField(verbose_name='base64_photo_string', max_length=256, null=True, blank=True)
    photo_link = models.CharField(verbose_name='photo_link', max_length=128, null=True, blank=True)
    interestGroups = models.ManyToManyField(verbose_name='Member interestGroup', to='InterestGroup', related_name='members', null=True, blank=True)
    # interestGroups = models.ManyToManyField(verbose_name='Member interestGroup', to='InterestGroup',
    #                                       related_name='members')
    race_code = models.CharField(verbose_name='race_code', max_length=64, null=True, blank=True)
    notify_post = models.NullBooleanField(verbose_name='notify_post', max_length=64, null=True, blank=True)
    notify_sms = models.NullBooleanField(verbose_name='notify_sms', max_length=64, null=True, blank=True)
    first_name = models.CharField(verbose_name='first_name', max_length=64, null=True, blank=True)
    last_name = models.CharField(verbose_name='last_name', max_length=64, null=True, blank=True)
    join_date = models.DateTimeField(verbose_name='join_date', auto_now_add=True)
    username = models.CharField(verbose_name='username', max_length=64, null=True, blank=True)
    password = models.CharField(verbose_name='password', max_length=128)
    role = models.ForeignKey(verbose_name='role', to='Role', related_name='members', on_delete=models.CASCADE,
                             null=True, blank=True)

class Card(models.Model):
    card_no = models.CharField(verbose_name=' Member card number Member', max_length=64, null=True, blank=True, unique=True)
    member = models.ForeignKey(verbose_name='Member', to='Member', related_name='cards', on_delete=models.CASCADE, null=True, blank=True)
    printed_name = models.CharField(verbose_name='The name of the member card', max_length=64, null=True, blank=True)
    membership_type_code = models.CharField(verbose_name='Member type code', max_length=64, null=True, blank=True)
    membership_status_code = models.CharField(verbose_name='Member status code', max_length=64, null=True, blank=True)
    membership_photo = models.CharField(verbose_name='Member photo', max_length=64, null=True, blank=True)
    issue_date = models.DateTimeField(verbose_name='Issue date', null=True, blank=True)
    effective_date = models.DateTimeField(verbose_name='Effective Date', null=True, blank=True)
    expiry_date = models.DateTimeField(verbose_name='Expiry Date ', null=True, blank=True)
    printed = models.NullBooleanField(verbose_name='printed', null=True, blank=True)
    printed_date = models.DateTimeField(verbose_name='Printed Date', null=True, blank=True)
    renewed_date = models.DateTimeField(verbose_name='Renewed Date', null=True, blank=True)
    tmp_effective_date = models.DateTimeField(verbose_name='Tmp Effective Date', null=True, blank=True)
    tmp_expiry_date = models.DateTimeField(verbose_name='Tmp Expiry Date', null=True, blank=True)
    tmp_membership_status_code = models.CharField(verbose_name='Tmp Membership Status Code', max_length=64, null=True, blank=True)
    points_bal = models.FloatField(verbose_name='Points Bal', max_length=32, null=True, blank=True)
    total_points_bal = models.FloatField(verbose_name='Total_Points Bal', max_length=32, null=True, blank=True)
    holding_points = models.FloatField(verbose_name='Holding Points', max_length=32, null=True, blank=True)
    remarks = models.CharField(verbose_name='Remarks', max_length=64, null=True, blank=True)
    membership_discount = models.FloatField(verbose_name='Membership Discount', max_length=32, null=True, blank=True)
    tier_code = models.CharField(verbose_name='Tier Code', max_length=64, null=True, blank=True)
    tier_anniversary_start_date=models.DateTimeField(verbose_name='Tier Anniversary Start Date', null=True, blank=True)
    tier_anniversary_end_date=models.DateTimeField(verbose_name='Tier Anniversary End Date', null=True, blank=True)
    loyalty_message = models.CharField(verbose_name='Loyalty Message', max_length=64, null=True, blank=True)
    dollar_to_points_ratio = models.FloatField(verbose_name='Dollar to Points Ratio', max_length=32, null=True, blank=True)
    is_supplementary = models.NullBooleanField(verbose_name='Is Supplementary', null=True, blank=True)
    is_burn_supplementary = models.NullBooleanField(verbose_name='Is Burn Supplementary', null=True, blank=True)
    relation_id = models.CharField(verbose_name='Relation Id', max_length=64, null=True, blank=True)
    primary_card_no = models.CharField(verbose_name='Primary Card No', max_length=64, null=True, blank=True)
    primary_relation_id = models.CharField(verbose_name='Primary Relation Id', max_length=64, null=True, blank=True)
    primary_card_expiry_date = models.DateTimeField(verbose_name='Primary Card Expiry Date ', null=True, blank=True)
    primary_card_effective_date = models.DateTimeField(verbose_name='Primary Card Effective Date', null=True, blank=True)
    pts_holding_days = models.IntegerField(verbose_name='Pts Holding Days', null=True, blank=True)
    current_net_spent = models.FloatField(verbose_name='Current Net Spent', max_length=32, null=True, blank=True)
    pass_code = models.CharField(verbose_name='Pass Code', max_length=64, null=True, blank=True)
    stored_value_balance = models.FloatField(verbose_name='Stored Value Balance', max_length=32, null=True, blank=True)
    currency = models.CharField(verbose_name='Currency', max_length=64, null=True, blank=True)
    last_visited_date = models.DateTimeField(verbose_name='Last Visited Date', null=True, blank=True)
    last_visited_outlet = models.CharField(verbose_name='Last Visited Outlet', max_length=64, null=True, blank=True)
    points_to_next_tier = models.FloatField(verbose_name='Points To Next Tier', max_length=32, null=True, blank=True)
    nett_to_next_tier = models.FloatField(verbose_name='Nett To Next Tier', max_length=32, null=True, blank=True)
    lucky_draw_conversion_pts_usage_type = models.CharField(verbose_name='Lucky Draw Conversion Pts Usage Type', max_length=64, null=True, blank=True)
    lucky_draw_conversion_rate = models.CharField(verbose_name='Lucky Draw Conversion Rate', max_length=64, null=True, blank=True)
    spent_quota_increasement = models.FloatField(verbose_name='Spent Quota Increasement', max_length=32, null=True, blank=True)
    spent_quota_increasement_expired_on = models.CharField(verbose_name='spent_quota_increasement_expired_on', max_length=64, null=True, blank=True)
    pickup_date = models.DateTimeField(verbose_name='pickup_date', null=True, blank=True)
    pickup_by = models.CharField(verbose_name='pickup_by', max_length=64, null=True, blank=True)
    current_rcnett_spent = models.IntegerField(verbose_name='current_rcnett_spent', null=True, blank=True)
    cmc_earned_points = models.FloatField(verbose_name='cmc_earned_points', max_length=32, null=True, blank=True)
    crc_earned_points = models.IntegerField(verbose_name='crc_earned_points', null=True, blank=True)
    current_tier_nett = models.FloatField(verbose_name='current_tier_nett', max_length=32, null=True, blank=True)
    current_tier_amt = models.FloatField(verbose_name='current_tier_amt', max_length=32, null=True, blank=True)
    bring_fwd_tier_nett = models.FloatField(verbose_name='bring_fwd_tier_nett', max_length=32, null=True, blank=True)
    bring_fwd_tier_amt = models.FloatField(verbose_name='bring_fwd_tier_amt', max_length=32, null=True, blank=True)
    bring_fwd_tier_expiry = models.CharField(verbose_name='bring_fwd_tier_expiry', max_length=64, null=True, blank=True)
    bring_fwd_tier_start_date = models.DateTimeField(verbose_name='bring_fwd_tier_start_date', null=True, blank=True)
    extended_tier_anniversary_end_date = models.DateTimeField(verbose_name='extended_tier_anniversary_end_date', null=True, blank=True)

#  top is the test for cobra

class MyUsers(models.Model):
    #REQUIRED_FIELDS = ('name',)
    #USERNAME_FIELD = ('name')
    groups = models.ForeignKey(
        'Groups',
        null=False,
        blank=False,
        related_name='myusers',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=125,
    )
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=125,
    )

    url = models.URLField(
        null=False,
        blank=True,
        max_length=125,
    )


class Groups(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=125,
    )

    url = models.URLField(
        null=False,
        blank=True,
        max_length=125,
    )

class Ip(models.Model):
    user = models.ForeignKey(
        'MyUsers',
        null=False,
        blank=False,
        related_name='ips',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        'Groups',
        null=False,
        blank=True,
        related_name='ips',
        on_delete=models.CASCADE
    )
    ip_addr = models.GenericIPAddressField(
        blank=False,
        null=False,
    )

class Comment(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=125,
    )
    content = models.CharField(
        null=False,
        blank=False,
        max_length=200,
    )

    created = models.DateTimeField(
        help_text=_('date'),
        auto_now_add=True
    )

    user = models.ForeignKey(
        'MyUsers',
        null=False,
        blank=False,
        related_name='comments',
        on_delete=models.CASCADE
    )

class Admire(models.Model):
    payment_method = models.EmailField(
        null=False,
        blank=False,
        max_length=125,
    )
    status = models.CharField(
        null=False,
        blank=False,
        max_length=200,
    )

    total_amount = models.IntegerField(
        null=False,
        blank=False,
        help_text=_('total amount'),
    )
    original_article = models.CharField(
        null=True,
        blank=True,
        max_length=200,
    )
    expired_at = models.DateTimeField(
        help_text=_('date'),
        auto_now_add=True
    )

    user = models.ForeignKey(
        'MyUsers',
        null=False,
        blank=False,
        related_name='admires',
        on_delete=models.CASCADE
    )
