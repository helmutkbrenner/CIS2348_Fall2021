#  Helmut Brenner  #
#  2037275  #

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print('{} {} @ ${:.0f} = ${:.0f}'.format(self.item_name, self.item_quantity, self.item_price,
                                                 (self.item_price * self.item_quantity)))


if __name__ == '__main__':
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print('Item 1')
    item1.item_name = str(input('Enter the item name:\n'))
    item1.item_price = float(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nItem 2')
    item2.item_name = str(input('Enter the item name:\n'))
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()

    print('\nTotal: ${:.0f}'.format((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)))
