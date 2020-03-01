from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Country(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)          
    country_code         = models.CharField(max_length=500)
    currency_code        = models.CharField(max_length=500)
    banner_image         = models.TextField() 
    country_logo         = models.TextField(max_length=500)
    country_thumbnail    = models.TextField()
    description          = models.TextField()         
    country_ranking      = models.PositiveIntegerField()
    isfeatured           = models.BooleanField()
    heading1             = models.TextField()
    heading2             = models.TextField()
    meta_title           = models.CharField(max_length=500)
    meta_keyword         = models.TextField()
    meta_description     = models.TextField()
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='country'

class City(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
    country              = models.ForeignKey(Country,on_delete=models.CASCADE)
    city_description     = models.TextField()
    city_banner_image    = models.TextField()
    city_logo            = models.TextField()
    city_thumbnail       = models.TextField()
    description          = models.TextField()
    is_featured          = models.BooleanField()
    city_ranking         = models.PositiveIntegerField()
    latitude             = models.FloatField()
    longitude            = models.FloatField()
    heading1             = models.TextField()
    heading2             = models.TextField()
    meta_title           = models.CharField(max_length=500)
    meta_keyword         = models.TextField()
    meta_description     = models.TextField()
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    status               = models.IntegerField(default=1)
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    is_enabled           = models.IntegerField(default=1)

    class Meta:
        db_table='city'

class Provider(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
    country              = models.ForeignKey(Country,on_delete=models.CASCADE)
    city                 = models.ForeignKey(City,on_delete=models.CASCADE)
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)

    class Meta:
        db_table='provider'

class Facility(models.Model):
    id                   = models.AutoField(primary_key=True)
    logo                 = models.CharField(max_length=500)
    title                = models.TextField()
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)
    
    class Meta:
        db_table='facility'


class University(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
    city                 = models.ForeignKey(City,on_delete=models.CASCADE)
    country              = models.ForeignKey(Country,on_delete=models.CASCADE)
    description          = models.TextField()
    banner_image         = models.TextField()
    logo                 = models.TextField()
    thumbnail            = models.TextField()
    has_campus           = models.CharField(max_length=500)
    campus_detail        = models.TextField()
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)
    # Name
    # campus Slug
    # isMainCampus
    # latitude
    # longitude
    
    class Meta:
        db_table='university'

# class Offer(models.Model):
#     id                   = models.AutoField(primary_key=True)
#     title                = models.CharField(max_length=500)
#     message              = models.TextField()
#     validity_date        = models.DateTimeField()
#     added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
#     added_date           = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         db_table='offer'

# class Property(models.Model):
#     id                   = models.AutoField(primary_key=True)
#     name                 = models.CharField(max_length=400)
#     description          = models.TextField()
#     provider             = models.ForeignKey(Provider,on_delete=models.CASCADE)
#     #property Images - Array of Objects (imageUrl, Ranking, Alt)
#     latitude             = models.FloatField()
#     longitude            = models.FloatField()
#     address              = models.TextField()
#     country              = models.ForeignKey(Country,on_delete=models.CASCADE)
#     city                 = models.ForeignKey(City,on_delete=models.CASCADE)
#     numbers_of_beds      = models.IntegerField()
#     # Offers - Array of Objects (Title, Description, Validity Date)
#     ranking              = models.IntegerField()
#     property_type        = models.CharField(max_length=500)
#     rating               = models.FloatField()
#     base_currency_code   = models.CharField(max_length=500)
#     offers               = models.ForeignKey(Offer,on_delete=models.Model)
#     whybook              = models.TextField()
#     payment_procedure    = models.TextField()
#     # distance_from_city_centre
#     # minimum_room_price   = models.
#     # is_extraOrdinary     = 
#     is_enabled           = models.IntegerField(default=1)
#     is_soldOut           = models.IntegerField(default=1)
#     # has_short_termRates  = models.
#     # amenities    
#     # rent_includes
#     # safety_and_security
#     # base_currency_code
#     # rate_type
    
    
    
#     # nearby_universities (Fields from Universities Table)
#     # room_categories

#     class Meta:
#         db_table='property' 


# class PropertyFeatures(models.Model):
#     id              = models.AutoField(primary_key=True)
#     alt_tag         = models.TextField()
#     url             = models.TextField()
#     property_type   = models.TextField()

#     class Meta:
#         db_table='property_feature'

# class PropertyImage(models.Model):
#     url             = models.CharField(max_length=500)
#     alt_tag         = CharField(max_length=500)
#     ranking         = models.IntegerField()
#     image_level     = models.TextField()
#     class Meta:
#         db_table='property_image'