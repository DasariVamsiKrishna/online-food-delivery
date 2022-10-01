from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,ItemsForm,UsgForm,Pfupd,Chgepwd,Order
from RestApp.models import Restaurant,Itemlist,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from Restaurant import settings

# Create your views here.
def home(request):
	w = Restaurant.objects.filter(uid_id=request.user.id)
	t = Restaurant.objects.all()
	return render(request,'app/home.html',{'c':w,'y':t})

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')



def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'app/usrregister.html',{'t':d})



@login_required
def pfle(request):
	return render(request,'app/profile.html')

@login_required
def feedback(request):
	if request.method == "POST":
		sd = request.POST['snmail'].split(',')
		sm = request.POST['sub']
		mg = request.POST['msg']
		rt = settings.EMAIL_HOST_USER
		dt = send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/')
	return render(request,'app/feedback.html')

@login_required
def pfleupd(request):
	t = User.objects.get(id=request.user.id)
	if request.method == "POST":
		pfl = Pfupd(request.POST,request.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/pfle')
	pfl = Pfupd(instance=t)
	return render(request,'app/pfleupdate.html',{'u':pfl})

@login_required
def changepwd(request):
	if request.method == "POST":
		k = Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = Chgepwd(user=request)
	return render(request,'app/changepwd.html',{'t':k})

@login_required
def order(request):
	p13 = Order()
	if request.method == "POST":
		p13 = Order(request.POST)
		if p13.is_valid():
			p13.save()
			messages.success(request,"order Added Successfully")
			return render(request,'app/orders.html',{'pp':p13})
	return render(request,'app/orders.html',{'pp':p13})


@login_required
def itemvew(request,s):
	r = Itemlist.objects.filter(rsid_id=s)
	return render(request,'app/itemuser.html',{'tq':r})