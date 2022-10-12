##############################################
#Delete contact master all records  
##############################################
def Delete_contacts():
  import psycopg2 
  try:
   conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
   cur=conn.cursor()
   delete_query=("Delete from contact_master")
   cur.execute(delete_query)
   conn.commit()
   print("=====================================================================================")
   print("All records have been deleted successfully from contact_master table")
   print("=====================================================================================")
   return 
  except Exception:
   print("=====================================================================================")
   print("Something went wrong, Plz try after sometime:- ")
   print("=====================================================================================")
  finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()  

##############################################
#Delete contact master one record  
##############################################
def Delete_one():
  import psycopg2 
  try:
   conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
   cur=conn.cursor()
   select_query=("select * from contact_master where contact_id = '{}' ;")
   select_value=(input("Enter the contact_id"))
   # insert_value=(id,fname,lname,emailid,phno)
   cur.execute(select_query.format(select_value))
   result=cur.fetchall()
   if result==[]:
      print("=====================================================================================")
      print(" The given contact_id desn't exist ")
      print("=====================================================================================")
      return 
   delete_query=("Delete from contact_master where contact_id = {} ")
   cur.execute(delete_query.format(select_value))
   conn.commit()
   print("=====================================================================================")
   print("The record has been deleted successfully for given contact_id  ", select_value)
   print("=====================================================================================")
   return 
  except Exception:
   print("=====================================================================================")
   print("Cant read records from dataBase, Plz try after sometime:- ")
   print("=====================================================================================")
  finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()  

##############################################
#Update contact master one record  
##############################################
def Update_one():
  import psycopg2 
  try:
   conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
   cur=conn.cursor()
   select_query=("select * from contact_master where contact_id = '{}' ;")
   select_value=(input("Enter the contact_id"))
   # insert_value=(id,fname,lname,emailid,phno)
   cur.execute(select_query.format(select_value))
   result=cur.fetchall()
   if result==[]:
      print("=====================================================================================")
      print(" The given contact_id doesn't exist ")
      print("=====================================================================================")
      return 
   print("=====================================================================================")   
   print("Enter a to update conatct_id")
   print("Enter b to update First Name")
   print("Enter c to update Last Name")
   print("Enter d to update email_ID")
   print("Enter e to update phone_number")
   upd=input("Which field would you like to update:-")
   match upd:
      case "a":
         print("=====================================================================================")
         print("Enter the new contact id for ", select_value)
         print("=====================================================================================")
         con=int(input())
         update_query=("update contact_master set contact_id={} where contact_id = {}")
         cur.execute(update_query.format(con,select_value))
         conn.commit()
          

      case "b":
         print("=====================================================================================")
         print("Enter the new First name for ", select_value)
         print("=====================================================================================")
         con=input()
         update_query=("update contact_master set first_name='{}' where contact_id = {}")
         cur.execute(update_query.format(con,select_value))
         conn.commit()
          

      case "c":
         print("=====================================================================================")
         print("Enter the new Last Name for ", select_value)
         print("=====================================================================================")
         con=input()
         update_query=("update contact_master set last_name='{}' where contact_id = {}")
         cur.execute(update_query.format(con,select_value))
         conn.commit()
         

      case "d":
         print("=====================================================================================")
         print("Enter the new email ID for ", select_value)
         print("=====================================================================================")
         con=input()
         update_query=("update contact_master set email_id='{}' where contact_id = {}")
         cur.execute(update_query.format(con,select_value))
         conn.commit()
                 
    
      case "e":
         print("=====================================================================================")
         print("Enter the new phone number for ", select_value)
         print("=====================================================================================")
         con=input()
         update_query=("update contact_master set phone_number='{}' where contact_id = {}")
         cur.execute(update_query.format(con,select_value))
         conn.commit()
   
   print("=====================================================================================")
   print("The record has been updated successfully for given contact_id  ", select_value)
   print("=====================================================================================")
   return 
  except Exception:
   print("=====================================================================================")
   print("Cant update record in dataBase, Plz try after sometime:- ")
   print("=====================================================================================")
  finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close() 

##############################################
#Read contact master one record  
##############################################
def Read_one():
  import psycopg2 
  try:
   conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
   cur=conn.cursor()
   select_query=("select * from contact_master where contact_id = '{}' ;")
   select_value=(input("Enter the contact_id"))
   # insert_value=(id,fname,lname,emailid,phno)
   cur.execute(select_query.format(select_value))
   result=cur.fetchall()
   if result==[]:
      print("=====================================================================================")
      print(" The given contact_id desn't exist ")
      print("=====================================================================================")
      return 
   print("=====================================================================================")
   print("           C O N T A C T   M A S T E R  D E T A I L S              ")
   print("=====================================================================================")
   print("{:<15} {:<15} {:<15} {:<20} {:<10}".format('Contact_Id','First_Name','Last_Name','Email','Phone_number'))
   for e in result:
    print("====================================================================================")  
    print("{:<15} {:<15} {:<15} {:<20} {:<10}".format(e[0],e[1],e[2],e[3],e[4]))
   print("=====================================================================================")
   return 
  except Exception:
   print("=====================================================================================")
   print("Cant read records from dataBase, Plz try after sometime:- ")
   print("=====================================================================================")
  finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()  

