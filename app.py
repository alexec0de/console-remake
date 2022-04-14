from flask import Flask, render_template,redirect, url_for, request
from db import  MYSQL
from config import  *
import json

conn = MYSQL(config['console_db_host'], config['console_db_user'], config['console_db_pass'], config['console_db_name'], dbcharset= 'utf8')


app = Flask(__name__)


#core settings
port = 9999
department_type = 1
situations = True
situation_is_attached = False
user_auth_var = True
avail = 1
fid = 1
ituation_is_attached = False
departament = 0
dept = None



#sql setting
settings_cound = {'id':2}

sit_cound = {}
db = True




#api route
@app.route('/api/auth', methods=['GET', 'POST'])
def user_auth():
	if request.method ==('POST'):
		test = request.form['idt']
		ip_addr = request.remote_addr
		user = conn.fetch_rows('users')
		for row in user:
			
	#	print(ip_addr)
	
			if ip_addr == row['ip']:
				return 'success'
			else:
				return 'error'
		if TypeError:
			return 'error'
	else:
		return redirect('/')

#api route
@app.route('/api/updatename', methods=['GET', 'POST'])
def update_officer_name():
	if request.method ==('POST'):
		if db == True:
			newnick = request.form.get('nick')
	#	user['officer-name'] = newnick
			return redirect('/mdt')
		else:
			return 'Нет подключение с БД'
	else:
		return redirect('/')
					
@app.route('/api/gamezone', methods=['GET', 'POST'])
def update_gamezone():
	if request.method ==('POST'):
		if db == True:
			newgamezone = request.form['gamezone']
		#	print(newgamezone)
			if newgamezone ==  '':
				return 'Error'
			else:
				data_gamezone = {'s_value':newgamezone}
				gamezone_cound={'id':2}
				conn.update('settings', data=data_gamezone, condition = gamezone_cound)
				return 'success'
		else:
			return 'Нет подключение с БД'
	else:
		return redirect('/')
	
@app.route('/api/steamid/update', methods=['GET', 'POST'])
def update_steamid():
	if request.method ==('POST'):
		if db == True:
			newsteamid = request.form.get('steamid')
#		user['steam_id'] = newsteamid
			return redirect('/profile')
		else:
			return 'Нет подключение с БД'
	else:
		return redirect('/')
@app.route('/api/name/update', methods=['GET', 'POST'])
def update_name():
	if request.method == ('POST'):
		if db == True:
			newname = request.form['name']
			if newname == '':
				return 'Error'
			else:
				name_data = {'name':newname}
				name_cound = {'ip':request.remote_addr}
				conn.update('users', data=name_data,condition= name_cound)
				return 'success'
		else:
			return 'Нет подключение с БД'
	else:
		return redirect('/')
		
@app.route('/api/situations/create', methods=['GET', 'POST'])
def create_situations():
	if request.method == 'POST':
		if db == True:
			street =request.form.get('street')
	#	intercepted-street_var = request.form.get('intercepted-street')
			blog = request.form.get('blog')
			description = request.form.get('description')
	#	sit_id = sit_id + 1
			data = {
		#	'id': sit_id,
				'street':street,
			#'intercepted-street':intercepted-street_var,
				'block':blog,
				'description':description
			}
			conn.insert('situations', data)
			description = 0
			blog =0
			street = 0
			data = 0
			return redirect('/civil')
		else:
			return 'Нет подключение с БД'
	else:
		return redirect('/')
@app.route('/api/characres/create', methods=['GET', 'POST'])
def charactes_create():
	if request.method == 'POST':
		name = request.form.get('name')
		date = request.form.get('date')
		sex = request.form .get('sex')
		race = request.form.get('race')
		job = request.form.get('job')
		address = request.form.get('address')
		med = request.form.get('med')
		med_alerg = request.form.get('med_alerg')
		med_drag = request.form.get('med_drag')
		contact = request.form.get('contact')
		mass = request.form.get('mass')
		rost = request.form.get('rost')
		draving_name = request.form.get('draving_name')
		license_draving = request.form.get('license_draving')
		gun_license = request.form.get('gun_license')
		description= request.form.get('description')
		data ={
			'name':name,
			'birth':date,
			'sex':sex,
			'race':race,
			'driving_license':license_draving,
			'gun_license':gun_license,
			'address':address,
			'work':job,
			'description':description,
			'med_diseases':med,
			'med_allergy':med_alerg,
			'med_drugs':med_drag,
			'med_contact':contact,
			'med_height':rost,
			'med_weight':mass,
			'owner':conn.fetch_rows('users', condition={'ip':request.remote_addr})[0]['name']
		}
		conn.insert('characters', data)
		return redirect('/civil')
		
	else:
		return redirect('/')
