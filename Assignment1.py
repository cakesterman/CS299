
class Item(object):

    def __init__(self, name, price, category, is_on_sale, sale_discount_percent):

        self.name = name
        self.price = price
        self.category = category
        self.is_on_sale = is_on_sale
        self.sale_discount_percent = sale_discount_percent

    def get_item_name(self):

        return self.name

    def get_item_price(self):

        return self.price

    def get_item_category(self):

        return self.category

    def get_is_on_sale(self):

        return self.is_on_sale

    def get_sale_discount_percent(self):

        return self.sale_discount_percent


class Customer(object):

    def __init__(self):

        self.cart = []
        self.payed_cash = False
        self.payed_card = False

    def get_cart_items(self):

        return self.cart

    def add_item_to_cart(self, item):

        self.cart.append(item)

    def remove_item_from_cart(self, item):

        self.cart.remove(item)

    def print_cart(self):

        print("Your cart contains:")

        for items in self.cart:

            print(items.get_item_name())

        print()

    # When returning the total, it needs to be formatted to display only up to 2 decimal places
    def get_cart_total(self):

        sum = 0
        tax_total = 0

        for items in self.cart:

            sum += items.get_item_price()

        tax_total += (my_store.get_sales_tax() * sum)

        sum += tax_total

        return sum, tax_total

    # When returning the subtotal, it needs to be formatted to display only up to 2 decimal places
    def get_cart_subtotal(self):

        subtotal_sum = 0

        for items in self.cart:
            subtotal_sum += items.get_item_price()

        return subtotal_sum

    def set_payed_cash(self, passed_cash):

        self.payed_cash = passed_cash

    def get_payed_cash(self):

        return self.payed_cash

    def set_payed_card(self, passed_card):

        self.payed_card = passed_card

    def get_payed_card(self):

        return self.payed_card



class Store(object):

    def __init__(self, Items):

        self.Items = Items

    def get_all_items(self):

        return self.Items

    def get_item_by_name(self, item_name):

        for item in Items:

            if item.get_item_name() == item_name:

                return item

    def get_item_by_category(self, category):

        category_list = []

        for item in self.Items:

            if item.get_item_category() == category:

                category_list.append(item)

        if len(category_list) > 0:

            return category_list

        else:

            print("Error returning category")

    def get_sales_tax(self):

        return .06


