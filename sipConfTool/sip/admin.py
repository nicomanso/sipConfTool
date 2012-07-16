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
    canreinvite = forms.BooleanField(initial=False, required=False)
    qualify = forms.BooleanField(initial=True,  required=False)
    pickupgroup = forms.IntegerField(initial=1)
    callgroup = forms.IntegerField(initial=1)

    def yesNo(self,  choice):
        if choice == 1:
            return "yes"
        else:
            return "no"


    def clean_callerid(self):
        from django.core.exceptions import ValidationError
        choiceCallerId = self.cleaned_data['callerid']
        try:
            user = Users.objects.get(username=choiceCallerId)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError("No existe el usuario")

    def clean_canreinvite(self):
        choiceCanReinvite = self.cleaned_data['canreinvite']
        return self.yesNo(choiceCanReinvite)

    def clean_qualify(self):
        choiceQualify = self.cleaned_data['qualify']
        return self.yesNo(choiceQualify)
        

    class Meta:
        model = SipUser


class SipAdmin(admin.ModelAdmin):
    form = SipForm
    js = ()

admin.site.register(SipUser, SipAdmin)
