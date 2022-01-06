from crispy_forms.layout import Layout
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field, Submit



class SignupForm(forms.Form):
    firstname = forms.CharField(label='First Name', required=True)
    lastname = forms.CharField(label='Last Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', required=True)
    confirn_password = forms.CharField(label='Confirm Password', required=True)
    signup_date = forms.DateField(label='Today Date', widget=forms.SelectDateWidget(), required=True)

    @property
    def helper(self):
        helper = FormHelper()

        helper.layout = Layout(
            HTML('<h2 class="text-center">Signup Form</h2>'),
            Field('firstname'),
            Field('lastname'),
            Field('email'),
            Field('password'),
            Field('confirn_password'),
            Field('signup_date'),
            Submit('submit','Submit', css_class='btn btn-outline-success float-right')
        )

        return helper
