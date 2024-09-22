from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Displays options for all functionalities

@app.route('/teams')
def all_teams():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('teams.html', teams=sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    if team1 and team2:
        response = requests.get(f'http://127.0.0.1:5000/api/teamvteam?team1={team1}&team2={team2}')
        result = response.json()
    else:
        result = None

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']
    return render_template('teamvteam.html', result=result, teams=sorted(teams))

@app.route('/team-record')
def team_record():
    team_name = request.args.get('team')
    if team_name:
        response = requests.get(f'http://127.0.0.1:5000/api/team-record?team={team_name}')
        record = response.json()
    else:
        record = None

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']
    return render_template('teamrecord.html', record=record, teams=sorted(teams))

@app.route('/batsman-record')
def batsman_record():
    batsman_name = request.args.get('batsman')
    if batsman_name:
        response = requests.get(f'http://127.0.0.1:5000/api/batsman-record?batsman={batsman_name}')
        record = response.json()
    else:
        record = None

    # Fetch all batsmen for dropdown
    batsmen_response = requests.get('http://127.0.0.1:5000/api/batsmen')
    batsmen = batsmen_response.json()['batsmen']

    return render_template('batsmanrecord.html', record=record, batsmen=sorted(batsmen))

app.run(debug=True, port=7000)