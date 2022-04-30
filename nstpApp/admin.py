from tabnanny import verbose
from django.contrib import admin
from .models import  extenduser, certifications, alphamodel, bravomodel, charliemodel, deltamodel, echomodel, foxtrotmodel, golfmodel, hotelmodel, indiamodel, julietmodel, kilomodel, limamodel,  carousel, sectiona, sectionb, sectionc



# class registrationInline(admin.StackedInline):
#     model = registration
#     can_delete = False
#     verbose_name_plural = 'registration'
    
    
# class CustomizedUserAdmin (UserAdmin):
#     inlines=(registrationInline,)
    
    
    
# admin.site.unregister(User)
# admin.site.register(User, CustomizedUserAdmin)
# Register your models here.

admin.site.register(extenduser)
# admin.site.register(certifications)
admin.site.register(alphamodel)
admin.site.register(bravomodel)
admin.site.register(charliemodel)
admin.site.register(deltamodel)
admin.site.register(echomodel)
admin.site.register(foxtrotmodel)
admin.site.register(golfmodel)
admin.site.register(hotelmodel)
admin.site.register(indiamodel)
admin.site.register(julietmodel)
admin.site.register(kilomodel)
admin.site.register(limamodel)

admin.site.register(carousel)


# admin.site.register(CustomUser)

