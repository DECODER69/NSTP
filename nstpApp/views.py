from dataclasses import field
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
from django.contrib.auth.decorators import login_required
import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import certificationsForm
from django.http import FileResponse


idnum=''
password=''




# studentside

def new_navbar(request):
    return render(request, 'activities/new_navbar.html')
def new_navbarstudent(request):
    return render(request, 'activities/new_navbar.html')

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
def cwtslist1(request):
    list2 = extenduser.objects.filter(field='CWTS').filter(status='ENROLLED')
    return render(request, 'activities/cwtslist.html', {'list2': list2})
    

def cnt(request):
    cnt = extenduser.objects.filter(field='ROTC').count()
    return render(request, 'activities/rotclist.html', {'cnt': cnt})

@login_required(login_url='/login')
def cwtslist(request):
    list1 = extenduser.objects.filter(field='CWTS').filter(status='ENROLLED')
    return render(request, 'activities/cwtslist.html', {'list1': list1})

def adminrotclist(request):
    rlist = extenduser.objects.filter(field='ROTC').filter(status='PENDING')
    return render(request, 'activities/adminrotclist.html', {'rlist': rlist})

def admincwtslist(request):
    clist = extenduser.objects.filter(field='CWTS').filter(status='PENDING')
    return render(request, 'activities/admincwtslist.html', {'clist': clist})



def enrolledrotc(request):
    
    count1 = extenduser.objects.filter(platoon='Alpha').filter(status='ENROLLED').count
    count2 = extenduser.objects.filter(platoon='Bravo').filter(status='ENROLLED').count
    count3 = extenduser.objects.filter(platoon='Charlie').filter(status='ENROLLED').count
    count4 = extenduser.objects.filter(platoon='Delta').filter(status='ENROLLED').count
    count5 = extenduser.objects.filter(platoon='Echo').filter(status='ENROLLED').count
    count6 = extenduser.objects.filter(platoon='Foxtrot').filter(status='ENROLLED').count
    count7 = extenduser.objects.filter(platoon='Golf').filter(status='ENROLLED').count
    count8 = extenduser.objects.filter(platoon='Hotel').filter(status='ENROLLED').count
    count9 = extenduser.objects.filter(platoon='India').filter(status='ENROLLED').count
    count10 = extenduser.objects.filter(platoon='Juliet').filter(status='ENROLLED').count
    count11 = extenduser.objects.filter(platoon='Kilo').filter(status='ENROLLED').count
    count12 = extenduser.objects.filter(platoon='Lima').filter(status='ENROLLED').count
    sheesh = extenduser.objects.filter(status='ENROLLED').filter(field='ROTC')
    context = {
        'count1': count1,
        'count2': count2,
        'count3': count3,
        'count4': count4,
        'count5': count5,
        'count6': count6,
        'count7': count7,
        'count8': count8,
        'count9': count9,
        'count10': count10,
        'count11': count11,
        'count12': count12,
        'sheesh': sheesh,
        
    }
    return render(request, 'activities/enrolledrotc.html', context)


def enrolledcwts(request):
    count1cwts = extenduser.objects.filter(platoon='Section A').filter(status='ENROLLED').count
    count2cwts = extenduser.objects.filter(platoon='Section B').filter(status='ENROLLED').count
    sheesh1 = extenduser.objects.filter(status='ENROLLED').filter(field='CWTS')
    
    context = {
        'count1cwts': count1cwts,
        'count2cwts': count2cwts,
        'sheesh1': sheesh1,
    }
    return render(request, 'activities/enrolledcwts.html', context)
    



# def grades_alpha(request):
    
#     return render (request, 'activities/grades_alpha.html', context)
    
    





@login_required(login_url='/login')
def dashboard(request):
    name = extenduser.objects.filter(user = request.user)
    return render(request, 'activities/dashboard.html', {'name': name})

 


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
    requests = extenduser.objects.filter(user = request.user).filter(status='ENROLLED')
    return render(request, 'activities/certification.html', {'requests': requests})



