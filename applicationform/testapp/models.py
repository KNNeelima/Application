from django.db import models
# from django.core.validators import RegexValidator
# Create your models here.

class AppForm(models.Model):
    Name=models.CharField(max_length=30)
    FatherName=models.CharField(max_length=30)
    MotherName=models.CharField(max_length=30)
    DOB=models.DateField()
    Email=models.EmailField()
    # MobileNo=models.IntegerField(validators=[validate_even])
    MobileNo=models.IntegerField()
    SSCMarks=models.IntegerField()
    NameOfTheSchool=models.CharField(max_length=30)
    InterMarks=models.IntegerField()
    NameOfTheCollege=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    Dist=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    Pincode=models.IntegerField()
