from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
from tkinter import messagebox
import base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import mimetypes
import pickle
import os
from apiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tkinter import font

root = Tk()
root.title("Vaccine Record System")
root.geometry("500x400")
root.config(bg="Lavender")
image1 = ImageTk.PhotoImage(Image.open("C:/Users/Irfan/Downloads/injection.png"))
root.iconphoto(False, image1)

title1 = Label(root, text = "       Vaccine Record System            ",font=("Georgia", 25,'bold'),bg="teal", fg="black" )
title1.grid(row=0, column=0, columnspan=4)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="lavender")
mylabel1.grid(row=1, column=0)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=2, column=0)

def patient_details_entry():
    new_window = Toplevel()
    new_window.geometry("600x600")
    new_window.config(bg="Lavender")
    new_window.title("Vaccine Record System")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/Irfan/Downloads/injection.png"))
    new_window.iconphoto(False, image1)

    title1 = Label(new_window, text = "           Vaccine Record System              ",font=("Georgia", 25,'bold'),bg="teal", fg="black")
    title1.grid(row=0, column=0, columnspan=4)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=1, column=0)

    patient_name_label = Label(new_window, text = "               Patient Entry Form          ", font=("Georgia", 20,'bold'),bg="Lavender", fg="black")
    patient_name_label.grid(row=2, column=0, columnspan=4)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=3, column=0)

    patient_name_label = Label(new_window, text = "Enter your name here:", font=("Georgia", 15),bg="Lavender", fg="black")
    patient_name_label.grid(row=5, column=0)

    name_entry = Entry(new_window, width= 20, bg = "white", fg = "black")
    name_entry.grid(row=5, column=1)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=6, column=0)

    patient_age_label = Label(new_window, text = "Enter your age here:", font=("Georgia", 15),bg="Lavender", fg="black")
    patient_age_label.grid(row=7, column=0)

    age_entry = Entry(new_window, width= 20, bg = "white", fg = "black")
    age_entry.grid(row=7, column=1)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=8, column=0)

    patient_weight_label = Label(new_window, text = "Enter your weight here(in Kg):", font=("Georgia", 15),bg="Lavender", fg="black")
    patient_weight_label.grid(row=9, column=0)

    weight_entry = Entry(new_window, width= 20, bg = "white", fg = "black")
    weight_entry.grid(row=9, column=1)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=10, column=0)

    patient_no_of_vaccine_label = Label(new_window, text = "Enter name of vaccine", font=("Georgia", 15),bg="Lavender", fg="black")
    patient_no_of_vaccine_label.grid(row=11, column=0)

    name_of_vaccine_entry = Entry(new_window, width= 20, bg = "white", fg = "black")
    name_of_vaccine_entry.grid(row=11, column=1)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=12, column=0)

    patient_date_taken_label = Label(new_window, text = "Enter vaccine date taken", font=("Georgia", 15),bg="Lavender", fg="black")
    patient_date_taken_label.grid(row=13, column=0)

    date_taken_entry = DateEntry(new_window,selectmode='day')
    date_taken_entry.grid(row=13, column=1)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=14, column=0)

    patient_date_due_label = Label(new_window, text = "Enter vaccine Date due", font=("Georgia", 15),bg="Lavender", fg="black")
    patient_date_due_label.grid(row=15, column=0)

    date_due_entry = DateEntry(new_window,selectmode='day')
    date_due_entry.grid(row=15, column=1)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=16, column=0)

    patient_date_due_label = Label(new_window, text = "Enter your email ID", font=("Georgia", 15),bg="Lavender", fg="black")
    patient_date_due_label.grid(row=17, column=0)

    email_entry = Entry(new_window, width= 20, bg = "white", fg = "black")
    email_entry.grid(row=17, column=1)

    mylabel1 = Label(new_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=18, column=0)

    back_button = Button(new_window, text="Go Back" ,font=('georgia',10,'bold'), command=new_window.destroy, border=3 , bg= "teal",fg="black" )
    back_button.grid(row=19, column=0)

    def saveit():
        if age_entry.get().isdigit() != True:
            warning_message = messagebox.showwarning("Warning", "Age should only be numbers only")
        
        if weight_entry.get().isdigit() != True:
            warning_message = messagebox.showwarning("Warning", "Weight should only be numbers only")

        if age_entry.get().isdigit() == True and weight_entry.get().isdigit() == True :
            record_list = [name_entry.get(), int(age_entry.get()), int(weight_entry.get()), name_of_vaccine_entry.get(), date_taken_entry.get_date(), date_due_entry.get_date(), email_entry.get()]
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="irfan",
            database="vaccine_record"
            )

            mycursor = mydb.cursor()

            sql_command = "INSERT INTO patients_record (name, age, weight, name_of_vaccine, date_taken, date_due, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            sql_value = (record_list[0], record_list[1], record_list[2], record_list[3], record_list[4], record_list[5],  record_list[6])
            mycursor.execute(sql_command, sql_value)

            mydb.commit()

            
            # If modifying these scopes, delete the file token.pickle.
            SCOPES = ['https://mail.google.com/']


            def get_service():
                creds = None
                # The file token.pickle stores the user's access and refresh tokens, and is
                # created automatically when the authorization flow completes for the first
                # time.
                if os.path.exists('token.pickle'):
                    with open('token.pickle', 'rb') as token:
                        creds = pickle.load(token)
                # If there are no (valid) credentials available, let the user log in.
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            'credentials.json', SCOPES)
                        creds = flow.run_local_server(port=0)
                    # Save the credentials for the next run
                    with open('token.pickle', 'wb') as token:
                        pickle.dump(creds, token)

                service = build('gmail', 'v1', credentials=creds)

                return service

            def send_message(service, user_id, message):
                try:
                    message = service.users().messages().send(userId=user_id,
                            body=message).execute()

                    print('Message Id: {}'.format(message['id']))

                    return message
                except Exception as e:
                    print('An error occurred: {}'.format(e))
                    return None


            def create_message_with_attachment(
                sender,
                to,
                subject,
                message_text,
                file,
                ):
                message = MIMEMultipart()
                message['to'] = to
                message['from'] = sender
                message['subject'] = subject

                msg = MIMEText(message_text)
                message.attach(msg)

                (content_type, encoding) = mimetypes.guess_type(file)

                if content_type is None or encoding is not None:
                    content_type = 'application/octet-stream'

                (main_type, sub_type) = content_type.split('/', 1)

                if main_type == 'text':
                    with open(file, 'rb') as f:
                        msg = MIMEText(f.read().decode('utf-8'), _subtype=sub_type)

                elif main_type == 'image':
                    with open(file, 'rb') as f:
                        msg = MIMEImage(f.read(), _subtype=sub_type)
                    
                elif main_type == 'audio':
                    with open(file, 'rb') as f:
                        msg = MIMEAudio(f.read(), _subtype=sub_type)
                    
                else:
                    with open(file, 'rb') as f:
                        msg = MIMEBase(main_type, sub_type)
                        msg.set_payload(f.read())

                filename = os.path.basename(file)
                msg.add_header('Content-Disposition', 'attachment',
                            filename=filename)
                message.attach(msg)

                raw_message = \
                    base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
                return {'raw': raw_message.decode('utf-8')}
            

            if __name__ == "__main__":
                service = get_service()
                user_id = 'me'
                msg = create_message_with_attachment('globaldeveloperconsortium@gmail.com', 
                email_entry.get(), 
                'Your Vaccine INFO ' + name_entry.get(),
                'Congratulation on getting your first dose of ' + name_of_vaccine_entry.get()+ " on "+str(date_due_entry.get_date()) +" take your second dose latest by "+ str(date_taken_entry.get_date()),
                "./sample_file.txt")
                send_message(service, user_id, msg)
            
            new_window.destroy()

    save_button =  Button(new_window, text="Save" ,font=('georgia',10,'bold'), command=saveit,border=3,bg="teal",fg="black")
    save_button.grid(row=19, column=1)

