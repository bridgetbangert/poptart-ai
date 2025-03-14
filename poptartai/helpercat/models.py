from django.db import models
from django.db.models import JSONField

class UserInfo(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    phone = models.BigIntegerField()
    phone_ext = models.SmallIntegerField()
    links = JSONField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class WorkExperienceMetadata(models.Model):
    exp_id = models.IntegerField(primary_key=True)
    worker_id = models.IntegerField()
    company = models.TextField()
    title = models.TextField()
    location = models.TextField()
    onsite_sts = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.exp_id
    

class WorkExperience(models.Model):
    exp_id = models.IntegerField()
    experience = models.TextField()

    def __str__(self):
        return self.exp_id
    

class ProjectsMetadata(models.Model):
    proj_id = models.IntegerField(primary_key=True)
    worker_id = models.IntegerField()
    title = models.TextField()
    link = models.TextField()
    org = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title + " for " + self.org
    

class Projects(models.Model):
    proj_id = models.IntegerField()
    experience = models.TextField()

    def __str__(self):
        return self.proj_id
   
class Skills(models.Model):
    worker_id = models.IntegerField()
    skill = models.TextField()

    def __str__(self):
        return self.id + " - " + self.skill
    
class Education(models.Model):
    worker_id = models.IntegerField()
    establishment = models.TextField()
    degree_cert = models.TextField()
    major = models.TextField()
    minor = models.TextField()
    concentration = models.TextField()
    city = models.TextField()
    gpa = models.FloatField()
    extracirriculars = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __init__(self):
        return self.id + " " + self.degree_cert + " at " + self.establishment