from os import name
from pyexpat.errors import messages
from django.contrib import messages 
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context

import nstpApp
# from .models import registration
from .models import certifications
from .models import extenduser
from .models import alphamodel, bravomodel, charliemodel, deltamodel, echomodel, foxtrotmodel, golfmodel, hotelmodel, indiamodel, julietmodel, kilomodel, limamodel, cwts, carousel


from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, permission_required
import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import certificationsForm
from django.http import FileResponse

idnum=''
password=''




# studentside

def index(request):
    images=carousel.objects.all()
    return render(request, 'activities/index.html', {'images': images})
def login(request):
    return render(request, 'activities/login.html')
def register(request):
    return render(request, 'activities/signup.html')

def navbar(request):
    data = registration.objects.all()
    return render(request, 'activities/base.html', {'data': data})

def footer(request):
    return render(request, 'activities/footer.html')

def navlanding(request):
    return render(request, 'activities/navlanding.html')

def indexcard1(request):
    return render(request, 'activities/index_card1.html')

def indexcard2(request):
    return render(request, 'activities/index_card2.html')

def indexcard3(request):
    return render(request, 'activities/index_card3.html')

def indexcard4(request):
    return render(request, 'activities/index_card4.html')

def rotclist(request):
    list = extenduser.objects.filter(field='ROTC').filter(status='ENROLLED')
    return render(request, 'activities/rotclist.html', {'list': list})
def cwtslist(request):
    list1 = extenduser.objects.filter(field='CWTS')
    return render(request, 'activities/cwtslist.html', {'list1': list1})

def adminrotclist(request):
    rlist = extenduser.objects.filter(field='ROTC').filter(status='PENDING')
    return render(request, 'activities/adminrotclist.html', {'rlist': rlist})

def admincwtslist(request):
    clist = extenduser.objects.filter(field='CWTS').filter(status='PENDING')
    return render(request, 'activities/admincwtslist.html', {'clist': clist})

def enrolledrotc(request):
    enrolled = extenduser.objects.filter(field='ROTC').filter(status='ENROLLED')
    return render(request, 'activities/enrolledrotc.html', {'enrolled': enrolled})



@login_required(login_url='/login')
def dashboard(request):
    name = extenduser.objects.filter(user = request.user)
    return render(request, 'activities/dashboard.html', {'name': name})

 

@login_required(login_url='/login')
# def requested(request):
#     requests = certifications.objects.filter(user = request.user)
#     return render(request, 'activities/certification.html', {'requests': requests})

# @login_required(login_url='/login')
def platoon(request):
    return render(request, 'activities/Platoon.html')
def cwtss(request):
    display = cwts.objects.all()
    return render(request, 'activities/Cwts.html', {'display': display})




def userlogout(request):
	return render(request, 'activities/login.html')

@login_required(login_url='/login')
def certification(request):
    requests = certifications.objects.all()
    return render(request, 'activities/certification.html', {'requests': requests})



def admincwts(request):
    fetch = cwts.objects.all()
    return render(request, 'activities/admincwts.html', {'fetch': fetch})


#                   STUDENT PLATOON DISPLAY

def student_alpha(request):
    alpha_display = alphamodel.objects.all()
    return render(request, 'activities/alpha.html', {'alpha_display': alpha_display})

def student_bravo(request):
    bravo_display = bravomodel.objects.all()
    return render(request, 'activities/bravo.html', {'bravo_display': bravo_display})

def student_charlie(request):
    charlie_display = charliemodel.objects.all()
    return render(request, 'activities/charlie.html', {'charlie_display': charlie_display})

def student_delta(request):
    delta_display = deltamodel.objects.all()
    return render(request, 'activities/delta.html', {'delta_display': delta_display})

def student_echo(request):
    echo_display = echomodel.objects.all()
    return render(request, 'activities/echo.html', {'echo_display': echo_display})

def student_foxtrot(request):
    foxtrot_display = foxtrotmodel.objects.all()
    return render(request, 'activities/foxtrot.html', {'foxtrot_display': foxtrot_display})

def student_golf(request):
    golf_display = golfmodel.objects.all()
    return render(request, 'activities/golf.html', {'golf_display': golf_display})

