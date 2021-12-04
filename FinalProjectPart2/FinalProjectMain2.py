#  Helmut Brenner  #
#  2037275  #

import csv
import string
import FinalProjectFunc2


if __name__ == '__main__':
    with open('ManufacturerList.csv', 'r') as manufacturer_file:
        #  Opens the file and writes the contents to our class constructor Item, outputs to a master_item_list
        line_reader = csv.reader(manufacturer_file, delimiter=',')
        line_count = 0
        master_item_list = []
        for row in line_reader:
            master_item_list.append(FinalProjectFunc2.Item(row[0], row[1], row[2], row[3]))
            line_count += 1

    with open('PriceList.csv', 'r') as price_list_file:
        #  Opens the Price list and saves the contents as a list of lists. The list is utilized in the add prices func.
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

    #  Adds the prices to the correct items in their respective object classes
    FinalProjectFunc2.add_prices(master_item_list, list_of_prices)

    #  Adds the service dates to the correct items in their respective object classes
    FinalProjectFunc2.add_service_dates(master_item_list, service_dates_list)

    #  This bit of code imports a special Operator function to sort the lists according to common attributes
    #  It even allows me to do two tier sorting, AMAZING.

    from operator import attrgetter
    sorted_by_manufacturer = sorted(master_item_list, key=attrgetter('manufacturer'))
    sorted_by_id = sorted(master_item_list, key=attrgetter('item_id'))
    sorted_by_type = sorted(master_item_list, key=attrgetter('item_type', 'item_id'))
    sorted_by_price = sorted(master_item_list, key=attrgetter('price'), reverse=True)

    with open('FullInventory.csv', 'w') as full_inventory:
        #  This piece of code creates the file FullInventory and writes the data in the required order.
        line_writer = csv.writer(full_inventory)

        for i in range(len(sorted_by_manufacturer)):
            line_writer.writerow([sorted_by_manufacturer[i].item_id, sorted_by_manufacturer[i].manufacturer,
                                  sorted_by_manufacturer[i].item_type, sorted_by_manufacturer[i].price,
                                  sorted_by_manufacturer[i].service_date, sorted_by_manufacturer[i].damaged])

    #  One list provides the formatting names for the file names, and the other provides a reference for all types
    #  encountered in the input files. Allows for scalability for any number of item types... Theoretically.

    ref_list_item_types = FinalProjectFunc2.get_item_type_list(sorted_by_type)
    formatted_file_names = FinalProjectFunc2.file_name_formatter(ref_list_item_types)

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

    # This piece of code will scan the sorted class objects by service date and add them to a list if they are past due.
    # It will also add a class object to the list if the service date and current date are the same.

    from datetime import datetime
    today_date = datetime.now()
    past_serv_date_list = []

    #  This piece of code checks to make sure that the service date is before today's date and transforms the date into
    #  a datetime object.
    for m in range(len(sorted_by_price)):
        sorted_by_price[m].service_date = datetime.strptime(sorted_by_price[m].service_date, '%m/%d/%Y')
        if sorted_by_price[m].service_date < today_date:
            past_serv_date_list.append(sorted_by_price[m])

    # Sort the list of class objects by date, once the dates are datetime objects the comparison is done by sorted()
    sorted_dates_list = sorted(past_serv_date_list, key=attrgetter('service_date'))

    # Here we use a csv writer to write the appropriate attributes from the list of class objects we just sorted above.
    # I used the datetime formatting codes to output the correctly formatted dates to the csv file.
    with open('PastServiceDateInventory.csv', 'w') as service_dates_file:
        line_writer3 = csv.writer(service_dates_file)
        for o in range(len(sorted_dates_list)):
            line_writer3.writerow([sorted_dates_list[o].item_id, sorted_dates_list[o].manufacturer,
                                   sorted_dates_list[o].item_type, sorted_dates_list[o].price,
                                   sorted_dates_list[o].service_date.strftime('%m/%d/%Y'),
                                   sorted_dates_list[o].damaged])

    # This is where we find damaged items and write them to their own file.
    with open('DamagedInventory.csv', 'w') as damaged_items_file:
        line_writer4 = csv.writer(damaged_items_file)
        for o in range(len(sorted_by_price)):
            if sorted_by_price[o].damaged != '':
                line_writer4.writerow([sorted_by_price[o].item_id, sorted_by_price[o].manufacturer,
                                       sorted_by_price[o].item_type, sorted_by_price[o].price,
                                       sorted_by_price[o].service_date.strftime('%m/%d/%Y')])

    #  Gonna need a list of brands later to strip user input of extraneous words
    brands = FinalProjectFunc2.get_list_of_brands(sorted_by_manufacturer)

    user_input = ''
    item_object = -1
    while user_input != 'q':
        # This statement gets the user input using a function and assigns to user query. Then user query is cleaned by
        # the query parser function which uses a list of all the brands and types in inventory to look for relevant words.
        user_query = FinalProjectFunc2.query_for_manufacturer_type()
        clean_user_query = FinalProjectFunc2.query_parser(user_query, brands, ref_list_item_types)

        # checks to make sure that the clean user query is IN inventory and that the user entered a single Manufacturer
        # and a single item type.
        user_query_verdict, item_object = FinalProjectFunc2.query_checker(clean_user_query, sorted_by_manufacturer)

        # if the above function returns a false flag then this print statement executes and re-prompts the user.
        if not user_query_verdict:
            print('No such item in inventory')
            continue

        #  With a list of class objects we got from inventory, the function statement below will see if any of the items
        #  that match the query are past service date or damaged. it will return a false flag if any or all of the items
        #  are damaged or past service date. It will return a True flag when a non-damaged and non-past due item is found.
        #  if multiple items are found, the priciest one will automatically be chosen.
        user_query_verdict2, item_object2 = FinalProjectFunc2.serv_damage_checker(item_object, past_serv_date_list)
        if not user_query_verdict2:
            print('The item you are looking for is past its service date or damaged')
            continue

        # This checks the user_query_verdict and user_query_verdict2. Both must be true to print the statement with the
        # user's query retrieved. item_object2 is the class object that the user is looking for.
        if user_query_verdict is True and user_query_verdict2 is True:
            print('Your item is: {} {} {} ${}'.format(item_object2.item_id, item_object2.manufacturer, item_object2.item_type,
                                                      item_object2.price))

        most_similar_item, user_query_verdict3 = FinalProjectFunc2.similar_item_finder(item_object2, sorted_by_type,
                                                                                       past_serv_date_list)

        if user_query_verdict3:
            print('You may also consider: {} {} {} ${}'.format(most_similar_item.item_id, most_similar_item.manufacturer,
                                                               most_similar_item.item_type, most_similar_item.price))

        #  This statement will allow the user to quit the program or enter a new query.
        if user_query_verdict2:
            user_input = input('Press any key to query again. Or press \'q\' to exit.\n')
            continue
