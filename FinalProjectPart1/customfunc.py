#  Helmut Brenner  #
#  2037275  #

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
