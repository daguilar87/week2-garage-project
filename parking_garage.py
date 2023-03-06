class Garage():  
    def __init__(self, tickets = [1,2,3,4,5,6,7,8,9,10], parking = [1,2,3,4,5,6,7,8,9,10], current = {"bill": "unpaid"}):
        self.tickets = tickets
        self.parking = parking
        self.current = current


    def takeTicket(self):
        x = input("Enter yes to park in the DBD garage!\n")
        if x.lower() == "yes":
            y = int(input('Pick parking spot 1-10\n'))
            if y > 10 or y <= 0:
                print("INVALID ONLY PARKING SPOTS 1-10")
            else:
                self.tickets.remove(y)    
                self.parking.remove(y)
                print(f"Your ticket number and parking spot number is: {y}")


    def paidforParking(self):
        while True:
            y = int(input(f"Please type in your ticket number and pay $15.\n"))
            if y > 0 and y <= 10 and y not in self.parking and y not in self.tickets:
                print("Your ticket is paid. You have 15 minutes to leave!")
                self.tickets.append(y)
                self.parking.append(y)
                self.current["bill"] = "paid"
                o = input("Would you like to leave the DBD garage now? Type yes to leave now.\n")
                if o.lower() == "yes":
                    self.leaveGarage()
                    break
            elif y <= 0:
                print("ONLY PARKING SPOTS 1-10")
                self.runGarage()
                break   
            else:
                print("Invalid!")
                self.runGarage()
                break


    def leaveGarage(self):
        print("CHECKING SYSTEM TO SEE IF YOU PAID")
        if self.current["bill"] == "paid":
            print("Thank You, have a nice day!")
        else:
            print("System showed you have not paid!")
            self.paidforParking()


    def runGarage(self):
        while True:
            resp = int(input("Welcome to the DBD Garage! What would you like to do? \n Type 1 - to park! \n Type 2 - to pay! \n Type 3 - to leave the garage!\n Type 0 - to cancel\n"))
            if resp == 1:
                self.takeTicket()
            elif resp == 2:
                self.paidforParking()
                if self.current["bill"] == "paid":
                    break
            elif resp == 3:
                self.leaveGarage()
                break
            elif resp == 0:
                break
            else: 
                print("Go away homeless person! Try again with a car!")
                break



#Type in your variable 
car = Garage()
#Run your variable
car.runGarage()