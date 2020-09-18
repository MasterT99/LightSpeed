
# DO NOT TOUCH ANYTHING WITHOUT MY PERMISSION
# CLASSIFIED FILE

import os
import secrets
import shutil
import string

from CDD import models
from CDD.function.CarDamage import *
from CDD.function.extras import handle_uploaded_file

from django.shortcuts import redirect
from django.http.response import HttpResponse
from django.template import loader
from django import forms
# Create your views here.


def index(request):
    # print(os.getcwd())
    images = ["image/clg/"+i for i in os.listdir("CDD/static/image/clg")[1:]]
    # print(images)
    template = loader.get_template("index.html")
    data = {"email": request.session.get("email", None),
            "fname": request.session.get("fname", "This is creepy!"),
            "lname": request.session.get("lname", "This is so creepy!"),
            "images": images
            }
    return HttpResponse(template.render(data))


def announcement(request):
    temp = loader.get_template("announcement.html")
    data = {"email": request.session.get('email'),
            "fname": request.session.get('fname'),
            "lname": request.session.get('lname')}
    return HttpResponse(temp.render(data, request))


def history(request):
    temp = loader.get_template("history.html")
    data = {"email": request.session.get('email'),
            "fname": request.session.get('fname'),
            "lname": request.session.get('lname')}
    return HttpResponse(temp.render(data, request))


def contact(request):
    temp = loader.get_template("contact.html")
    data = {"email": request.session.get('email'),
            "fname": request.session.get('fname'),
            "lname": request.session.get('lname')}
    return HttpResponse(temp.render(data, request))


def dashboard(request):
    email = request.session.get('email', None)
    if email is None:
        return redirect("/index")
    temp = loader.get_template("dashboard.html")
    claims = models.Claims.objects.all().filter(email=email)
    user = models.User.objects.get(email=email)
    request.session['total_claims'] = user.total_claims
    partcost = models.PartCost.objects.get(make=user.degree)
    color = {"Pending":"warning", "Passed":"success", "Rejected":"danger"}
    for i in range(len(claims)):
        claims[i].sr = i+1
        claims[i].color = color[claims[i].processed]
        claims[i].passed = False
        if claims[i].processed == "Passed": claims[i].passed = True
    data = {"email": request.session['email'], "fname": request.session['fname'], "mname": request.session['mname'],
    "lname": request.session['lname'], "gender": request.session['gender'], "degree": request.session['degree'],
            "total_claims": request.session['total_claims'], "claims": claims, "partcost": partcost}
    return HttpResponse(temp.render(data))


def chat(request):
    boolean_message_sent = False
    receiver = ""
    email = request.session.get('email', None)
    if email is None:
        return redirect("/index")
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            for i in form.data.values():
                print(i)
            receiver = form.data.get("receiver")
            if receiver is not None:
                message = form.data.get('message')
                chat = models.Chat(sender=email, receiver=receiver, message=message)
                chat.save()
                boolean_message_sent = True
    chat = models.Chat.objects.raw("SELECT * FROM CHAT WHERE RECEIVER='" + email + "' OR SENDER='" + email
                                   + "' ORDER BY ID DESC")
    temp = loader.get_template("chat.html")
    data = {"email": email,
            "fname": request.session['fname'],
            "lname": request.session['lname'],
            "receiver": receiver,
            "boolean1": boolean_message_sent,
            "messages": chat
            }
    return HttpResponse(temp.render(data, request))


