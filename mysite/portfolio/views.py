from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from firebase import firebase

# Create your views here.
def index(request):
    return(render(request, 'portfolio/index.html'))


def message(firstName, lastName, email, messageBody):

    firebaseReq = firebase.FirebaseApplication("https://portfolio-5b10d.firebaseio.com/", None)

    data = {
        'FirstName' : firstName,
        'LastName' : lastName,
        'Email' : email,
        'Message' : messageBody,
    }
    result = firebaseReq.post('/WebsiteUser',data)
    print(result)
    

def contact(request):
    print("In contact")
    if request.method == 'POST':
        firstName = request.POST['FirstName']
        lastName = request.POST['LastName']
        email = request.POST['Email']
        messageBody = request.POST['messageBody']
        message(firstName, lastName, email, messageBody)
        return HttpResponse('Message sent successfully')
        
    


    