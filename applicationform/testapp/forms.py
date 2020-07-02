from django import forms
from testapp.models import AppForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

my_validator = RegexValidator(r"^[A-Z][a-z]*", "First Letter should be Upper case.")


class ApplicatonForm(forms.ModelForm):
    error_css_class = "error"
    Name =forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter Name'}),validators=[my_validator])
    FatherName  =forms.CharField(label='Father Name',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter Fathername'}),validators=[my_validator])
    MotherName =forms.CharField(label='Mother Name',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter Mothername'}),validators=[my_validator])
    DOB=forms.CharField(label='Date Of Birth',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter DOB'}))
    Email=forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter Email'}))
    SSCMarks=forms.CharField(label='SSC Marks',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter Marks'}))
    NameOfTheSchool=forms.CharField(label='School Name',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"School Name"}))
    InterMarks=forms.CharField(label='Inter Marks',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"Marks"}))
    NameOfTheCollege=forms.CharField(label='College Name',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"College Name"}))
    MobileNo=forms.CharField(label='Mobile No',widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"MobileNo"}))
    State=forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"State"}))
    Dist=forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"District"}))
    Address=forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"Address"}))
    Pincode=forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px',"placeholder":"Pincode"}))

    class Meta:
        model=AppForm
        fields='__all__'

    def clean_Name(self, *args, **kwargs):
        Name=self.cleaned_data.get("Name")
        if len(Name)<2:
            raise forms.ValidationError("Not valid")
        else:
            return Name

    def clean_MobileNo(self,*args, **kwargs):
        MobileNo=self.cleaned_data.get("MobileNo")
        if len(MobileNo)<9:
            raise forms.ValidationError("Not a valid number")
        else:
            return MobileNo

    def clean_Pincode(self,*args,**kwargs):
        Pincode=self.cleaned_data.get("Pincode")
        if len(Pincode)<6:
            raise forms.ValidationError("Pincode should contain 6 digits")
        else:
            return Pincode



class SignUpForm(forms.ModelForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter Name'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Password'}))
    email =forms.CharField(widget=forms.EmailInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Email'}))
    first_name =forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter First Name'}))
    last_name =forms.CharField(widget=forms.TextInput(attrs={'class':'input-md form-control','style':'width:500px','placeholder':'Enter Last Name'}))
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
