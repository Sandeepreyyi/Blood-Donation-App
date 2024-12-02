from datetime import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.

class CustomUser(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model( email=self.normalize_email(email), **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None ):

        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

# Custom User Model
class User(AbstractBaseUser):
    BLOOD_GROUPS = [
            ('o+','O+'),
            ('a+', 'A+'),
            ('b+','B+'),
            ('ab+', 'AB+'),
            ('o-','O-'),
            ('a-', 'A-'),
            ('b-','B-'),
            ('ab-', 'AB-')
    ]
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Stored in hashed format
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="customer_profile",blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number =models.CharField(max_length=10, null=True)
    blood_group_type = models.CharField(max_length=3,choices=BLOOD_GROUPS,null=True,default='o+')
    address=models.CharField(max_length=300,null=True,blank=True)
    pincode = models.CharField(max_length=100,blank=True, null=True)






    objects = CustomUser()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    def update_login_time(self):
        self.last_login_time = timezone.now()
        self.save()