@app.route('/api/dbsearch', methods=[ 'POST'])
def dbsearch():
	test = request.form['name']
	print(test)
	
@app.route('/api/weapon/create', methods=['GET', 'POST'])
def create_weapon():
	if request.method == 'POST':
		modal = request.form.get('modal')
		char = request.form.get('char')
		print(modal, char)
		data ={
			'char_id':char,
			'model':modal
		}
	#	conn.insert('characters_weapons', data)
		return redirect('/civil')
	else:
		return redirect('/')
#main route		
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dashboard')
def dashboard():
	rows  = conn.fetch_rows('users', condition={'ip':request.remote_addr})

	for row in rows:
		if conn.fetch_rows('users', condition={'ip':request.remote_addr})[0]['auth'] == 1:
			return render_template('dashboard.html', users = conn.fetch_rows('users', condition={'ip':request.remote_addr}), 
			user=conn.fetch_rows('users'), settings=conn.fetch_rows('settings', 	condition = settings_cound), port=port, departament=departament)
		else:
			return render_template('ban.html')
	if TypeError:
		return 'Ваш айпи не в вайт листе консоли'



@app.route('/profile')
def profile():
	rows  = conn.fetch_rows('users', condition={'ip':request.remote_addr})
	for row in rows:
		if conn.fetch_rows('users', condition={'ip':request.remote_addr})[0]['auth']  == 1:
			user_cound = {'ip':request.remote_addr}
			return render_template('profile.html', users=conn.fetch_rows('users', 	condition=user_cound), settings=conn.fetch_rows('settings', 	condition = settings_cound))
		else:
			return render_template('ban.html')
	if TypeError:
		return 'Ваш айпи не в вайт листе консоли'
@app.route('/mdt')
def mdt():
	rows  = conn.fetch_rows('users', condition={'ip':request.remote_addr})
	for row in rows:
		if conn.fetch_rows('users', condition={'ip':request.remote_addr})[0]['auth']  == 1:
			user_cound = {'ip':request.remote_addr}
			return render_template('mdt.html', users=conn.fetch_rows('users', condition=user_cound), sit=conn.fetch_rows('situations'), settings=conn.fetch_rows('settings', 	condition = settings_cound), avail=avail, ituation_is_attached=ituation_is_attached, situations=situations, situation_is_attached=situation_is_attached, department_type=department_type)
		else:
			return render_template('ban.html')
	if TypeError:
		return 'Ваш айпи не в вайт листе консоли'
				
@app.route('/admin/dashboard')
def admin():
	rows  = conn.fetch_rows('users', condition={'ip':request.remote_addr})
	for row in rows:
		if conn.fetch_rows('users', condition={'ip':request.remote_addr})[0]['auth'] == 1:
			if conn.fetch_rows('users', condition={'ip':request.remote_addr})[0]['is_admin'] == 1:
				return render_template('admin.html', settings=conn.fetch_rows('settings', 	condition = settings_cound), users = conn.fetch_rows('users', condition={'ip':request.remote_addr}))
			else:
				return 'Вы не админ'
		else:
			return render_template('ban.html')
	if TypeError:
		return 'Ваш айпи не в вайт листе консоли'
		
	
@app.route('/civil')
def civil():
	rows  = conn.fetch_rows('users', condition={'ip':request.remote_addr})
	for row in rows:
			
		if row['auth'] == 1:
			user_cound = {'ip':request.remote_addr}
			return render_template('civil.html', settings=conn.fetch_rows('settings', 	condition = settings_cound), user=conn.fetch_rows('users', 	condition=user_cound), sex_types=sex_types, gun_license_types=gun_license_types, races=races, driving_license_types=driving_license_types, characters=conn.fetch_rows('characters'),characters_weapons=conn.fetch_rows('characters_weapons'))
		else:
			return render_template('ban.html')
	if TypeError:
		return 'Ваш айпи не в вайт листе консоли'	
		
@app.route('/cad')
def cad():
	rows  = conn.fetch_rows('users', condition={'ip':request.remote_addr})
	for row in rows:
			
		if row['auth'] == 1:
			user_cound = {'ip':request.remote_addr}
			return render_template('cad.html', users=conn.fetch_rows('users', 	condition=user_cound), settings=conn.fetch_rows('settings', 	condition = settings_cound), sit=conn.fetch_rows('situations'))
		else:
			return render_template('ban.html')
	if TypeError:
		return 'Ваш айпи не в вайт листе консоли'
		

if __name__ == '__main__':
	app.run(debug=True, port=port)