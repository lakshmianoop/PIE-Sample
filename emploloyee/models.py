from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.

class Employee(models.Model):
	name = models.CharField('Name',max_length = 100)
	address = models.CharField('Address',max_length=200)
	manager = models.ForeignKey("self", blank = True, null = True,  help_text= 'Manager')
	department = models.ForeignKey("Department")
	doj = models.DateTimeField('Joined On',auto_now_add=True, null=True, blank=True)
#	doj = models.DateField(_("Date"), default=date.today)
	def __str__(self):
		return self.name
class Department(models.Model):
	name = models.CharField(max_length = 100)
#	hod = models.ForeignKey("Employee",help_text= 'Head of the Department', related_name='hods',null = True)
	def __str__(self):
		return self.name


