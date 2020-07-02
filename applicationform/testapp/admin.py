from django.contrib import admin
from testapp.models import AppForm
# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display=['Name','FatherName','MotherName','DOB','Email','MobileNo','SSCMarks','NameOfTheSchool','InterMarks','NameOfTheCollege','State','Dist','Address','Pincode']

admin.site.register(AppForm,FormAdmin)
