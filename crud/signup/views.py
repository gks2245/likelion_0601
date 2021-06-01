from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Signup

# Create your views here.
def home(request):
    signups = Signup.objects.all()
    return render(request, 'home.html', {'signups':signups})

def detail(request, id):
    signup = get_object_or_404(Signup, pk=id)
    return render(request, 'detail.html', {'signup':signup})

def new(request): # new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    new_signup = Signup()
    new_signup.name = request.POST['name']
    new_signup.age = request.POST['age']
    new_signup.email = request.POST['email']
    new_signup.pub_date = timezone.now()
    new_signup.introduce = request.POST['introduce']
    new_signup.save()
    return redirect('detail', str(new_signup.id))

def edit(request, id):
    edit_signup = Signup.objects.get(id=id)
    return render(request, 'edit.html', {'signup':edit_signup})

def update(request, id):
    update_signup = Signup.objects.get(id=id)
    update_signup.name = request.POST['name']
    update_signup.age = request.POST['age']
    update_signup.email = request.POST['email']
    update_signup.pub_date = timezone.now()
    update_signup.introduce = request.POST['introduce']
    update_signup.save()
    return redirect('detail', str(update_signup.id))

def delete(request, id):
    delete_signup = Signup.objects.get(id=id)
    delete_signup.delete()
    return redirect('home')