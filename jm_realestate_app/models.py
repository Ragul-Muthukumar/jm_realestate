from django.db import models

class userdetail(models.Model):
	user_id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=100)
	emailid=models.CharField(max_length=100)
	mobilenumber=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

	class Meta:
		db_table="userdb"

class storeproperty(models.Model):
	id=models.AutoField(primary_key=True)
	p_id=models.CharField(max_length=100,default=None)
	city=models.CharField(max_length=100,default=None)
	area=models.CharField(max_length=100,default=None)
	landmark=models.CharField(max_length=100,default=None)
	length=models.CharField(max_length=100,default=None)
	width=models.CharField(max_length=100,default=None)
	totalsqft=models.IntegerField()
	image=models.FileField(max_length=100,upload_to='',blank=True,null=True,default=None)
	description=models.CharField(max_length=500)
	cat=models.CharField(max_length=20,default=None)
	price=models.IntegerField()
	opensides=models.CharField(max_length=100,default=None)
	water=models.CharField(max_length=100,default=None)
	electricity=models.CharField(max_length=100,default=None)
	sewage=models.CharField(max_length=100,default=None)
	road=models.CharField(max_length=100,default=None)
	squarefeet=models.CharField(max_length=100,default=None)
	bedroom=models.CharField(max_length=100,default=None)
	bathroom=models.CharField(max_length=100,default=None)


	class Meta:
		db_table="post_db"	

class report(models.Model):
	id=models.AutoField(primary_key=True)
	emailid=models.CharField(max_length=100)
	description=models.CharField(max_length=100)

	class Meta:
		db_table="report_db"
class order(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=100)
	emailid=models.CharField(max_length=100)
	mobilenumber=models.CharField(max_length=100)
	message=models.CharField(max_length=100,default=None)
	productid=models.CharField(max_length=100)

	class Meta:
		db_table="order_db"
class profit(models.Model):
	id=models.AutoField(primary_key=True)
	earning=models.IntegerField()

	class Meta:
		db_table='profit_db'


	
# Create your models here.
