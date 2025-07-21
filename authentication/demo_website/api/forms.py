from django import forms
from django.contrib.auth.models import User

class TehmanMethod(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        # The above will hash the password for little security reasons
        if commit:
            user.save()
        return user


