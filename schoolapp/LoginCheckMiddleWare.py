from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):
#process_view() called just before django view call, where request and view_func are object
# finally returns httpresponse
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__ #file-name hold our sent request
        user=request.user #store logindata
        if user.is_authenticated:
            #user type 1 can access Hodviews.py and views.py so on file 
            if user.user_type == "1":
                if modulename == "schoolapp.HodViews":
                    pass
                elif modulename == "schoolapp.views" or modulename=="django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                     pass    
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            #user type 2 can access StaffViews.py and views.py file but do nothing       
            elif user.user_type == "2":
                if modulename == "schoolapp.StaffViews"  or modulename == "schoolapp.EditResultViewClass":
                    pass
                elif modulename == "schoolapp.views" or modulename=="django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            #user type 3 can access StudentViews.py and views.py file  but do nothing         
            elif user.user_type == "3":
                if modulename == "schoolapp.StudentViews":
                    pass
                elif modulename == "schoolapp.views" or modulename=="django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))

        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites" or modulename=="schoolapp.views" :
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))