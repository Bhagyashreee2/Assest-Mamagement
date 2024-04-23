from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    def create_user(self, First_Name, Last_Name, Email, Terms_Privacy_Policy, password=None, Re_type_Your_password=None):
        
        # Creates and saves a User with the given email and other details
        
        if not Email:
            raise ValueError("User must have an email address")

        user = self.model(
            Email=self.normalize_email(Email),
            First_Name = First_Name,
            Last_Name = Last_Name,
            Terms_Privacy_Policy = Terms_Privacy_Policy,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, First_Name, Last_Name, Email, Terms_Privacy_Policy, password=None):
        
        # Creates and saves a superuser with the given email and other details
        

        user = self.create_user(
        Email,
        password=password,
        First_Name=First_Name,
        Last_Name=Last_Name,
        Terms_Privacy_Policy=Terms_Privacy_Policy,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
    
#Custom User Model
class User(AbstractBaseUser):
    Email = models.EmailField(verbose_name='Email Address', max_length=250, unique=True)
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    Re_type_Your_password = models.CharField(max_length=250)
    Terms_Privacy_Policy = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['First_Name','Last_Name','Terms_Privacy_Policy']

    def __str__(self):
        return self.Email
    
    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        return True
    
    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        return self.is_admin

#add asset
class Employee(models.Model):
    Full_Name = models.CharField(max_length=100)
    Employee_ID = models.CharField(max_length=50, unique=True)
    Title = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Site = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Notes = models.TextField()

class Asset(models.Model):
    ASSET_STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Checked Out', 'Checked Out'),
    )

    Asset_Tag_ID = models.CharField(max_length=50, unique=True, primary_key=True)
    Asset_Name = models.CharField(max_length=100)
    Description = models.TextField()
    Purchase_From = models.CharField(max_length=100)
    Purchase_Date = models.DateField()
    Brand = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Serial_Number = models.CharField(max_length=50)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Site = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Asset_Photo = models.ImageField(upload_to='asset_photos/', null=True, blank=True) 
    Status = models.CharField(max_length=20, choices=ASSET_STATUS_CHOICES, default='Available')  
    

class Transaction(models.Model):
    TRANSACTION_STATUS_CHOICES = (
        ('Check Out', 'Check Out'),
        ('Check In', 'Check In'),
    )

    Asset_Tag_ID = models.ForeignKey(Asset, on_delete=models.CASCADE, db_column='Asset_Tag_ID')
    Check_Out_Date = models.DateField(null=True, blank=True)
    Check_In_Date = models.DateField(null=True, blank=True)
    Status = models.CharField(max_length=20, choices=TRANSACTION_STATUS_CHOICES)
    Department = models.CharField(max_length=100)
    Check_Out_To = models.CharField(max_length=100)
    Due_Date = models.DateField(null=True, blank=True)
    Check_Out_Notes = models.TextField(blank=True)
    Check_In_Note = models.TextField(blank=True)
    Email = models.EmailField()
    Assigned_To = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, db_column='Assigned_To')
  