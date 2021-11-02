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

    def add_item(self, item_object):
        self.cart_items.append(item_object)

    def remove_item(self, item_name):
        # TODO
        for i in range(len(self.cart_items)):
            if item_name == self.cart_items[i].item_name:
                del self.cart_items[i]
                break
            print('Item not found in cart. Nothing removed.')


if __name__ == '__main__':
    test1 = ItemToPurchase('Nike Romaleos', 189, 2, 'Volt color, Weightlifting shoes')
    test2 = ItemToPurchase('Chocolate Chips', 3, 5, 'Semi-Sweet')

    test1.print_item_description()
    test1.print_item_cost()
    test2.print_item_description()
    test2.print_item_cost()

    shopping_cart1 = ShoppingCart('Helmut Brenner', 'November 2, 2021')
    shopping_cart1.add_item(test1)
    shopping_cart1.add_item(test2)

    print(shopping_cart1.cart_items)

    shopping_cart1.remove_item('Chocolate Chips')

    print(shopping_cart1.cart_items[0].item_name)

    print(shopping_cart1.cart_items)
