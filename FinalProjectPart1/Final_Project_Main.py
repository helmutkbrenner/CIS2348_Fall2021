#  Helmut Brenner  ##
#  2037275  ##

import csv


class Item:
    #  Making an item class with the following attributes and methods:
    def __init__(self, item_id, manufacturer, item_type, damaged='undamaged', price=0, service_date=''):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.damaged = damaged
        self.price = price
        self.service_date = service_date

    def __repr__(self):
        return repr((sel.item_id, self.manufacturer, self.item_type, self.damaged))


if __name__ == '__main__':
    with open('ManufacturerList.csv', 'r') as manufacturer_file:
        #  Opens the file and writes the contents to our class object Item, outputs to a master_item_list
        line_reader = csv.reader(manufacturer_file, delimiter=',')
        line_count = 0
        master_item_list = []
        for row in line_reader:
            master_item_list.append(Item(row[0], row[1], row[2], row[3]))
            line_count += 1

    for i in range(7):
        #  TEST should produce the list as is
        print(master_item_list[i].item_id, master_item_list[i].manufacturer, master_item_list[i].item_type,
              master_item_list[i].damaged)
    print('\n')

    #  This bit of code imports a special Operator function to reverse the lists according to common attributes
    from operator import attrgetter
    sorted_by_manufacturer = sorted(master_item_list, key=attrgetter('manufacturer'))
    sorted_by_id = sorted(master_item_list, key=attrgetter('item_id'))

    for i in range(7):
        #  TEST should produce the list sorted by manufacturer
        print(sorted_by_manufacturer[i].item_id, sorted_by_manufacturer[i].manufacturer,
              sorted_by_manufacturer[i].item_type, sorted_by_manufacturer[i].damaged)

    print('\n')

    for i in range(7):
        #  TEST should produce the list sorted by id
        print(sorted_by_id[i].item_id, sorted_by_id[i].manufacturer, sorted_by_id[i].item_type, sorted_by_id[i].damaged)

