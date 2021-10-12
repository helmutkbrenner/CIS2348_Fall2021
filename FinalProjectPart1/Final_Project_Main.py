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
        line_reader = csv.reader(manufacturer_file, delimiter=',')
        line_count = 0
        master_item_list = []  # fill a list with the custom class objects?
        for row in line_reader:
            master_item_list.append(Item(row[0], row[1], row[2], row[3]))
            line_count += 1
    print(master_item_list[0].item_id, master_item_list[0].manufacturer, master_item_list[0].item_type,
          master_item_list[0].damaged)
    print(master_item_list[1].item_id, master_item_list[1].manufacturer, master_item_list[1].item_type,
          master_item_list[1].damaged)
    print(master_item_list[2].item_id, master_item_list[2].manufacturer, master_item_list[2].item_type,
          master_item_list[2].damaged)
    print(master_item_list[3].item_id, master_item_list[3].manufacturer, master_item_list[3].item_type,
          master_item_list[3].damaged)
    print(master_item_list[4].item_id, master_item_list[4].manufacturer, master_item_list[4].item_type,
          master_item_list[4].damaged)
    print('\n')
    from operator import attrgetter
    master_item_list = sorted(master_item_list, key=attrgetter('manufacturer'))
    sorted_by_id = sorted(master_item_list, key=attrgetter('item_id'))

    print(master_item_list[0].item_id, master_item_list[0].manufacturer, master_item_list[0].item_type,
          master_item_list[0].damaged)
    print(master_item_list[1].item_id, master_item_list[1].manufacturer, master_item_list[1].item_type,
          master_item_list[1].damaged)
    print(master_item_list[2].item_id, master_item_list[2].manufacturer, master_item_list[2].item_type,
          master_item_list[2].damaged)
    print(master_item_list[3].item_id, master_item_list[3].manufacturer, master_item_list[3].item_type,
          master_item_list[3].damaged)
    print(master_item_list[4].item_id, master_item_list[4].manufacturer, master_item_list[4].item_type,
          master_item_list[4].damaged)
    print('\n')

    for i in range(5):
        print(sorted_by_id[i].item_id)
