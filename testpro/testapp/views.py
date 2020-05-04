from django.shortcuts import render
from django.views import View

# Create your views here.
class count_cookies(View):
    def get(self,request):
        # count=int(request.COOKIES.get("count",0))
        # count+=1
        # response=render(request,"testapp/index.html",{"counts":count})
        # response.set_cookie("count",count,max_age=2)
        # return response
        count=request.session.get("count",0)
        count+=1
        request.session["count"]=count
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        return render(request,"testapp/index.html",{"counts":count})