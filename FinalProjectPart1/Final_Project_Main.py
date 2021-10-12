#  Helmut Brenner  ##
#  2037275  ##

import csv

##  Making an item class with the following attributes and methods:
class Item:
    def __init__(self, item_id, manufacturer, item_type, damaged='undamaged', price=0, service_date=''):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.damaged = damaged
        self.price = price
        self.service_date = service_date


if __name__ == '__main__':
    with open('ManufacturersList.csv', 'r') as manufacturerfile:
        line_reader = csv.reader(manufacturerfile, delimiter=',')
        line_count= 0
        mega_item_list = []  ## fill a list with the custom class objects?
        for row in line_reader????:
            mega_item_list[line_count] = Item(row[0],row[1],row[2], row[3])
