from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    loaction=models.CharField( max_length=50)
    about=models.TextField()
    type=models.CharField( max_length=50,choices=(('IT','IT'),('WEB','WEB'),('Software','Software')))
    
    date=models.DateTimeField( auto_now=True,)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name +'--'+self.loaction
    
    
class Employee(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    about=models.TextField()
    postion=models.CharField( max_length=50,choices=(('CEO','CEO'),('manager','Manger'),('Developer','Developer')))
    company=models.ForeignKey(Company, on_delete=models.CASCADE)