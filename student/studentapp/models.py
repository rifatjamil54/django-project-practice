from django.db import models

# Create your models here.
class Student(models.Model):
    m_name = models.CharField(max_length=100)
    m_roll = models.IntegerField()
    m_number = models.IntegerField()
    m_year = models.IntegerField()

    class Meta:
        db_table = "student"    

    def __str__(self):
        return self.m_name
