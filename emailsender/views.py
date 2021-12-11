from django.shortcuts import get_object_or_404, render, get_list_or_404,redirect

from emailsender.models import EmailModel
from .forms import EmailMaster

# from .models import EmailModel
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render (request, 'emailsender/index.html',{})

def createEmailModel(request):
    dd =  EmailModel.dbTableForEmail.all()
    if request.method == 'POST':
        form = EmailMaster(request.POST)
        print(form.data)
        print(form.errors,form)
        if form.is_valid(): 
            user = form.save(commit=False)                
            user.save()                
            return render(request,'emailsender/index.html',{'form':form,'dd':dd})
    else:
        form = EmailMaster()
    return render(request,'emailsender/index.html',{'form':form,'dd':dd})



def editEmailModel(request, id):
    emailobjects = EmailModel.dbTableForEmail.get(id =id)
    return render(request,'emailsender/editemails.html', {'ddlcompanyobjects': emailobjects})

def sendEmail (request):
    dd =  EmailModel.dbTableForEmail.all()
    ll = ['oyaleke.philip@gmail.com']
    if dd ==1 :
        return
    for i in dd:
        ll.append(i.emailadress)

    if request.method == 'POST':
        message = request.POST.get("message")
        subject = request.POST.get("subject")

        data ={
            'email': 'oyaleke.philip@gmail.com',
            'subject': subject,
            'message': message
        }
        message = '''
        New message:{}

        From: {}
        '''.format(data['message'], data['email'])

        send_mail(data['subject'],message,'',ll,fail_silently=False,)
    return render(request, 'emailsender/success.html',{})


def deleteEmailModel(request, id): 
    ddlcompanyobjects = EmailModel.dbTableForEmail.get(id=id) 
    print(ddlcompanyobjects.emailadress)      
    ddlcompanyobjects.delete()
    return redirect('index')

def UpdateEmailModel(request, id):
        print('t')          
        obj= get_object_or_404(EmailModel, id=id)       
        form = EmailMaster(request.POST, instance= obj)
        context= {'form': form}
        print(obj)
        if form.is_valid():
            ddlcompanyobjects = EmailModel.dbTableForEmail.all()               
            user = form.save(commit=False)      
            user.save()       
            # messages.success(request, "You successfully updated the Data")
            context= {'form': form}     
            return redirect('index')                      
            return render(request, 'emailsender/index.html',{'form':form,'ddlcompanyobjects':ddlcompanyobjects})
        else:
            context= {'form': form,
                           'error': 'The Data  was not updated successfully.'}
            return render(request,'emailsender/index.html' , context)