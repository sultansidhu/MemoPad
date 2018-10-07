"""Server side file for the login-screen of project MemoPad."""
# ---------IMPORTS------------
import socket
import sqlite3

# ---------CONSTANTS-----------
connection_collection = []
address_collection = []
file = open("db_names.txt", "r")
stuff = file.read()
name_list = stuff.split("\n")
name_list.remove("")
# print(name_list)  [this print call was called as a checker]
file.close()

# --------- FILE MANAGEMENT ---------------


def write_to_file(string, file_name):
    """Writes string to file"""
    thefile = open(file_name, "r")
    stuff_in_file = thefile.read().split("\n")
    thefile.close()
    openedfile = open(file_name, "w")
    for things in stuff_in_file:
        openedfile.write(things)
        openedfile.write("\n")
    openedfile.write(string)
    openedfile.close()


# ----------SERVER SIDE FUNCTIONS-----------


def listen_for_data():
    """Listens for the data from the client. This function receives the login credentials."""
    sockett = socket.socket()
    host = "100.65.251.47"
    port = 9996
    # sockett.connect((host, port))
    sockett.bind((host, port))
    sockett.listen(5)
    conn, addr = sockett.accept()
    with conn:
        print("We are now connected: {}".format(addr[0]))
        while True:
            thedata = conn.recv(1024)
            if not thedata:
                break
            credentials = thedata.decode("utf-8")
            return credentials


# ---------DATABASE FUNCTIONS-----------


def display_all_db_names(db_names_list):
    """Displays all the taken db names."""
    for names in db_names_list:
        print(names, end="\n")


def create_db(name):
    """Creates the database, if there doesn't exist one already. Returns a cursor object."""
    database_name = name + ".db"
    db_conn = sqlite3.connect(database_name)
    cursor = db_conn.cursor()
    cursor.execute("""CREATE TABLE credential_database(
                        Name text, 
                        Username text, 
                        Password text)""")
    return cursor


def connect_to_db(name):
    """Connects to an already existing database. Returns a cursor object."""
    db_name = name + ".db"
    db_conn = sqlite3.connect(db_name)
    cursor = db_conn.cursor()
    return cursor


def add_data(name, username, password, cursor_object):
    """Adds a newly registered user to the database."""
    print("ADDING USER: " + username + "\n")
    cursor_object.execute("INSERT INTO credential_database VALUES(?, ?, ?)", (name, username, password))


def check_credentials(given_username, given_password, cursor_object):
    """Checks if the username and password supplied are credible credentials."""
    validity_bool = False
    index = 0
    cursor_object.execute("SELECT * FROM credential_database;")
    obtained_data = cursor_object.fetchall()
    for i in range(len(obtained_data)):
        if given_username in obtained_data[i]:
            validity_bool = True
            index = i
    # above code block will check if the username is present.
    if validity_bool is False:
        print("Please sign in as you are not registered in the database.")
    else:
        registered_password = obtained_data[index][2]
        if registered_password == given_password:
            return "True"
        else:
            print("Wrong credentials! Try again!")
            return "False"


def show_all_db_entries(cursor_obj):
    """Shows all entries currently in the database."""
    cursor_obj.execute("SELECT * FROM credential_database;")
    x = cursor_obj.fetchall()
    for y in x:
        print(y, end="\n\n")


def add_new_user(name, username, password, cursor_object):
    """Checks if the user is already in the database. If not, registers the new user."""
    validity_bool = False
    cursor_object.execute("SELECT * FROM credential_database;")
    obtained_data = cursor_object.fetchall()
    for i in range(len(obtained_data)):
        if username in obtained_data[i]:
            validity_bool = True
    # above code block will check if the username is present.
    if validity_bool is False:
        add_data(name, username, password, cursor_object)
    else:
        print("YOU ARE ALREADY REGISTERED. PLEASE TRY LOGGING IN.")


def delete_user(username, cursor_object):
    """Deletes the user with the specified username from the database."""
    print("DELETING USER: " + username)
    # stringg = "DELETE FROM credential_database WHERE Username = " + username + ";"
    cursor_object.execute("DELETE FROM credential_database WHERE Username = ?", (username,))


if __name__ == "__main__":

    # ------------ DATABASE ACTION STARTS NOW ----------------

    print("============== NETWORK STUFF ==============\n")

    print("SHOWING ALL TAKEN DATABASE NAMES...\n")
    if len(name_list) < 1:
        print("No databases currently exist.\n")

    else:
        display_all_db_names(name_list)
    print("Which database do you wish to connect with? ")
    given_database_name = input("It may be new or pre-existing. >>").lower().strip()
    if given_database_name not in name_list:
        write_to_file(given_database_name, "db_names.txt")
        db_cursor = create_db(given_database_name)
    else:
        db_cursor = connect_to_db(given_database_name)

# ----------- DATABASE MAIN CONTROLLER METHOD WAS PARSED ABOVE --------------

    add_new_user("sultan", "sultan123", "sidhuismypw", db_cursor)
    add_new_user("abhishek", "abhi123", "kapoorishispw", db_cursor)
    add_new_user("yosef", "yosef123", "leibmanishispw", db_cursor)
    add_new_user("tejbir", "tejbir123", "bhullarishispw", db_cursor)
    add_new_user("jun", "jun123", "junweiwong", db_cursor)
    add_new_user("utkarsh", "utkarsh123", "kickhimoutofuoft", db_cursor)

    show_all_db_entries(db_cursor)

    # now some defective calls

    add_new_user("sultan", "sultan123", "sidhuismypw", db_cursor)

    x = check_credentials("yosef123", "leibmanishispw", db_cursor)
    print(x)
    y = check_credentials("sultan123", "isabitch", db_cursor)
    print(y)
    delete_user("yosef123", db_cursor)
    add_new_user("yosef", "yosef123", "leibmanishispw", db_cursor)

    print("################# COMPLETE DATABASE BELOW ##################")
    show_all_db_entries(db_cursor)


# ------------ Sending queries back --------------

    query = check_credentials("yosef", "leibmanishispw", db_cursor)
    print(query)
