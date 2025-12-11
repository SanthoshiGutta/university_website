from django.shortcuts import render
from marks.models import Admin,Marks
from .forms import AdminForm

# Create your views here.
def Home_page(req):
    return render(req,'home.html')
def About_us(req):
    return render(req,'about_us.html')
def Contact(req):
    return render(req,'contact.html')
def Branches(req):
    return render(req,'branches.html')
def courses(req):
    return render(req,'courses.html')

def Register_marks_form(req):
   return render(req,'Register_marks_form.html')
def posting_marks(req):
    if req.method=="POST":
        hall_ticket_number=req.POST.get('hall_ticket_number')
        m1=req.POST.get('m1')
        physics=req.POST.get('physics')
        chemistry=req.POST.get('chemistry')
        english=req.POST.get("english")
        drawing=req.POST.get("drawing")
        qs=Marks(hall_ticket_number=hall_ticket_number,m1=m1,physics=physics,chemistry=chemistry,english=english,drawing=drawing).save()
        return render(req,"Register_marks_form.html",{"message":"marks saved successfully"})
    return render(req,"Register_marks_form.html")
def result(req):
    return render(req,"result.html")
def confirm_hall_ticket(req):
    
    
    if req.method=="POST":
        hall_ticket_numberr=req.POST.get('confirm_hall_tickett')
        qs=Marks.objects.filter(hall_ticket_number=hall_ticket_numberr)
        form=Admin.objects.filter(hall_ticket_number=hall_ticket_numberr)
        if qs.exists():

            return render(req,"display_result.html",{"result":qs,"result1":form})
        else:
            return render(req,"display_result.html",{"message":"Hall ticket number does not exist"})
    else:
        return render(req,"confirm_hall_ticket.html")



