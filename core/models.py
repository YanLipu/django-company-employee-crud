from django.db import models

# Create your models here.    
class Company(models.Model):
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    
class Employe(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    start_vacation_date = models.CharField(max_length=50)
    end_vacation_date = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name