from django.shortcuts import render
from upload.models import Video
from register.models import User
import demjson
from register.forms import WhaleBlockChainForm, SmokeBlockChainForm, SteemBlockChainForm, UserRegistrationCompletionForm
# Create your views here.

def mychannel(request, pk):
        video = Video.objects.filter(user_id=pk)
        resolution = [2160, 1440, 1080, 720, 480, 360, 240  , 144]

        for each_videot in video:
                for each_res in resolution:
                        if str(each_res) in each_videot.video:
                                hasht = demjson.decode(each_videot.video)
                                each_videot.bestHash_Trending = hasht[str(each_res)]
                                break  

        ch = User.objects.get(id=pk)
        print(ch)
        context = {'video': video, 'channel':ch.channel_name}
        return render(request, 'single_channel/detail.html', context)  

def myprofile(request,pk ):
        whaleForm = WhaleBlockChainForm()
        smokeForm = SmokeBlockChainForm()
        steemForm = SteemBlockChainForm()
        userdetails = UserRegistrationCompletionForm()

        context = {'whaleForm':whaleForm, 'smokeForm':smokeForm, 'steemForm':steemForm, 'userdetails':userdetails}
        return render(request, 'single_channel/userProfile.html', context)  


def steem_blockchain(request):
        whaleForm = WhaleBlockChainForm()
        smokeForm = SmokeBlockChainForm()
        steemForm = SteemBlockChainForm()
        userdetails = UserRegistrationCompletionForm()
        if request.user.is_authenticated == True:
                current = User.objects.get(id=request.user.id)
                formBl = SteemBlockChainForm() 
                
                if request.method == 'POST':
                        formb = SteemBlockChainForm(request.POST)
                        success=''
                        if formb.is_valid():
                                data = {}
                                data['steem'] = formb.cleaned_data['steem']
                                data['steem_name'] = formb.cleaned_data['steem_name']

                                if formb.save(data, current.id):
                                        success='true'
                                else:
                                        print('Database error')    
                        else:
                                print('The submitted form is not valid')
                
                
                        context = {'whaleForm':whaleForm, 'smokeForm':smokeForm, 'steemForm':steemForm, 'userdetails':userdetails,'success':success}
                        return render(request, 'single_channel/userProfile.html', context) 

def smoke_blockchain(request):
        whaleForm = WhaleBlockChainForm()
        smokeForm = SmokeBlockChainForm()
        steemForm = SteemBlockChainForm()
        userdetails = UserRegistrationCompletionForm()
        if request.user.is_authenticated == True:
                current = User.objects.get(id=request.user.id)

                if request.method == 'POST':
                        formb = SmokeBlockChainForm(request.POST)
                        success=''
                        if formb.is_valid():
                                data = {}
                                data['smoke'] = formb.cleaned_data['smoke']
                                data['smoke_name'] = formb.cleaned_data['smoke_name']

                                if formb.save(data, current.id):
                                        success='true'
                                else:
                                        print('Database error') 
                        else:
                                print('The submitted form is not valid')
                        
                        context = {'whaleForm':whaleForm, 'smokeForm':smokeForm, 'steemForm':steemForm, 'userdetails':userdetails,'success':success}
                        return render(request, 'single_channel/userProfile.html', context) 

def whale_blockchain(request):
        whaleForm = WhaleBlockChainForm()
        smokeForm = SmokeBlockChainForm()
        steemForm = SteemBlockChainForm()
        userdetails = UserRegistrationCompletionForm()    
        if request.user.is_authenticated == True:
                current = User.objects.get(id=request.user.id)

                if request.method == 'POST':
                        formb = WhaleBlockChainForm(request.POST)
                        success=''
                        if formb.is_valid():
                                data = {}
                                data['whaleshare'] = formb.cleaned_data['whaleshare']
                                data['whaleshare_name'] = formb.cleaned_data['whaleshare_name']

                                if formb.save(data, current.id):
                                        success='true'
                                else:
                                        print('Database error') 
                        else:
                                print('The submitted form is not valid')
                        
                        context = {'whaleForm':whaleForm, 'smokeForm':smokeForm, 'steemForm':steemForm, 'userdetails':userdetails,'success':success}
                        return render(request, 'single_channel/userProfile.html', context) 