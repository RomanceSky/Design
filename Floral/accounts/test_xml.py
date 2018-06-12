import  xml.etree.ElementTree as ET

country_data="""<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""
root = ET.fromstring(country_data)
a = root.find("body/p")
b = root.findall(".")
c = root.findall("./country/neighbor")
d = root.findall(".//year/..[@name='Singapore']")
e = root.findall(".//*[@name='Singapore']/year")
f = root.findall(".//neighbor[2]")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
    等级                                    促销        号召/召集行动                 条件设置                 条款/期限和条件

选择个人:学生、老师、妈妈、爸爸、清洁工、护士等   折扣:享受X %   每个$ Y                     目标群体                与其他优惠无效。
所有非成员国                                               每个Y美元都要加到电子钱包里     age                不可退款、不可转让、不可重复使用、不可兑换的现金/积分/实物信用证
XX成员              每次使用X 'bubble' point              每次使用X 'bubble' point       性别              每个成员或者会员偿还（赎回）X
YY members          抵用券: 价值X的抵用券                  每次购买X 'bubble' point       促销时期            独家的AA/BB分店（专卖店）
ZZ members        会员:XX会员                           每次购买X杯中杯饮料              促销时间             专属于新会员/ XX会员/ YY会员/ ZZ会员/非会员
AA公司员工，BB公司员工等       会员:YY会员                 每次购买X大杯饮料    重复:每天，每星期一，每个月，  甚至只能在XX使用
                会员:ZZ会员                             每次购买X大杯或中杯饮料          参与店铺              限制第一次赎回（仅限一次偿还）
                产品:在菜单上兑换X中杯饮料                每次购买X中杯饮料(味道)          订购模式:无需预约的散客/移动订购   付款时必须使用优惠券
                产品:在菜单上兑换X大杯饮料                 每次购买X大杯饮料(味道)   支付方式:现金/ apple pay /    必须充分利用凭证的金额。任何未使用的款项将不予退还。
andriod pay / visa / mastercard / ezylink / QR code / favepay / grabpay / Alipay / Internet Banking
                                产品:赎回X中号饮品(香精)           每次买甜点时               限制X救赎            itea保留修改条款的权利，恕不另行通知
                                产品:赎回X大杯饮料(香精)      每次购买经典甜点。       选择每一次方(如。10日)客户   必须在订购时显示赎回以进行反向订购
                                产品:赎回X大中型饮料(香精)     每次购买布丁甜点时    凭证有效期(ddmmyy) - (ddmmyy)  itea将不负责替换过期的凭证
                                产品:救赎(味道)配料                每次买爱裕甜品   发布/发射日期
                                产品:赎回X冰淇淋           每次购买新鲜山药甜点时    现在发布
                                产品:可兑换X(味道)甜点。      每次买冰淇淋的时候
就像我们的facebook主页itea.sg
Like our facebook post
Rate us on facebook
Post on our facebook page

两个表：
会员表和会员类型表，多对一，一个会员类型下可以由多个会员

Parameter	                        Description
salutation	 	                    Nickname of member（e.g Mr）
name	 	                        Name of member
NRIC	 	                        Member id number
passport	                        Member's passport number
email	 	                        Member's Email(e.g carson@sd.com)
gender		                        Member of the gender（default=M）
dob                                Date of birth
mobile_no	                        Member phone number
interest_group_list                   FK(InterestGroup) The foreign bond is associated with the InterestGroup
join_date	                        Membership registration date and membership card generation date
notify_post                          Email notification(default=false)
notify_SMS	                        SMS notification(default=false)
first_name	                        Member's first name
last_name	                        Member's last name
card_no(foreign key(card.id))	                            Member card number Member
    printed_name                         The name of the member on the membership card
    membership_type_code	                MembershipTypeCode
    MembershipStatusCode	            MembershipStatusCode
    IssueDate	                        IssueDate
    EffectiveDate	                    EffectiveDate
    ExpiryDate	                        ExpiryDate
    Printed	                            Select print or not（default=false）
    PrintedDate		                    PrintedDate
    RenewedDate	                        RenewedDate
    PointsBAL                           Points balance
    TotalPointsBAL                      Total Points balance
    HoldingPoints	                    Holding Points
    MembershipDiscount	                Membership Discount
    Remarks	                            Remarks
    TierCode	                        Member Tier Code
    IsSupplementary	                    IsSupplementary(default=false)
    IsBurnSupplementary                 isBurnSupplementaryCard(default=false)
    PtsHoldingDays                  	Points Holding Days
    CurrentNetSpent                     Current net consumption
    Passcode	                        Passcode
    StoredValueBalance	                Stored Value Balance
    Currency	                       	Currency
    PointsToNextTier	                Points To Next Tier
    NettToNextTier	                    Nett To Next Tier
    LuckyDrawConversionPtsUsageType	    LuckyDrawConversionPtsUsageType
    LuckyDrawConversionRate             LuckyDrawConversionRate
    CurrentRCNettSpent	                CurrentRCNettSpent
    CMCEarnedPoints	                    CMCEarnedPoints
    CRCEarnedPoints	                    CRCEarnedPoints
    CurrentTierNett	                    CurrentTierNett
    CurrentTierAmt	                    CurrentTierAmt
    BringFwdTierNett	                BringFwdTierNett
    BringFwdTierAmt	                    BringFwdTierAmt

Additional paramaters are not included:
MembershipMovementHistory
MembershipMovementHistory
    MembershipType
    CardNo
    MovementType
    From
    To
    ChangedOn
    TierAnniversaryStartDate
    TierAnniversaryEndDate
    OldTierAnniversaryStartDate
    OldTierAnniversaryEndDate
Parameter	                        Description
salutation	 	                Nickname of member（e.g Mr）
name	 	                        Name of member
nric	 	                        Member id number
passport	                        Member's passport number
email	 	                        Member's Email(e.g carson@sd.com)
gender		                        Member of the gender（default=M）
dob                                Date of birth
mobile_no	                        Member phone number
interest_group_list                   FK(InterestGroup) The foreign bond is associated with the InterestGroup
join_date	                        Membership registration date and membership card generation date
notify_post                          Email notification(default=false)
notify_SMS	                        SMS notification(default=false)
first_name	                        Member's first name
last_name	                        Member's last name
card_no(foreign key(card.id))	         Member card number Member
    Parameter	                         Description
    printed_name                         The name of the member on the membership card
    membership_type_code	         MembershipTypeCode
    membership_status_code	         MembershipStatusCode
    issue_date	                         IssueDate
    effective_date	                 EffectiveDate
    expiry_date	                         ExpiryDate
    printed	                         Select print or not（default=false）
    printed_date		                 PrintedDate
    renewed_date	                         RenewedDate
    points_bal                           Points balance
    total_points_bal                      Total Points balance
    holding_points	                 Holding Points
    membership_discount	                 Membership Discount
    remarks	                         Remarks
    tier_code	                         Member Tier Code
    is_supplementary	                 IsSupplementary(default=false)
    is_burn_supplementary                  IsBurnSupplementaryCard(default=false)
    pts_holding_days                  	 Points Holding Days
    current_net_spent                      Current net consumption
    pass_code	                         Passcode
    stored_value_balance	                 Stored Value Balance
    currency	                       	Currency
    points_to_next_tier	                Points To Next Tier
    nett_to_next_tier	                    Nett To Next Tier
    lucky_draw_conversion_pts_usage_type	    LuckyDrawConversionPtsUsageType
    lucky_draw_conversion_rate             LuckyDrawConversionRate
    current_RCnett_spent	                CurrentRCNettSpent
    cmc_earned_points	                    CMCEarnedPoints
    crc_earned_points	                    CRCEarnedPoints
    current_tier_nett	                    CurrentTierNett
    current_tier_amt	                    CurrentTierAmt
    bring_fwd_tier_nett	                BringFwdTierNett
    bring_fwd_tier_amt	                    BringFwdTierAmt

{
    "ReturnStatus": "1",
    "ReturnMessage": "SUCCESS",
"campaign_list": [{
	“id”: “1”,
            "name": "campaign_name2",
            "description": "",
            "type": 0,  # 0: Discount_per,1: Discount_amount,2: Cash Voucher,3: Product Voucher
            "discount_amount": 10,
            "discount_per": 0.86,
            "start_time": "2018-06-06T10:08:05.234324Z",
            "end_time": "2018-06-06T10:08:05.234324Z",
            "product_id": "1",
            "size": "0",  # 0: medium,1: large
	“limit_level”: 1,
	“age_min”: 20,
	“age_max”: 28,
	“gender”: 0,  # 0:female,1:male
	“company”: “company_name”,
	“receipients”: “students”,
	“promo”: “Discount: Enjoy X% off”,√
	“call_to_action”: “with every $Y spent”,
	“conditions_to_set”: “every mon”,
	“Terms & Conditions”: “”
   }]
}



card_no(foreign key(card.id))
member_id
printed_name
membership_type_code
membership_status_code
membership_photo
issue_date
effective_date
expiry_date
printed
printed_date
renewed_date
tmp_effective_date
tmp_expiry_date
tmp_membership_status_code
points_bal
total_points_bal
holding_points
membership_discount
remarks
membership_discount
tier_code
tier_anniversary_start_date
tier_anniversary_end_date
loyalty_message
dollar_to_points_ratio
is_supplementary
is_burn_supplementary
relation_id
primary_card_no
primary_relation_id
primary_card_expiry_date
primary_card_effective_date
pts_holding_days
current_net_spent
pass_code
stored_value_balance
currency
last_visited_date
last_visited_outlet
points_to_next_tier
nett_to_next_tier
lucky_draw_conversion_pts_usage_type
lucky_draw_conversion_rate
spent_quota_increasement
spent_quota_increasement_expired_on
pickup_date
pickup_by
current_rcnett_spent
cmc_earned_points
crc_earned_points
current_tier_nett
current_tier_amt
bring_fwd_tier_nett
bring_fwd_tier_amt
bring_fwd_tier_expiry
bring_fwd_tier_start_date
extended_tier_anniversary_end_date

memberid(FK——Member)
    salutation	 	                Nickname of member（e.g Mr）
    name	 	                        Name of member
    nric	 	                        Member id number
    passport	                        Member's passport number
    email	 	                        Member's Email(e.g carson@sd.com)
    gender		                        Member of the gender（default=M）
    dob                                 Date of birth
    mobile_no	                        Member phone number
    interest_group_list                 FK(InterestGroup) The foreign bond is associated with the InterestGroup
    join_date	                        Membership registration date and membership card generation date
    notify_post                         Email notification(default=false)
    notify_SMS	                        SMS notification(default=false)
    first_name	                        Member's first name
    last_name	                        Member's last name

