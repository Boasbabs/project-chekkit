from django import forms
from django.contrib.auth.models import User

"""
The company name, reg. Number, contact email, company  size (no. Of employee range


e.g. Petere.g. Peter
LAST NAME 

e.g. Jones
JOB TITLE 

e.g. CEO
COMPANY NAME 

e.g. Project Provenance Ltd
ABOUT YOUR COMPANY 

e.g. We make wine from grapes grown in the UK
WHICH OF THE FOLLOWING BEST DESCRIBES YOU? 

Maker or manufacturer of physical products

Ingredient or material producer

Brand

Retailer or wholesaler

Certifier or auditor
LOCATION 

Ghana
Please specify a location as close to street level as possible
WEBSITE 

e.g. https://www.yourwebsite.com
WHY ARE YOU INTERESTED IN USING OUR SOFTWARE?

Maker or manufacturer of physical products

Ingredient or material producer

Brand

Retailer or wholesaler

Certifier or auditor


A small / medium business looking to be more transparent with my customers

An enterprise interested in improving brand trust through supply chain transparency

An organisation looking to explore partnership opportunities

An interested individual


"""


class SignupForm(forms.Form):
    USER_TYPE_CHOICES = [
        ("SME", "small / medium business"),
        ("ENTERPRISE", "enterprise"),
        ("ORGANISATION", "organisation"),
        ("INDIVIDUAL", "individual"),

    ]
    USER_BUSINESS_CHOICES = (
        ("MANUFACTURER", "Maker or manufacturer of physical products"),
        ("PRODUCER", "Ingredient or material producer"),
        ("RETAILER", "Retailer"),
        ("AUDITOR", "Auditor"),
    )

    email = forms.EmailField(label="Company Email", max_length=254, help_text='Required. Inform a valid email address.')
    company_name = forms.CharField(max_length=30, required=False)
    registration_number = forms.CharField(max_length=30, required=False,)
    phone_number = forms.CharField(max_length=15, label="Company Phone Number", help_text='Required' )
    location = forms.CharField(label="Location", max_length=225,  required=False,)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="I am", widget=forms.RadioSelect(), required=True)
    user_business = forms.ChoiceField(choices=USER_BUSINESS_CHOICES,
                                      label="Which of the following best describes you?")

    field_order = [
        "company_name",
        "email",
        "user_type",
        "phone_number",
        "user_business",
        "location",
        "registration_number",

    ]

    class Meta:
        model = User
        fields = ('company_name', 'location', 'registration_number', 'phone_number', 'email', 'password1', 'password2',)

    def signup(self, request, user):

        # Ensure you call the parent classes save.
        user.company_name = self.cleaned_data["company_name"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.location = self.cleaned_data["location"]
        user.registration_number = self.cleaned_data["registration_number"]

        user.save()
        user.profile.user_type = self.cleaned_data["user_type"]
        user.profile.user_business = self.cleaned_data["user_business"]

        # .save() returns a User object.
        # user = super(SignupForm, self).save()


        # You must return the original result.
        return user
