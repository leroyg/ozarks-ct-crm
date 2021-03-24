from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(help_text='01-30-2001', null=True)
    contact_phone = models.CharField(max_length=12, help_text='+14156665555', null=True)
    basketball_womens = 'WBB'
    basketball_mens = 'MBB'
    baseball = 'BB'
    softball = 'SB'
    shooting_sports = 'Shoot'
    cross_country = 'XC'
    womens_soccer = 'WSC'
    mens_soccer = 'MSC'
    tennis = 'TNS'
    swimming_diving = 'SD'
    track = 'TR'
    womens_wrestling = 'WWR'
    mens_wrestling = 'MWR'
    team_choices = [
    (basketball_womens, "Women's Basketball"),
    (basketball_mens, "Men's Basketball"),
    (baseball, "Baseball"),
    (softball, "Softball"),
    (shooting_sports, "Shooting Sports"),
    (cross_country, "Cross Country"),
    (womens_soccer, "Women's Soccer"),
    (mens_soccer, "Men's Soccer"),
    (tennis, "Tennis"),
    (swimming_diving, "Swimming & Diving"),
    (track, "Track"),
    (womens_wrestling, "Women's Wrestling"),
    (mens_wrestling, "Men's Wrestling"),
    ]
    sports_team = models.CharField(
    max_length = 5,
    choices = team_choices,
    null=True
    )
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
        null = True
    )
