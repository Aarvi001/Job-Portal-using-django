from django.db import models
from django.db.models.deletion import CASCADE


GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)

STATUS_PENDING = 'pending'
STATUS_ACCEPT = 'accepted'
STATUS_REJECT = 'rejected'
STATUS_CHOICES = (
    (STATUS_PENDING, 'PENDING PLEASE WAIT', ),
    (STATUS_ACCEPT, 'ACCEPTED CONGRATS'),
    (STATUS_REJECT, 'SORRY REEJECTED'),
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
        return "{} - {}".format(self.name, self.mobile)


class CandidateJobMap(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=CASCADE)
    job = models.ForeignKey('jobs.Job', on_delete=CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.candidate.name, self.job.position_name)
