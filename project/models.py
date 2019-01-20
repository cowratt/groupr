from django.db import models
from django.contrib.auth.models import AbstractUser
#import project.models_.graph as Graph
#import networkx as nx


from django.core.validators import int_list_validator

# Create your models here.

class Test(models.Model):
	count = models.IntegerField(default=0)

#class User(AbstractUser):
#	bio = models.TextField(max_length=500, blank=True)
#	birth_date = models.DateField(null=True, blank=True)
#	pic = models.ImageField(null=True)

class Graph(models.Model):
	nodes = models.CharField(max_length=500)
	edges_a = models.CharField(max_length=5000)
	edges_b = models.CharField(max_length=5000)
	def __str__(self):
		pass
	def getEdges(self):
		if len(self.edges_a) == 0:
			return[]
		else:
			a = [int(i) for i in self.edges_a.split(' ')]

		if len(self.edges_b) == 0:
			return[]
		else:
			b = [int(i) for i in self.edges_b.split(' ')]
		return list(zip(a, b))

	def setEdges(self, edges):
		(a, b) = list(zip(*edges))

		self.edges_a = ' '.join(map(str,a))
		self.edges_b = ' '.join(map(str,b))

	def getNodes(self):
		if len(self.nodes) == 0:
			return []
		else:
			return list([int(i) for i in self.nodes.split(' ')])

	def setNodes(self, nodes):
		self.nodes = ' '.join(map(str,nodes))

class Event(models.Model):
	name = models.TextField(max_length=50)
	group_size = models.IntegerField()
	di = models.OneToOneField(
        Graph,
        on_delete=models.PROTECT,
        related_name = 'di',
    )
    """
	undi = models.OneToOneField(
        Graph,
        on_delete=models.PROTECT,
        related_name = 'undi',
    )
    """
	users = models.CharField(max_length=5000, default="", blank = True) #optional
	creator = models.CharField(max_length=150, blank=False)
	userson = models.CharField(max_length=5000, default="", blank = True) #optional

	def getUsers(self):
		a = self.users.split(' ')
		return a

	def getUsersOn(self):
		a = self.userson.split(' ')
		return a

	def setUserOn(self, pos, num):
		a = self.userson.split(' ')
		a[pos] = num
		self.userson = ' '.join(str(x) for x in a)

	def addUser(self, id):
		if len(self.users) == 0:
			self.users = self.users + id
			self.userson = self.userson + str(0)
		else:
			self.users = self.users + " " + id
			self.userson = self.userson + " " + str(0)

		self.di.

class Groups(models.Model):
	linkedEventId = models.TextField(max_length=50)
	users = models.CharField(max_length=5000);

	def getEventId(self):
		return self.linkedEventId

	def getUsers(self):
		a = self.users.split(' ')
		return a

	def addUser(self, id):
		if len(self.users) == 0:
			self.users = self.users + id
		else:
			self.users = self.users + " " + id