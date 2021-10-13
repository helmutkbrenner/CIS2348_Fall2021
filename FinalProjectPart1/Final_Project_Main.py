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
    for i in range(7):
        #  TEST should produce the list as is
        print(master_list[i].item_id, master_list[i].manufacturer, master_list[i].item_type,
              master_list[i].damaged, master_list[i].price, master_list[i].service_date)
    print('\n')


if __name__ == '__main__':
    with open('ManufacturerList.csv', 'r') as manufacturer_file:
        #  Opens the file and writes the contents to our class object Item, outputs to a master_item_list
        line_reader = csv.reader(manufacturer_file, delimiter=',')
        line_count = 0
        master_item_list = []
        for row in line_reader:
            master_item_list.append(Item(row[0], row[1], row[2], row[3]))
            line_count += 1

    print_tester(master_item_list)

    with open('PriceList.csv', 'r') as price_list_file:
        #  Opens the Price list and saves the contents as a list of lists. The list is utilizes on line
        line_reader1 = csv.reader(price_list_file, delimiter=',')
        line_count1 = 0
        list_of_prices = []
        for row in line_reader1:
            list_of_prices.append([row[0], row[1]])
            line_count1 += 1

    for i in range(7):
        print(list_of_prices[i][0], list_of_prices[i][1])
    print('\n')

    with open('ServiceDatesList.csv', 'r') as service_dates_list_file:
        #  Opens
        line_reader2 = csv.reader(service_dates_list_file, delimiter=',')
        line_count2 = 0
        service_dates_list = []
        for row in line_reader2:
            service_dates_list.append([row[0], row[1]])
            line_count2 += 1

    for i in range(7):
        print(service_dates_list[i][0], service_dates_list[i][1])
    print('\n')

    #  This bit of code imports a special Operator function to reverse the lists according to common attributes
    from operator import attrgetter
    sorted_by_manufacturer = sorted(master_item_list, key=attrgetter('manufacturer'))
    sorted_by_id = sorted(master_item_list, key=attrgetter('item_id'))

    print_tester(sorted_by_manufacturer)

    print_tester(sorted_by_id)

    #  Adds the prices to the correct items in their respective object classes
    add_prices(sorted_by_id, list_of_prices)

    print_tester(sorted_by_id)

    #  Adds the service dates to the correct items in their respective object classes
    add_service_dates(sorted_by_id, service_dates_list)

    print_tester(sorted_by_id)
