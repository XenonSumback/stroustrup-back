from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm_password', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']
            if password == confirm_password:
                return confirm_password
        raise forms.ValidationError('Passwords do not match.')
