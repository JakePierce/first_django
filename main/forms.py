from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div 
from crispy_forms.bootstrap import FormActions
from main.models import City, State, StateCapital

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    #arg are variables, key-word arguments are variables and a value.
    #val, val2="something"
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact_view/'
        self.helper.layout = Layout(
            Div('name', 'email', 'phone', css_class='col-md-6'),
            Div('message', css_class='col-md-6')
            )

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class="btn-primary"))

        )
            

class CityEditForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        #['NAME', 'county', 'state']

    def __init__(self, *args, **kwargs):
        super(CityEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/city_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )


class StateEditForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StateEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary")
                )
            )


class StateCapitalEditForm(forms.ModelForm):
    class Meta:
        model = StateCapital
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StateCapitalEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/statecapital_edit/%s' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save changes', "Save Changes", css_class="btn-primary")
                )
            )
