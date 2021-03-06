from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import Results_Set
import json, polling, random as rng, requests

#-----------------------------------------------------------------------------
# Purpose:     Create views fuction to retrieve results from data layer and
#              store it using Results_Set model from /models.py
#
# Functions:   retrieve
#
#-----------------------------------------------------------------------------

def retrieve(request,result_id):
    """
    Purpose: Retrieve data from either the database created by back end or 
    alternativly, if that is unavailable, through a URL that contains a 
    randomly generated JSON in a specific template

    Return: HTTP response

    How: Use polling to ping the website and store the json in the 
    Results_Set model from .models.py.
    
    Template expected can be found in Results-example.json
    """
    url = settings.GLOBAL_SETTINGS['BACKEND_URL']+'/api/json/get/ceeCPfmcoi'
    # Alternative site for example JSONs
    #url = settings.GLOBAL_SETTINGS['BACKEND_URL']+'users/%s/' % result_id
    
    response = 'URL: ' +url+' | Resp OK = '
    
    try:
        # poll the results table and get the JSON object when complete
        polling.poll(lambda: requests.get(url).status_code == 200,
                     step=1,
                     max_tries=5)
        jsonObj = requests.get(url).json()

        # create a new result set to store the data
        resultset = Results_Set()
        resultset.jsonObjs = jsonObj
        resultset.id = 1

        ALTERNATIVE_URL=False
        if (ALTERNATIVE_URL):
            resultset.id = jsonObj['id'];
            fakedResult={'result_id':jsonObj['id'],
                         'meta_file_info':{},
                         'results':{'topic_stats':[],'instructor_stats':[]}
            }
            # Fake Metadata
            fakedMeta={'document_id_number':rng.randint(1,1000),
                       'user_selected_number_topics':rng.randint(1,5),
                       'user_selected_number_interations':rng.randint(1,30),
                       'user_selected_number_words_per_topic':rng.randint(1,5)}
            fakedResult['meta_file_info']=fakedMeta
            #Fake Topic Results
            fakedTopic_comments={
                'positive':jsonObj['company']['name'].split(),
                'neutral':jsonObj['company']['catchPhrase'].split(),
                'negative':jsonObj['company']['bs'].split()}                
            fakedTopic_stats={'words':jsonObj['website'].split(),
                              'comments':fakedTopic_comments}
            fakedTopicStatsList=[fakedTopic_stats,fakedTopic_stats]
            fakedResult['results']['topic_stats']=fakedTopicStatsList
            #Fake Instructor Results
            fakedInstr_comments={
                'positive':jsonObj['address']['street'].split(),
                'neutral':jsonObj['address']['suite'].split(),
                'negative':jsonObj['address']['city'].split()}
            fakedInstr_stats={
                'instructor_first_name':jsonObj['name'].split()[0],
                'instructor_first_name':jsonObj['name'].split()[0],
                'course_num_sect_id':jsonObj['address']['geo']['lat'],
                'comments':fakedInstr_comments}
            fakedInstrList=[fakedInstr_stats,fakedInstr_stats]
            fakedResult['results']['instructor_stats']=fakedInstrList
            resultset.jsonObjs = fakedResult
            
        resultset.save()
        response = response + 'OK'
    except polling.MaxCallException:
        response = response + 'FAIL'      
    return HttpResponse(response)
    
def index(request):
    return HttpResponse("Hello, world. You're at the results index.")
