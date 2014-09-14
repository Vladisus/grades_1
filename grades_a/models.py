from django.db import models

class student(models.Model):
    name = models.CharField(max_length=20)
    alg_grades = models.TextField(max_length=500, blank=True)
    alg_term_grades = models.TextField(max_length=200, blank=True)
    geom_grades = models.TextField(max_length=500, blank=True)
    geom_term_grades = models.TextField(max_length=200, blank=True)
    latest_grade = models.CharField(max_length=20, default='---')

    def __str__(self):
        return self.name





        

