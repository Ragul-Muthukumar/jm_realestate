from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from jm_realestate_app.models import userdetail,storeproperty,report,order,profit
from django.contrib.auth.decorators import login_required
import math
username_navbar=0
def home(request):
	global username_navbar
	if request.session.has_key('user'):
		email=request.session['user']
		username_navbar=userdetail.objects.get(emailid=email).username
	else:
		username_navbar=''#if else for fetch username from user after login and signup and display in navbar
	return render(request,"home.html",{'user':username_navbar})
def checklogin(request):#login
	if request.method=='POST':
		emailid=request.POST['emailid']
		password=request.POST['password']

		if userdetail.objects.filter(emailid=emailid).exists():
			if userdetail.objects.filter(password=password).exists():
				request.session['user']=emailid
				request.session['uid']=userdetail.objects.get(emailid=emailid).username
				return HttpResponseRedirect("/")
			else:
				messages.info(request,"Incorrect password")
				return render(request,"userlogin.html")
		else:
			messages.info(request,"Username Not found,Signup Now")
			return render(request,"userlogin.html")
	else:
		return render(request,"userlogin.html")
def postfullview(request,id):
	if request.session.has_key('user'):#this is for, if user has session,then only get inside this page 
		res=storeproperty.objects.get(id=id)
		u=request.session['uid']
		usr=userdetail.objects.get(username=u)#to fetch user details, and display in buy property input box
		return render(request,"postfullview.html",{'res':res,'res1':usr,'user':username_navbar})
	else:
		messages.success(request,"Login to see full details")
		return render(request,"Userlogin.html")
	
def userlogin(request):
	return render(request,"userlogin.html")

def adminlogin(request):
	return render(request,"adminlogin.html")
	

def userdetails(request):
	if request.session.has_key('user1'):
		res=userdetail.objects.all()
		return render(request,"userdetails.html",{'res':res})
	else:
		messages.success(request,"Login to see full details")
		return render(request,"adminlogin.html")
def enquirydetails(request):
	if request.session.has_key('user1'):
		res=order.objects.all()
		return render(request,"enquirydetails.html",{'res':res})
	else:
		messages.success(request,"Login to see full details")
		return render(request,"adminlogin.html")
def viewproperty(request):
	if request.session.has_key('user1'):
		res=storeproperty.objects.all()
		return render(request,"viewproperty.html",{'res':res})
	else:
		messages.success(request,"Login to see full details")
		return render(request,"adminlogin.html")
def deleteuser(request,user_id):
	res=userdetail.objects.get(user_id=user_id)
	del request.session['user']
	res.delete()	
	return HttpResponseRedirect('/userdetails')
def deletepost(request,id):
	res=storeproperty.objects.get(id=id)
	res.delete()
	return HttpResponseRedirect('/viewproperty')
def postproperty(request):
	if request.session.has_key('user1'):
		return render(request,"postproperty.html")
	else:
		messages.success(request,"Login to see full details")
		return render(request,"adminlogin.html")
def getreports(request):
	if request.session.has_key('user1'):
		res=report.objects.all()
		return render(request,"reports.html",{'res':res})
	else:
		messages.success(request,"Login to see full details")
		return render(request,"adminlogin.html")
def sellersignup(request):
	return render(request,"sellersignup.html")
def sell(request):
	return render(request,"sell.html")
def homeviewpage(request):
	cat="House"
	res1="Home"
	res=storeproperty.objects.filter(cat=cat)#to seprate home posts in homepageview.html
	return render(request,"homeviewpage.html",{'res':res,'res1':res1,'user':username_navbar})
def landviewpage(request):
	cat="Empty Land"
	res1="Plot/land"
	res=storeproperty.objects.filter(cat=cat)#to seprate land posts in homepage.html
	return render(request,"homeviewpage.html",{'res':res,'res1':res1,'user':username_navbar})
def searchpage(request):
	return render(request,"searchpage.html")
