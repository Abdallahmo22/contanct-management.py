contacts = {}

while True:
  print("""       
        *** Contact Management ***
       1. Add a contact
       2. View a contact
       3. Update a contact
       4. Exit
         """)
  choice = input("please choose a number from 1-4 : ")

  if choice == "1":
            id_count = 0
            while id_count <2:
                   
             Id = input("please enter the contact Id : ")
             name = input("please type a name : ")
             number = input("please type a phone number : ")
             contacts[Id] ={"data" :{"name": name , "phone": number}}
             id_count += 1
              
             print(f"\n\n{name} was added succesfully\n\n ")       
              
  elif choice == "2":              
            print(contacts)

  elif choice == "3":
            
            id_count = 0
            while id_count <1:
           
             ubdating_Id = input("please enter the contact Id : ")
             if ubdating_Id in contacts:
                    
               new_name = input("please type a new name : ")
               new_number = input("please type a new phone number : ")
               id_count += 1

               contacts[ubdating_Id] ={"data" :{"name": new_name , "phone": new_number}}    

               print("\nSuccess....\n")
               print("Great , Data was ubdated succesfully.")

             else: 

               print(f"\nsorry {ubdating_Id} was not found...!\n")
      

  elif choice == "4":
            print("\n<<<<<< Thank you for using our program. >>>>>>\n") 
            break
  else:
            print("\nInvalid Choice!\n")
            
            