@login_required(login_url='/login')
def admincwts(request):
    fetch = cwts.objects.all()
    return render(request, 'activities/admincwts.html', {'fetch': fetch})


#                   STUDENT PLATOON DISPLAY

@login_required(login_url='/login')
def student_alpha(request):
    alpha_display = alphamodel.objects.all()
    return render(request, 'activities/alpha.html', {'alpha_display': alpha_display})


@login_required(login_url='/login')
def student_bravo(request):
    bravo_display = bravomodel.objects.all()
    return render(request, 'activities/bravo.html', {'bravo_display': bravo_display})

@login_required(login_url='/login')
def student_charlie(request):
    charlie_display = charliemodel.objects.all()
    return render(request, 'activities/charlie.html', {'charlie_display': charlie_display})

@login_required(login_url='/login')
def student_delta(request):
    delta_display = deltamodel.objects.all()
    return render(request, 'activities/delta.html', {'delta_display': delta_display})

@login_required(login_url='/login')
def student_echo(request):
    echo_display = echomodel.objects.all()
    return render(request, 'activities/echo.html', {'echo_display': echo_display})

@login_required(login_url='/login')
def student_foxtrot(request):
    foxtrot_display = foxtrotmodel.objects.all()
    return render(request, 'activities/foxtrot.html', {'foxtrot_display': foxtrot_display})

@login_required(login_url='/login')
def student_golf(request):
    golf_display = golfmodel.objects.all()
    return render(request, 'activities/golf.html', {'golf_display': golf_display})

@login_required(login_url='/login')
def student_hotel(request):
    hotel_display = hotelmodel.objects.all()
    return render(request, 'activities/hotel.html', {'hotel_display': hotel_display})
@login_required(login_url='/login')
def student_india(request):
    india_display = indiamodel.objects.all()
    return render(request, 'activities/india.html', {'india_display': india_display})

@login_required(login_url='/userlogin')
def student_juliet(request):
    juliet_display = julietmodel.objects.all()
    return render(request, 'activities/juliet.html', {'juliet_display': juliet_display})

@login_required(login_url='/login')
def student_kilo(request):
    kilo_display = kilomodel.objects.all()
    return render(request, 'activities/kilo.html', {'kilo_display': kilo_display})

@login_required(login_url='/login')
def student_lima(request):
    lima_display = limamodel.objects.all()
    return render(request, 'activities/lima.html', {'lima_display': lima_display})






# #                   admin
# def platooncount(request):
#     pass




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
    



def admincertificate(request):
    request1 = extenduser.objects.exclude(cert_document__isnull=True).exclude(cert_document__exact='')
    return render(request, 'activities/admincertification.html', {'request1': request1})

def navadmin(request):
    return render(request, 'activities/NavAdmin.html')

def pdfb(request, id):
    namess = extenduser.objects.filter(id=id)
    return render(request, 'activities/certificate.html', {'namess': namess})


def certi(request):
    if request.method == 'POST':
        pd = request.post.GET('pdfbtn')
        return render(request, 'activities/certificate.html', {'pd': pd})
    return render(request, 'activities/certificate.html')

# admin platoon display

def adminplatoon(request):

    return render(request, 'activities/adminplatoons.html')