def storeuser(request):#signup
	if request.method=="POST":
		username=request.POST['username']
		mobilenumber=request.POST['mobilenumber']
		emailid=request.POST['emailid']
		password=request.POST['password']
		password2=request.POST['password2']
		if userdetail.objects.filter(emailid=emailid).exists():
			messages.info(request,"Email Id Already Exists,Try Another Email Id")
			return render(request,"userlogin.html")
		if userdetail.objects.filter(mobilenumber=mobilenumber).exists():
			messages.info(request,"Mobile Number Already Exists,Try Another Mobile Number")
			return render(request,"userlogin.html")
		if password==password2:
			saveuser=userdetail()
			saveuser.username=username
			saveuser.mobilenumber=mobilenumber
			saveuser.emailid=emailid
			saveuser.password=password
			saveuser.save()
			request.session['user']=emailid  
			request.session['uid']=userdetail.objects.get(emailid=emailid).username
			return HttpResponseRedirect("/")
		else:
			messages.info(request,"passwords are didn't match")
			return render(request,"userlogin.html")
	else:
		return render(request,"userlogin.html")



def property(request):
	if request.method=='POST':
		city=request.POST['city']
		area=request.POST['area']
		landmark=request.POST['landmark']
		length=request.POST['length']
		width=request.POST['width']
		totalsqft=request.POST['totalsqft']
		image=request.FILES['image']
		description=request.POST['description']
		cat=request.POST['cat']
		price=request.POST['price']	
		opensides=request.POST['opensides']
		water=request.POST['water']
		electricity=request.POST['electricity']
		sewage=request.POST['sewage']
		road=request.POST['road']
		bedroom=request.POST['bedroom']
		bathroom=request.POST['bathroom']
		p_id=request.POST['p_id']
		psq1=int(price)/int(totalsqft)
		psq=int(psq1)
		saveproperty=storeproperty()
		saveproperty.city=city
		saveproperty.area=area
		saveproperty.landmark=landmark
		saveproperty.length=length
		saveproperty.width=width
		saveproperty.totalsqft=totalsqft
		saveproperty.image=image
		saveproperty.description=description
		saveproperty.cat=cat
		saveproperty.price=price
		saveproperty.opensides=opensides
		saveproperty.water=water
		saveproperty.electricity=electricity
		saveproperty.sewage=sewage
		saveproperty.road=road
		saveproperty.bedroom=bedroom
		saveproperty.bathroom=bathroom
		saveproperty.squarefeet=psq
		saveproperty.p_id=p_id
		saveproperty.save()
		return render(request,"postproperty.html")
	else:
		return render(request,"postingform.html")
def searchbox(request):
	# result="Home"
	# result1=storeproperty.objects.filter(cat=result)
	e=request.POST['search']
	res=''
	if e!='':
		res=storeproperty.objects.filter(city__contains=e) or storeproperty.objects.filter(area__contains=e) or storeproperty.objects.filter(landmark__contains=e)
	if request.session.has_key('user'):
		email=request.session['user']
		name=userdetail.objects.get(emailid=email).username
	else:
		name=''	
	return render(request,"homeviewpage.html",{'res3':res,'res4':e,'user':name})

def searchbox1(request):
	e=request.POST['search']
	res=''
	if e!='':
		res=storeproperty.objects.filter(city__contains=e) or storeproperty.objects.filter(area__contains=e) or storeproperty.objects.filter(landmark__contains=e) or storeproperty.objects.filter(id__contains=e)
		
	return render(request,"viewproperty.html",{'res3':res})
def usersearch(request):
	e=request.POST['search']
	res=''
	if e!='':
		res=userdetail.objects.filter(user_id__contains=e) or userdetail.objects.filter(username__contains=e) or userdetail.objects.filter(emailid__contains=e) or userdetail.objects.filter(mobilenumber__contains=e)
		
	return render(request,"userdetails.html",{'res2':res})	
def editpostproperty(request,id):
	if request.session.has_key('user1'):
		res=storeproperty.objects.get(id=id)
		return render(request,"editpostproperty.html",{'res':res})
	else:
		messages.success(request,"Login to see full details")
		return render(request,"adminlogin.html")

