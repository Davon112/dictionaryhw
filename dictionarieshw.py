#Question 1 Task 1

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
Beverages = {"Coke": 2.99, "Coffee": 1.99}
restaurant_menu["Beverages"] = Beverages

restaurant_menu["Main Course"].update({"Steak": 17.99})

restaurant_menu["Starters"].popitem()
print(restaurant_menu)


#Question 2
open = "open"
update = "update"
display = "display"

def service_ticket():
    tickets = {"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
    
    while True: 
        response = input(f"Choose one: {open} {update} {display}: ")
        if response == open:
            new_ticket = input("Ticket Number: ")
            new_customer = input("Customer Name: ")
            new_issue = input("Type of issue: ")
            new_status = input("Staus: open or closed? ")
            new_item = {"Customer name": {new_customer}, "Issue": {new_issue}, "Status": {new_status} }
            tickets[new_ticket] = new_item
            print(tickets)
            break
        elif response == update:
            update_ticket = input(f"which ticket would you like to update? 1 {tickets['Ticket002']} 2 {tickets['Ticket002']}")
            if update_ticket == "1":
                open_close = input("open or closed? :")
                if open_close == "open":
                    tickets["Ticket001"].update({"Status": "open"})
                    print(tickets["Ticket001"])
                if open_close == "closed":
                    tickets["Ticket001"].update({"Status": "closed"})
                    print(tickets["Ticket001"])
            if update_ticket == 2:
                open_close = input("open or closed? :")
                if open_close == "open":
                    tickets["Ticket002"].update({"Status": "open"})
                    print(tickets["Ticket002"])
                if open_close == "closed":
                    tickets["Ticket002"].update({"Status": "closed"})
                    print(tickets["Ticket002"])


        elif response == display:
            print(tickets)
       



service_ticket()