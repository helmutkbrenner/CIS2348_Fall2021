#  Helmut Brenner  ##
#  2037275  ##

import csv
import string


class Item:
    #  Making an item class with the following attributes and methods:
    def __init__(self, item_id, manufacturer, item_type, damaged='undamaged', price=0, service_date=''):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.damaged = damaged
        self.price = price
        self.service_date = service_date


def add_prices(master_list, price_pairs):
    # This function is used to take the list of class objects and "append" the price onto the correct item entry
    for k in range(len(master_list)):
        j = 0
        while master_list[k].item_id != price_pairs[j][0]:
            j += 1
        master_list[k].price = price_pairs[j][1]
    return master_list


def add_service_dates(master_list, service_dates):
    for k in range(len(master_list)):
        j = 0
        while master_list[k].item_id != service_dates[j][0]:
            j += 1
        master_list[k].service_date = service_dates[j][1]
    return master_list


def print_tester(master_list):
    for h in range(7):
        #  TEST should produce the list as is
        print(master_list[h].item_id, master_list[h].manufacturer, master_list[h].item_type,
              master_list[h].damaged, master_list[h].price, master_list[h].service_date)
    print('\n')


def get_item_type_list(class_list_by_type):
    list_of_types = []
    for p in range(len(class_list_by_type)):
        if class_list_by_type[p].item_type not in list_of_types:
            list_of_types.append(class_list_by_type[p].item_type)
    return list_of_types


def file_name_formatter(type_list):
    formatted_list = [type.capitalize() + 'Inventory.csv' for type in type_list]
    return formatted_list


if __name__ == '__main__':
    with open('ManufacturerList.csv', 'r') as manufacturer_file:
        #  Opens the file and writes the contents to our class object Item, outputs to a master_item_list
        line_reader = csv.reader(manufacturer_file, delimiter=',')
        line_count = 0
        master_item_list = []
        for row in line_reader:
            master_item_list.append(Item(row[0], row[1], row[2], row[3]))
            line_count += 1

    with open('PriceList.csv', 'r') as price_list_file:
        #  Opens the Price list and saves the contents as a list of lists. The list is utilizes on line
        line_reader1 = csv.reader(price_list_file, delimiter=',')
        line_count1 = 0
        list_of_prices = []
        for row in line_reader1:
            list_of_prices.append([row[0], row[1]])
            line_count1 += 1

    with open('ServiceDatesList.csv', 'r') as service_dates_list_file:
        #  Opens service dates list and saves the service dates list as a list of lists similar to before
        line_reader2 = csv.reader(service_dates_list_file, delimiter=',')
        line_count2 = 0
        service_dates_list = []
        for row in line_reader2:
            service_dates_list.append([row[0], row[1]])
            line_count2 += 1

    #  This bit of code imports a special Operator function to sort the lists according to common attributes
    #  It even allows me to do two tier sorting, AMAZING.
    from operator import attrgetter
    sorted_by_manufacturer = sorted(master_item_list, key=attrgetter('manufacturer'))
    sorted_by_id = sorted(master_item_list, key=attrgetter('item_id'))
    sorted_by_type = sorted(master_item_list, key=attrgetter('item_type', 'item_id'))

    #  Adds the prices to the correct items in their respective object classes
    add_prices(sorted_by_id, list_of_prices)

    #  Adds the service dates to the correct items in their respective object classes
    add_service_dates(sorted_by_id, service_dates_list)

    with open('FullInventory.csv', 'w') as full_inventory:
        #  This piece of code creates the file FullInventory and writes the data in the required order.
        line_writer = csv.writer(full_inventory)

        for i in range(len(sorted_by_manufacturer)):
            line_writer.writerow([sorted_by_manufacturer[i].item_id, sorted_by_manufacturer[i].manufacturer,
                                  sorted_by_manufacturer[i].item_type, sorted_by_manufacturer[i].price,
                                  sorted_by_manufacturer[i].service_date, sorted_by_manufacturer[i].damaged])

    #  One list provides the formatting names for the file names, and the other provides a reference for all types
    #  encountered in the input files. Allows for scalability for any number of item types... Theoretically.

    ref_list_item_types = get_item_type_list(sorted_by_type)
    formatted_file_names = file_name_formatter(ref_list_item_types)

    for i in range(len(formatted_file_names)):
        # This piece of code takes a list of formatted file names and makes the appropriate files from the appropriate
        # data
        with open(formatted_file_names[i], 'w') as type_file:
            line_writer2 = csv.writer(type_file)
            for q in range(len(sorted_by_type)):
                if sorted_by_type[q].item_type == ref_list_item_types[i]:
                    line_writer2.writerow([sorted_by_type[q].item_id, sorted_by_type[q].manufacturer,
                                           sorted_by_type[q].price, sorted_by_type[q].service_date,
                                           sorted_by_type[q].damaged])

    print_tester(master_item_list)
    print_tester(sorted_by_manufacturer)
    print_tester(sorted_by_id)
    print_tester(sorted_by_type)
    print(ref_list_item_types)
    print(formatted_file_names)