def login(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            for i in form.data.values():
                print(i)
            email = form.data.get("email")
            password = form.data.get("password")
            if email == "" or email is None or password == "" or password is None:
                return redirect("/login", permanent=True)
            try:
                user = models.User.objects.get(email=email)
            except:
                return scaffold_template("signup", "warning", "User doesn't exists!", "Redirecting you to the sign up page shortly..." + getprogress("warning"))
            if password == user.password:
                request.session['email'] = user.email
                request.session['fname'] = user.fname
                request.session['mname'] = user.mname
                request.session['lname'] = user.lname
                request.session['gender'] = user.gender
                request.session['degree'] = user.degree
                request.session['total_claims'] = user.total_claims
                return scaffold_template("dashboard", "success", "Logging in...", "Redirecting you to the dashboard "
                                                                                  "shortly..." + getprogress("success"))
            if password != user.password:
                return scaffold_template("login", "danger", "Incorrect Password", "Redirecting you to the login page "
                                                                                  "shortly..." + getprogress("danger"))

    else:
        temp = loader.get_template("login.html")
        return HttpResponse(temp.render({},request))


def signup(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            for i in form.data.values():
                print(i)
            email = form.data.get("Email")
            try:
                user = models.User.objects.get(email=email)
                return scaffold_template("login", "success", "User already exists!",
                                         "Redirecting you to the login page shortly..." + getprogress("success"))
            except:
                pass
            user = models.User(fname=form.data['First-Name'], mname=form.data['Middle-Name'],
                               lname=form.data['Last-Name'], gender=form.data['Sex'], degree=form.data['Degree'],
                               email=form.data['Email'], password=form.data['Password'])
            # user = models.User()
            # user.fname = form.data.get('First-name')
            user.save()
            return redirect("/login", permanent=True)
    # print(form.data.keys())
    else:
        temp = loader.get_template("signup.html")
        return HttpResponse(temp.render({},request))


def logout(request):
    email = request.session.get('email', None)
    if email is None:
        return redirect("/index")
    # request.session.delete()
    # request.COOKIES.clear()
    # request.session.flush()
    # # request.session.set_expiry()
    # request.session['email'] = None
    # temp = loader.get_template("index.html")
    # data = {"email": "None"}
    # respose = HttpResponse(temp.render(data, request))
    response = scaffold_template("index", "primary", "Logging out...", "Redirecting you to the home page shortly..."
                                 + getprogress("primary"))
    response.delete_cookie("sessionid")
    response.delete_cookie("csrftoken")
    request.session['email'] = None
    return response
# How are you?


def about(request):
    temp = loader.get_template("about.html")
    data = {"email": request.session.get('email'),
            "fname": request.session.get('fname'),
            "lname": request.session.get('lname')}
    return HttpResponse(temp.render(data, request))


def ajax(request):
    # if request.is_ajax():
    form = forms.Form(request.GET)
    year = form.data.get('year')
    month = form.data.get('month')
    field = form.data.get('field')
    circular = models.Circular.objects.raw("SELECT * FROM CIRCULAR WHERE YEAR LIKE " + year + " AND MONTH LIKE "
                       + month + " AND FIELD LIKE '" + field + "' ORDER BY YEAR DESC, MONTH DESC")
    # print(len(circular))
    # print(circular)
    data = {"length":len(circular), "circular": circular}
    temp = loader.get_template("ajax.html")
    return HttpResponse(temp.render(data))
    # else:
    #     return redirect("/index", permanent=True)


def process(request):
    email = request.session.get('email', None)
    if email is None:
        return redirect("/index")
    elif request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            for i in form.data.values():
                print(i)
            action = form.data.get('action', None)
            if action == "" or action is None:
                return redirect("/index")
            if str(action).__contains__("Sent"):
                models.Chat.objects.filter(sender=email).all().delete()
            elif str(action).__contains__("Received"):
                models.Chat.objects.filter(receiver=email).all().delete()
        return redirect("/chat")
    else:
        return redirect("/index")


def scaffold_template(redir, color, head1, head2, time=3):
    data = {"time":time, "page": redir, "type": color, "head1": head1, "head2": head2}
    temp = loader.get_template("scaffold1.html")
    return HttpResponse(temp.render(data))


def apply(request):
    email = request.session.get('email', None)
    if email is None:
        return redirect("/index")
    temp = loader.get_template("apply.html")
    data = {"email": email,
            "fname": request.session['fname'],
            "lname": request.session['lname']}
    return HttpResponse(temp.render(data, request))


# def prediction_landing(request):
#     return scaffold_template("prediction", "primary", "Please wait...", 'Your images are being '
#     'processed...</h3><br><br><br><h3><center><div class="progress" style="width: 80%;"><div class="progress-bar '
#     'progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="100" aria-valuemin="0" '
#     'aria-valuemax="100" style="width: 100%"></div></div>',
#                              1)
def getprogress(type):
    return '</h3><br><br><br><h3><center><div class="progress" style="width: 70%;"><div class="progress-bar ' \
           'progress-bar-striped progress-bar-animated bg-' + type + '" role="progressbar" aria-valuenow="100" ' \
           'aria-valuemin="0" aria-valuemax="100" style="width: 100%"></div></div>'


def prediction(request):
    email = request.session.get('email', None)
    if email is None:
        return redirect("/index")
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            al = string.ascii_letters + string.digits
            k = 8
            file_front = request.FILES['accident_front']
            file_rear = request.FILES['accident_rear']
            file_left = request.FILES['accident_left']
            file_right = request.FILES['accident_right']
            accident_date = form.data.get('accident_date')
            accident_front = "".join(secrets.SystemRandom().choices(al, k=k)) + file_front.name
            accident_rear = "".join(secrets.SystemRandom().choices(al, k=k)) + file_rear.name
            accident_left = "".join(secrets.SystemRandom().choices(al, k=k)) + file_left.name
            accident_right = "".join(secrets.SystemRandom().choices(al, k=k)) + file_right.name
            # request.session['front'] = accident_front
            # request.session['rear'] = accident_rear
            # request.session['left'] = accident_left
            # request.session['right'] = accident_right
            message = form.data.get('message')
            handle_uploaded_file(file_front, "front", accident_front)
            handle_uploaded_file(file_rear, "rear", accident_rear)
            handle_uploaded_file(file_left, "left", accident_left)
            handle_uploaded_file(file_right, "right", accident_right)
            claims = models.Claims(accident_date=accident_date, accident_front=accident_front,
                                   accident_rear=accident_rear, accident_left=accident_left,
                                   accident_right=accident_right, message=message, email=email)
            user = models.User.objects.get(email=email)
            user.total_claims += 1
            user.save()

            claims.bool_is_car = is_car()
            if not claims.bool_is_car:
                claims.processed = "Rejected"
                claims.total_cost_estimation = 0
                # claims.bool_is_car = False
                # return HttpResponse("<h1>Upload Image of Car!!!!</h1>")
            else:
                # claims.bool_is_car = True
                claims.bool_boot,claims.bool_bumper_front,claims.bool_bumper_rear,claims.bool_door_left=(False for i in range(4))
                claims.bool_door_right,claims.bool_window_left,claims.bool_window_right,claims.bool_windshield_front=(False for i in range(4))
                claims.bool_windshield_rear,claims.bool_hood=(False for i in range(2))
                if is_front():
                    claims.bool_hood = is_hood()
                    claims.bool_bumper_front = is_bumper()
                    claims.bool_windshield_front = is_windshield()
                if is_side('left'):
                    claims.bool_window_left = is_window('left')
                    claims.bool_door_left = is_door('left')
                if is_side('right'):
                    claims.bool_door_right = is_door('right')
                    claims.bool_window_right = is_window('right')
                if is_rear():
                    claims.bool_boot = is_boot()
                    claims.bool_bumper_rear = is_bumper_rear()
                    claims.bool_windshield_rear = is_windshield_rear()
                if any([claims.bool_hood, claims.bool_boot, claims.bool_bumper_front, claims.bool_bumper_rear,
                     claims.bool_windshield_front, claims.bool_windshield_rear, claims.bool_door_left,
                     claims.bool_door_right, claims.bool_window_left, claims.bool_window_right]):
                    partcost = models.PartCost.objects.get(make=user.degree)
                    claims.processed = "Passed"
                    claims.total_cost_estimation = partcost.hood * int(claims.bool_hood) + partcost.boot * int(
                        claims.bool_boot) + partcost.bumper * (int(claims.bool_bumper_front) + int(
                        claims.bool_bumper_rear)) + partcost.windshield * (int(claims.bool_windshield_front) + int(
                        claims.bool_windshield_rear)) + partcost.door * (int(claims.bool_door_left) + int(
                        claims.bool_door_right)) + partcost.window * (int(claims.bool_window_left) + int(
                        claims.bool_window_right))
                else:
                    claims.processed = "Rejected"
                    claims.total_cost_estimation = 0


            # data = {"hood": hood, "bumper": bumper, "winshild": winshield, "door": door, "window": window, "boot": boot,
            #         "rwinshild": rwinshild, "rbumper": rbumper, "door_right": door_right, "window_right": window_right,
            #         "front": request.session.get('front'), "left": request.session.get('left'),
            #         "right": request.session.get('right'), "rear": request.session.get('rear')}

            shutil.move('CDD/static/upload/predict/front/a/' + os.listdir('CDD/static/upload/predict/front/a/')[0],
                        'CDD/static/upload/coldstorage/front/' + os.listdir('CDD/static/upload/predict/front/a/')[0])
            shutil.move('CDD/static/upload/predict/rear/a/' + os.listdir('CDD/static/upload/predict/rear/a/')[0],
                        'CDD/static/upload/coldstorage/rear/' + os.listdir('CDD/static/upload/predict/rear/a/')[0])
            shutil.move('CDD/static/upload/predict/left/a/' + os.listdir('CDD/static/upload/predict/left/a/')[0],
                        'CDD/static/upload/coldstorage/left/' + os.listdir('CDD/static/upload/predict/left/a/')[0])
            shutil.move('CDD/static/upload/predict/right/a/' + os.listdir('CDD/static/upload/predict/right/a/')[0],
                        'CDD/static/upload/coldstorage/right/' + os.listdir('CDD/static/upload/predict/right/a/')[0])
            claims.save()


    # temp = loader.get_template("prediction.html")
    # return HttpResponse(temp.render(data, request))
    return redirect("/dashboard")


