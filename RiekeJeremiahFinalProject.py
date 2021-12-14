"""
Jeremiah Rieke
SDEV something
Assignment
December 12, 2021

This program generates estimates for 3D print and design work

"""

from breezypythongui import EasyFrame, EasyDialog
import tkinter.filedialog
class Estimator(EasyFrame):
    
    def __init__(self):
        #set up our labels and text fields
        #Window Title
        EasyFrame.__init__(self, "3D Estimator")
        #Text Input fields
        self.addLabel(text = "Company Name:", row = 0, column = 0)
        self.companyName = self.addTextField("", row = 0, column = 1, width = 20)
        self.addLabel(text = "Customer Name:", row = 1, column = 0)
        self.customerName = self.addTextField("", row = 1, column = 1, width = 20)
        self.addLabel(text = "Customer Email", row = 2, column = 0)
        self.email = self.addTextField("", row = 2, column = 1, width = 20)
        self.addLabel(text = "Customer Phone Number:", row = 3, column = 0)
        self.phone = self.addTextField("", row = 3, column = 1, width = 20)
        self.addLabel(text = "Project Name:", row = 4, column = 0)
        self.projectName = self.addTextField("", row = 4, column = 1, width = 20)
        #Float input fields. Note that these have been populated with current pricing but can be alterd by the user
        #Data input fields Row 5
        self.addLabel(text = "Design Cost:", row = 5, column = 0)
        self.designCost = self.addFloatField(value = 50.0, row = 5, column = 0, width = 10,)
        self.addLabel(text = "Design hours:", row = 5, column = 1)
        self.designHours = self.addFloatField(value = 10.0, row =5, column = 1, width = 10)
        #Data input fields Row 6
        self.addLabel(text = "Print hourly cost:", row = 6, column = 0)
        self.printCost = self.addFloatField(value = 1.13, row = 6, column = 0, width = 10)
        self.addLabel(text = "Print hours:", row = 6, column = 1)
        self.printHours = self.addFloatField(value = 8.0, row = 6, column = 1, width = 10)
        #Data input fields Row 7
        self.addLabel(text = "Material cost:", row = 7, column = 0)
        self.materialCost = self.addFloatField(value = 0.07, row = 7, column = 0, width = 10)
        self.addLabel(text = "Material Required in Meters:", row = 7, column = 1)
        self.materialMeters = self.addFloatField(value = 10.0, row = 7, column = 1, width = 10)
        #Text input box for project notes. I could not get text wrapping to work on this either.
        self.addLabel(text = "Notes:", row = 12, column = 0)
        self.notes = self.addTextArea("", row = 13, column = 0,
                                          columnspan = 3,
                                          width = 75,
                                          height = 5)

        #Estimate button calls self.Estimate to create estimate text
        buttonPanel = self.addPanel(row = 20, column = 0, columnspan = 2)
        self.addButton(text = "Estimate", row = 20, column = 0, columnspan = 2, command = self.Estimate)
        self.addLabel(text = "Cut and paste estimate into email", row = 21, column = 0, columnspan = 3)
        #Create our text area to add notes. I tried to get text wrapping to work with this but it did not...
        self.outputArea = self.addTextArea("", row = 23, column = 0,
                                          columnspan = 3,
                                          width = 75,
                                          height = 20)
        #Create our buttons for saving an estimate and opening a previously saved version for modification
        buttonPanel = self.addPanel(row = 45, column = 0, columnspan = 2)
        buttonPanel.addButton(text = "Open", row = 45, column = 0, command = self.openFile)
        buttonPanel.addButton(text = "Save As...", row = 45, column = 2, command = self.saveFileAs)

    # Event handling methods
    #compiles the info entered in spaces above and generates the text output of an estimate to be cut and pasted into an email to send to customer
    def Estimate(self):
            #Defining all of our new variables
            CompanyName = self.companyName.getText()
            CustomerName = self.customerName.getText()
            Email = self.email.getText()
            Phone = self.phone.getText()
            ProjectName = self.projectName.getText()
            DesignCost = self.designCost.getNumber()
            PrintCost = self.printCost.getNumber()
            MaterialCost = self.materialCost.getNumber()
            DesignHours = self.designHours.getNumber()
            PrintHours = self.printHours.getNumber()
            MaterialMeters = self.materialMeters.getNumber()
            Notes = self.notes.getText()
            #Lets do some math...
            DesignEstimate = DesignCost * DesignHours
            PrintEstimate = PrintCost * PrintHours
            MaterialEstimate = MaterialCost * MaterialMeters
            TotalEstimate = DesignEstimate + PrintEstimate + MaterialEstimate
            ThreeDestimate = PrintEstimate ++ MaterialEstimate     
            #formatting the output of the results to our text box 
            result = ("Estimate for Custom 3D Design and Print Job \n")
            result += ("\n")
            result += ("%s \n") % CustomerName
            result += ("%s \n") % Email
            result += ("%s \n") % Phone
            result += ("%s \n") % ProjectName
            result += ("\n")
            result += "Estimate cost for Custom Design work: $%0.2f\n" % DesignEstimate
            result += "Estimated cost for 3d Printing:       $%0.2f\n" % ThreeDestimate
            result += "Total Estimate cost is:               $%0.2f\n" % TotalEstimate
            result += ("\n")
            result += ("%s \n") % Notes
            result += ("Thank you for your business \n")
            result += ("\n")
            result += ("\n")
            result += ("Sincerely \n")
            result += ("\n")
            result += ("Jeremiah Rieke \n")
            
            # Output the result        
            self.outputArea["state"] = "normal"
            self.outputArea.setText(result)
            self.outputArea["state"] = "disabled"


    # Event handling methods
    # opens a file for editing in the estimator. Borrowed from the man himself Ken Lambert
    def openFile(self):
        """Pops up an open file dialog, and if a file is selected,
        displays its text in the text area."""
        filetypes = [("Text files", "*.txt"), ("Python files", "*.py")]
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = filetypes)
        if fileName != "":
            file = open(fileName, "r")
            text = file.read()
            file.close()
            self.outputArea.setText(text)

    # Saves a file for future reference. Borrowed from the man himself Ken Lambert
    def saveFileAs(self):
        """Pops up a save file dialog, and if a file is selected,
        saves the contents of the text area to the file."""
        fileName = tkinter.filedialog.asksaveasfilename(parent = self)
        if fileName != "":
            text = self.outputArea.getText()
            file = open(fileName, "w")
            file.write(text)
            file.close()


if __name__ == "__main__":
    Estimator().mainloop()
