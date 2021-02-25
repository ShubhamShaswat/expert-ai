# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import json
import os
from .api.expertai_api import ExpertAi
#from .api import discordBot as bot
from datetime import datetime
import discord
from django.views.decorators.csrf import csrf_exempt
import random



#open Files
filepath = os.path.join(os.getcwd(),'app/api/msg.txt')
#f =  open(filepath,'r')
#lines = f.readlines()
count = 0
average_sentiment = 0
length = 0
msg_user = ''


@csrf_exempt
@login_required(login_url="/login/")
def index(request):

    sentiment = 0
    text = ''
    all_tokens = []
    if request.method == 'POST':

        client_api = ExpertAi()
        #text =  request.POST.get('myText')
        timestamp = datetime.now().strftime('%H:%M')
        f =  open(filepath,'r')

        global average_sentiment
        global count
        global msg_user
        global length

        #idx = random.randint(0,len(lines))
        if f.read(1):

            count+=1
            msg_user = ''


            text = f.read()
            msg_user = text.split(':: ')[0]
            text = text.split(':: ')[1]

            length = len(text)
            f.close()
            with open(filepath,'w') as f:
                f.write('')

            sentiment = client_api.sentiment_analysis(text)

            average_sentiment += int(sentiment)
            average_sentiment /= count


            entities = client_api.get_tokens(text)

            all_tokens = [entity.lemma for entity in entities if entity.type_ == 'NPH']
            print(all_tokens)

        #shtml_template = loader.get_template( 'includes/analysedText.html' )
        return HttpResponse(json.dumps([{'text' : text, 'timestamp' : timestamp,'sentiment' : sentiment,'average_sentiment' : round(average_sentiment,2), 'length' : length, 'chatsNum' : count, 'msg_user' : msg_user, 'all_tokens' : all_tokens}]))

        #return HttpResponse(html_template.render({'text' : text, 'timestamp' : timestamp,'sentiment' : sentiment}, request))




    context = {'name':['BTC', 'ETH', 'ADA', 'XLM', 'ATOM', 'XRP'],'sentiment' : 23 } #store that in other files
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