def initialize_items():

    items_list = []

    # Produce
    strawberry = Item("Strawberry", 4.99, "Produce", False, 0)
    items_list.append(strawberry)
    blueberry = Item("Blueberry", 3.99, "Produce", False, 0)
    items_list.append(blueberry)
    banana = Item("Banana", 2.99, "Produce", False, 0)
    items_list.append(banana)

    # Dairy
    milk = Item("Milk", 5.99, "Dairy", False, 0)
    items_list.append(milk)
    cheddar_cheese = Item("Cheddar Cheese", 2.99, "Dairy", False, 0)
    items_list.append(cheddar_cheese)
    butter = Item("Butter", 2.50, "Dairy", False, 0)
    items_list.append(butter)

    # Meats
    chicken = Item("Chicken", 6.99, "Meats", False, 0)
    items_list.append(chicken)
    steak = Item("Steak", 8.99, "Meats", False, 0)
    items_list.append(steak)
    pork = Item("Pork", 5.99, "Meats", False, 0)
    items_list.append(pork)

    # Clothing
    tshirt = Item("T-Shirt", 10.99, "Clothing", False, 0)
    items_list.append(tshirt)
    pants = Item("Pants", 15.99, "Clothing", False, 0)
    items_list.append(pants)
    socks = Item("Socks", 8.99, "Clothing", False, 0)
    items_list.append(socks)

    # Canned Items
    corned_beef_hash = Item("Corned Beef Hash", 2.99, "Canned Items", False, 0)
    items_list.append(corned_beef_hash)
    canned_corn = Item("Canned Corn", 2.99, "Canned Items", False, 0)
    items_list.append(canned_corn)
    canned_peas = Item("Canned Peas", 1.99, "Canned items", False, 0)
    items_list.append(canned_peas)

    # Microwaveable Meals
    ramen = Item("Ramen", 1.50, "Microwaveable Meals", False, 0)
    items_list.append(ramen)
    mac_and_cheese = Item("Mac and Cheese", 2.99, "Microwaveable Meals", False, 0)
    items_list.append(mac_and_cheese)
    frozen_dinner = Item("Frozen Dinner", 6.99, "Microwaveable Meals", False, 0)
    items_list.append(frozen_dinner)

    # Drinks
    soda = Item("Soda", 1.99, "Drinks", False, 0)
    items_list.append(soda)
    water = Item("Water", 1.50, "Drinks", False, 0)
    items_list.append(water)
    coffee = Item("Coffee", 2.99, "Drinks", False, 0)
    items_list.append(coffee)

    # Bakery
    bread = Item("Bread", 3.99, "Bakery", False, 0)
    items_list.append(bread)
    muffins = Item("Muffins", 3.99, "Bakery", False, 0)
    items_list.append(muffins)
    bagels = Item("Bagels", 3.99, "Bakery", False, 0)
    items_list.append(bagels)

    # Desserts
    cookie = Item("Cookie", 1.99, "Desserts", False, 0)
    items_list.append(cookie)
    cupcake = Item("Cupcake", 2.99, "Desserts", False, 0)
    items_list.append(cupcake)
    frosted_sugar_cookie = Item("Frosted Sugar Cookie", 4.99, "Desserts", False, 0)
    items_list.append(frosted_sugar_cookie)

    # Pharmacy
    pills = Item("Pills", 9.99, "Pharmacy", False, 0)
    items_list.append(pills)
    allergy_medicine = Item("Allergy Medicine", 14.99, "Pharmacy", False, 0)
    items_list.append(allergy_medicine)
    painkillers = Item("Painkillers", 19.99, "Pharmacy", False, 0)
    items_list.append(painkillers)

    # Electronics
    phone = Item("Phone", 599.99, "Electronics", False, 0)
    items_list.append(phone)
    tv = Item("Television", 150.99, "Electronics", False, 0)
    items_list.append(tv)
    watch = Item("Watch", 69.99, "Electronics", False, 0)
    items_list.append(watch)

    return items_list


def shopping():

    print("Welcome to my store!")
    print("The following categories for purchase are: Produce, Dairy, Meats, Clothing, "
          "Canned Items, Microwaveable meals, Drinks, Bakery, Desserts, Pharmacy, Electronics")

    print()
    print("To select a category, choose a number from 1 - 11 of the corresponding category that you want to buy.")

    is_shopping = True
    while is_shopping:

        print("1: Produce")
        print("2: Dairy")
        print("3: Meats")
        print("4: Clothing")
        print("5: Canned Items")
        print("6: Microwaveable Meals")
        print("7: Drinks")
        print("8: Bakery")
        print("9: Desserts")
        print("10: Pharmacy")
        print("11: Electronics")
        print("12: Finished Shopping")

        choice = input("Select number: ")
        print()

        if choice == '1':

            is_shopping = print_category_list("Produce")

        elif choice == '2':

            is_shopping = print_category_list("Dairy")

        elif choice == '3':

            is_shopping = print_category_list("Meats")

        elif choice == '4':

            is_shopping = print_category_list("Clothing")

        elif choice == '5':

            is_shopping = print_category_list("Canned Items")

        elif choice == '6':

            is_shopping = print_category_list("Microwaveable Meals")

        elif choice == '7':

            is_shopping = print_category_list("Drinks")

        elif choice == '8':

            is_shopping = print_category_list("Bakery")

        elif choice == '9':

            is_shopping = print_category_list("Desserts")

        elif choice == '10':

            is_shopping = print_category_list("Pharmacy")

        elif choice == '11':

            is_shopping = print_category_list("Electronics")

        elif choice == '12':

            is_shopping = False

        else:

            print("Choice not recognized, please use the correct numbers")

    customer.print_cart()

    checkout()


