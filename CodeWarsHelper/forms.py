from django.forms import ModelForm, TextInput, DateField

from CodeWarsHelper.models import Members, Subdivision, Group


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
            }),
        }


class SubdivisionForm(ModelForm):
    class Meta:
        model = Subdivision
        fields = '__all__'

        widgets = {
            'division_name': TextInput(attrs={
                'placeholder': 'Например, Python'
            })
        }


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'name_group': TextInput(attrs={
                'placeholder': 'Например, поток 12'
            }),
            'start_date': DateField()
        }