def student_hotel(request):
    hotel_display = hotelmodel.objects.all()
    return render(request, 'activities/hotel.html', {'hotel_display': hotel_display})

def student_india(request):
    india_display = indiamodel.objects.all()
    return render(request, 'activities/india.html', {'india_display': india_display})

def student_juliet(request):
    juliet_display = julietmodel.objects.all()
    return render(request, 'activities/juliet.html', {'juliet_display': juliet_display})

def student_kilo(request):
    kilo_display = kilomodel.objects.all()
    return render(request, 'activities/kilo.html', {'kilo_display': kilo_display})

def student_lima(request):
    lima_display = limamodel.objects.all()
    return render(request, 'activities/lima.html', {'lima_display': lima_display})






#                   admin
def platooncount(request):
    pass

def adminlogin(request):
    return render(request, 'activities/login-admin.html')

def admindashboard(request):
    imagex=carousel.objects.all()
    # users = User.objects.all()
    return render(request, 'activities/admindashboard.html', {'imagex': imagex})

def deleteimage(request, id):
    carouimage = carousel.objects.get(id=id)
    if request.method == 'POST':
        carouimage.delete()
        return redirect('/admindashboard')
    return render(request, 'activities/imagedelete.html')

def pdf(request, id):
    ss = certifications.objects.get(id=id)
    return render(request, 'activities/certificate.html', {'ss': ss})
    
def certi(request):
    if request.method == 'POST':
        pd = request.post.GET('pdfbtn')
        return render(request, 'activities/certificate.html', {'pd': pd})
    return render(request, 'activities/certificate.html')


def admincertificate(request):
    request1 = certifications.objects.all()
    return render(request, 'activities/admincertification.html', {'request1': request1})

def navadmin(request):
    return render(request, 'activities/NavAdmin.html')

def pdfb(request):
    if request.method == 'POST':
        pdfbt=request.POST.get('pdfbtn')
        return render(request, 'activities/certificate.html', {'pdfbt': pdfbt})

# admin platoon display

def adminplatoon(request):
    return render(request, 'activities/adminplatoons.html')

def d_alpha(request):
    alpha_display = alphamodel.objects.all()
    return render(request, 'activities/adminalpha.html', {'alpha_display': alpha_display})

def d_bravo(request):
    bravo_display = bravomodel.objects.all()
    return render(request, 'activities/adminbravo.html', {'bravo_display': bravo_display})

def d_charlie(request):
    charlie_display=charliemodel.objects.all()
    return render(request, 'activities/admincharlie.html', {'charlie_display': charlie_display})
def d_delta(request):
    delta_display = deltamodel.objects.all()
    return render(request, 'activities/admindelta.html', {'delta_display': delta_display})

def d_echo(request):
    echo_display = echomodel.objects.all()
    return render(request, 'activities/adminecho.html', {'echo_display': echo_display})
def d_foxtrot(request):
    foxtrot_display = foxtrotmodel.objects.all()
    return render(request, 'activities/adminfoxtrot.html', {'foxtrot_display': foxtrot_display})

def d_golf(request):
    golf_display = golfmodel.objects.all()
    return render(request, 'activities/admingolf.html', {'golf_display': golf_display})

def d_hotel(request):
    hotel_display = hotelmodel.objects.all()
    return render(request, 'activities/adminhotel.html', {'hotel_display': hotel_display})

def d_india(request):
    india_display = indiamodel.objects.all()
    return render(request, 'activities/adminindia.html', {'india_display': india_display})

def d_juliet(request):
    juliet_display = julietmodel.objects.all()
    return render(request, 'activities/adminjuliet.html', {'juliet_display': juliet_display})
def d_kilo(request):
    kilo_display = kilomodel.objects.all()
    return render(request, 'activities/adminkilo.html', {'kilo_display': kilo_display})
def d_lima(request):
    lima_display = limamodel.objects.all()
    return render(request, 'activities/adminlima.html', {'lima_display': lima_display})



                    # ADMIN PLATOON DIAPLAY ENd
def updateform(request):
    return render(request, 'activities/updateform.html')