patient_details_entry_button = Button(root, text="Patient Entry",font=('georgia',10,'bold'), command=patient_details_entry, border="3",bg="teal", fg="black")
patient_details_entry_button.grid(row=2, column=1)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=3, column=0)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=4, column=0)

def delete_entry():
    global patient_name_entry_box
    delete_window = Toplevel()
    delete_window.geometry("700x550")
    delete_window.config(bg="Lavender")
    delete_window.title("Vaccine Record System")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/Irfan/Downloads/injection.png"))
    delete_window.iconphoto(False, image1)

    title1 = Label(delete_window, text = "               Vaccine Record System                ",font=("Georgia", 25,'bold'),bg="teal", fg="black")
    title1.grid(row=0, column=0, columnspan=8)

    title1 = Label(delete_window, text = "        Enter the name of patient",font=("Georgia", 15),bg="Lavender", fg="black")
    title1.grid(row=2, column=0)

    patient_name_entry = Entry(delete_window, width= 20, bg = "white", fg = "black")
    patient_name_entry.grid(row=2, column=1)
    title1 = Label(delete_window, text = "Name",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=5, column=0)
    title1 = Label(delete_window, text = "Age",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=5, column=1)
    title1 = Label(delete_window, text = "Weight",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=5, column=2)
    title1 = Label(delete_window, text = "Name of vaccine",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=5, column=3)
    title1 = Label(delete_window, text = "Date taken",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=5, column=4)
    title1 = Label(delete_window, text = "Date due",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=5, column=5)
    title1 = Label(delete_window, text = "Email ID",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=5, column=6)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="irfan",
    database="vaccine_record"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM patients_record order by name")

    i=0 
    for patients_record in mycursor: 
        for j in range(len(patients_record)):
            e = Entry(delete_window, width=10, fg='black', bg="Lavender", font=("Georgia", 15))
            e.grid(row=i + 30, column=j) 
            e.insert(END, patients_record[j])
        i=i+1
    exit_button = Button(delete_window, text="Back", font=('georgia',10,'bold'), command=delete_window.destroy, border=3, bg='teal', fg="black")
    exit_button.grid(row=4, column=2)
    def pop_up_response():
        response= messagebox.askyesno("Delete Window", "Are you sure you want to delete")
        if response == 1:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="irfan",
            database="vaccine_record"
            )

            mycursor = mydb.cursor()
            sql_command = "DELETE FROM patients_record WHERE name = %s"
            sql_value = [patient_name_entry.get()]
            mycursor.execute(sql_command, sql_value)

            mydb.commit()

            delete_window.destroy()

    mylabel1 = Label(delete_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=3, column=0)

    delete_button = Button(delete_window, text="Delete", font=('georgia',10,'bold'), command=pop_up_response, border="3",bg="teal", fg="black")
    delete_button.grid(row=4, column=1)

