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
    def modify_item(self, item_object, new_quantity):
        found_flag = False
        for i in range(len(self.cart_items)):
            if item_object == self.cart_items[i]:
                self.cart_items[i].item_quantity = new_quantity
                found_flag = True
                break
        if not found_flag:
            print('Item not found in cart. Nothing modified')


if __name__ == '__main__':
    test1 = ItemToPurchase('Nike Romaleos', 189, 2, 'Volt color, Weightlifting shoes')
    test2 = ItemToPurchase('Chocolate Chips', 3, 5, 'Semi-Sweet')
    test3 = ItemToPurchase('RTX 3090', 1399, 1, 'Top of the line graphics card')

    shopping_cart1 = ShoppingCart('Helmut Brenner', 'November 2, 2021')
    shopping_cart1.add_item(test1)
    shopping_cart1.add_item(test2)
    shopping_cart1.add_item(test3)

    print(shopping_cart1.cart_items)
    shopping_cart1.modify_item(shopping_cart1.cart_items[2], 5)
    print(shopping_cart1.cart_items[2].item_quantity)