def registerprocess(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'], email=request.POST['email'])
            return render(request, 'activities/signup.html', {'error': 'User already exists'})
        except:
            username = request.POST['username']
            lname=request.POST.get('last_name')
            fname=request.POST.get('first_name')
            minitial=request.POST.get('middle')
            address=request.POST.get('address')
            cpnumber=request.POST.get('contact')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            age=request.POST.get('age')
            bdate=request.POST.get('birthday')
            password=request.POST.get('password')
            section=request.POST.get('section')
            field=request.POST.get('field')
            
            user = User.objects.create_user(username=username, password=password,)
            
            newextenduser = extenduser( lname=lname, fname=fname, minitial=minitial, address=address, cpnumber=cpnumber, email=email, gender=gender, age=age, bdate=bdate, 
         password=password, section=section, field=field, user=user)
            newextenduser.save()
            auth.login(request, user)
            return render(request, 'activities/login.html')
    else:
        return render(request, 'activities/login.html')
                
            






    

# def registerprocess(request):
#     if request.method == 'POST':
#         idnum=request.POST['idnum']
#         lname=request.POST.get('last_name')
#         fname=request.POST.get('first_name')
#         minitial=request.POST.get('middle')
#         address=request.POST.get('address')
#         cpnumber=request.POST.get('contact')
#         email=request.POST.get('email')
#         gender=request.POST.get('gender')
#         age=request.POST.get('age')
#         bdate=request.POST.get('birthday')
#         password=request.POST.get('password')
#         section=request.POST.get('section')
#         field=request.POST.get('field')
        
#     try:
#         create = registration.objects.create(idnum=idnum, lname=lname, fname=fname, minitial=minitial, address=address, cpnumber=cpnumber, email=email, gender=gender, age=age, bdate=bdate, 
#         password=password, section=section, field=field)
#         create.save()
#         return render(request, 'activities/login.html')
#     except:
#         messages.error(request, 'Invalid Inputs! Please Check it and Try Again')
#         return render(request, 'activities/signup.html')
        
    #  else:
    #      return render(request, 'activities/signup.html')
        
# def userlogin(request):
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",password="",database='nstpsystem')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="username":
#                 idnum=value
#             if key=="password":
#                 password=value
        
#         c="select * from nstpapp_registration where idnum='{}' and password='{}'".format(idnum,password)
        
#         cursor.execute(c)
#         t=tuple(cursor.fetchall())
#         if t==():
#             messages.error(request, 'Invalid username or password')
#             return render(request, 'activities/login.html')
            
#         else:
#             # name = registration.objects.filter(idnum=idnum)
#             return render(request, 'activities/Dashboard.html')

#     return render(request, 'activities/login.html')
def userlogin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'activities/login.html')
    else:
        return render(request, 'activities/Dashboard.html')


#       ADMIN LOGIN

# def userlogin(request):
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",password="",database='nstpsystem')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="username":
#                 idnum=value
#             if key=="password":
#                 password=value
        
#         c="select * from User where idnum='{}' and password='{}'".format(idnum,password)
        
#         cursor.execute(c)
#         t=tuple(cursor.fetchall())
#         if t==():
#             return render(request, 'activities/login.html')
            
#         else:
#             name = registration.objects.filter(idnum=idnum)
#             return render(request, 'activities/Dashboard.html', {'name': name})

#     return render(request, 'activities/login.html')

