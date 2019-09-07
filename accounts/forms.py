from django.contrib.auth.models import User
from django import forms

class RegistForm(forms.ModelForm):
    password  = forms.CharField(label='Password', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget= forms.PasswordInput)



    # 메타 클래스를 이용하면 기존에 있는 모델의 입력 폼을 쉽게 만들 수 있다.
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
