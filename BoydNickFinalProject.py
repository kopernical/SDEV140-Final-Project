# Course: SDEV 140
# Author: Nick Boyd
# Date: 2021-10-06
# Program: Crazy Joe's Amusements Ticket Purchase
# Purpose: SDEV 140 - Final Project


from tkinter import *

# Color codes used:
# #77DD77 = Pastel Green
# #B1907F = Pastel Brown

# Define root as the main window instance and set title
root = Tk()
root.title("Crazy Joe's Amusements by Nick Boyd")


def main():
    readFile()
    """Main Function"""
    # Create program as MainFrame class and place in root
    order = MainFrame()
    order.mainloop()


# Create class for the MainFrame with parent class Frame
class MainFrame(Frame):
    def __init__(self):
        super().__init__()
        self.grid(row=0, column=0)

        self.lblErrorValue = StringVar()  # Define variable for Error Value Label
        
        self.lblAdultCostVal = StringVar(value="$0")    # Define variable for text displayed on Adult Cost Label
        self.lblChildCostVal = StringVar(value="$0")    # Define variable for text displayed on Child Cost Label
        self.lblVoucherCostVal = StringVar(value="$0")  # Define variable for text displayed on Food Voucher Cost Label
        self.lblFastPassCostVal = StringVar(value="$0") # Define variable for text displayed on Fast Pass Label
        self.lblTotalCostVal = StringVar(value="$0")    # Define variable for text displayed on Total Cost Label
             
        self.spinAdultVal=IntVar()      # Define variable for the value of Adult Ticket Spinbox
        self.spinChildVal=IntVar()      # Define variable for the value of Child Ticket Spinbox
        self.spinVoucherVal=IntVar()    # Define variable for the value of Food Voucher Spinbox
        self.spinFastPassVal=IntVar()   # Define variable for the value of Fast Pass Spinbox
        
        # Call functions to build initial labels
        self.createHeaderFrame(self, color = "#B1907F", pic1="CJ_1.png", pic2="Roller.png")
        self.createInfoLabels(self)
        self.createOrderLabels(self)
        self.createEntryBoxes()
        self.createSpinBoxes()
        self.createErrorLabel()
        self.createMainButtons()

    def btnContinueClick(self):
        """ Function for clicking the Continue Button"""
        # Clear any error label
        self.lblErrorValue.set("")
        #  If all text fields validated open confirmation window
        if self.entryValidation() == 1:
            self.openConfirmWindow()
            
    def openConfirmWindow(self):
        """Function for defining the Confirmation Window"""
        # Open new window on top using SecondaryFrame Class and set Title
        confirm = Toplevel(self.SecondaryFrame(root))
        confirm.title("Crazy Joe's Amusements Confirmation Window")
        # Call function to create Header and Labels on Confirmation Window
        self.createHeaderFrame(confirm, color = "#77DD77", pic1="CJ_2.png", pic2="Ferris.png")
        self.createInfoLabels(confirm)
        self.createOrderLabels(confirm)
        # Call function to create buttons on Confirmation Window
        self.createConfirmButtons(confirm)
        # Call function to create label to display message on bottom of Confirmation Window
        self.createConfirmLabel(confirm)
        # Call function to create labels for quantities in Spinboxes on Confirmation Window
        self.createSpinQty(confirm)
        # Call function to create labels for imported entry box data on Confirmation Window
        self.createTxtImport(confirm)      

    def btnClearClick(self):
        """Function for clicking the Clear Button"""
        # Set Error Label to say Form Cleared
        self.lblErrorValue.set("Form Cleared")
        # Clear the entry boxes
        self.txtName.delete(0, END)
        self.txtAddress.delete(0, END)
        self.txtEmail.delete(0, END)
        # Set all cost value labels to $0
        self.lblAdultCostVal.set("$0")
        self.lblChildCostVal.set("$0")
        self.lblVoucherCostVal.set("$0")
        self.lblFastPassCostVal.set("$0")
        self.lblTotalCostVal.set("$0")
        # Set all spinboxe values to 0
        self.spinAdultVal.set(0)
        self.spinChildVal.set(0)
        self.spinVoucherVal.set(0)
        self.spinFastPassVal.set(0)
                
    def spinClick(self, box, value, label): # box=spinbox, value=price of item denoted by box, label=label denoting total cost of that item
        """Function for clicking a spinbox button"""
        # Gets value from spinbox, converts to integer and set as variable 'temp'
        temp = int(box.get())
        # Multiply spinbox item quantity by value to determine total cost of items
        result = temp * value
        # Update label for that item
        label.set(f'${result}')
        # Calcluate total cost of all spinbox items and set to variable 'total'
        total = (self.spinAdultVal.get() * 50) + (self.spinChildVal.get() * 25) + (self.spinVoucherVal.get() * 10) + (self.spinFastPassVal.get() * 10)
        # Update label for total cost
        self.lblTotalCostVal.set(f'${total}')
    
    def btnOrderClick(self, parent):
        """Function for clicking the Order button"""
        # Display message label on bottom of screen thanking for the order
        parent.lblConfirm.config(bg = "#77DD77", width=26, text = "Order Confirmed!\nWe Look Forward to Your Visit!", font =("Arial", 20, "bold"))
        # Hide the Order, Back and Button Buttons
        parent.btnOrder.grid_forget()
        parent.btnBack.grid_forget()
        parent.btnCancel.grid_forget()
        writeToFile(self.txtName.get(), self.txtAddress.get(), self.txtEmail.get(), self.spinAdult.get(), self.spinChild.get(), self.spinVoucher.get(), self.spinFastPass.get(), self.lblTotalCostVal.get())
        # Clear the main form by restarting main module
        main()

    def btnBackClick(self, parent):
        """Function for clicking the Back Button"""
        # Close the Confirmation Window
        parent.destroy()

    def btnCancelClick(self, parent):
        """Function for clicking the Cancel Button"""
        # Close the Confirmation Window and clear the main form by restarting main module
        parent.destroy()
        main()

    def createHeaderFrame(self, parent, color, pic1, pic2): # pic1=image for upper left of frame pic2=image for upper right of frame
        """ Function to create frame for the Header and Images"""
        parent.lblHeader = Label(
            parent, 
            text="Crazy Joe's\nAmusements", 
            bg = color, fg= "White",
            width = 26,
            font = ("Arial", 20, "bold")
            )
        parent.lblHeader.grid(row=0, column=0, columnspan=4)

        # Import Images
        parent.photo1 = PhotoImage(file = pic1)
        parent.photo2 = PhotoImage(file = pic2)
        # Set Labels with photo1 on top left and photo2 on top right
        parent.lblImage1 = Label(parent, image = parent.photo1)
        parent.lblImage1.grid(row = 0, column=0, stick ="WS")
        parent.lblImage2 = Label(parent, image = parent.photo2)
        parent.lblImage2.grid(row=0, column=3, sticky="EN")

    def createInfoLabels(self, parent):
        """Function for creating and placing the Info Labels"""
        parent.lblName = Label(
            parent, 
            text="Name: ",
            border =  4,
            font = 12
            )
        
        parent.lblAddress = Label(
            parent, 
            text="Address: ", 
            font = 12
            )

        parent.lblEmail = Label(
            parent, 
            text="E-mail: ", 
            font = 12
            )
        
        parent.lblAdult = Label(
            parent, 
            text="Adult Ticket ($50.00) ", 
            font = 12
            )
        
        parent.lblChild = Label(
            parent, 
            text="Child Ticket ($25.00) ",
            font = 12
            )
        
        parent.lblVoucher = Label(
            parent, 
            text ="Meal Voucher ($10.00) ", 
            font = 12)
        
        parent.lblFastPass = Label(
            parent, 
            text="Fast Pass ($10.00) ",
            font = 12
            )
        
        parent.lblTotal = Label(
            parent, 
            text="Total Cost: ",
            font = 12,
        )
        # Place labels
        parent.lblName.grid(row=1, column=0, pady = 5)
        parent.lblAddress.grid(row=2, column=0, pady = 5)
        parent.lblEmail.grid(row=3, column=0, pady =5)
        parent.lblAdult.grid(row=4, column=0, pady=5)
        parent.lblChild.grid(row=5, column=0, pady=5)
        parent.lblVoucher.grid(row=6, column=0, pady=5)
        parent.lblFastPass.grid(row=7, column=0, pady=5)
        parent.lblTotal.grid(row=8, column=0, pady=5)
    
    def createOrderLabels(self, parent):
        """Function to create and place the labels for Cost Values"""
        parent.lblAdultCost = Label(
            parent, 
            width = 6,
            font = 12,
            textvariable=self.lblAdultCostVal
            )
        
        parent.lblChildCost = Label(
            parent, 
            width = 6, 
            font = 12,
            textvariable=self.lblChildCostVal
            )
        
        parent.lblVoucherCost = Label(
            parent,
            width = 6, 
            font = 12,
            textvariable=self.lblVoucherCostVal
            )
        
        parent.lblFastPassCost = Label(
            parent, 
            width = 6, 
            font = 12,
            textvariable=self.lblFastPassCostVal
            )
        
        parent.lblTotalCost = Label(
            parent, 
            width = 6, 
            font = 12,
            textvariable=self.lblTotalCostVal
            )

        parent.lblAdultCost.grid(row=4, column=2)
        parent.lblChildCost.grid(row=5, column=2)
        parent.lblVoucherCost.grid(row=6, column=2)
        parent.lblFastPassCost.grid(row=7, column=2)
        parent.lblTotalCost.grid(row=8, column=2, pady = 5)
    
    def createEntryBoxes(self):
        """Function to create the Entry Boxes on the Order Window"""
        # Create Entry Boxes for Name, Address and Email Fields
        self.txtName = Entry(self, font = 12, width=40)
        self.txtAddress = Entry(self, font = 12, width=40)
        self.txtEmail = Entry(self, font = 12, width=40)

        # Place the Entry Boxes
        self.txtName.grid(row=1, column=1, columnspan=3)
        self.txtAddress.grid(row=2, column=1, columnspan=3)
        self.txtEmail.grid(row=3, column=1, columnspan=3)

        # Enter default text into the entry boxes
        self.txtName.insert(0, "ex. Joe Smith")
        self.txtAddress.insert(0, "ex. 123 Main Street")
        self.txtEmail.insert(0, "ex. name@example.com")

    def createSpinBoxes(self):
        """Function to create the SpinBoxes on the Order Window"""
        # Create the Spinbox for Adult Tickets
        self.spinAdult = Spinbox(
            self, width=3,
            from_=0, to=30,
            font = 12,
            textvariable=self.spinAdultVal,
            state = 'readonly',
            command=lambda:self.spinClick(self.spinAdultVal, 50, self.lblAdultCostVal)
        )
        # Create the Spinbox for Child Tickets
        self.spinChild = Spinbox(
            self, width = 3,
            from_=0, to=30, 
            font = 12,
            textvariable=self.spinChildVal,
            state = 'readonly',
            command=lambda:self.spinClick(self.spinChildVal, 25, self.lblChildCostVal)
            )
        # Create the Spinbox for Food Vouchers
        self.spinVoucher = Spinbox(
            self, width = 3,
            from_=0, to=30, 
            font = 12,
            state = 'readonly',
            textvariable=self.spinVoucherVal,
            command=lambda:self.spinClick(self.spinVoucherVal, 10, self.lblVoucherCostVal)
            )
        # Create the Spinbox for Fast Pass Tickets
        self.spinFastPass = Spinbox(
            self, width = 3,
            from_=0, to=30, 
            font = 12,
            state = 'readonly',
            textvariable=self.spinFastPassVal,
            command=lambda:self.spinClick(self.spinFastPassVal, 10, self.lblFastPassCostVal)
        )

        # Place the Spinboxes
        self.spinAdult.grid(row=4, column=1)
        self.spinChild.grid(row=5, column=1)
        self.spinVoucher.grid(row=6, column=1)
        self.spinFastPass.grid(row=7, column=1)

    def createErrorLabel(self):
        """Function to create the label for Error Text on the Order Window"""
        self.lblError = Label(self, fg = "Red", font=12, textvariable=self.lblErrorValue)
        self.lblError.grid(row=9, column=0, columnspan = 4)

    def createMainButtons(self):
        """Function to create the Buttons on the Order Window"""
        # Create the Continue Button
        self.btnContinue = Button(
            self, 
            text ="Continue", 
            font=12,
            bg="#B1907F", fg="White", 
            command=self.btnContinueClick
            )
        
        # Create the Clear Button 
        self.btnClear = Button(
            self, 
            text ="Clear",
            font=12,
            bg="#B1907F", fg = "White",
            command=self.btnClearClick
            )
        
        # Place Continue and Clear Buttons
        self.btnContinue.grid(row=4, column=3)
        self.btnClear.grid(row=6, column=3)
  
    def createConfirmButtons(self, parent):
        """Function to create the Buttons on the Confirmation Window"""
        # Create the Order Button
        parent.btnOrder = Button(
            parent, 
            text ="Order", 
            font=12,
            bg="#77DD77",
            command=lambda:self.btnOrderClick(parent)
            )
        # Create the Back Button 
        parent.btnBack = Button(
            parent, 
            text ="Go Back", 
            font=12,
            bg="#77DD77",
            command=lambda:self.btnBackClick(parent)
            )
        # Create the Cancel Button
        parent.btnCancel = Button(
            parent, 
            text ="Cancel",
            font=12,
            bg="#77DD77",
            command=lambda:self.btnCancelClick(parent)
            )
        
        # Place the Order, Back and Cancel Buttons
        parent.btnOrder.grid(row=4, column=3)
        parent.btnBack.grid(row=6, column=3)
        parent.btnCancel.grid(row=8, column=3)

    def createConfirmLabel(self, parent):
        """Function to create the Label for the Confirmation Window"""
        parent.lblConfirm=Label(parent, width=26)
        parent.lblConfirm.grid(row=9, column = 0, columnspan=4)

    def createSpinQty(self, parent):
        """Function to create labels with values of spinboxes"""
        parent.lblSpinAdultQty = Label(parent, width=3, font = 12,
            textvariable=self.spinAdultVal,
            )
        parent.lblSpinChildQty = Label(parent, width=3, font = 12, 
            textvariable=self.spinChildVal,
            )
        parent.lblSpinVoucherQty = Label(parent, width=3, font = 12, 
            textvariable=self.spinVoucherVal,
            )
        parent.lblSpinFastPassQty = Label(parent, width=3, font = 12, 
            textvariable=self.spinFastPassVal,
            )
        # Place labels
        parent.lblSpinAdultQty.grid(row=4, column=1)
        parent.lblSpinChildQty.grid(row=5, column=1)
        parent.lblSpinVoucherQty.grid(row=6, column=1)
        parent.lblSpinFastPassQty.grid(row=7, column=1)  

    def createTxtImport(self, parent):
        """Imports the values from the entry boxes in main frame into the confirmation frame"""
        parent.lblName=Label(parent, text = self.txtName.get(), font = 12)
        parent.lblName.grid(row=1, column=1)
        parent.lblAddress=Label(parent, text = self.txtAddress.get(), font = 12)
        parent.lblAddress.grid(row=2, column=1)
        parent.lblEmail=Label(parent, text = self.txtEmail.get(), font = 12)
        parent.lblEmail.grid(row=3, column=1)
        
    def entryValidation(self):
        """Function to check whether all 3 text fields are valid and at least 1 spinbox is filled"""
        # Each function will return None if validation fails and display an error message
        if self.nameValidation(self.txtName.get()) == None:
            return
        elif self.addressValidation(self.txtAddress.get()) == None:
            return
        elif self.emailValidation(self.txtEmail.get()) == None:
            return
        elif self.spinValidation() == None:
            return
        # If all fields are validated function returns value of 1 which is evaluted by btnContinueClick()
        else:
            valid = 1
            return valid
    
    def spinValidation(self):
        """Validates that spinboxes are not set to 0"""
        # Get each spinbox value and if all are "0" display error message and return
        if self.spinAdult.get() == "0" and self.spinChild.get() == "0" and self.spinVoucher.get() == "0" and self.spinFastPass.get() == "0":
            self.lblErrorValue.set("At Least One Product Must Be Selected")
            return
        # Spinboxes are valid, return value of 1 
        else:
            valid=1
            return valid

    def nameValidation(self, entry):
        """Validates name entry to be in proper form"""
        # Import re for regular expression evaluation
        import re
        # Regular Expression for name is 2 blocks of letters separated by a space
        regex = '[A-Za-z]+ [A-Za-z]+'
        # Check if entry is blank, set error message and return
        if entry == "":
            self.lblErrorValue.set("Name Cannot be Blank")
            return
        # Check if entry doesn't match defined regular expression, set error message and return
        elif re.fullmatch(regex, entry) == None:
            self.lblErrorValue.set("Please enter 'FirstName' 'Last Name' with no numbers or symbols")
            return
        # Entry is valid, return value of 1
        else:
            valid = 1
            return valid

    def addressValidation(self, entry):
        """Validates address to be in proper form"""
        # Import re for regular expression evaluation
        import re
        # Regular Expression for address is a block of numbers followed by 2 blocks of letters,
        # each separated by blank spaces, ex. 123 Main Street
        regex = '[0-9]+ [A-Za-z]+ [A-Za-z]+'
        # Check if entry is blank, set error message, and return
        if entry == "":
            self.lblErrorValue.set("Address cannot be blank")
            return
        # Check if entry doesn't match defined regular expression, set error message and return
        elif re.fullmatch(regex, entry) == None:
            self.lblErrorValue.set("Address must be in proper form, ex '123 Main St'")
            return
        # Entry is valid, return value of 1
        else:
            valid = 1
            return valid

    def emailValidation(self, entry):
        """Validates email to be in proper form"""
        # Import re for regular expression evaluation
        import re
        # Regular Expression for email is block of letters/numbers, followed by '@', followed by another 
        # block of letters/numbers, followed by '.', followed by another block of letters 
        regex = '[0-9A-Za-z]+@[0-9A-Za-z]+\.[A-Za-z]+'
        # Check if entry is blank, set error message and return
        if entry == "":
            self.lblErrorValue.set("Email cannot be blank")
            return
        # Check if entry doesn't match defined regular expression, set error message and return
        elif re.fullmatch(regex, entry) == None:
            self.lblErrorValue.set("Email must be in proper form, ex 'name@example.com'")
            return
        # Entry is valid, return value of 1
        else:
            valid = 1
            return valid

    # Define Class for the Secondary Frame
    class SecondaryFrame(Frame):
        def __init__(self, parent):
            super().__init__()

