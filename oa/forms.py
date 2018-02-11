from django import forms
# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    #next = forms.CharField(required=True, show_hidden_initial=True)