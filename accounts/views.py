from django.shortcuts import render
from .forms import RegistForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = RegistForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # commit = False DB에 저장되는 것이 아니라 메모리 상에 저
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # 데이터 베이스에 저장
            return render(request,'registration/register_done.html',{'new_user':new_user})
    else:
        user_form = RegistForm()

    return render(request,'registration/register.html',{'form':user_form})