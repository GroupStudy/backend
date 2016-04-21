from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    netID = models.CharField(max_length=8)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    def __str__(self):
        return self.netID

class studentClasses(models.Model):
    className = models.CharField(max_length=40)
    student = models.ForeignKey(Student, related_name="student")
    def __str__(self):
        return self.className

class Places(models.Model):
    building = models.CharField(max_length=25)
    def __str__(self):
        return self.building

class checkedIn(models.Model):
    people = models.CharField(max_length=8)
    atBuilding = models.ForeignKey(Places, related_name="location")
    def __str__(self):
        return self.people


