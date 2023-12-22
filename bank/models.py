from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def __str__(self):
        return  '{}' .format(self.name)

class Branch(models.Model):
    name = models.CharField(max_length=250,unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return '{}' . format(self.name)

class Material(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.name

class UserForm(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
    ]
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone_number = models.IntegerField()
    mail_id = models.EmailField()
    address = models.CharField(max_length=250)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType,on_delete=models.CASCADE)
    material_provided = models.ManyToManyField(Material)

    class Meta:
        ordering = ('name',)
        verbose_name = 'form'
        verbose_name_plural = 'forms'

    def __str__(self):
        return '{}' . format(self.name)

