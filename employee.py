from tkinter import*
from tkinter import ttk
import mysql.connector # type: ignore
from tkinter import messagebox
class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")



        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_country=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_salary=StringVar()

        
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        

        #Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=60,width=1530,height=700)

         #upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',28,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1510,height=350)

        #Label and Entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('arial',15),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)


        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',15),width=22,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        lbl_Name=Label(upper_frame,text='Name',font=('arial',15),bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=24,font=('arial',15))
        txt_name.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        lbl_desig=Label(upper_frame,text='Designation',font=('arial',15),bg='white')
        lbl_desig.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_desig=ttk.Entry(upper_frame,textvariable=self.var_designation,width=24,font=('arial',15))
        txt_desig.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        
        lbl_email=Label(upper_frame,text='Email',font=('arial',15),bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=24,font=('arial',15))
        txt_email.grid(row=1,column=3,padx=2,pady=7,sticky=W)


        lbl_address=Label(upper_frame,text='Address',font=('arial',15),bg='white')
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=24,font=('arial',15))
        txt_address.grid(row=2,column=1,padx=2,pady=7,sticky=W)
  
        
        lbl_dob=Label(upper_frame,text='Date of Birth',font=('arial',15),bg='white')
        lbl_dob.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=24,font=('arial',15))
        txt_dob.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        lbl_doj=Label(upper_frame,text='Date of Joining',font=('arial',15),bg='white')
        lbl_doj.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=24,font=('arial',15))
        txt_doj.grid(row=3,column=1,padx=2,pady=7,sticky=W)
        
        lbl_country=Label(upper_frame,text='Country',font=('arial',15),bg='white')
        lbl_country.grid(row=5,column=0,padx=2,pady=7,sticky=W)
        
        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=24,font=('arial',15))
        txt_country.grid(row=5,column=1,padx=2,pady=7,sticky=W)


        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",font=('arial',15),width=24)
        com_txt_proof['value']=('Select Id Proof','Adhaar Card','Pan Card','Voter Id','Driving License')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=3,column=2,padx=2,pady=10,sticky=W)
        
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=24,font=('arial',15))
        txt_proof.grid(row=3,column=3,padx=2,pady=7,sticky=W)
        
        lbl_gender=Label(upper_frame,text='Gender',font=('arial',15),bg='white')
        lbl_gender.grid(row=4,column=0,padx=2,pady=7,sticky=W)
         
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=('arial',15),width=22)
        com_txt_gender['value']=('Male','Female','Not applicable')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=1,padx=2,pady=10,sticky=W)
        

        lbl_phone=Label(upper_frame,text='Phone number',font=('arial',15),bg='white')
        lbl_phone.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=24,font=('arial',15))
        txt_phone.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        lbl_ctc=Label(upper_frame,text='Salary(CTC)',font=('arial',15),bg='white')
        lbl_ctc.grid(row=5,column=2,padx=2,pady=7,sticky=W)
        
        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=24,font=('arial',15))
        txt_ctc.grid(row=5,column=3,padx=2,pady=7,sticky=W)


        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1010,y=0,width=300,height=270)
        

        btn_add=Button(button_frame,text="Save",command=self.add_data,font=('arial',15,'bold'),width=22,bg='skyblue',fg='white')
        btn_add.grid(row=0,column=0,padx=7,pady=7)
        
        btn_update=Button(button_frame,text="Update",command=self.update_data,font=('arial',15,'bold'),width=22,bg='skyblue',fg='white')
        btn_update.grid(row=1,column=0,padx=7,pady=7)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=('arial',15,'bold'),width=22,bg='skyblue',fg='white')
        btn_delete.grid(row=2,column=0,padx=7,pady=7)

        btn_clear=Button(button_frame,text="Clear",command=self.clear_fields,font=('arial',15,'bold'),width=22,bg='skyblue',fg='white')
        btn_clear.grid(row=3,column=0,padx=7,pady=7)

         #downFrame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Lists',font=('times new roman',28,'bold'),fg='red')
        down_frame.place(x=10,y=360,width=1510,height=350)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search',font=('times new roman',15,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1500,height=70)
         
        search_by=Label(search_frame,bg='skyblue',text='Search By',font=('arial',12,'bold'),fg='white')
        search_by.grid(row=0,column=0,padx=5,sticky=W)


        self.com_txt_search=ttk.Combobox(search_frame,state='readonly',font=('arial',12),width=18)
        self.com_txt_search['value']=("Select Option","phone","id_proof")
        self.com_txt_search.current(0)
        self.com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        

        self.txt_search=ttk.Entry(search_frame,width=22,font=('arial',12))
        self.txt_search.grid(row=0,column=2,sticky=W,padx=5)
        
        btn_search=Button(search_frame,text="Search",command=self.search_data,width=22,font=('arial',12))
        btn_search.grid(row=0,column=3,sticky=W,padx=5)


        btn_showall=Button(search_frame,text="Show All",width=22,font=('arial',12))
        btn_showall.grid(row=0,column=4,sticky=W,padx=5)


        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=70,width=1500,height=200)
        

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','desig','email','address','dob','doj','country','id_proofcomb','id_proof','gender','phone','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('dob',text='Date of Birth')
        self.employee_table.heading('doj',text='Date of Joining')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('id_proofcomb',text='ID type')
        self.employee_table.heading('id_proof',text='ID number')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone number')
        self.employee_table.heading('salary',text='Salary')
        
        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("desig",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("id_proofcomb",width=100)
        self.employee_table.column("id_proof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("salary",width=100)



        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    
    #function declarations
    #SAVE function
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn = mysql.connector.connect(
                host="localhost",   # Change if your MySQL server is on a different host
                user="root",        # Your MySQL username
                password=" ",  # Your MySQL password
               database=" "  # The database you want to connect to
            )
                
                # Create a cursor object to interact with the database
                my_cursor = conn.cursor()

                my_cursor.execute('insert into employee values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                  self.var_dep.get(),
                  self.var_name.get(),
                  self.var_designation.get(),
                  self.var_email.get(),
                  self.var_address.get(),
                  self.var_dob.get(),
                  self.var_doj.get(),
                  self.var_country.get(),
                  self.var_idproofcomb.get(),
                  self.var_idproof.get(),
                  self.var_gender.get(),
                  self.var_phone.get(),
                  self.var_salary.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added',parent=self.root)
            except Exception as es:
              messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="your pssword",database="your databse")
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("","end",values=i)
            conn.commit()
        conn.close()

    #get-cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_dob.set(data[5])
        self.var_doj.set(data[6])
        self.var_country.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_salary.set(data[12])
    
    #update
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure you want to update this employee data')
                if update>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="your password",database="your database")
                           my_cursor=conn.cursor()
                           my_cursor.execute("Update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,DOB=%s,DOJ=%s,Country=%s,id_proof_type=%s,Gender=%s,Phone=%s,Salary=%s where id_number=%s",(
                                self.var_dep.get(),
                                self.var_name.get(),
                                self.var_designation.get(),
                                self.var_email.get(),
                                self.var_address.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_country.get(),
                                self.var_idproofcomb.get(),
                                self.var_gender.get(),
                                self.var_phone.get(),
                                self.var_salary.get(),
                                self.var_idproof.get()
                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee Successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    def delete_data(self):
        if self.var_idproof.get() == "":
             messagebox.showerror("Error", "ID Proof is required for deletion")
        else:
            try:
               delete = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")
               if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="your password", database="your database")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM employee WHERE id_number = %s", (self.var_idproof.get(),))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Employee record has been deleted")
            except Exception as es:
                 messagebox.showerror("Error", f"Due to: {str(es)}")

    def clear_fields(self):
        self.var_dep.set("")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_country.set("")
        self.var_idproofcomb.set("")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_salary.set("")


    def search_data(self):
        search_by =self.com_txt_search.get()  # Get selected option
        search_value =self.txt_search.get()  # Get user input
    
        if search_by == "Select Option" or search_value == "":
            messagebox.showerror("Error", "Please select a search criteria and enter a value", parent=self.root)
        else:
           try:
               conn = mysql.connector.connect(host="localhost", username="root", password="your password", database="your database")
               my_cursor = conn.cursor()
            
            # Mapping search_by values to actual column names in the database
               column_map = {
                "phone": "Phone",
                "id_proof": "id_number"
             }
            
               if search_by in column_map:
                 query = f"SELECT * FROM employee WHERE {column_map[search_by]} LIKE %s"
                 my_cursor.execute(query, (f"%{search_value}%",))
                 data = my_cursor.fetchall()
                
                 if len(data) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in data:
                        self.employee_table.insert("", "end", values=i)
                 else:
                    messagebox.showinfo("Info", "No matching records found", parent=self.root)
                
                 conn.commit()
               else:
                messagebox.showerror("Error", "Invalid search option", parent=self.root)
            
               conn.close()
           except Exception as es:
               messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
    