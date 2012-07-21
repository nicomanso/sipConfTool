from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.core.files import File
import syncLdap, hashlib,  time
from sip.models import Users,SipUser

@login_required
def sync(request):
    user_list = syncLdap.getUserList(['uid','cn'])
    for each in user_list:
        if (len(Users.objects.filter(username=each['uid'][0])) == 0):
            newUser = Users(username = each['uid'][0], name = each['uid'][0])
            newUser.save()
    return HttpResponse("Importaci&oacute;n exitosa")

@login_required
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

@login_required
def writeSipConf(request):
    users = SipUser.objects.all().order_by("username")
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    with open('/tmp/'+hash.hexdigest()[:7],  'w') as f:
        newFile = File(f);
        for each in users:
            newFile.write("["+str(each.username)+"](base)\n")
            newFile.write("username=" + str(each.username) + "\n")
            newFile.write("context=" + each.context + "\n")
            newFile.write("secret=" + each.secret + "\n")
            newFile.write("callerid=" + str(each.callerid) + " <" +str(each.username) +">\n")
            newFile.write("host=" + each.host + "\n")
            newFile.write("canreinvite=" + str(each.canreinvite) + "\n")
            newFile.write("qualify=" + str(each.qualify) + "\n")
            newFile.write("pickupgroup=" + str(each.pickupgroup) + "\n")
            newFile.write("callgroup=" + str(each.callgroup) + "\n")
            newFile.write( "\n\n")
    
    return HttpResponse("Archivo escrito correctamente")
