import requests
from django.shortcuts import render
import json

import google.generativeai as genai

from django.conf import settings

CODEFORCES_API = "https://codeforces.com/api/user.status?handle={handle}"
CODEFORCES_USER_INFO = "https://codeforces.com/api/user.info?handles={handle}"


genai.configure(api_key = settings.GOOGLE_API_KEY)

models = genai.GenerativeModel('gemini-pro')


def GenerativeText(promt):
	promt = f"hey I am give the username of codeforces user could you suggest the topic that the user need to study for better result also provide the resources for each topic {promt} , try to get most of the link from cp-algorithm and geeksforgeeks"
	response = models.generate_content(promt)
	return response.text



def strengthWeakness(promt):
	promt = f"hey I am give the username of codeforces user could you suggest what are the weakness and strength of user  "
	response = models.generate_content(promt)
	return response.text

def fetch_codeforces_data(handle):
	url = CODEFORCES_API.format(handle=handle)
	response = requests.get(url)
	if response.status_code != 200:
		return []
	return response.json().get('result', [])

def analyze_topics(submissions):
    topic_stats = {}
    for submission in submissions:
        if 'problem' in submission and 'tags' in submission['problem']:
            tags = submission['problem']['tags']
            verdict = submission.get('verdict', '')
            for tag in tags:
                if tag not in topic_stats:
                    topic_stats[tag] = {'solved': 0, 'unsolved': 0}
                if verdict == 'OK':
                    topic_stats[tag]['solved'] += 1
                else:
                    topic_stats[tag]['unsolved'] += 1
    
    strong_topics = [tag for tag, stats in topic_stats.items() if stats['solved'] > stats['unsolved']]
    weak_topics = [tag for tag, stats in topic_stats.items() if stats['solved'] <= stats['unsolved']]
    
    topic_labels = list(topic_stats.keys())
    solved_counts = [topic_stats[tag]['solved'] for tag in topic_labels]
    unsolved_counts = [topic_stats[tag]['unsolved'] for tag in topic_labels]
    
    return strong_topics, weak_topics, topic_labels, solved_counts, unsolved_counts

def analyze(request):
	if(request.user == None):
		return redirect('/')

	url = CODEFORCES_USER_INFO.format(handle = request.user.CodeForcesID)
	response = requests.get(url).json()
	if(response['status'] != "OK"):
		return redirect('/')

	response = response['result'][0]

	profile_url = response['titlePhoto']


	username = request.GET.get('username', 'Nehal21')  # Default user is 'Nehal21'
	submissions = fetch_codeforces_data(username)
	strong_topics, weak_topics, topic_labels, solved_counts, unsolved_counts = analyze_topics(submissions)
    
	context = {
		'strong_topics': strong_topics,
		'weak_topics': weak_topics,
		'topic_labels': topic_labels,
		'solved_counts': solved_counts,
		'unsolved_counts': unsolved_counts,
		'profile_url':profile_url,
	}
	return render(request, 'Predictions/analyzer.html', context)




def CodeforcesPrediction(request):
	if(request.user == None):
		return redirect('/')
	return render(request,'Predictions/codeforces.html')

def recommendTopic(request):
	if(request.user == None):
		return redirect('/')
	response = GenerativeText(request.user.CodeForcesID)
	url = CODEFORCES_USER_INFO.format(handle=request.user.CodeForcesID)
	response1 = requests.get(url).json()
	response1 = response1['result'][0]
	profile_url = response1['titlePhoto']
	context = {'RecommendTopic': response,'profile_url':profile_url}
	return render(request,'Predictions/recommendTopic.html',context)