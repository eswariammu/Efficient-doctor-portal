from connection import *

	
def patReg(name,mobno,email,address):
	mycursor = conn.cursor()
	sql = "INSERT INTO userreg (name,mobno,email,address) VALUES (%s, %s, %s, %s)"
	val = (name,mobno,email,address)
	mycursor.execute(sql, val)
	conn.commit()
	loginSave(email,email,"user","active")

def loginSave(email,password,role,status):
	mycursor = conn.cursor()
	sql = "INSERT INTO login (username,passwrd,role,status) VALUES (%s, %s, %s, %s)"
	val = (email,password,role,status)
	mycursor.execute(sql, val)
	conn.commit()

def getLogin(username,passwrd):
	mycursor = conn.cursor()
	query="SELECT * FROM login where username='"+username+"'  and passwrd='"+passwrd+"' "
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	#print("-------------------------"+myresult[0])
	#for x in myresult:
	#	print(x)  
	return myresult
	
def addAppt(category, date, time, username):
		mycursor = conn.cursor()
		query = "insert into booking (category, date, time, username) values ('"+category+"','"+date+"','"+time+"','"+username+"')"
		mycursor.execute(query)
		conn.commit()

def cancelAppt(bid):
	print("-----------------------------------------------------------------------")	
	mycursor = conn.cursor()
	query = "delete from booking where id='"+bid+"'"
	mycursor.execute(query)
	conn.commit()
	
def orgDr(username,name, mob, blood, organ):
	mycursor = conn.cursor()
	query = "insert into organDoner (username, name, mobno, bloodgrp, organ) values ('"+username+"','"+name+"','"+mob+"','"+blood+"','"+organ+"')"
	mycursor.execute(query)
	conn.commit()
	
def srchDnr(organ):
	mycursor = conn.cursor()
	print("-------------------------organ--------"+organ)
	query = "select * from organDoner where organ='"+organ+"'"
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)  
	
	return myresult
	
	
def feedBck(email,name,feed):
	mycursor = conn.cursor()
	query = "insert into feedBack (name, email, feed) values ('"+name+"','"'email'"','"+feed+"') "
	myresult=mycursor.execute(query)
	conn.commit()

def addDoctor(name,mob,email,address,specialist):
	mycursor = conn.cursor()
	query = "insert into addDoctor (docname, mobno, address, email, category) values ('"+name+"','"+mob+"','"+email+"', '"+address+"','"+specialist+"')"
	myresult=mycursor.execute(query)
	conn.commit()
	
	
	
