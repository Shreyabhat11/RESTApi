from django.db import models

# Create your models here.

#Company model
class Company(models.Model):
    app_label = 'api'
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ("Mobile phones","Mobile Phones")
                           ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) 

    def __str__(self) -> str:
        return self.name + '-' +self.location

#Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=20,choices=
                                (('Manager','Manager'),
                                 ('Software Developer','SD'),
                                 ('Data Analyst','DA'),
                                 ('Project Leader','PL')
                                 ))
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
