from django import forms
class PersonForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Name Here...'
            }
        )
    )
    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Company Name Here...'
            }
        )
    )
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Location Here...'
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Here...'
            }
        )
    )
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number Here...'
            }
        )
    )
    desc = forms.CharField(
        help_text="Write a brief about a Person.",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Description...'
            }
        )
    )