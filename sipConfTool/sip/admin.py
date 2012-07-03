from sip.models import SipUser,Users
from django.contrib import admin
from django import forms


class SipForm(forms.ModelForm):
    #Show users that haven't been configured yet
    users = Users.objects.filter(sipuser__callerid__isnull=True).values('name','username')
    userChoices = tuple([(each['username'],each['name']) for each in users])
    callerid = forms.CharField(widget=forms.Select(choices=userChoices))
    
    username = forms.IntegerField(initial=999)
    context = forms.CharField(initial='usuario_4')
    host = forms.CharField(initial='dynamic')
    canreinvite = forms.BooleanField(initial=False)
    qualify = forms.BooleanField(initial=True)
    pickupgroup = forms.IntegerField(initial=1)
    callgroup = forms.IntegerField(initial=1)

    def clean_callerid(self):
        from django.core.exceptions import ValidationError
        choiceCallerId = self.cleaned_data['callerid']
        try:
            user = Users.objects.get(username=choiceCallerId)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError("No existe el usuario")



    class Meta:
        model = SipUser


        


class SipAdmin(admin.ModelAdmin):
    form = SipForm

admin.site.register(SipUser, SipAdmin)