def sort_entry_on_date():
    sort_window = Toplevel()
    sort_window.geometry("700x550")
    sort_window.config(bg="Lavender")
    sort_window.title("Vaccine Record System")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/Irfan/Downloads/injection.png"))
    sort_window.iconphoto(False, image1)
    title1 = Label(sort_window, text = "Name",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=0)
    title1 = Label(sort_window, text = "Age",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=1)
    title1 = Label(sort_window, text = "Weight",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=2)
    title1 = Label(sort_window, text = "Name of vaccine",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=3)
    title1 = Label(sort_window, text = "Date taken",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=4)
    title1 = Label(sort_window, text = "Date due",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=5)
    title1 = Label(sort_window, text = "Email ID",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=6)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="irfan",
    database="vaccine_record"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM patients_record order by date_due")

    title1 = Label(sort_window, text = "                    Vaccine Record System                       ",font=("Georgia", 25,'bold'),bg="teal", fg="black")
    title1.grid(row=0, column=0, columnspan=8)


    i=0 
    for patients_record in mycursor: 
        for j in range(len(patients_record)):
            e = Entry(sort_window, width=10, fg='black', bg="Lavender", font=("Georgia", 15))
            e.grid(row=i+5, column=j) 
            e.insert(END, patients_record[j])
        i=i+1

    back_button = Button(sort_window, text="Back" ,font=('Georgia',10,'bold'), command=sort_window.destroy, border=3, bg='teal' , fg='black')
    back_button.grid(row= i + 10, column= 0)

