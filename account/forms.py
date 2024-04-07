from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}),
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}),
        label=''
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'input100'})

        self.fields['old_password'].label = ''
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'

        self.fields['new_password1'].help_text = ''

        # Customize error messages
        self.fields['new_password1'].validators = [
            self.validate_length,
            self.validate_common_sequences,
            self.validate_numeric_password,
        ]
    
    def validate_length(self, password):
        if len(password) < 8:
            raise ValidationError(_("Your password must contain at least 8 characters."))
        
    def validate_common_sequences(self, password):
        # Add your own logic to check for common sequences
        pass
        
    def validate_numeric_password(self, password):
        if password.isdigit():
            raise ValidationError(_("Your password can't be entirely numeric."))

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'input100'})

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'Add your Email'

        
class CustomPasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'input100'})
        
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'

        self.fields['new_password1'].help_text = ''

        # Customize error messages
        self.fields['new_password1'].validators = [
            self.validate_length,
            self.validate_common_sequences,
            self.validate_numeric_password,
        ]
    
    def validate_length(self, password):
        if len(password) < 8:
            raise ValidationError(_("Your password must contain at least 8 characters."))
        
    def validate_common_sequences(self, password):
        # Add your own logic to check for common sequences
        pass
        
    def validate_numeric_password(self, password):
        if password.isdigit():
            raise ValidationError(_("Your password can't be entirely numeric."))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='',
                                widget=forms.PasswordInput({'class': 'input100', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput({'class': 'input100', 'placeholder': 'Repeat Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input100',
                'placeholder': 'Username'}),

            'first_name': forms.TextInput(attrs={
                'class': 'input100', 
                'placeholder': 'First_Name'}),

            'last_name': forms.TextInput(attrs={
                'class': 'input100', 
                'placeholder': 'Last_Name'}),

            'email': forms.EmailInput(attrs={
                'class': 'input100',
                'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match")
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First_Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last_Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),  
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo', 'bio', 'detail_photo', 'back_photo']

        labels = {
            'date_of_birth': '',
            'photo': '',
            'bio': '',
            'detail_photo': 'Detail Image',
            'back_photo': 'Back Image',
        }

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter your birthday'}),
            'photo': forms.FileInput(attrs={'class': 'input-file', 'value': 'Upload new image'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'value': 'Tell us about yourself', 'rows': "5"}),
            'detail_photo': forms.FileInput(attrs={'class': 'btn btn-info', 'value': ''}),
            'back_photo': forms.FileInput(attrs={'class': 'btn btn-info'}),
        }