def edit(request):
	if request.method=='POST':
		
		p_id=request.POST['p_id']
		city=request.POST['city']
		area=request.POST['area']
		landmark=request.POST['landmark']
		length=request.POST['length']
		width=request.POST['width']
		totalsqft=request.POST['totalsqft']
		image=request.FILES['image']
		description=request.POST['description']
		price=request.POST['price']
		cat=request.POST['cat']
		bedroom=request.POST['bedroom']
		bathroom=request.POST['bathroom']
		opensides=request.POST['opensides']	
		water=request.POST['water']
		electricity=request.POST['electricity']
		sewage=request.POST['sewage']
		road=request.POST['road']
		
		psq=int(price)/int(totalsqft)
		
		saveproperty=storeproperty.objects.get(p_id=p_id)
		saveproperty.p_id=p_id
		saveproperty.city=city
		saveproperty.area=area
		saveproperty.landmark=landmark
		saveproperty.length=length
		saveproperty.width=width
		saveproperty.totalsqft=totalsqft
		saveproperty.image=image
		saveproperty.description=description
		saveproperty.cat=cat
		saveproperty.bedroom=bedroom
		saveproperty.bathroom=bathroom
		saveproperty.opensides=opensides
		saveproperty.price=price
		saveproperty.water=water
		saveproperty.electricity=electricity
		saveproperty.sewage=sewage
		saveproperty.road=road
		saveproperty.squarefeet=psq
		saveproperty.save()
		return HttpResponseRedirect('/viewproperty')
def reports(request):#contact us page inbox 
	if request.method=='POST':
		emailid=request.POST['emailid']
		description=request.POST['description']
		savereport=report()
		savereport.emailid=emailid
		savereport.description=description
		savereport.save()

		return render(request,"home.html")
def tobuy(request,id):#buy property box inside full post view
	if request.method=='POST':
		username=request.POST['username']
		mobilenumber=request.POST['mobilenumber']
		emailid=request.POST['emailid']
		res1=storeproperty.objects.get(id=id)
		res2=res1.id
		saveorder=order()
		saveorder.username=username
		saveorder.mobilenumber=mobilenumber
		saveorder.emailid=emailid
		saveorder.productid=res2
		saveorder.save()
		#request.path_info
		return HttpResponseRedirect("/")
def adminviewfulldetails(request,id):
	res=order.objects.get(id=id)
	res1=res.productid
	res2=storeproperty.objects.get(id=res1)

	return render(request,"adminviewfulldetails.html",{'res':res,'res2':res2})
def earning(request,id):
	x=0
	res=storeproperty.objects.filter(id=id)
	for n in res:
		x+=n.price  #price got filter and stored in db 'profit'
		saveearn=profit()
		saveearn.earning=x
		saveearn.save()
		res.delete() #after clicking soldout the post should be deleted
	return HttpResponseRedirect('/adminpage1')
def adminpage1(request):
	if request.session.has_key('user1'):
		x=0
		res=userdetail.objects.all()
		res1=storeproperty.objects.all()
		res5=order.objects.all()
		res6=len(res5)
		res3=len(res)
		res4=len(res1)
		res7=profit.objects.all()
		for n in res7:
			x+=n.earning #get earning from profit ,add and display in totl earnings in dashboard
		return render(request,"adminpage1.html",{'res3':res3,'res4':res4,'res6':res6,'res10':x})
	else:
		messages.success(request,"Login to see full details")
		return render(request,"adminlogin.html")
def checkadminlogin(request):
	if request.method=='POST':
		adminid=request.POST['adminid']
		adminpassword=request.POST['adminpassword']
		if adminid == 'admin' and adminpassword == 'admin':
			request.session['user1']=adminid
			return HttpResponseRedirect ("/adminpage1")
		else:
			messages.info(request,"Incorrect password")
			return render(request,"adminlogin.html")

def adminlogout(request):
	if request.session.has_key('user1'):
		request.session.pop('user1')
	return render(request,"adminlogin.html")

# Create your views here.