patient_details_entry_button = Button(root, text="Sort entries based on Date due", font=('georgia',10,'bold'),command=sort_entry_on_date, border="3",bg="teal", fg="black")
patient_details_entry_button.grid(row=4, column=1)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=5, column=0)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=6, column=0)

def sort_entry_on_age():
    age_window = Toplevel()
    age_window.geometry("700x550")
    age_window.config(bg="Lavender")
    age_window.title("Vaccine Record System")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/Irfan/Downloads/injection.png"))
    age_window.iconphoto(False, image1)
    title1 = Label(age_window, text = "Name",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=0)
    title1 = Label(age_window, text = "Age",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=1)
    title1 = Label(age_window, text = "Weight",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=2)
    title1 = Label(age_window, text = "Name of vaccine",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=3)
    title1 = Label(age_window, text = "Date taken",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=4)
    title1 = Label(age_window, text = "Date due",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=5)
    title1 = Label(age_window, text = "Email ID",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=6)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="irfan",
    database="vaccine_record"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM patients_record order by age")
    title1 = Label(age_window, text = "                    Vaccine Record System                       ",font=("Georgia", 25,'bold'),bg="teal", fg="black")
    title1.grid(row=0, column=0, columnspan=8)
    i=0 
    for patients_record in mycursor: 
        for j in range(len(patients_record)):
            e = Entry(age_window, width=10, fg='black', bg="Lavender", font=("Georgia", 15))
            e.grid(row=i+5, column=j) 
            e.insert(END, patients_record[j])
        i=i+1

    back_button = Button(age_window, text="Back",font=('georgia',10,'bold') ,command=age_window.destroy, border="3",bg="teal", fg="black")
    back_button.grid(row= i + 10, column= 0)

patient_details_entry_button = Button(root, text="Sort entries based on age",font=('georgia',10,'bold'), command=sort_entry_on_age ,border="3",bg="teal", fg="black")
patient_details_entry_button.grid(row=6, column=1)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=5, column=0)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=6, column=0)

def sort_entry_on_name():
    name_window = Toplevel()
    name_window.geometry("700x550")
    name_window.config(bg="Lavender")
    name_window.title("Vaccine Record System")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/Irfan/Downloads/injection.png"))
    name_window.iconphoto(False, image1)
    title1 = Label(name_window, text = "Name",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=0)
    title1 = Label(name_window, text = "Age",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=1)
    title1 = Label(name_window, text = "Weight",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=2)
    title1 = Label(name_window, text = "Name of vaccine",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=3)
    title1 = Label(name_window, text = "Date taken",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=4)
    title1 = Label(name_window, text = "Date due",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=5)
    title1 = Label(name_window, text = "Email ID",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
    title1.grid(row=1, column=6)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="irfan",
    database="vaccine_record"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM patients_record order by name")

    title1 = Label(name_window, text = "                    Vaccine Record System                  ",font=("Georgia", 25,'bold'),bg="teal", fg="black")
    title1.grid(row=0, column=0, columnspan=8)

    i=4
    for patients_record in mycursor: 
        for j in range(len(patients_record)):
            e = Entry(name_window, width=10, fg='black', bg="Lavender", font=("Georgia", 15))
            e.grid(row=i, column=j) 
            e.insert(END, patients_record[j])
        i=i+1

    back_button = Button(name_window, text="Back", font=('georgia',10,'bold'), command=name_window.destroy,border=3,bg='teal',fg='black')
    back_button.grid(row= i + 10, column= 0)


patient_details_entry_button = Button(root, text="Sort entries based on Name",font=('georgia',10,'bold'), command=sort_entry_on_name, border="3",bg="teal", fg="black")
patient_details_entry_button.grid(row=8, column=1)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=7, column=0)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=8, column=0)

