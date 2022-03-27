from django.urls import path
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.urls import include, re_path



app_name = 'activities'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admin2', views.admin2, name='admin2'),
    path('register/', views.register, name='register'),
    path('registerprocess/', views.registerprocess, name='registerprocess'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('navbar/', views.navbar, name='navbar'),
    path('rotclist/', views.rotclist, name='rotclist'),
    path('cwtslist/', views.cwtslist, name='cwtslist'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('platoon/', views.platoon, name='platoon'),
    path('cwtss/', views.cwtss, name='cwtss'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('certification/', views.certification, name='certification'),
    path('cert/', views.cert, name='cert'),
    path('enrollupdate/', views.enrollupdate, name='enrollupdate'),
    path('certi/', views.certi, name='certi'),
    # path('requested/', views.requested, name='requested'),
    path('admincertificate/', views.admincertificate, name='admincertificate'),
    path('navadmin', views.navadmin, name='navadmin'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('navlanding/', views.navlanding, name='navlanding'),
    path('updateform/', views.updateform, name='updateform'),
    path('indexcard1/', views.indexcard1, name='indexcard1'),
    path('indexcard2/', views.indexcard2, name='indexcard2'),
    path('indexcard3/', views.indexcard3, name='indexcard3'),
    path('indexcard4/', views.indexcard4, name='indexcard4'),
    
    path('admincwtslist/', views.admincwtslist, name='admincwtslist'),
    path('adminrotclist/', views.adminrotclist, name='adminrotclist'),
    path('enrolledrotc/', views.enrolledrotc, name='enrolledrotc'),
    path('platoonupdate/', views.platoonupdate, name='platoonupdate'),
    # path('alphacount/', views.alphacount, name='alphacount'),
    # path('counts/', views.counts, name='counts'),

    path('admincwts/', views.admincwts, name='admincwts'),
    path('cwtsupload/', views.cwtsupload, name='cwtsupload'),
    path('cwts_delete/<str:id>', views.cwts_delete, name='cwts_delete'),
    path('dashboardupload/', views.dashboardupload, name='dashboardupload'),
    path('footer/', views.footer, name='footer'),
    path('deleteimage/<str:id>', views.deleteimage, name='deleteimage'),
 
    path('deleteform/', views.deleteform, name='deleteform'),
    path('pdf/<str:id>', views.pdf, name='pdf'),
    path('pdfb/<str:id>', views.pdfb, name='pdfb'),
    path('profile/', views.profile, name='profile'),
    #             ADMIN PLATOON UPLOAD
    path('alpha/', views.alpha, name='alpha'),
    path('bravo/', views.bravo, name='bravo'),
    path('charlie/', views.charlie, name='charlie'),
    path('delta/', views.delta, name='delta'),
    path('echo/', views.echo, name='echo'),
    path('foxtrot/', views.foxtrot, name='foxtrot'),
    path('golf/', views.golf, name='golf'),
    path('hotel/', views.hotel, name='hotel'),
    path('india/', views.india, name='india'),
    path('juliet/', views.juliet, name='juliet'),
    path('kilo/', views.kilo, name='kilo'),
    path('lima/', views.lima, name='lima'),

    
    #             END OF ADMIN PLATOON UPLOADS

#                    START OD ADMIN PLATOON DISPLAY
    path('adminplatoon/', views.adminplatoon, name='adminplatoon'),
    path('d_alpha/', views.d_alpha, name='d_alpha'),
    path('d_bravo/', views.d_bravo, name='d_bravo'),
    path('d_charlie/', views.d_charlie, name='d_charlie'),
    path('d_delta/', views.d_delta, name='d_delta'),
    path('d_echo/', views.d_echo, name='d_echo'),
    path('d_foxtrot/', views.d_foxtrot, name='d_foxtrot'),
    path('d_golf/', views.d_golf, name='d_golf'),
    path('d_hotel/', views.d_hotel, name='d_hotel'),
    path('d_india/', views.d_india, name='d_india'),
    path('d_juliet/', views.d_juliet, name='d_juliet'),
    path('d_kilo/', views.d_kilo, name='d_kilo'),
    path('d_lima/', views.d_lima, name='d_lima'),
    
    
    

#                    END OF ADMIN PLATOON DISPLAY
    
    
                 # STUDENT PLATOON DISPLAY
    
    path('student_alpha/', views.student_alpha, name='student_alpha'),
    path('student_bravo/', views.student_bravo, name='student_bravo'),
    path('student_charlie/', views.student_charlie, name='student_charlie'),
    path('student_delta/', views.student_delta, name='student_delta'),
    path('student_echo/', views.student_echo, name='student_echo'),
    path('student_foxtrot/', views.student_foxtrot, name='student_foxtrot'),
    path('student_golf/', views.student_golf, name='student_golf'),
    path('student_hotel/', views.student_hotel, name='student_hotel'),
    path('student_india/', views.student_india, name='student_india'),
    path('student_juliet/', views.student_juliet, name='student_juliet'),
    path('student_kilo/', views.student_kilo, name='student_kilo'),
    path('student_lima/', views.student_lima, name='student_lima'),
    
#                       END OF STUDENT PLATOON DISPLAY
  
    
    
     
#                     START OF PLATOON DELETION
    
    path('alpha_delete/<str:id>', views.alpha_delete, name='alpha_delete'),
    path('bravo_delete/<str:id>', views.bravo_delete, name='bravo_delete'),
    path('charlie_delete/<str:id>', views.charlie_delete, name='charlie_delete'),
    path('delta_delete/<str:id>', views.delta_delete, name='delta_delete'),
    path('echo_delete/<str:id>', views.echo_delete, name='echo_delete'),
    path('foxtrot_delete/<str:id>', views.foxtrot_delete, name='foxtrot_delete'),
    path('golf_delete/<str:id>', views.golf_delete, name='golf_delete'),
    path('hotel_delete/<str:id>', views.hotel_delete, name='hotel_delete'),
    path('india_delete/<str:id>', views.india_delete, name='india_delete'),
    path('juliet_delete/<str:id>', views.juliet_delete, name='juliet_delete'),
    path('kilo_delete/<str:id>', views.kilo_delete, name='kilo_delete'),
    path('lima_delete/<str:id>', views.lima_delete, name='lima_delete'),
    
#                     END OF PLATOON DELETION

   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