def writeToFile(name, address, email, adult, child, vouchers, fastpass, total): # Get values from entry and spinboxes to write to file
    """Function to writes orders to file"""
    # Use try-except to check if a file already exists
    try:
        f=open("CJ's Amusements Orders.txt", "r")
    # If file doesn't exist create the file and write the header
    except:
        f=open("CJ's Amusements Orders.txt", "a")
        f.write("Name, Address, Email, Adult Tickets, Child Tickets, Food Vouchers, Fast Pass Tickets, Total Cost\n")
        f.close()
    # Append order info to existing file
    f=open("CJ's Amusements Orders.txt", "a")
    f.write(f'\n{name}, {address}, {email}, {adult}, {child}, {vouchers}, {fastpass}, {total}')
    f.close

def readFile():
    """Function to read number of orders from existing file"""
    # Use try-except to check if a file already exists
    try:
        f=open("CJ's Amusements Orders.txt", "r")
    # Display error if no existing file
    except:
        print("There are 0 previous orders")
    else:
        # If file exists open for reading   
        f=open("CJ's Amusements Orders.txt", "r")   
        # Start count at -2 to remove the header lines 
        count = -2
        # Count the lines and add to count
        for line in f:
            count +=1   
        # Print the number of orders in terminal       
        print(f'There are {count} recorded order(s)')
        f.close
   
main()