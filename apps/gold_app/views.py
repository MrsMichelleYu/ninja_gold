from django.shortcuts import render, redirect
import random
from time import gmtime, strftime 

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    if "total_gold" not in request.session:
        request.session['total_gold'] = 0
    if 'activities_list' not in request.session: 
        request.session['activities_list'] = []
    return render(request, "gold_app/index.html", context)

def process_money(request, location):
    print(location)
    if location == "farm":
        coins = random.randint(10,20)
        request.session['total_gold'] += coins
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        message = f"<p class='green'> Earned {coins} golds from the house! ({time})</p>"
        print(message)
        request.session['activities_list'].append(message)
    elif location == "cave":
        coins = random.randint(5,10)
        request.session['total_gold'] += coins
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        message = f"<p class='green'> Earned {coins} golds from the cave! ({time})</p>"
        print(message)
        request.session['activities_list'].append(message)
    elif location == "house":
        coins = random.randint(2,5)
        request.session['total_gold'] += coins
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        message = f"<p class='green'> Earned {coins} golds from the house! ({time})</p>"
        print(message)
        request.session['activities_list'].append(message)
    elif location == "casino":
        coins = random.randint(-50,50)
        request.session['total_gold'] += coins
        if coins > 0:
            time = strftime("%Y-%m-%d %H:%M %p", gmtime())
            message = f"<p class='green'> Earned {coins} golds from the casino! ({time})</p>"
        else:
            coins = -1 * coins # amount of coins lost, made into a positive number 
            time = strftime("%Y-%m-%d %H:%M %p", gmtime())
            message = f"<p class='red'> Entered a casino and lost {coins} golds...Ouch..({time})</p>"
        print(message)
        request.session['activities_list'].append(message)

    #     elif request.POST['building'] == "cave":
    #         coins = random.randint(5,10)
    #         request.session['total_gold'] += coins
    #         time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    #         message = f"<p class='green'> Earned {coins} golds from the cave! ({time})</p>"
    #         print(message)
    #         request.session['activities_list'].append(message)
    #     elif request.POST['building'] == "house":
    #         coins = random.randint(2,5)
    #         request.session['total_gold'] += coins
    #         time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    #         message = f"<p class='green'> Earned {coins} golds from the house! ({time})</p>"
    #         print(message)
    #         request.session['activities_list'].append(message)
    #     elif request.POST['building'] == "casino":
    #         coins = random.randint(-50,50)
    #         request.session['total_gold'] += coins
    #         if coins > 0:
    #             time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    #             message = f"<p class='green'> Earned {coins} golds from the casino! ({time})</p>"
    #         else:
    #             coins = -1 * coins # amount of coins lost, made into a positive number 
    #             time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    #             message = f"<p class='red'> Entered a casino and lost {coins} golds...Ouch..({time})</p>"
    #         print(message)
    #         request.session['activities_list'].append(message)
    return redirect('/')

def reset(request):
    if 'total_gold' in request.session:
        request.session['total_gold'] = 0
    if 'activities_list' in request.session:
        request.session['activities_list'] = []
    return redirect ('/')

