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
    #  This statement checks for a double input by filtering unique inputs into query_list2. Will allow for double input
    # of brands and items that ARE in inventory. I see this as a feature lol.
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


def query_checker(clean_query_list, item_list_sorted_by_manufacturer):
    #  This function takes the cleaned query as a list of words. it also takes a list of item objects sorted by manufacturer
    #  that we sorted earlier. This function will return false if user entered multiple types or manufacturer. if the user
    # input is correct then it will check inventory to see if the combo is available, and will provide a list of matching
    # items as well as a true flag.
    verdict = False
    list_of_items = []

    if range(len(clean_query_list) == 2):
        manufacturer = clean_query_list[0]
        item_type = clean_query_list[1]

    #  This statement will check if Combo in inventory.
        for i in range(len(item_list_sorted_by_manufacturer)):
            if item_list_sorted_by_manufacturer[i].manufacturer == manufacturer and item_list_sorted_by_manufacturer[i].item_type == item_type:
                verdict = True
                list_of_items.append(item_list_sorted_by_manufacturer[i])
        return verdict, list_of_items
    return verdict, -1


def serv_damage_checker(found_item_object_list, past_serv_date_list):
    #  This function takes a list of parsed objects that meet the criteria of the original query,
    verdict = False
    from operator import attrgetter
    # here we sort the list of parsed objects so that they are sorted by price. This way the very first item that meets
    # the query criteria is always the priciest one.
    found_item_object_list1 = sorted(found_item_object_list, key=attrgetter('price'), reverse=True)

    # If only a single match is found in the database then this statement executes. It will compare the object to the
    # past service date lists and will then also check to see if the item is past service date or damaged.
    for i in range(len(found_item_object_list1)):
        if found_item_object_list1[i] not in past_serv_date_list and found_item_object_list1[i].damaged == '':
            verdict = True
            return verdict, found_item_object_list1[i]
    return verdict, found_item_object_list


def similar_item_finder(item_object2, sorted_by_type, past_serv_date_list):
    item_to_look_for = item_object2.item_type
    item_to_look_for_id = item_object2.item_id
    item_to_look_for_price = item_object2.price
    similar_items_list = []
    most_similar_item = None
    found_flag = False

    #  This statement searches through the list of class objects and appends items of the same type to similar_item_list
    for i in range(len(sorted_by_type)):
        if item_to_look_for == sorted_by_type[i].item_type and item_to_look_for_id != sorted_by_type[i].item_id:
            similar_items_list.append(sorted_by_type[i])

    # This statement will ensure that the returned item is the closest in price to the item_object2 and it is NOT the same
    #  manufacturer.
    smallest_differential = 99999
    for i in range(len(similar_items_list)):
        if similar_items_list[i].manufacturer != item_object2.manufacturer:
            if similar_items_list[i] not in past_serv_date_list and similar_items_list[i].damaged == '':
                differential = abs(item_to_look_for_price - similar_items_list[i].price)
                if differential < smallest_differential:
                    smallest_differential = differential
                    most_similar_item = similar_items_list[i]
                    found_flag = True

    if found_flag:
        return most_similar_item, found_flag

    return item_object2, found_flag
