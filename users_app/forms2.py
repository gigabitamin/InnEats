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
            'user_address',
            'preferred_region_no',
            'preferred_accommodation_type_no',
            'preferred_tour_theme_type_no'
        )

        labels = {
            'username' : 'ID',
            'password' : '비밀번호',
            'email' : '이메일',
            'user_name' : '성명',
            'user_phone' : '전화번호',
            'user_address' : '주소',
            'preferred_region_no' : 'preferred_region',
            'preferred_accommodation_type_no' : 'preferred_accommodation_type',
            'preferred_tour_theme_type_no' :'preferred_tour_theme_type'
        }