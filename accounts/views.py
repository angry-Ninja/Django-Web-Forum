from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
def signup(request):
	if request.method=='POST':
		form=NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f"New Account Created :{username}")
			login(request,user)
			return redirect('home')
		else:

			for msg in form.error_messages:
				#print(form.error_messages[msg])
				messages.warning(request,"password Mismatch")
				
			
			return render(request = request,
				          template_name="accounts/signup.html",
				          context={"form": form})
	else:
		form=NewUserForm()
		return render(request, 'accounts/signup.html', {'form': form})

def login_request(request):
	if request.method=="POST":
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				messages.success(request, "User Logged in Successfully")
				login(request, user)

				return redirect('home')
			else:
				messages.warning(request,"Invalid Username or Password")
		else:
			messages.error(request,"Invalid Username or Password")

	form = AuthenticationForm()
	return render(request = request,
					template_name = "accounts/login.html",
					context={"form":form})
	

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'email', )
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
