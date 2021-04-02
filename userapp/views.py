from django.shortcuts import render,HttpResponse,redirect
from administrator.models import tbl_user
from .models import tbl_client,tbl_project,tbl_project_user
# Create your views here.
def homepage(request):
    title = 'homepage'
    return render(request,'index.html',{'title':title})
    

def userlogin(request):
    title = 'login'
    if request.method == "GET":
        return render(request,'login.html',{'title':title})
    else:
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        try:
            tbl_user.objects.get(username=uname,password=pwd)
        except:
            message = "Invalid User Credentials"
            return render(request,'login.html',{'message':message,'title':title})
        else:
            request.session['uname'] = uname
            return redirect(homepage)

def logout(request):
    request.session.clear()
    return redirect(userlogin)

def addclient(request):
    if 'uname' in request.session:
        title = 'Addclient'
        if request.method == "GET":
            return render(request,'addclient.html',{'title':title})
        else:
            client = request.POST['client']
            uname = request.session['uname']
            clientobj = tbl_client()
            clientobj.client_name = client
            clientobj.created_by = uname
            clientobj.save()
            return redirect(homepage)
    else:
        return redirect(userlogin)

def viewclient(request):
    title = 'ViewClients'
    clients = tbl_client.objects.all()
    projects = tbl_project_user.objects.all()
    return render(request,'viewclient.html',{'title':title,'clients':clients,'projects':projects})
        
def editclient(request,id):
    if 'uname' in request.session:
        title='EditClient'
        if request.method == "GET":
            client = tbl_client.objects.get(id=id)
            return render(request,'editclient.html',{'title':title,'client':client})
        else:
            cid = request.POST['cid']
            client = request.POST['client']
            uname = request.session['uname']
            clientobj = tbl_client.objects.get(id=cid)
            clientobj.client_name = client
            clientobj.created_by = uname
            clientobj.save()
            return redirect(viewclient)
    else:
        return redirect(userlogin)

def deleteclient(request,id):
    client = tbl_client.objects.get(id=id)
    client.delete()
    return redirect(viewclient)

def addproject(request):
    if 'uname' in request.session:
        title = 'addproject'
        if request.method == "GET":
            clients = tbl_client.objects.all
            return render(request,'addproject.html',{'title':title,'clients':clients})
        else:
            project = request.POST['project']
            cid = request.POST['client']
            uname = request.session['uname']
            client = tbl_client.objects.get(id=cid)
            projectobj = tbl_project()
            projectobj.project_name = project
            projectobj.client = client
            projectobj.created_by = uname
            projectobj.save()
            return redirect(homepage)
    else:
        return redirect(userlogin)

def assignuser(request):
    if 'uname' in request.session:
        title = 'AssignUser'
        if request.method == "GET":
            users = tbl_user.objects.all()
            projects = tbl_project.objects.all()
            return render(request,'assignuser.html',{'title':title,'users':users,'projects':projects})
        else:
            pid = request.POST["project"]
            username = request.POST["user"]
            project = tbl_project.objects.get(id = pid)
            user = tbl_user.objects.get(username = username)
            try:
                tbl_project_user.objects.get(project=project,user=user)
            except:
                userobj = tbl_project_user()
                userobj.project = project
                userobj.user = user
                userobj.save()
                return redirect(homepage)
            else:
                message = 'This user is already assigned to the same project'
                return render(request,'assignuser.html',{'title':title,'message':message})
    else:
        return redirect(userlogin)

def myprojects(request):
    title = 'Myprojects'
    if 'uname' in request.session:
        uname = request.session["uname"]
        projects = tbl_project_user.objects.filter(user=uname)
        return render(request,'myprojects.html',{'title':title,'projects':projects})
    else:
        return redirect(userlogin)