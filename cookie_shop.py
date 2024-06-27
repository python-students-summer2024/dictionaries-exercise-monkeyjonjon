"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""


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
        if '$' in cookie_price:
            cookie_price = cookie_price.replace('$', '')
        cookie['id'] = int(cookie_id)
        cookie['title'] = cookie_title
        cookie['description'] = cookie_description
        cookie['price'] = float(cookie_price)
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

def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    print("Here are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        cookie_id = cookie['id']
        cookie_name = cookie['title']
        cookie_description = cookie['description']
        cookie_price = cookie['price']
        cookie_price = format(cookie_price, '.2f')
        print(f"\t#{cookie_id} - {cookie_name}\n\t{cookie_description}\n\tPrice: ${cookie_price}\n")

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

def solicit_order(cookies):
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
        if id_input in cookie_id_list:
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
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
