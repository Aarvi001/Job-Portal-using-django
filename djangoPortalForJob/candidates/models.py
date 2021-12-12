from django.db import models

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    expected_Salary = models.IntegerField()
    will_relocate = models.BooleanField(default=False)

    def __str__(self):
        return self.name
