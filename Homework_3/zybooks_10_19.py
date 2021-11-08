#  Helmut Brenner  #
#  2037275  #

class ItemToPurchase:
    #  Class constructor
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    #  Prints the cost equation
    def print_item_cost(self):
        print('{} {} @ ${:.0f} = ${:.0f}'.format(self.item_name, self.item_quantity, self.item_price,
                                                 (self.item_price * self.item_quantity)))

    #  Prints item name and item description
    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))


class ShoppingCart:
    #  Class constructor for a shopping cart object.
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    #  takes a item object and adds it to the shopping cart cart_item list.
    def add_item(self, item_object):
        self.cart_items.append(item_object)

    #  Takes a name of an item and finds/removes it from the cart.
    def remove_item(self, item_name):
        found_flag = False
        for i in range(len(self.cart_items)):
            if item_name == self.cart_items[i].item_name:
                del self.cart_items[i]
                found_flag = True
                break
        if not found_flag:
            print('Item not found in cart. Nothing removed.')

    #  similar logic to the above function, takes a object item and a new quantity and assigns the quantity if found.
    def modify_item(self, item_name, new_quantity):
        found_flag = False
        for i in range(len(self.cart_items)):
            if item_name == self.cart_items[i].item_name:
                self.cart_items[i].item_quantity = new_quantity
                found_flag = True
                break
        if not found_flag:
            print('Item not found in cart. Nothing modified.')

    # returns the quantity of all items in the cart
    def get_num_items_in_cart(self):
        total_items = 0
        for i in range(len(self.cart_items)):
            total_items += self.cart_items[i].item_quantity
        return total_items

    #  Retrieve and totals the cost of items in the cart according to the quantity chosen
    def get_cost_of_cart(self):
        total_cost = 0
        for i in range(len(self.cart_items)):
            total_cost += (self.cart_items[i].item_quantity * self.cart_items[i].item_price)
        return total_cost

    # uses the function get_cost_of_cart and then prints it. Alternate message if cart is empty.
    def print_total(self):
        if self.get_cost_of_cart() == 0:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
            print('SHOPPING CART IS EMPTY\n')
            print('Total: ${}'.format(self.get_cost_of_cart()))
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))

            for k in range(len(self.cart_items)):
                print('{} {} @ ${:.0f} = ${:.0f}'.format(self.cart_items[k].item_name, self.cart_items[k].item_quantity,
                                                         self.cart_items[k].item_price,
                                                         (self.cart_items[k].item_price * self.cart_items[k].item_quantity)))
            print('\nTotal: ${}'.format(self.get_cost_of_cart()))

    # Prints a list of the items in the cart and their quantities.
    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('\nItem Descriptions')
        for j in range(len(self.cart_items)):
            print('{}: {}'.format(self.cart_items[j].item_name, self.cart_items[j].item_description))


def print_menu():
    #  Prints the main menu
    print('\nMENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit\n')


if __name__ == '__main__':
    #  Get customer input for shopping cart object
    customer_input_name = str(input('Enter customer\'s name:\n'))
    customer_input_date = str(input('Enter today\'s date:\n'))

    #  Output the information given
    print('\nCustomer name: {}'.format(customer_input_name))
    print('Today\'s date: {}'.format(customer_input_date))

    #  Make a shopping class object with given info
    shopping_cart1 = ShoppingCart(customer_input_name, customer_input_date)

    #  This is the main part of the interface where required information is gotten and
    user_command = ''
    print_menu()
    while user_command != 'q':
        user_command = str(input('Choose an option:\n'))
        if user_command == 'a':
            print('ADD ITEM TO CART')
            item_name1 = str(input('Enter the item name:\n'))
            item_description1 = str(input('Enter the item description:\n'))
            item_price1 = int(input('Enter the item price:\n'))
            item_quantity1 = int(input('Enter the item quantity:\n'))
            shopping_cart1.add_item((ItemToPurchase(item_name1, item_price1, item_quantity1, item_description1)))
            print_menu()
            continue
        elif user_command == 'o':
            print('OUTPUT SHOPPING CART')
            shopping_cart1.print_total()
            print_menu()
            continue
        elif user_command == 'i':
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            shopping_cart1.print_descriptions()
            print_menu()
            continue
        elif user_command == 'r':
            print('REMOVE ITEM FROM CART')
            shopping_cart1.remove_item(str(input('Enter name of item to remove:\n')))
            print_menu()
            continue
        elif user_command == 'c':
            print('CHANGE ITEM QUANTITY')
            item_name3 = str(input('Enter the item name:\n'))
            desired_quantity = int(input('Enter the new quantity:\n'))
            shopping_cart1.modify_item(item_name3, desired_quantity)
            print_menu()
            continue
        else:
            #  This might be a cheesy way to re prompt, but it works.
            continue
