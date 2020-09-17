
from flask import Flask,request,url_for,redirect,flash,session
from flask import render_template
import json 
from service import *
from flask import *  

app = Flask(__name__)
app.secret_key = "abc"  

@app.route("/")
def index():
	return render_template("home.html") 

@app.route("/home.html")
def homePage():
	return render_template("home.html") 

@app.route("/AboutContact.html")
def aboutPage():
	return render_template("AboutContact.html") 

@app.route("/user.html")
def userPage():
	return render_template("user.html") 

@app.route("/Admin.html")
def adminLogin():
	return render_template("Admin.html") 

@app.route("/doctor.html")
def doctorLogin():
	return render_template("doctor.html") 

@app.route("/userHome.html")
def userHom():
	return render_template("userHome.html")

@app.route("/search doner.html")
def searchDonor():
	return render_template("search doner.html")

@app.route("/newBooking.html")
def newBooking():
	return render_template("newBooking.html")

@app.route("/feed.html")
def feedBack():
	return render_template("feed.html")

@app.route("/feedtable.html")
def feedTable():
	return render_template("feedtable.html")

@app.route("/searchDonar.html")
def searchDonar():
	return render_template("searchDonar.html")

@app.route("/appointmentCancel.html")
def cancelBooking():
	return render_template("appointmentCancel.html")

@app.route("/organ.html")
def organ():
	return render_template("organ.html")

@app.route("/feed.html")
def feed():
	return render_template("feed.html")

@app.route("/register.html")
def registerHtml():
	return render_template("register.html") 


@app.route("/admin.html")
def admin():
	return render_template("admin.html") 



@app.route("/Add_doctor.html")
def addDocter():
	return render_template("/Add_doctor.html")
	
	
@app.route("/adminlogin.html")
def adminHome():
	return render_template("adminlogin.html") 
	
@app.route("/logout")
def logout():
	return redirect("/") 


@app.route("/addUser",methods=['POST','GET'])
def patRegister():
	if request.method == "POST":				
		name=request.form['name']
		mobno=request.form['mobno']
		email=request.form['email']
		address=request.form['address']
		patReg(name,mobno,email,address)
		return redirect("/")

@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == "POST":
		username=request.form['Username']
		passwrd=request.form['password']
		if username =="admin@gmail.com":
			if passwrd=="admin":
				session["user_id"]="admin@gmail.com"
				session["username"]="admin@gmail.com"
				session["role"]="admin"
				return redirect("/adminlogin.html")
				
		result=getLogin(username,passwrd)
		if(len(result)>0):			
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
				print("------------------------role-------"+x[2])
				if(x[4]=="admin"):
					return redirect("/Admin.html")					
			return redirect("/userHome.html")
		
		return render_template("user.html",status="username or password is wrong")
	

@app.route("/appBooking",methods=['POST','GET'])
def appBooking():
	print(request.method)
	if request.method == "POST":
		if 'username' in session:
			username = session['username']
			category = request.form['category']
			date = request.form['date']
			time = request.form['time']
			addApp = addAppt(category, date, time, username)
			return redirect("/newBooking.html")
		return render_template("userHome.html")
	

@app.route("/removeBooking", methods=['POST','GET'])
def cancelUserBooking():
	if request.method == "POST":
		if 'username' in session:
			bid = request.form['BookingId']
			cancalApp = cancelAppt(bid)
			return redirect("/appointmentCancel.html")
		return render_template("userHome.html")

@app.route("/organDoner", methods=['POST','GET'])
def organDoner():
	if request.method == "POST":
		if 'username' in session:
			username = session['username']
			name = request.form['name']
			mob = request.form['mobileno']
			blood = request.form['bloodgroup']
			organ = request.form['organ']
			organDr = orgDr(username,name, mob, blood, organ)
			return redirect("/organ.html")
		return render_template("userHome.html")

@app.route("/seacrhDonor", methods=['POST','GET'])
def seacrhDonor():
	if request.method == "POST":
		if 'username' in session:
			username = session['username']
			organ = request.form['organList']
			searchDnr = srchDnr(organ)
			print (searchDnr)
			return render_template("/donartable.html", data=searchDnr)
			
@app.route("/feedBack", methods=['POST','GET'])
def feedback():
	if request.method == "POST":
		if 'username' in session:
			email = session['username']
			name = request.form['name']
			feed = request.form['feed']
			feedBk = feedBck(email,name,feed)
			return redirect("/feed.html")
		return render_template("userHome.html")
			
@app.route("/addDoc", methods=['POST','GET'])
def addDoct():
	if request.method == "POST":
		if 'username' in session:
			name = request.form['name']
			mob = request.form['mobileno']
			email = request.form['email']
			address = request.form['Address']
			specialist = request.form['speciality']
			addDoc = addDoctor(name,mob,email,address,specialist)
			return redirect("/Add_doctor.html")
		return render_template("userHome.html")
			
			
			
			
if __name__=="__main__":
	app.run(debug=True)