def admin2(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/admindashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/adminlogin')
       
    else:
        messages.error(request, 'Invalid username or password')
        return redirect('/adminlogin')
            

# @login_required(login_url='/login/')
def cert(request):
    if request.method == 'POST':
        cert_email = request.POST.get('cert_email')
        cert_fullname = request.POST.get('cert_fullname')
        cert_course = request.POST.get('cert_course')
        cert_datereq = request.POST.get('cert_datereq')
        cert_document = request.POST.get('cert_document')

        certificate = certifications.objects.create(cert_email=cert_email, cert_fullname=cert_fullname, cert_course=cert_course, cert_datereq=cert_datereq, cert_document=cert_document)
        certificate.save()
        return redirect('/certification')
       
        
       
def logout_user(request):
    logout(request)
    return redirect('/')



# def updatestatus(request, cert_email):
#     data = certifications.objects.get(id=cert_email)
#     form = request.POST(instance=data)
#     if request.method == "POST":
#         form = AdminUpdate(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect('/admin/')
#     # content = {'datas':datas, 'form':form}
#     content = {'form':form}
#     return render(request, 'admins/form_modification.html', content)

        
        
# def delete(request, cert_email):
#     data = certifications.objects.get(id=cert_email)
#     data.delete()
#     return redirect('/admincertificate')    
def delete(request, id):
    member = certifications.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/admincertificate')
    return render(request, 'activities/delete.html')

def deleteform(request):
    return render(request, 'activities/delete.html')

    



def update(request):
    stat1 = request.POST.get('status')
    stat2 = request.POST.get('getID')
    certifications.objects.filter(id=stat2).update(cert_status=stat1)
    print(stat1, stat2)
    return redirect('/admincertificate')

def enrollupdate(request):
    en1 = request.POST.get('status')
    en2 = request.POST.get('getID')
    extenduser.objects.filter(id=en2).update(status=en1)
    return redirect('/adminrotclist')

def platoonupdate(request):
    enr1 = request.POST.get('plat')
    enr2 = request.POST.get('getID')
    extenduser.objects.filter(id=enr2).update(platoon=enr1)
    return redirect('/enrolledrotc')
    



# def update(request, id):
#     data = certifications.objects.get(id=id)
#     data.cert_status=request.POST.get('status')
#     data.save()
#     return redirect('/admincertificate')
    
        
            
    



                                #START PLATOON UPLOADS

def alpha(request):
    if request.method == 'POST':    

        alpha_file = request.FILES["document"]
        alpha_name = request.POST["notes"]
        file = alphamodel.objects.create(pdf=alpha_file, name=alpha_name)
        file.save()
        print("error")
        return redirect('/d_alpha')
    else:
        print("error2")
        return redirect('/d_alpha')
    
    
    
def bravo(request):
    if request.method == 'POST':    
        bravo_file = request.FILES["document"]
        bravo_name = request.POST["notes"]
        file = bravomodel.objects.create(pdf=bravo_file, name=bravo_name)
        file.save()
        print("error")
        return redirect('/d_bravo')
    else:
        print("error2")
        return redirect('/d_bravo')
    
    
    
def charlie(request):
    if request.method == 'POST':    

        charlie_file = request.FILES["document"]
        charlie_name = request.POST["notes"]
        file = charliemodel.objects.create(pdf=charlie_file, name=charlie_name)
        file.save()
        print("error")
        return redirect('/d_charlie')
    else:
        print("error2")
        return redirect('/d_charlie')

def delta(request):
    if request.method == 'POST':    

        delta_file = request.FILES["document"]
        delta_name = request.POST["notes"]
        file = deltamodel.objects.create(pdf=delta_file, name=delta_name)
        file.save()
        print("error")
        return redirect('/d_delta')
    else:
        print("error2")
        return redirect('/d_delta')
    
    

def echo(request):
    if request.method == 'POST':    

        echo_file = request.FILES["document"]
        echo_name = request.POST["notes"]
        file = echomodel.objects.create(pdf=echo_file, name=echo_name)
        file.save()
        print("error")
        return redirect('/d_echo')
    else:
        print("error2")
        return redirect('/d_echo')
        


def foxtrot(request):
    if request.method == 'POST':    

        foxtrot_file = request.FILES["document"]
        foxtrot_name = request.POST["notes"]
        file = foxtrotmodel.objects.create(pdf=foxtrot_file, name=foxtrot_name)
        file.save()
        print("error")
        return redirect('/d_foxtrot')
    else:
        print("error2")
        return redirect('/d_foxtrot')
    
    
    
def golf(request):
    if request.method == 'POST':    

        golf_file = request.FILES["document"]
        golf_name = request.POST["notes"]
        file = golfmodel.objects.create(pdf=golf_file, name=golf_name)
        file.save()
        print("error")
        return redirect('/d_golf')
    else:
        print("error2")
        return redirect('/d_golf')
    
    
    
def hotel(request):
    if request.method == 'POST':    

        hotel_file = request.FILES["document"]
        hotel_name = request.POST["notes"]
        file = hotelmodel.objects.create(pdf=hotel_file, name=hotel_name)
        file.save()
        print("error")
        return redirect('/d_hotel')
    else:
        print("error2")
        return redirect('/d_hotel')
    
    
    
def india(request):
    if request.method == 'POST':    

        india_file = request.FILES["document"]
        india_name = request.POST["notes"]
        file = indiamodel.objects.create(pdf=india_file, name=india_name)
        file.save()
        print("error")
        return redirect('/d_india')
    else:
        print("error2")
        return redirect('/d_india')
    
    
    
def juliet(request):
    if request.method == 'POST':    

        juliet_file = request.FILES["document"]
        juliet_name = request.POST["notes"]
        file = julietmodel.objects.create(pdf=juliet_file, name=juliet_name)
        file.save()
        print("error")
        return redirect('/d_juliet')
    else:
        print("error2")
        return redirect('/d_juliet')
    
    
    
    
def kilo(request):
    if request.method == 'POST':    

        kilo_file = request.FILES["document"]
        kilo_name = request.POST["notes"]
        file = kilomodel.objects.create(pdf=kilo_file, name=kilo_name)
        file.save()
        print("error")
        return redirect('/d_kilo')
    else:
        print("error2")
        return redirect('/d_kilo')
    
    
    
    
def lima(request):
    if request.method == 'POST':    

        lima_file = request.FILES["document"]
        lima_name = request.POST["notes"]
        file = limamodel.objects.create(pdf=lima_file, name=lima_name)
        file.save()
        print("error")
        return redirect('/d_lima')
    else:
        print("error2")
        return redirect('/d_lima')
    
    

def cwtsupload(request):
    if request.method == 'POST':    

        cwts_file = request.FILES["document"]
        cwts_name = request.POST["notes"]
        file = cwts.objects.create(pdf=cwts_file, name=cwts_name)
        file.save()
        print("error")
        return redirect('/admincwts')
    else:
        print("error2")
        return redirect('/admincwts')
    
def cwts_delete(request, id):
    member = cwts.objects.get(id=id)
    member.delete()
    return redirect('/admincwts')




def dashboardupload(request):
    if request.method == 'POST':
        dashboard_file = request.FILES["upload"]
        file = carousel.objects.create(imagefile=dashboard_file)
        file.save()
        print("error")
        return redirect('/admindashboard')
    else:
        print("error2")
        return redirect('/admindashboard')
            

    
    
                            #P END OF PLATOON UPLOADS
    
    
    
    


    

                                # PLATOON DELETE

def alpha_delete(request, id):
    member = alphamodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_alpha')
    return render(request, 'activities/alphadel.html')

def bravo_delete(request, id):
    member = bravomodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_bravo')
    return render(request, 'activities/bravodel.html')

def charlie_delete(request, id):
    member = charliemodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_charlie')
    return render(request, 'activities/charliedel.html')

def delta_delete(request, id):
    member = deltamodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_delta')
    return render(request, 'activities/deltadel.html')

def echo_delete(request, id):
    member = echomodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_echo')
    return render(request, 'activities/echodel.html')


def foxtrot_delete(request, id):
    member = foxtrotmodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_foxtrot')
    return render(request, 'activities/foxtrotdel.html')

def golf_delete(request, id):
    member = golfmodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_golf')
    return render(request, 'activities/golfdel.html')

def hotel_delete(request, id):
    member = hotelmodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_hotel')
    return render(request, 'activities/hoteldel.html')

def india_delete(request, id):
    member = indiamodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_india')
    return render(request, 'activities/indiadel.html')

def juliet_delete(request, id):
    member = julietmodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_juliet')
    return render(request, 'activities/julietdel.html')

def kilo_delete(request, id):
    member = kilomodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_kilo')
    return render(request, 'activities/kilodel.html')

def lima_delete(request, id):
    member = limamodel.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('/d_lima')
    return render(request, 'activities/limadel.html')






# DELETION FOR IMAGES

                         # END PLATOON DELETE