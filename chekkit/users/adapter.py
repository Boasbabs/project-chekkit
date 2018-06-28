from allauth.account.adapter import DefaultAccountAdapter


class MyCustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        user.email = data['email']
        user.company_name = data['company_name']
        user.registration_number = data['registration_number']
        user.phone_number = data['phone_number']
        user.company_address = data['company_address']
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
