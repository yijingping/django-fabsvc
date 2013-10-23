from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.name 

class Host(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.name 

class Service(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    group = models.ForeignKey(Group)
    host = models.ForeignKey(Host)

    def __unicode__(self):
        return '%s' % self.name 

