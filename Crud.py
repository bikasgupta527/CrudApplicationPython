# Importing mysql Module
import mysql.connector as sql

# Establish the connections
con = sql.connect(host='localhost',user='rootuser',password='vikas',database='PythonDB')

# Making Cursor Object
mycursor = con.cursor()


# Function Call
def Option():
    

    # Function for inserting the data
    def Insert():

        #Enter Roll Number
        r = int(input("Enter Roll Number :"))
        # Checking weather the value is integer or string
        if type(r) !=int:
            print("Please Enter Valid Roll Number :")
            Insert()
        # Enter Name
        n = input("Enter Name :")
        # Enter Marks
        m = int(input("Enter Marks :"))
	# Cheking weather the marks is integer or string
        if type(r) !=int:
            print("Please Enter Valid Marks")
            Insert()
        # Writing query variable
        query = "Insert into Student values(%s,%s,%s)"
        val = (r,n,m)
        # Executing query
        mycursor.execute(query,val)
        con.commit()
        # Giving option weather you want to insert again or not
        print("\n---------------------\nValue Inserted\n------------------------")
        print("Do You Want To Insert Again")
        ch = input("Enter 'Y' for Yest 'N' for No :-")
        ch = ch.lower()
        if ch=='y':
            Insert()
        else:
            print("\n---------\nOk You Are Done.....")
    
   
    # Function for Updating data
    def Update():
        # Choose weather you want to update Name or Marks
        print("\n--------\nWhat are u want to update :")
        up = int(input("\nEnter 1-Name 2-Marks :"))
        # If the input value is 1
        if up==1:
            # Asking for the roll to update
            r = int(input("Enter Roll -"))
            if type(r) !=int:
                print("Please Enter Valid Roll Number")
                Update()
            #Asking for the name to update
            n = input("Enter Name -")
            #Updating
            mycursor.execute('Update Student set name = %s Where roll=%s',(n,r))
        #If the input value is 2
        if up==2:
            #Asking for the roll to update
            r = int(input("Enter Roll -"))
            if type(r) !=int:
                print("Please Enter Valid Roll Number")
                Update()
            # Asking for the marks to update
            m = int(input("Enter Marks -"))
            if type(r) !=int:
                print("Please Enter Valid Marks")
                Update()
            # Updating marks
            mycursor.execute('Update Student set marks = %s Where roll=%s',(m,r))
        #Saving Value
        con.commit()
        print('--------------------------')
        print("User Updated\n----------------")
        

    # Function for Deleting Data
    def Delete():
        print("\n------------------\nWhich Details Do You Want To Delete")
        # Asking for the roll to delete columns
        r = int(input("Enter Roll -"))
        if type(r) !=int:
            print("Please Enter Valid Roll Number")
            Delete()
        # Deleting Columns
        mycursor.execute('Delete from Student where roll = %s',(r,))
        con.commit()
        print('--------------------')
        print(f"{r} User Deleted...",)
        print('----------------------')


    # Function For Fetching Data
    def FetchData():
        # Fetching All The value from table
        mycursor.execute("SELECT * FROM Student")
        print(mycursor.fetchall())


    # Choose One Option
    print("Choose Your options-")
    print("1-Insert Table")
    print("2-Update Table")
    print("3-Delete Table")
    print("4-Fetch Data")
    print("--------------")
    # Enter your option 
    option = int(input("Enter Your Option- "))
    # If the input value is 1
    if(option==1):
        Insert()
    elif(option==2):
        Update()
    elif(option==3):
        Delete()
    elif(option==4):
        FetchData()
    else:
        print("Please Enter Valid Number")
        Option()
    print("\n----------\nThank You.......")
    
# Calling the function
Option()
