def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    cookies = []
    cookie_file = open(filepath, mode = 'r', encoding='utf-8')
    first_line = cookie_file.readline() # skips the first line
    for line in cookie_file: # iterates through the remaining lines one-by-one
        cookie = {}
        cookie_info_baked = []
        cookie_info = line.split(",") # splits by comma and returns a list
        for string in cookie_info: # washes the data
            string = string.strip()
            cookie_info_baked.append(string)
        cookie_id = cookie_info_baked[0]
        cookie_title = cookie_info_baked[1]
        if cookie_title[-1] != 's':
            cookie_title = cookie_title + 's'
        cookie_description = cookie_info_baked[2]
        cookie_price = cookie_info_baked[3]
        cookie_sugar_free = cookie_info_baked[4]
        cookie_gluten_free = cookie_info_baked[5]
        cookie_has_nuts = cookie_info_baked[6]
        if '$' in cookie_price:
            cookie_price = cookie_price.replace('$', '')
        cookie['id'] = int(cookie_id)
        cookie['title'] = cookie_title
        cookie['description'] = cookie_description
        cookie['price'] = float(cookie_price)
        cookie['sugar_free'] = int(cookie_sugar_free)
        cookie['gluten_free'] = int(cookie_gluten_free)
        cookie['contains_nuts'] = int(cookie_has_nuts)
        cookies.append(cookie) # appends the cookie dictionary to the list
    cookie_file.close()
    return cookies

def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("\nWelcome to the Python Cookie Shop!\nWe feed each according to their need.\n")

def get_dietary_restriction():
    print("We'd hate to trigger an allergic reaction in your body. So please answer the following questions:\n")
    allergies = {}
    asking_for_nut_allergy = True
    asking_for_gluten_allergy = True
    asking_for_diabetes = True
    while asking_for_nut_allergy:
        response_nuts = input("Are you allergic to nuts? ").strip().lower()
        if response_nuts in ['yes', 'no']:
            if response_nuts == 'yes':
                allergies['nut'] = 1
            elif response_nuts == 'no':
                allergies['nut'] = 0
            asking_for_nut_allergy = False
    while asking_for_gluten_allergy:
        response_gluten = input("Are you allergic to gluten? ").strip().lower()
        if response_gluten in ['yes', 'no']:
            if response_gluten == 'yes':
                allergies['gluten'] = 1
            elif response_gluten == 'no':
                allergies['gluten'] = 0
            asking_for_gluten_allergy = False
    while asking_for_diabetes:
        response_sugar = input("Do you suffer from diabetes? ").strip().lower()
        if response_sugar in ['yes', 'no']:
            if response_sugar == 'yes':
                allergies['sugar'] = 1
            elif response_sugar == 'no':
                allergies['sugar'] = 0
            asking_for_diabetes = False
    return allergies

def display_suitable_cookies(allergies, cookies):
    # write your code for this function below this line
    cookie_counter = 0
    found_cookies = True
    return_values = []
    acceptable_cookies = []
    nut_allergy = allergies['nut']
    gluten_allergy = allergies['gluten']
    diabetes = allergies['sugar']

    if nut_allergy + gluten_allergy + diabetes > 0:
        if nut_allergy + gluten_allergy + diabetes == 3:
            print("Here are the cookies without nuts, gluten nor sugar that we think you might like:\n")
            for cookie in cookies:
                if cookie['contains_nuts'] == 0 and cookie['sugar_free'] == 1 and cookie['gluten_free'] == 1:
                    cookie_counter += 1
                    cookie_id = cookie['id']
                    cookie_name = cookie['title']
                    cookie_description = cookie['description']
                    cookie_price = cookie['price']
                    cookie_price = format(cookie_price, '.2f')
                    acceptable_cookies.append(cookie_id)
                    print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")

        elif nut_allergy + gluten_allergy + diabetes == 2:
            allergy_message = "Here are the cookies without {} or {} that we think you might like:\n"
            if nut_allergy == 1 and gluten_allergy == 1:
                print(allergy_message.format('nuts', 'gluten'))
                for cookie in cookies:
                    if cookie['contains_nuts'] == 0 and cookie['gluten_free'] == 1:
                        cookie_counter += 1
                        cookie_id = cookie['id']
                        cookie_name = cookie['title']
                        cookie_description = cookie['description']
                        cookie_price = cookie['price']
                        cookie_price = format(cookie_price, '.2f')
                        acceptable_cookies.append(cookie_id)
                        print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")
            elif nut_allergy == 1 and diabetes == 1:
                print(allergy_message.format('nuts', 'sugar'))
                for cookie in cookies:
                    if cookie['contains_nuts'] == 0 and cookie['gluten_free'] == 1:
                        cookie_counter += 1
                        cookie_id = cookie['id']
                        cookie_name = cookie['title']
                        cookie_description = cookie['description']
                        cookie_price = cookie['price']
                        cookie_price = format(cookie_price, '.2f')
                        acceptable_cookies.append(cookie_id)
                        print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")
            elif gluten_allergy == 1 and diabetes == 1:
                print(allergy_message.format('gluten', 'sugar'))
                for cookie in cookies:
                    if cookie['contains_nuts'] == 0 and cookie['gluten_free'] == 1:
                        cookie_counter += 1
                        cookie_id = cookie['id']
                        cookie_name = cookie['title']
                        cookie_description = cookie['description']
                        cookie_price = cookie['price']
                        cookie_price = format(cookie_price, '.2f')
                        acceptable_cookies.append(cookie_id)
                        print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")

        elif nut_allergy + gluten_allergy + diabetes == 1:
            allergy_message = "Here are the cookies without {} that we think you might like:\n"
            if nut_allergy == 1:
                print(allergy_message.format('nuts'))
                for cookie in cookies:
                    if cookie['contains_nuts'] == 0:
                        cookie_counter += 1
                        cookie_id = cookie['id']
                        cookie_name = cookie['title']
                        cookie_description = cookie['description']
                        cookie_price = cookie['price']
                        cookie_price = format(cookie_price, '.2f')
                        acceptable_cookies.append(cookie_id)
                        print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")
            elif gluten_allergy == 1:
                print(allergy_message.format('gluten'))
                for cookie in cookies:
                    if cookie['gluten_free'] == 1:
                        cookie_counter += 1
                        cookie_id = cookie['id']
                        cookie_name = cookie['title']
                        cookie_description = cookie['description']
                        cookie_price = cookie['price']
                        cookie_price = format(cookie_price, '.2f')
                        acceptable_cookies.append(cookie_id)
                        print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")
            elif diabetes == 1:
                print(allergy_message.format('sugar'))
                for cookie in cookies:
                    if cookie['sugar_free'] == 1:
                        cookie_counter += 1
                        cookie_id = cookie['id']
                        cookie_name = cookie['title']
                        cookie_description = cookie['description']
                        cookie_price = cookie['price']
                        cookie_price = format(cookie_price, '.2f')
                        acceptable_cookies.append(cookie_id)
                        print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")
        
        if cookie_counter == 0:
            print("We couldn't find any! Sorry\n")
            found_cookies = False

    else:
        print("Here are the cookies we have in the shop for you:\n")
        for cookie in cookies:
            cookie_id = cookie['id']
            cookie_name = cookie['title']
            cookie_description = cookie['description']
            cookie_price = cookie['price']
            cookie_price = format(cookie_price, '.2f')
            acceptable_cookies.append(cookie_id)
            print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")
    return_values.append(found_cookies)
    return_values.append(acceptable_cookies)
    return return_values