def d_alpha(request):
    alpha_display = alphamodel.objects.all()
    gradess = extenduser.objects.filter(platoon='Alpha')
    context = {
      
        'alpha_display': alpha_display,
        'gradess': gradess,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('getID1')
        a_grades = request.POST.get('a_grades')
        a_grades1 = request.POST.get('a_grades1')
        extenduser.objects.filter(id=enr2).update(grades=a_grades, grades1=a_grades1)
        
    return render(request, 'activities/adminalpha.html', context)

# def alphagrade(request):
#     gradess = extenduser.objects.filter(platoon='Alpha')
#     context = {
#         'gradess': gradess,
#     }
#     return render(request, 'activities/adminalpha.html', context)

def d_bravo(request):
    bravo_display = bravomodel.objects.all()
    bravo_grade = extenduser.objects.filter(platoon='Bravo')
    context = {
        'bravo_display': bravo_display,
        'bravo_grade': bravo_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('bravo_id')
        b_grades = request.POST.get('b_grades')
        b_grades1 = request.POST.get('b_grades1')
        extenduser.objects.filter(id=enr2).update(grades=b_grades, grades1=b_grades1)
    return render(request, 'activities/adminbravo.html', context)

def d_charlie(request):
    charlie_display=charliemodel.objects.all()
    charlie_grade = extenduser.objects.filter(platoon='Charlie')
    context = {
        'charlie_display': charlie_display,
        'charlie_grade': charlie_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('charlie_id')
        c_grades = request.POST.get('c_grades')
        c_grades1 = request.POST.get('c_grades1')
        extenduser.objects.filter(id=enr2).update(grades=c_grades, grades1=c_grades1)
    return render(request, 'activities/admincharlie.html', context)

def d_delta(request):
    delta_display = deltamodel.objects.all()
    delta_grade = extenduser.objects.filter(platoon='Delta')
    context = {
        'delta_display': delta_display,
        'delta_grade': delta_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('delta_id')
        d_grades = request.POST.get('d_grades')
        d_grades1 = request.POST.get('d_grades1')
        extenduser.objects.filter(id=enr2).update(grades=d_grades, grades1=d_grades1)
    return render(request, 'activities/admindelta.html', context)

def d_echo(request):
    echo_display = echomodel.objects.all()
    echo_grade = extenduser.objects.filter(platoon='Echo')
    context = {
        'echo_display': echo_display,
        'echo_grade': echo_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('echo_id')
        e_grades = request.POST.get('e_grades')
        e_grades1 = request.POST.get('e_grades1')
        extenduser.objects.filter(id=enr2).update(grades=e_grades, grades1=e_grades1)
    return render(request, 'activities/adminecho.html', context)

def d_foxtrot(request):
    foxtrot_display = foxtrotmodel.objects.all()
    foxtrot_grade = extenduser.objects.filter(platoon='Foxtrot')
    context = {
        'foxtrot_display': foxtrot_display,
        'foxtrot_grade': foxtrot_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('foxtrot_id')
        f_grades = request.POST.get('f_grades')
        f_grades1 = request.POST.get('f_grades1')
        extenduser.objects.filter(id=enr2).update(grades=f_grades, grades1=f_grades1)
    return render(request, 'activities/adminfoxtrot.html', context)

def d_golf(request):
    golf_display = golfmodel.objects.all()
    golf_grade = extenduser.objects.filter(platoon='Golf')
    context = {
        'golf_display': golf_display,
        'golf_grade': golf_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('golf_id')
        g_grades = request.POST.get('g_grades')
        g_grades1 = request.POST.get('g_grades1')
        extenduser.objects.filter(id=enr2).update(grades=g_grades, grades1=g_grades1)
    
    return render(request, 'activities/admingolf.html', context)

def d_hotel(request):
    hotel_display = hotelmodel.objects.all()
    hotel_grade = extenduser.objects.filter(platoon='Hotel')
    context = {
        'hotel_display': hotel_display,
        'hotel_grade': hotel_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('hotel_id')
        h_grades = request.POST.get('h_grades')
        h_grades1 = request.POST.get('h_grades1')
        extenduser.objects.filter(id=enr2).update(grades=h_grades, grades1=h_grades1)
    return render(request, 'activities/adminhotel.html', context)

def d_india(request):
    india_display = indiamodel.objects.all()
    india_grade = extenduser.objects.filter(platoon='India')
    context = {
        'india_display': india_display,
        'india_grade': india_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('india_id')
        i_grades = request.POST.get('i_grades')
        i_grades1 = request.POST.get('i_grades1')
        extenduser.objects.filter(id=enr2).update(grades=i_grades, grades1=i_grades1)
    return render(request, 'activities/adminindia.html', context)

def d_juliet(request):
    juliet_display = julietmodel.objects.all()
    india_grade = extenduser.objects.filter(platoon='Juliet')
    context = {
        'juliet_display': juliet_display,
        'juliet_grade': india_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('india_id')
        i_grades = request.POST.get('i_grades')
        i_grades1 = request.POST.get('i_grades1')
        extenduser.objects.filter(id=enr2).update(grades=i_grades, grades1=i_grades1)
    return render(request, 'activities/adminjuliet.html', context)

def d_kilo(request):
    kilo_display = kilomodel.objects.all()
    kilo_grade = extenduser.objects.filter(platoon='Kilo')
    context = {
        'kilo_display': kilo_display,
        'kilo_grade': kilo_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('kilo_id')
        k_grades = request.POST.get('k_grades')
        k_grades1 = request.POST.get('k_grades1')
        extenduser.objects.filter(id=enr2).update(grades=k_grades, grades1=k_grades1)
    return render(request, 'activities/adminkilo.html', context)

def d_lima(request):
    lima_display = limamodel.objects.all()
    lima_grade = extenduser.objects.filter(platoon='Lima')
    context = {
        'lima_display': lima_display,
        'lima_grade': lima_grade,
    }
    if request.method == 'POST':
        enr2 = request.POST.get('lima_id')
        l_grades = request.POST.get('l_grades')
        l_grades1 = request.POST.get('l_grades1')
        extenduser.objects.filter(id=enr2).update(grades=l_grades, grades1=l_grades1)
    return render(request, 'activities/adminlima.html', context)



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
            picture = request.FILES['picture']
            
            user = User.objects.create_user(username=username, password=password,)
            
            newextenduser = extenduser( lname=lname, fname=fname, minitial=minitial, address=address, cpnumber=cpnumber, email=email, gender=gender, age=age, bdate=bdate, 
         password=password, section=section, field=field, user=user, picture=picture)
            newextenduser.save()
            auth.login(request, user)
            return render(request, 'activities/login.html')
    else:
        return render(request, 'activities/login.html')
                
            






    


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
        cert_datereq = request.POST.get('cert_datereq')
        cert_document = request.POST.get('cert_document')
        certificate = extenduser.objects.filter(user = request.user).filter(status = 'ENROLLED').update(cert_datereq=cert_datereq, cert_document=cert_document, cert_status='PENDING')
        return redirect('/certification', {'certificate': certificate})

def logout_user(request):
    logout(request)
    return redirect('/')


def delete_request(request):
    if request.method == 'POST':
        cert_datereq = request.POST.get('docum')
        cert_document = request.POST.get('datereq')
        certificate = extenduser.objects.filter(status = 'ENROLLED').update(cert_datereq=cert_datereq, cert_document=cert_document, cert_status='PENDING')
        return redirect('/certification', {'certificate': certificate})
    
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
    extenduser.objects.filter(id=stat2).update(cert_status=stat1)
    print(stat1, stat2)
    return redirect('/admincertificate')

def enrollupdate(request):
    en1 = request.POST.get('status')
    en2 = request.POST.get('getID')
    extenduser.objects.filter(id=en2).update(status=en1)
    return redirect('/adminrotclist')

def platoonupdate(request):
    if request.method == 'POST':
        enr1 = request.POST.get('plat')
        enr2 = request.POST.get('getID')
        
        extenduser.objects.filter(id=enr2).update(platoon=enr1)
    return redirect('/enrolledrotc')
    
def sectionupdate(request):
    if request.method == 'POST':
        sec1 = request.POST.get('sec')
        enr4 = request.POST.get('getIDs')
        extenduser.objects.filter(id=enr4).update(platoon=sec1)
    return redirect('/enrolledcwts')



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

def profile(request):
    edit = extenduser.objects.filter(user=request.user)
    if request.method =='POST':
        address = request.POST.get('address')
        cpnumber = request.POST.get('cpnumber')
        section = request.POST.get('section')
        extenduser.objects.filter(user=request.user).update(address=address, cpnumber=cpnumber, section=section)
    return render (request, 'activities/profile.html', {'edit':edit})




    

                         
                         
