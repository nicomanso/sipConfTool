from sip.models import SipUser,Users
from django.contrib import admin
from django import forms


class SipForm(forms.ModelForm):

    class Meta:
        model = SipUser


class SipAdmin(admin.ModelAdmin):
    form = SipForm

admin.site.register(SipUser, SipAdmin)