def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    for cookie in cookies:
        if cookie['id'] == id:
            desired_cookie = cookie
    return desired_cookie

def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line
    getting_quantity = True
    cookie = get_cookie_from_dict(id, cookies)
    cookie_title = cookie['title']
    cookie_price = cookie['price']
    while getting_quantity:
        quantity_input = input(f"\nMy favorite! How many {cookie_title} would you like? ")
        if quantity_input.isdigit():
            cookie_quantity = int(quantity_input)
            getting_quantity = False
    total_price = cookie_price * cookie_quantity
    total_price = format(total_price, '.2f')
    if cookie_quantity == 1:
        if cookie_title[-1] == 's':
            cookie_title = cookie_title[:-1]
        print(f"Your subtotal for 1 {cookie_title} is ${total_price}.\n")
    else:
        print(f"Your subtotal for {cookie_quantity} {cookie_title} is ${total_price}.\n")
    return cookie_quantity

def solicit_order(cookies, acceptable_cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    getting_order = True
    order = []
    cookie_id_list = []
    abort_order = ['finished', 'done', 'quit', 'exit']
    for cookie in cookies:
        cookie_id = cookie['id']
        cookie_id_list.append(cookie_id)
    while getting_order:
        id_input = input("Please enter the id of the cookie you want. ")
        if id_input.isdigit():
            id_input = int(id_input)
        if id_input in cookie_id_list and id_input in acceptable_cookies:
            sub_order = {}
            cookie_quantity = solicit_quantity(id_input, cookies)
            sub_order['id'] = id_input
            sub_order['quantity'] = cookie_quantity
            order.append(sub_order)
        elif id_input in abort_order:
            getting_order = False
            return order

def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line
    total_cost = 0
    print("\nThank you for your order. You have ordered:\n")
    for sub_order in order:
        cookie_id = sub_order['id']
        cookie_quantity = sub_order['quantity']
        cookie = get_cookie_from_dict(cookie_id, cookies)
        cookie_name = cookie['title']
        cookie_price = cookie['price']
        total_cost += cookie_price * cookie_quantity
        if cookie_quantity == 1:
            if cookie_title[-1] == 's':
                cookie_title = cookie_title[:-1]
            print(f"-{cookie_quantity} {cookie_name}")
        else:
            print(f"-{cookie_quantity} {cookie_name}")
    total_cost = format(total_cost, '.2f')
    print(f"Your total is ${total_cost}.\nPlease pay with Bitcoin before picking-up.\n")
    print("Thank you!\n-The Python Cookie Shop Robot.\n")


def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    allergies = get_dietary_restriction()
    find_cookies = display_suitable_cookies(allergies, cookies)
    found_cookies = find_cookies[0]
    acceptable_cookies = find_cookies[1]
    if found_cookies:
        order = solicit_order(cookies, acceptable_cookies)
        display_order_total(order, cookies)

        
        