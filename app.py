import os
import re
import shutil
import csv
import sys
import pyodbc
from io import BytesIO
# from turtle import title, width
from flask import Flask,render_template, url_for, flash, redirect, request
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
# from wtforms import StringField, IntegerField, SubmitField, SelectField
# from wtforms.validators import DataRequired
from PIL import Image

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = '0626fuyi'
server = 'notminusone.database.windows.net'
database = 'notminusoneDatabase'
username = 'not-1'
password = '0626Fuyi' 
driver= '{ODBC Driver 17 for SQL Server}'
# 
# ROUTES!


@app.route('/')
def part10():
	# cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
	# cursor = cnxn.cursor()
	# cnxn.excute("select count(*) from [dbo].[nquakes2]")
	# row = cursor.fetchval()
	# cnxn.excute("select id,place from [dbo].[nquakes2] where mag=(select max(mag) from [dbo].[nquakes2])")
	# row1 = cursor.fetchval()
	# cnxn.excute("select id,place from [dbo].[nquakes2] where mag=(select min(mag) from [dbo].[nquakes2])")
	# row2 = cursor.fetchval()
	# return render_template('part10.html',sum=row,part10_active="active",title="Part 10",max={
	# 	'id':row1[0],
	# 	'location':row1[1]
	# },min={
	# 	'id':row2[0],
	# 	'location':row2[1]
	# })
	return render_template('part10.html',part10_active = "active",title="Part 10")

@app.route('/part11',methods=['GET','POST'])
def part11():
	if request.method=='GET':
		return render_template('part11.html',part11_active = "active",title="Part 11")
	if request.method=='POST':
		low = request.form["low"]
		high = request.form["high"]
		N = request.form["N"]
		cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
		cursor = cnxn.cursor()
		data = []
		step = (high-low)/N
		for i in range(N):
			cursor.execute("select count(*) from nquakes2 where mag>?",low+step*i,"and mag<?",low+step*(i+1))
			num = cursor.fetchval()
			cursor.execute("select max(mag) from nquakes2 where mag>?",low+step*i,"and mag<?",low+step*(i+1))
			max = cursor.fetchval()
			cursor.execute("select time,place from nquakes2 where mag=?",max)
			row = cursor.fetchone()
			data.append({
				"num":num,
				"time":row[0],
				"place":row[1]
			})
		if len(data) != 0:
			return render_template('part11.html',part11_active = "active",title="Part 11",data=data)
		else:
			return render_template('part11.html',part11_active = "active",title="Part 11")

@app.route('/part12',methods=['GET','POST'])
def part12():
	if request.method=='GET':
		return render_template('part12.html',part12_active = "active",title="Part 12")
	if request.method=='POST':
		latitude = request.form["latitude"]
		longitude = request.form["longitude"]
		cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
		cursor = cnxn.cursor()
		# cursor.execute("select id,latitude,longitude,net,place from nquakes2 where latitude=?",latitude," and longitude=?",longitude)
		cursor.execute("select id,latitude,longitude,net,place from nquakes2 where latitude=35.051 and longitude=-117.6728333")
		row = cursor.fetchall()
		if row is not None:
			return render_template('part12.html',part12_active = "active",data =row)
		else:
			return render_template('part12.html',part12_active = "active",title="Part 12")

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')


if __name__ == '__main__':
	app.run()