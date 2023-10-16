from django import forms # 상속
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = (
            'username',
            'password',
            'email',
            'user_name',
            'user_phone',
            'user_address'
        )

        labels = {
            'username' : 'ID',
            'password' : '비밀번호',
            'email' : '이메일',
            'user_name' : '성명',
            'user_phone' : '전화번호',
            'user_address' : '주소'
        }