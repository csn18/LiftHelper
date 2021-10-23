from django.forms import ModelForm, TextInput

from CodeWarsHelper.models import Members


class MemberForm(ModelForm):
    class Meta:
        model = Members
        fields = '__all__'

        widgets = {
            'member_name': TextInput(attrs={
                'placeholder': 'Имя пользователя',
                'class': 'member_name'
            }),

            'code_wars_username': TextInput(attrs={
                'placeholder': 'Ник на CodeWars'
            })
        }
