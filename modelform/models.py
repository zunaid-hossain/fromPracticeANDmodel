from django.db import models

# Create your models here.
class studentModel(models.Model):
    ID = models.AutoField(primary_key=True)
    AGE = models.IntegerField()
    image = models.ImageField(upload_to='templates/images')
    CGPA = models.FloatField()
    email = models.EmailField()
    PhoneNumber = models.BigIntegerField()
    duration_field = models.DurationField()
    birthday = models.DateTimeField()
    Application_date = models.DateField()    
    file_field = models.FileField(upload_to='templates/images')
    rating = models.SmallIntegerField()
    NAME=models.CharField(max_length=20)

    def __str__(self):
        return self.NAME