def print_category_list(category):

    temp_category_list = my_store.get_item_by_category(category)

    index_counter = 1
    for items in temp_category_list:
        print(index_counter, ":", items.get_item_name(), "---- ${0:.2f}".format(items.get_item_price()))

        index_counter += 1

    print(index_counter, ":", "Cancel")

    choice = input("Select number: ")
    print()

    if choice == '1':

        customer.add_item_to_cart(temp_category_list[0])
        print("Added", temp_category_list[0].get_item_name(), "to your cart")

    elif choice == '2':

        customer.add_item_to_cart(temp_category_list[1])
        print("Added", temp_category_list[1].get_item_name(), "to your cart")
        print()

    elif choice == '3':

        customer.add_item_to_cart(temp_category_list[2])
        print("Added", temp_category_list[2].get_item_name(), "to your cart")
        print()

    elif choice == '4':

        customer.add_item_to_cart(temp_category_list[3])
        print("Added", temp_category_list[3].get_item_name(), "to your cart")
        print()

    else:

        print("Invalid command, returning to main screen")

    choice = input("Continue shopping?: (y/n)")
    print()
    if choice == 'n':
        is_shopping = False
        return is_shopping

    return True


def checkout():

    total_price, total_tax = customer.get_cart_total()

    print("Your total is ${0:.2f}".format(total_price))
    print("Tax is: ${:.2f}".format(total_tax))

    choice = input("Would you like to continue with payment?: (y/n)")
    print()
    if choice == 'y':

        print("Payment Options:")
        print("1: Cash")
        print("2: Credit Card")
        choice = input("Select choice: ")
        print()

        if choice == '1':

            is_enough_cash = False
            while(not is_enough_cash):

                # Pay with cash
                cash = input("Enter the amount of cash you want to use: ")

                if cash.isdigit():

                    cash = float(cash)

                else:

                    index_of_decimal = cash.index('.')
                    #print(index_of_decimal)

                    first_half = cash
                    first_half = first_half[0:index_of_decimal]
                    second_half = cash
                    second_half = second_half[index_of_decimal + 1:len(cash)]

                    #print(first_half)
                    #print(second_half)

                    if first_half.isdigit():

                        if second_half.isdigit():

                            cash = float(cash)

                if cash >= total_price:

                    change = cash - total_price
                    is_enough_cash = True

                else:

                    print("Not enough cash")

            print("Your change is ${0:.2f}".format(change))
            print("Thank you for your purchase!")
            print()

            customer.set_payed_cash(True)

            print_recepit(cash, change)


        elif choice == '2':

            # Pay with credit card
            print("Thank you for your purchase!")
            print()

            customer.set_payed_card(True)

            print_recepit(None, None)

    elif choice == 'n':

        pass

    else:

        print("Command not recognized. ABORTING")

def print_recepit(cash, change):

    total, tax_total = customer.get_cart_total()

    print("\t\t\tCOSCTO")
    print("\t\t\t----WHOLESALE\n\n\n")

    for items in customer.get_cart_items():

        print("\t\t", items.get_item_name(), "\t\t\t\t${:.2f}".format(items.get_item_price()))

    print()
    print("\t\t\t   Subtotal\t\t${:.2f}".format(customer.get_cart_subtotal()))
    print("\t\t\t   {0:.2f}% Tax\t${1:.2f}".format((my_store.get_sales_tax() * 100), tax_total))
    print()
    #print("---------------------------------------------")
    print("\t\t\t   TOTAL\t\t{:.2f}".format(total))

    if customer.get_payed_cash():

        print("\t\t\t   CASH\t\t\t{:.2f}".format(cash))
        print("\t\t\t   CHANGE\t\t{:.2f}".format(change))

    else:

        print("\t\t\t   American Express\t\t${:.2f}".format(total))


customer = Customer()
my_store = Store(initialize_items())

shopping()
