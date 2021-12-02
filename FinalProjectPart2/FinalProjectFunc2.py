#  Helmut Brenner  #
#  2037275  #

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
    # This function is used to take the list of class objects and "append" the price onto the correct item entry. Upon
    #  second looks, I know these search algos are NOT efficient, maybe room for improvement on part 2 of the project?
    for k in range(len(master_list)):
        j = 0
        while master_list[k].item_id != price_pairs[j][0]:
            j += 1
        master_list[k].price = int(price_pairs[j][1])
    return master_list


def add_service_dates(master_list, service_dates):
    #  Basic same functionality as the add_prices function above.
    for k in range(len(master_list)):
        j = 0
        while master_list[k].item_id != service_dates[j][0]:
            j += 1
        master_list[k].service_date = service_dates[j][1]
    return master_list


def print_tester(master_list):
    for h in range(len(master_list)):
        #  TEST  function that was used to verify the sorting of the class object lists
        print(master_list[h].item_id, master_list[h].manufacturer, master_list[h].item_type,
              master_list[h].damaged, master_list[h].price, master_list[h].service_date)
    print('\n')


def get_item_type_list(class_list_by_type):
    #  Gets a list of all the item types, without repeats for reference in the main program.
    list_of_types = []
    for p in range(len(class_list_by_type)):
        if class_list_by_type[p].item_type not in list_of_types:
            list_of_types.append(class_list_by_type[p].item_type)
    return list_of_types


def file_name_formatter(type_list):
    # List comprehension is POG
    from string import capwords
    formatted_list = [type.capitalize() + 'Inventory.csv' for type in type_list]
    return formatted_list


def get_list_of_brands(class_list_by_brand):
    #  Gets a list of all the brands, without repeats for reference in the main program. Will be used to strip extra
    #  words from the user input.
    list_of_brands = []
    for p in range(len(class_list_by_brand)):
        if class_list_by_brand[p].manufacturer not in list_of_brands:
            list_of_brands.append(class_list_by_brand[p].manufacturer)
    return list_of_brands


def query_for_manufacturer_type():
    #  This function will get the user query. and return a list of the results.
    qd_manufacturer_item_type = input('What Manufacturer and Item Type are you looking for?\n').split()
    return qd_manufacturer_item_type


def query_parser(query_list, brands, types):
    # This function will parse the query list for relevant words. and check to make sure man. or item_type was not entered
    # twice.
    query_list1 = []
    query_list2 = []
    query_list3 = []
    #  This statement checks for relevant words and adds them to query_list1
    for i in range(len(query_list)):
        if query_list[i] in brands:
            query_list1.append(query_list[i])
        elif query_list[i] in types:
            query_list1.append(query_list[i])
    #  This statement checks for a double input by filtering unique inputs into query_list2
    for i in range(len(query_list1)):
        if query_list1[i] not in query_list2:
            query_list2.append(query_list1[i])
    #  This statement ensures proper order of the entries and adds them to query_list3
    for i in range(len(query_list2)):
        if query_list2[i] in brands:
            query_list3.insert(0, query_list2[i])
        elif query_list2[i] in types:
            query_list3.append(query_list2[i])
    return query_list3





#  def query_checker(query_list):
    # This function will check the query for a number of exceptional inputs. #1 Manufacturer or Item type NOT in
    # inventory. #2 more than one type or manufacturer entered #3 Combo NOT in inventory. It must also strip excess words
    # that are not a brand or an item type. Gonna break this down.


#  def inventory_check(manufacturer, item_type):
