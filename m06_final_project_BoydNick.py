# Course: SDEV 140
# Author: Nick Boyd
# Date: 2021-09-28
# Program m06_assn2_ex4_BoydNick.py
# Purpose: Final Project Basic Form with Clear


from tkinter import *

# Color codes:
# #77DD77 = Pastel Green
# #B1907F = Pastel Brown

# Define root as the main window instance
root = Tk()
root.title("Crazy Joe's Amusements by Nick Boyd")

# Create class for DataFrame with parent class Frame
class DataFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self.grid(row=0, column=0)
        self.config(bg="#77DD77")
        
        # Define variable for Error Value
        self.lblErrorValue = StringVar()
        
        # Define variables for Cost Labels
        self.lblAdultCurVal = StringVar(value="$0")
        self.lblChildCurVal = StringVar(value="$0")
        self.lblVoucherCurVal = StringVar(value="$0")
        self.lblFastPassCurVal = StringVar(value="$0")
        self.lblTotalCurVal = StringVar(value="$0")
             
        # Define variables for Spinbox values
        self.spinAdultCurVal=IntVar()
        self.spinChildCurVal=IntVar()
        self.spinVoucherCurVal=IntVar()
        self.spinFastPassCurVal=IntVar()
        

        # Create and place label for header
        self.createHeaderFrame(self)
       
        # Create and place labels for field names
        self.createEntryLabels(self)

         # Create labels for current Cost Values
        self.lblAdultCost = Label(
            self, 
            width = 6,
            font = 12,
            textvariable=self.lblAdultCurVal
            )
        
        self.lblChildCost = Label(
            self, 
            width = 6, 
            font = 12,
            textvariable=self.lblChildCurVal
            )
        
        self.lblVoucherCost = Label(
            self,
            width = 6, 
            font = 12,
            textvariable=self.lblVoucherCurVal
            )
        
        self.lblFastPassCost = Label(
            self, 
            width = 6, 
            font = 12,
            textvariable=self.lblFastPassCurVal
            )
        
        self.lblTotalCost = Label(
            self, 
            width = 6, 
            font = 12,
            textvariable=self.lblTotalCurVal
            )

        self.lblAdultCost.grid(row=4, column=2)
        self.lblChildCost.grid(row=5, column=2)
        self.lblVoucherCost.grid(row=6, column=2)
        self.lblFastPassCost.grid(row=7, column=2)
        self.lblTotalCost.grid(row=8, column=2, pady = 5)


        # Create and place label for Error Value
        self.lblError = Label(self, fg = "Red", font=12, textvariable=self.lblErrorValue)
        self.lblError.grid(row=9, column=0, columnspan = 3)

        # Create and place labels for Image
        self.photo1 = PhotoImage(file = "CJ - Copy2.png")
        self.photo2 = PhotoImage(file = "Ferris.png")
        self.lblImage1 = Label(self, image = self.photo1)
        self.lblImage1.grid(row = 0, column=3, stick ="EN")
        self.lblImage2 = Label(self, image = self.photo2)
        self.lblImage2.grid(row=0, column=0, sticky="WS")
        

        # Create Entry Boxes
        self.txtName = Entry(self, font = 12, width=40)
        self.txtAddress = Entry(self, font = 12, width=40)
        self.txtEmail = Entry(self, font = 12, width=40)

        # Place the Entry Boxes
        self.txtName.grid(row=1, column=1, columnspan=3)
        self.txtAddress.grid(row=2, column=1, columnspan=3)
        self.txtEmail.grid(row=3, column=1, columnspan=3)

        # Create the Spin Boxes
        self.spinAdult = Spinbox(
            self, width=3,
            from_=0, to=30,
            font = 12,
            textvariable=self.spinAdultCurVal,
            command=lambda:self.spinClick(self.spinAdultCurVal, 50, self.lblAdultCurVal)
        )

        self.spinChild = Spinbox(
            self, width = 3,
            from_=0, to=30, 
            font = 12,
            textvariable=self.spinChildCurVal,
            command=lambda:self.spinClick(self.spinChildCurVal, 25, self.lblChildCurVal)
            )

        self.spinVoucher = Spinbox(
            self, width = 3,
            from_=0, to=30, 
            font = 12,
            textvariable=self.spinVoucherCurVal,
            command=lambda:self.spinClick(self.spinVoucherCurVal, 10, self.lblVoucherCurVal)
            )
        self.spinFastPass = Spinbox(
            self, width = 3,
            from_=0, to=30, 
            font = 12,
            textvariable=self.spinFastPassCurVal,
            command=lambda:self.spinClick(self.spinFastPassCurVal, 10, self.lblFastPassCurVal)
        )

        # Place the Spinboxes
        self.spinAdult.grid(row=4, column=1)
        self.spinChild.grid(row=5, column=1)
        self.spinVoucher.grid(row=6, column=1)
        self.spinFastPass.grid(row=7, column=1)

       

        # Create the Buttons
        self.btnContinue = Button(
            self, 
            text ="Continue", 
            font=12,
            bg="#B1907F", fg="White", 
            command=self.btnContinueClick
            )
        
        self.btnClear = Button(
            self, 
            text ="Clear",
            font=12,
            bg="#B1907F", fg = "White",
            command=self.btnClearClick
            )
        
        
        # Place the Buttons
        self.btnContinue.grid(row=4, column=3)
        self.btnClear.grid(row=6, column=3)
        
        

    # Define function for clicking the continue button
    def btnContinueClick(self):
    #     if self.entryValidation(self.txtName.get()) == 0:
    #         self.lblErrorValue.set("Invalid Entry")

        order = Toplevel(self.OrderForm(root))
        order.title("Second Window Title")
        order.config(bg="#77DD77")
        self.createHeaderFrame(order)
        self.createEntryLabels(order)
        name=self.txtName.get()
        order.lblName=Label(order, text = name, font = 12)
        order.lblName.grid(row=1, column=1)

        self.createOrderLabels(order)
        self.createSpinQty(order)
        
        
        
        #Create and place labels for Images
        order.lblImage1 = Label(order, image = self.photo1)
        order.lblImage1.grid(row = 0, column=3, sticky =  "ES")
        order.lblImage2 = Label(order, image = self.photo2)
        order.lblImage2.grid(row=0, column=0, sticky="WS")
        
        
        # Create labels for field names
        # order.lblName = Label(
        #     order, 
        #     text = name,
        #     #text="Name: " + str(self.txtName.get()), 
        #     bg="#77DD77", 
        #     font = 12
        #     )
        # order.lblName.grid(row=1, column=0)

        self.lblErrorValue.set("")

    # Define function for clicking the clear button
    def btnClearClick(self):
        self.lblErrorValue.set("Form Cleared")
        self.txtName.delete(0, END)
        self.txtAddress.delete(0, END)
        self.txtEmail.delete(0, END)
        self.lblAdultCurVal.set("$0")
        self.lblChildCurVal.set("$0")
        self.lblVoucherCurVal.set("$0")
        self.lblFastPassCurVal.set("$0")
        self.lblTotalCurVal.set("$0")
        self.spinAdultCurVal.set(0)
        self.spinChildCurVal.set(0)
        self.spinVoucherCurVal.set(0)
        self.spinFastPassCurVal.set(0)
        
    def spinClick(self, box, value, label):
        temp = int(box.get())
        result = temp * value
        label.set(f'${result}')
        
        #total = int(self.CostList[0].get()) * 50 + int(self.CostList[1].get()) * 25 + int(self.CostList[2].get()) * 10 + int(self.CostList[3].get()) * 10
        total = (int(self.spinAdultCurVal.get()) * 50) + (int(self.spinChildCurVal.get()) * 25) + (int(self.spinVoucherCurVal.get()) * 10) + (int(self.spinFastPassCurVal.get()) * 10)
        self.lblTotalCurVal.set(f'${total}')

    def createHeaderFrame(self, parent):
        # Create and place label for header
        parent.lblHeader = Label(
            parent, 
            text="Crazy Joe's Amusements", 
            bg = "#B1907F", fg = "White", 
            width = 34,
            font = ("Arial", 20, "bold")
            )
        parent.lblHeader.grid(row=0, column=0, columnspan=3)

    def createEntryLabels(self, parent):
        parent.lblName = Label(
            parent, 
            text="Name: ", 
            bg="#77DD77", 
            font = 12
            )
        
        parent.lblAddress = Label(
            parent, 
            text="Address: ",
            bg="#77DD77", 
            font = 12
            )

        parent.lblEmail = Label(
            parent, 
            text="E-mail: ",
            bg="#77DD77", 
            font = 12
            )
        
        parent.lblAdult = Label(
            parent, 
            text="Adult Ticket ($50.00) ",
            bg="#77DD77", 
            font = 12
            )
        
        parent.lblChild = Label(
            parent, 
            text="Child Ticket ($25.00) ",
            bg="#77DD77", 
            font = 12
            )
        
        parent.lblVoucher = Label(
            parent, 
            text ="Meal Voucher ($10.00:) ",
            bg="#77DD77", 
            font = 12)
        
        parent.lblFastPass = Label(
            parent, 
            text="Fast Pass ($10.00) ",
            bg="#77DD77", 
            font = 12
            )
        
        parent.lblTotal = Label(
            parent, 
            text="Total Cost: ",
            bg="#77DD77", 
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
    
    # Create and placelabels for current Cost Values
    def createOrderLabels(self, parent):
        parent.lblAdultCost = Label(
            parent, 
            width = 6,
            font = 12,
            textvariable=self.lblAdultCurVal
            )
        
        parent.lblChildCost = Label(
            parent, 
            width = 6, 
            font = 12,
            textvariable=self.lblChildCurVal
            )
        
        parent.lblVoucherCost = Label(
            parent,
            width = 6, 
            font = 12,
            textvariable=self.lblVoucherCurVal
            )
        
        parent.lblFastPassCost = Label(
            parent, 
            width = 6, 
            font = 12,
            textvariable=self.lblFastPassCurVal
            )
        
        parent.lblTotalCost = Label(
            parent, 
            width = 6, 
            font = 12,
            textvariable=self.lblTotalCurVal
            )

        parent.lblAdultCost.grid(row=4, column=2)
        parent.lblChildCost.grid(row=5, column=2)
        parent.lblVoucherCost.grid(row=6, column=2)
        parent.lblFastPassCost.grid(row=7, column=2)
        parent.lblTotalCost.grid(row=8, column=2, pady = 5)
    
    def createSpinQty(self,parent):
        parent.lblSpinAdultQty = Label(parent, width=3, font = 12,
            textvariable=self.spinAdultCurVal,
            )
        parent.lblSpinChildQty = Label(parent, width=3, font = 12,
            textvariable=self.spinChildCurVal,
            )
        parent.lblSpinVoucherQty = Label(parent, width=3, font = 12,
            textvariable=self.spinVoucherCurVal,
            )
        parent.lblSpinFastPassQty = Label(parent, width=3, font = 12,
            textvariable=self.spinFastPassCurVal,
            )

        parent.lblSpinAdultQty.grid(row=4, column=1)
        parent.lblSpinChildQty.grid(row=5, column=1)
        parent.lblSpinVoucherQty.grid(row=6, column=1)
        parent.lblSpinFastPassQty.grid(row=7, column=1)  
    
    def entryValidation(self, entry):
        """Validates entry to be positive integer and/or between 1 and 300"""
        # Check for blank entry  
        if entry == "":
            valid = 0
            return valid
        # # Check for entry that is not a number
        # elif entry.isdigit() == False:
        #     valid = "That is not a valid number."
        #     return valid
        # # Check for entry between 1 and 300
        # elif int(entry) < 1 or int(entry) > 300:
        #     valid = "0"
        #     return valid
        # # Entry valid
        # else:
        #     valid = "1"
        #     return valid         




    class OrderForm(Frame):
        def __init__(self, parent):
            super().__init__()
            

def main():
    # Create Window1 as MainForm class and place in root
    data = DataFrame(root)
    root.mainloop()

main()