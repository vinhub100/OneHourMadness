from crispy_forms.layout import Layout
from django import forms
from django.forms.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field, Submit



class SignupForm(forms.Form):
    firstname = forms.CharField(label='First Name', required=True)
    lastname = forms.CharField(label='Last Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    username = forms.CharField(label='User Name', required=True)
    password = forms.CharField(label='Password', required=True)
    confirn_password = forms.CharField(label='Confirm Password', required=True)
    signup_date = forms.DateField(label='Today Date', widget=AdminDateWidget)

    @property
    def helper(self):
        helper = FormHelper()

        helper.layout = Layout(
            HTML('<h2 class="text-center p-3">Rigistration Form</h2>'),
            Field('firstname', wrapper_class='row'),
            Field('lastname', wrapper_class='row '),
            Field('email', wrapper_class='row '),
            Field('username', wrapper_class='row '),
            Field('password', wrapper_class='row '),
            Field('confirn_password', wrapper_class='row '),
            Field('signup_date', wrapper_class='row'),
            Submit('submit','Register', css_class='btn btn-outline-success btn-block')
        )
        helper.field_class = 'col-md-9 '
        helper.label_class = 'col-md-3'
        



        return helper