patient_details_entry_button = Button(root, text="Delete Entry",font=('georgia',10,'bold'), command=delete_entry ,border="3",bg="teal", fg="black")
patient_details_entry_button.grid(row=10, column=1)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=9, column=0)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=10, column=0)

def search():
    search_window = Toplevel()
    search_window.geometry("1100x400")
    search_window.config(bg="Lavender")
    search_window.title("Vaccine Record System")

    image1 = ImageTk.PhotoImage(Image.open("C:/Users/Irfan/Downloads/injection.png"))
    search_window.iconphoto(False, image1)

    title1 = Label(search_window, text = "        Vaccine Record System"         ,font=("Georgia", 25,'bold'),bg="teal", fg="black")
    title1.grid(row=0, column=0, columnspan=8)


    mylabel1 = Label(search_window, text = "Enter the name of the patient: ",font=("Georgia", 15),bg="Lavender", fg="black")
    mylabel1.grid(row=1, column=0)

    patient_name_entry = Entry(search_window, width=10, fg='black', bg="white", font=("Georgia", 15))
    patient_name_entry.grid(row=1, column=2) 

    mylabel1 = Label(search_window, text = "        ",font=("Georgia", 15),bg="Lavender")
    mylabel1.grid(row=2, column=0)

    def search_name():
        title1 = Label(search_window, text = "Name",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
        title1.grid(row=3, column=0)
        title1 = Label(search_window, text = "Age",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
        title1.grid(row=3, column=1)
        title1 = Label(search_window, text = "Weight",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
        title1.grid(row=3, column=2)
        title1 = Label(search_window, text = "Name of vaccine",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
        title1.grid(row=3, column=3)
        title1 = Label(search_window, text = "Date taken",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
        title1.grid(row=3, column=4)
        title1 = Label(search_window, text = "Date due",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
        title1.grid(row=3, column=5)
        title1 = Label(search_window, text = "Email ID",font=("Georgia", 15,'bold'),bg="Lavender", fg="black")
        title1.grid(row=3, column=6)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irfan",
        database="vaccine_record"
        )

        mycursor = mydb.cursor()
        sql_command="SELECT * FROM patients_record where name = %s"
        sql_value = [patient_name_entry.get()]
        mycursor.execute(sql_command, sql_value)

        i = 0
        test = ''

        for patients_record in mycursor: 
            for j in range(len(patients_record)):
                e = Entry(search_window, width=10, fg='black', bg="Lavender", font=("Georgia", 15))
                e.grid(row=i + 30, column=j) 
                e.insert(END, patients_record[j])
            i=i+1
            test = patients_record[0]    
        
        if test != patient_name_entry.get():
            response = messagebox.showwarning("Warning", "Patient is not present in the database")

    searchbutton = Button(search_window, text="Search", font=('georgia',10,'bold'), command=search_name, border=3,bg="teal", fg="black")
    searchbutton.grid(row=2, column=0)
    
    def destroy():
        search_window.destroy()

    exit_button = Button(search_window, text="Back", font=('georgia',10,'bold'), command=destroy, border=3, bg='teal', fg="black")
    exit_button.grid(row=2, column=2)


patient_details_entry_button = Button(root, text="Search", font=('georgia',10,'bold'),command=search, border="3" ,bg="teal", fg="black")
patient_details_entry_button.grid(row=12, column=1)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=11, column=0)

mylabel1 = Label(root, text = "        ",font=("Georgia", 15),bg="Lavender")
mylabel1.grid(row=12, column=0)

patient_details_entry_button = Button(root, text="Exit", font=('georgia',10,'bold'), command=root.destroy, border="3",bg="teal", fg="black")
patient_details_entry_button.grid(row=16, column=1)

root.mainloop()