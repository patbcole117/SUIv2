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
    return render_template('dashboard.html', title='Dashboard')


@app.route('/bouts')
def bouts():
    c = get_config()
    page=request.args.get('page', default=0, type=int)
    sort=request.args.get('sort', default='id')
    bouts = json.loads(requests.get(c['SUI_SDC_URL'] + f'bouts?sort={sort}').content)
    num_bouts = len(bouts)

    page_size = 100
    max_page = num_bouts// page_size
    if num_bouts % page_size > 0:
        max_page = max_page + 1

    disp_pages_start = page - 5

    disp_pages_end = disp_pages_start + 50
    if disp_pages_end > max_page:
        disp_pages_end = max_page
        disp_pages_start = max_page - 50

    if disp_pages_start < 0:
        disp_pages_start = 0

    pages = list(range(disp_pages_start, disp_pages_end))
    if pages[0] != 0:
        pages.insert(0, 0)
    if pages[-1] != max_page:
        pages.append(max_page)

    if page > max_page:
        page = max_page
    
    first_index = page * page_size
    last_index = first_index + page_size

    if last_index > len(bouts):
        last_index = len(bouts)
        first_index = last_index - page_size
    return render_template('searchdata.html', title='bouts', items=bouts[first_index:last_index], table_title='BOUTS', pages=pages)


@app.route('/fighters')
def fighters():
    c = get_config()
    page=request.args.get('page', default=0, type=int)
    sort=request.args.get('sort', default='name')

    fighters = json.loads(requests.get(c['SUI_SDC_URL'] + f'fighters?sort={sort}').content)
    num_fighters = len(fighters)

    page_size = 100
    max_page = num_fighters // page_size
    if num_fighters % page_size > 0:
        max_page = max_page + 1

    disp_pages_start = page - 5

    disp_pages_end = disp_pages_start + 50
    if disp_pages_end > max_page:
        disp_pages_end = max_page
        disp_pages_start = max_page - 50
    
    if disp_pages_start < 0:
        disp_pages_start = 0

    pages = list(range(disp_pages_start, disp_pages_end))
    if pages[0] != 0:
        pages.insert(0, 0)
    if pages[-1] != max_page:
        pages.append(max_page)

    if page > max_page:
        page = max_page
    
    first_index = page * page_size
    last_index = first_index + page_size

    if last_index > len(fighters):
        last_index = len(fighters)
        first_index = last_index - page_size

    return render_template('searchdata.html', title='fighters', items=fighters[first_index:last_index], table_title='FIGHTERS', pages=pages)

@app.route('/configurations')
def configurations():

    return render_template('configurations.html', title='Configurations')

@app.route('/api/v1/help')
def api_v1_help():
    help = {}
    help['/api/v1/help'] = 'Display avalible URLs and descriptions.'
    help['/api/v1/status'] = 'Display config.txt information.'
    help['/bouts'] = 'Display and filter bouts from the database.'
    help['/configurations'] = 'Display config information for all Saly Microservices.'
    help['/dashboard'] = 'Display the dashboard for Saly Microservices.'
    help['/fighters'] = 'Display and filter fighters from the database.'
    return jsonify(help)


@app.route('/api/v1/status')
def api_v1_status():
    c = get_config()
    return jsonify(c)


@app.route('/e_clock')
def e_clock():
    time = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    return render_template('/elements/e_clock.html', time=time)


@app.route('/e_current_bout_table')
def e_current_bout_table():
    c = get_config()
    
    sbo_status = json.loads(requests.get(c['SUI_SBO_URL'] + 'status').content)

    p1name = sbo_status['bout']['p1name']
    p1bets = sbo_status['bout']['p1total']

    p2name = sbo_status['bout']['p2name']
    p2bets = sbo_status['bout']['p2total']

    red = {'team': 'RED', 'name': p1name, 'bets': p1bets, 'wins': None, 'losses': None, 'elo': None, 'num_upsets': None, 'current_streak': None, 'date_of_debut': None}
    blue = {'team': 'BLUE', 'name': p2name, 'bets': p2bets, 'wins': None, 'losses': None, 'elo': None, 'num_upsets': None, 'current_streak': None, 'date_of_debut': None}

    try:
        req_p1 = requests.get(c['SUI_SDC_URL'] + f'exactfighter?name={p1name}').content
        rf = json.loads(req_p1)
        for k, v in red.items():
            if k in rf.keys():
                red[k] = rf[k]
    except:
        pass
        
    try:
        req_p2 = requests.get(c['SUI_SDC_URL'] + f'exactfighter?name={p2name}').content
        bf = json.loads(req_p2)
        for k, v in blue.items():
            if k in bf.keys():
                blue[k] = bf[k]
    except:
        pass
    
    current_bout = [red, blue]
    print (current_bout)
    return render_template('/elements/e_table.html', items=current_bout, table_title='CURRENT BOUT')


@app.route('/e_latest_bouts_table')
def e_latest_bouts_table():
    c = get_config()
    latest_bouts = json.loads(requests.get(c['SUI_SDC_URL'] + f'bouts?num=10&sort=id&sort_type=bottom').content)
    return render_template('/elements/e_table.html', items=latest_bouts, table_title='LATEST BOUTS')


@app.route('/e_latest_fighters_table')
def e_latest_fighters_table():
    c = get_config()
    latest_fighters = json.loads(requests.get(c['SUI_SDC_URL'] + f'fighters?num=10&sort=id&sort_type=bottom').content)
    return render_template('/elements/e_table.html', items=latest_fighters, table_title='LATEST FIGHTERS')



@app.route('/e_top')
def e_top():
    return render_template('/elements/e_top.html')


@app.route('/e_sbo_config')
def e_sbo_config():
    c = get_config()
    sbo_status = json.loads(requests.get(c['SUI_SBO_URL'] + f'status').content)
    sbo_status = json.dumps(sbo_status, indent=2)
    return render_template('/elements/e_config.html', items=sbo_status, title='SBO CONFIGURATION')


@app.route('/e_sdc_config')
def e_sdc_config():
    c = get_config()
    sdc_status = json.loads(requests.get(c['SUI_SDC_URL'] + f'status').content)
    sdc_status = json.dumps(sdc_status, indent=2)
    return render_template('/elements/e_config.html', items=sdc_status, title='SDC CONFIGURATION')


@app.route('/e_sui_config')
def e_sui_config():
    sui_status = get_config()
    sui_status = json.dumps(sui_status, indent=2)
    return render_template('/elements/e_config.html', items=sui_status, title='SUI CONFIGURATION')