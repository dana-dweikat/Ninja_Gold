from django.shortcuts import render,redirect
import datetime
import random

# Create your views here.


def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session.save()
    
    if 'msgs' not in request.session:
        request.session['msgs'] = []
        request.session.save()
    
   
    
    return render(request,"index.html")

def users_gold(request):
    ### Request : POST
    ### Which Form Is Called ?
    is_plus = True
    form = request.POST['location']
    ## form = ( 'cave' , 'house' , 'farm' , 'quest')
    random_number = None
    #gold_in_first = request.session['gold']

    if form == 'farm':
        ## Write Logic for random number in farm form
        print('This Is farm Form')
        random_number = random.randint(10,20)

    if form == 'cave':
        ## Write Logic for random number in Cave form
        print('This Is Cave Form')
        random_number = random.randint(10,20)
        
    if form == 'house':
        ## Write Logic for random number in house form
        print('This Is house Form')
        random_number = random.randint(10,20)

    if form == 'quest':
        ## Write Logic for random number in quest form
        print('This Is Quest Form')
        random_number = random.randint(-50,50)
    
    ## Create Var 'gold' and add random number to gold
    # gold_in_first += random_number
    # gold = gold + random_number
    ## Save 'gold' value in key 'gold'
    request.session['gold'] += random_number
    request.session.save()
    
    

    
   
    # Return End Of Function
    time_now = datetime.datetime.now()
    earn_or_take = "earned"
    if random_number < 0:
        is_plus = False
        earn_or_take = "lost"
    message = "You Entered a " + str(form) + " and " + earn_or_take + " a " + str(random_number) + " gold ." + "(" + str(time_now) + ")"
    request.session['msgs'].append(
        {'text':message,'is_plus':is_plus}
        )
    # msgs = [
    #     {'text':"you entered ... ",'is_plus':True},
    #     {'text':"you entered ... ",'is_plus':True},
    #     {'text':"you entered ... ",'is_plus':True},
    #     {'text':"you entered ... ",'is_plus':True},
    #     {'text':"you entered ... ",'is_plus':True},
    # ]
    request.session.save()
    ## Get gold 'key' from session and add random integer from 10 : 20
    # request.session['gold'] = request.session['gold'] + random.randint(10,20)
    # request.session.save()
    return redirect("home")


def destroy_session(request):
    del request.session['gold']
    del request.session['msgs']
    return redirect("home")
