import email
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password, **extra_fields):
#         if not email:
#             raise ValueError(_("Users must have an email address"))
#         if not username:
#             raise ValueError(_("Users must have an username address"))
        
#         user = self.model(
#             email=self.normalize_email(email), 
#             username=username,
#             )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, username, password, **extra_fields):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password = password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

        
        



class extenduser(models.Model):
    STATUS = (
    ("PENDING", "PENDING"),
    ("ENROLLED", "ENROLLED"),
    )
    
    GRADE = (
        ("PENDING", "PENDING"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        
    )

    field_rotc = 0
    field_cwts = 1
    field_choices = [(field_rotc, 'ROTC'), (field_cwts, 'CWTS')]
    platoon = models.CharField(max_length=10, blank=True, null=True)
    lname = models.CharField(max_length=20, default='')
    fname = models.CharField(max_length=30, default='')
    minitial = models.CharField(max_length=3, default='')
    address = models.CharField(max_length=100, default='')
    cpnumber = models.DecimalField(max_digits=11, decimal_places=0, default='')
    email = models.EmailField(max_length=254, null=True, unique=True)
    gender = models.CharField(max_length=6, default='')
    age = models.DecimalField(max_digits=3, decimal_places=0)
    bdate = models.CharField(max_length=15, default='')
    password = models.CharField(max_length=20)
    grades = models.CharField(max_length=20, choices=GRADE, default='PENDING')
    grades1 = models.CharField(max_length=20, choices=GRADE, default='PENDING')
    section = models.CharField(max_length=20, default='')
    field = models.CharField(max_length=20, default='')
    picture = models.ImageField(upload_to='images/', null=False)
    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')
    cert_datereq = models.CharField(max_length=20, default='') 
    cert_document = models.CharField(max_length=20, default='') 
    cert_status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    
    def __str__(self):
    
        return self.email
    

    

class certifications(models.Model):
    STATUS = (
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        )
    cert_email = models.EmailField(max_length=254, null=True)
    cert_fullname = models.CharField(max_length=100)
    cert_course = models.CharField(max_length=20 )
    cert_datereq = models.CharField(max_length=20 )
    cert_document = models.CharField(max_length=20 )
    cert_status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
  
    
    def __str__(self):
        return self.cert_email
    
    
    
# platons

class alphamodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    # alphaImage = models.ImageField(upload_to='images/', null=False)
    def __str__(self):
        return self.name
    
class bravomodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class charliemodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class deltamodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class echomodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class foxtrotmodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class golfmodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class hotelmodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class indiamodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class julietmodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class kilomodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class limamodel(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

    
    
class carousel(models.Model):
    imagefile= models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.imagefile
    
    
    
class sectiona(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class sectionb(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class sectionc(models.Model):
    name = models.CharField(max_length=20)
    pdf= models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

