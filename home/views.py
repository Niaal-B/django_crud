from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def add(request):
    details=User.objects.all()

    if request.method=="POST":
      name=request.POST.get('name')
      email=request.POST.get('email')
      password=request.POST.get('password')

      user=User.objects.create(username=name,email=email,password=password)
      user.save()
      return redirect('add')
    return render(request,'add.html',{
       'd':details
    })

def delete(request, user_id):
    print(f"Attempting to delete user with ID: {user_id}")
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('add')  # Ensure 'add' is a valid URL name

def update(request,user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        new_name = request.POST.get('name')

        if new_name:
            user.username = new_name

        user.save()
        return redirect('add')

    return render(request, 'update.html', {'user': user})