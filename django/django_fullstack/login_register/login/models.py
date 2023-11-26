from django.db import models
import re
# Create your models here.
class Validation(models.Manager):
    def validate(self, data):
        errors = {}
        if len(data['first_name']) < 2 :
            errors['firs_name'] = "First Name should be at least 2 characters"
        
        if len(data['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        
        if data['password'] != data['conf_password']:
            errors['password_conf'] = "Password and Password Confirmation should Match!"
        
        if len(data['password']) < 8 :
            errors['password'] = "Password Must be at least 8 characters"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email  = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    uodated_at = models.DateTimeField(auto_now=True)
    objects = Validation()