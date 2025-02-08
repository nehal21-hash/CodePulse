import requests
import matplotlib.pyplot as plt
import io
import urllib
import json
import base64
from django.shortcuts import render,redirect
from collections import defaultdict
import time
CODEFORCES_API = "https://codeforces.com/api/user.status?handle={handle}"

CODEFORCES_CONTEST_LIST = "https://codeforces.com/api/contest.list"

CODEFORCES_User_Info = "https://codeforces.com/api/user.info?handles={handle}"


# Function to fetch upcoming contest
def Fetch_UpcomingContest():
    url = CODEFORCES_CONTEST_LIST
    response = requests.get(url).json()
    response = response['result']
    upcomingContest =[]
    for contest in response:
        if(contest['startTimeSeconds']>time.time()):
            upcomingContest.append({
                'name': contest['name'],
                'duration':f"{contest['durationSeconds']//(24*60)}Hr : {contest['durationSeconds']%60}Mins",
                'time':contest['startTimeSeconds'],
                'contestId':contest['id']

            })


    return upcomingContest


# Function to fetch user data
def fetch_codeforces_data(handle):
    url = CODEFORCES_API.format(handle=handle)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Function to analyze user data
def analyze_user_data(submissions):
    problem_count = defaultdict(int)
    languages_used = defaultdict(int)
    verdicts = defaultdict(int)
    topic_distribution = defaultdict(int)
    
    for submission in submissions:
        problem_id = f"{submission['problem']['contestId']}-{submission['problem']['index']}"
        problem_count[problem_id] += 1
        languages_used[submission['programmingLanguage']] += 1
        verdicts[submission['verdict']] += 1
        
        if "tags" in submission["problem"]:
            for tag in submission["problem"]["tags"]:
                topic_distribution[tag] += 1
    
    return {
        "total_solved": len(problem_count),
        "language_usage": dict(languages_used),
        "verdict_distribution": dict(verdicts),
        "topic_distribution": dict(topic_distribution)
    }

# Function to generate a graph for language usage
def generate_graph(data_dict, title):
    plt.figure(figsize=(8, 5))
    plt.bar(data_dict.keys(), data_dict.values(), color="skyblue")
    plt.xlabel("Categories")
    plt.ylabel("Count")
    plt.title(title)
    plt.xticks(rotation=45, ha="right")

    # Convert the graph to a base64 string
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    graph_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return f"data:image/png;base64,{graph_base64}"

# Django view to display user stats
def user_stats(request):
    if(request.user  == None):
        return redirect('accounts/register')
    handle = request.user.CodeForcesID
    url = CODEFORCES_User_Info.format(handle=handle)
    response = requests.get(url).json()
    user_infos = response['result'][0]
    profile_url = user_infos['titlePhoto']
    data = None
    analysis = None
    data = {}
    if handle:
        data = fetch_codeforces_data(handle)
        if data and "result" in data:
            analysis = analyze_user_data(data["result"])

            # Generate graphs
            if analysis:
                data["language_usage"] = json.dumps(analysis['language_usage'])
                data["verdict_distribution"] = json.dumps(analysis['verdict_distribution'])
                data["topic_distribution"] = json.dumps(analysis['topic_distribution'])
                data["total_solved"] = analysis['total_solved']

    return render(request, "Codeforces/user_stats.html", {
        "handle": handle,
        "analysis": data,
        "profile_url":profile_url,
    })




def events(request):
    if(request.user == None):
        return redirect('/')

    upcomingContest = Fetch_UpcomingContest()
    print(upcomingContest)
    context  = {'upComingContest': upcomingContest}
    return render(request,'Codeforces/events.html',context)


