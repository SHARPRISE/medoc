"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import MyDoctor

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Email'}))
    country = forms.CharField(widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Country'}))
    specialite = forms.CharField(widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'specialite'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput({
        'class': 'form-control',
        'placeholder':'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput({
        'class': 'form-control',
        'placeholder':'Another one! Enter your password again!'}))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 4:
        	raise forms.ValidationError("Password is too short")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_name(self):
    	name = self.cleaned_data.get('name')
    	try:
    		exists = MyDoctor.objects.get(name=name)
    		raise forms.ValidationError("This name already exists")
    	except MyDoctor.DoesNotExist:
    		return name
    	except:
    		raise forms.ValidationError("There was an error, please try again or contact us.")

    def clean_email(self):
    	email = self.cleaned_data.get("email")
    	try:
    		exists = MyDoctor.objects.get(email=email)
    		raise forms.ValidationError("This email is taken")
    	except MyDoctor.DoesNotExist:
    		return email
    	except:
    		raise forms.ValidationError("There was an error, please try again or contact us.")

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Another one! Write it again', widget=forms.PasswordInput)
    country = forms.CharField(label='Country', widget=forms.TextInput)
    specialite = forms.CharField(label='specialite', widget=forms.TextInput)

    class Meta:
        model = MyDoctor
        fields = ('email', 'name', 'country', 'specialite', 'owner_first_name', 'owner_last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = MyDoctor
        fields = ('email', 'password', 'country', 'specialite', 'name', 'owner_first_name', 'owner_last_name', 'is_active', 'is_admin', "is_member")

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class LoginForm(forms.Form):
    #Authentication form which WILL USE BOOTSTRAP NOW AND NOT THIS RAW UGLY LOOKING SHIT THAT WAS THERE BEFORE"
	name = forms.CharField(label="Your username", widget=forms.TextInput({
                                       'class': 'form-control',
                                       'placeholder': 'User name'}))
	password = forms.CharField(label=_("Password"),
                widget=forms.PasswordInput({
                'class':'form-control',
                'placeholder':'Password'}))



class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
