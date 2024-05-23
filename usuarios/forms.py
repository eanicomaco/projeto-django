from django import forms

class LoginForms(forms.Form):
    login=forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Digite o nome...'
            }
        )
    )
    senha=forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 12,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Digite a senha...'
            }
        )
    )