###############################################
# Add Contacts 
###############################################
def Add_contacts():
  id=input("Please share contact_id")
  fname=input("Please share First_name")
  lname=input("Please share last_Name")
  emailid=input("Please share email_ID")
  phno=input("Please share Phone_number")
  import psycopg2 
  try:
   conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
   cur=conn.cursor()
   insert_query=("insert into contact_master values (%s,%s,%s,%s,%s);")
   insert_value=(id,fname,lname,emailid,phno)
   cur.execute(insert_query,insert_value)
   conn.commit()
   print("=====================================================================================")
   print("Given details have been addedd to DataBase Successfully")
   print("=====================================================================================")
   return 
  except Exception:
   print("=====================================================================================")
   print("Given details couldn't be addedd to DataBase")
   print("=====================================================================================")
  finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()  

##############################################
#Read contact master 
##############################################
def Read_all():
  import psycopg2 
  try:
   conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
   cur=conn.cursor()
   select_query=("select * from contact_master;")
   # insert_value=(id,fname,lname,emailid,phno)
   cur.execute(select_query)
   result=cur.fetchall()
   print("=====================================================================================")
   print("           C O N T A C T   M A S T E R  D E T A I L S              ")
   print("=====================================================================================")
   print("{:<15} {:<15} {:<15} {:<20} {:<10}".format('Contact_Id','First_Name','Last_Name','Email','Phone_number'))
   for e in result:
    print("====================================================================================")  
    print("{:<15} {:<15} {:<15} {:<20} {:<10}".format(e[0],e[1],e[2],e[3],e[4]))
   print("=====================================================================================")
   return 
  except Exception:
   print("=====================================================================================")
   print("Cant read records from dataBase, Plz try after sometime:- ")
   print("=====================================================================================")
  finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()  

##############################################
#Create New User 
##############################################
def new_user():
 user=input("Please give a user name:- ")
 password=input("Please give a password for the new ID:- ")
 #database connectivity 
 import psycopg2 
 try:
  conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
  #creating cursor
  cur=conn.cursor()
  insert_query=("insert into user_master values (%s,%s);")
  insert_value=(user,password)
  cur.execute(insert_query,insert_value)
  conn.commit()
  print("=====================================================================================")
  print("User {} has been created Successfully:- ".format(user))
  print("=====================================================================================")
 except Exception:
   print("Error")
 finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()  
##############################################
# Validate User 
##############################################
def validate_user(userid):
 #database connectivity 
 import psycopg2 
 try:
  conn=psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="SomDB",
    user="postgres",
    password="db123"
  )
  #creating cursor
  cur=conn.cursor()
  cur.execute(("select * from user_master where user_id = '%s'")%userid)
  result=cur.fetchall()
  if result!=[]:
   t1=result[0]
   if userid!=t1[0]:
     print("Invalid User:- ")
     return "a"   
   cnt=3
   while cnt>=1:
    inp_pw=input("Please enter the password:- ")
    if inp_pw!=t1[1]:
      cnt-=1
      if cnt==0:
         print("You have tried invalid password for 3 times..logging out..try next time")         
         break
      pw=input("You have entered invalid Password:-, you have {} more chances left would you like to retry with the correct passowrd y/n:- ".format(cnt))
      if pw=="y":
         pass
      else:
        break    
    else:
     return "c" 
   return "b"  
  else:
   return "a" 
 except Exception as error:
    print(error)
 finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()    
############################################################ 
def main_menu():
 print("=====================================================================================")
 print("Welcome to the Phone_Menu")
 print("=====================================================================================")
 print(" ")
 print("Please Login with your userID and Password:-")
 print("=============================================")
 userid=input("Please enter your user ID:-")
 return userid 
############################################################
# Phone Menu
############################################################
def phone_menu():
 while True:
  print("a. Add contacts")
  print("b. Read all contacts")
  print("c. Read any specific contact")
  print("d. Update any specific contact")
  print("e. Delete any specific contact")
  print("f. Delete all contacts")
  print("=====================================================================================")
  opt=input("Please choose one from the above option:-")
  match opt: 
   case "a":
    Add_contacts()
   case "b":
    Read_all()
   case "c":
    Read_one()
   case "d":
    Update_one()
   case "e":
    Delete_one()
   case "f":
    Delete_contacts()
   case _:
    print("You didnt choose the right option")
  choice=input("Would you like to try once y/n:-")
  if choice=='y':
   pass 
  else:
   break 
 return choice 
############################################################ 
# Main Statements 
############################################################
while True:
 userid=main_menu() 
 wk_result=validate_user(userid)
 if wk_result=="c":
    print("=====================================================================================")
    print(userid , "Logged in successfully" )
    print("=====================================================================================")
    choice=phone_menu()
    if choice=="n":
      break  
 elif wk_result=="a":
    opt=input("User doesn't exist , do you want to get registered:- y/n:- ")
    if opt=="y":
        new_user()
    else:
        break  
 elif wk_result=="b":
    break  





