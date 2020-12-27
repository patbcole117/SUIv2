from app import app
from app.utils.conf_parse import get_config
from datetime import datetime
from flask import request, jsonify, redirect, render_template
import json
import requests

@app.route('/')
@app.route('/home')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/e_clock')
def e_clock():
    time = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    return render_template('e_clock.html', time=time)

@app.route('/e_current_bout_table')
def e_current_bout_table():
    c = get_config()
    
    sbo_status = json.loads(requests.get(c['sbo_url'] + 'status').content)

    p1name = sbo_status['bout']['p1name']
    p1bets = sbo_status['bout']['p1total']
    rf = json.loads(requests.get(c['sdc_url'] + f'fighters?name={p1name}').content)
    
    p2name = sbo_status['bout']['p2name']
    p2bets = sbo_status['bout']['p2total']
    bf = json.loads(requests.get(c['sdc_url'] + f'fighters?name={p2name}').content)

    red = {'team': 'RED', 'name': p1name, 'bets': p1bets, 'wins': None, 'losses': None, 'elo': None, 'num_upsets': None, 'current_streak': None, 'date_of_debut': None}
    blue = {'team': 'BLUE', 'name': p2name, 'bets': p2bets, 'wins': None, 'losses': None, 'elo': None, 'num_upsets': None, 'current_streak': None, 'date_of_debut': None}

    if len(rf) > 0:
        for k, v in red.items():
            if k in rf[0].keys():
                red[k] = rf[0][k]

    if len(bf) > 0:
        for k, v in blue.items():
            if k in bf[0].keys():
                blue[k] = bf[0][k]
    
    current_bout = [red, blue]

    return render_template('table.html', items=current_bout, table_title='CURRENT BOUT')

@app.route('/e_latest_bouts_table')
def e_latest_bouts_table():
    c = get_config()
    latest_bouts = json.loads(requests.get(c['sdc_url'] + f'bouts?num=10&sort=id&sort_type=bottom').content)
    return render_template('table.html', items=latest_bouts, table_title='LATEST BOUTS')

@app.route('/e_latest_fighters_table')
def e_latest_fighters_table():
    c = get_config()
    latest_fighters = json.loads(requests.get(c['sdc_url'] + f'fighters?num=10&sort=id&sort_type=bottom').content)
    return render_template('table.html', items=latest_fighters, table_title='LATEST FIGHTERS')