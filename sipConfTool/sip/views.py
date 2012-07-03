from django.http import HttpResponse
from django.template import Context, loader
import syncLdap
from sip.models import Users,SipUser

def sync(request):
    ###This list of attributes must match whit the next mark list
    user_list = syncLdap.getUserList(['uid','cn'])
    for each in user_list:
        if (len(Users.objects.filter(username=each['uid'][0])) == 0):
            #### *** Mark of list
            newUser = Users(username = each['uid'][0], name = each['cn'][0])
            newUser.save()
    return HttpResponse(each['uid'][0])

def show(request):
    t = loader.get_template('users.html')
    all_entries = Users.objects.all().values('username')
    usernames = []
    for each in all_entries:
        usernames.append(each['username'])
    c = Context({
        'user_list' : usernames,
        })
    return HttpResponse(t.render(c))

