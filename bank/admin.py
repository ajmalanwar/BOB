from django.contrib import admin
from . models import  District,Branch,Material,AccountType,UserForm

# Register your models here.
class AdminDistrict(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(District,AdminDistrict)

class AdminBranch(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Branch,AdminBranch)

class AdminMaterial(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Material,AdminMaterial)

class AdminAccountType(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(AccountType,AdminAccountType)

class AdminUserForm(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'district', 'branch' , 'account_type', 'mail_id' , 'phone_number' , 'address' ]
    list_per_page = 20
admin.site.register(UserForm,AdminUserForm)
