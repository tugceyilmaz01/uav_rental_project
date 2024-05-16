from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    """
    abstract : True -> BaseModel'in bir tablo oluşturmasını engeller ve 
    sadece diğer modellerin bu sınıfı miras almasını sağlar.
    Yukarıdaki alanların her kayıt için gerekli olduğunu düşündüğüm için
    Burada abstract bir model oluşturup diğer modelleri bu class'tan türettim
    """

    class Meta:
        abstract = True  # This makes the model abstract


class Category(BaseModel):

    '''

    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UAV(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.category.name}-{self.brand.name}-{self.model}"


class Rental(BaseModel):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_start_date = models.DateTimeField()
    rental_end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.uav.model} rented by {self.user.get_full_name()}"
