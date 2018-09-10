"""Server side file for the login-screen of project MemoPad."""
# ---------IMPORTS------------
import socket
import sqlite3

# ---------CONSTANTS-----------
connection_collection = []
address_collection = []
database_exists = False

# ----------SERVER SIDE FUNCTIONS-----------


# def create_socket():
#     """Creates a socket to establish connection between the server and client."""
#     try:
#         global host  # the host IP address
#         global port  # the port over which connection will be done
#         global sockett
#
#         host = ""
#         port = 9999
#         sockett = socket.socket()
#
#     except socket.error as msg:
#         print("Error creating the socket. \nError: {}".format(str(msg)))
#
#
# def bind_socket():
#     """A function that binds the sockets and listens for connections."""
#     try:
#         global host
#         global port
#         global sockett
#         # these globals need redeclaration because their values need to be accessed from within another function.
#
#         print("Binding the port: {}".format(port))
#         sockett.bind((host, port))
#         sockett.listen(10)
#
#     except socket.error as msg:
#         print("Error occurred while binding the socket.\nError: {}  \nRETRYING...".format(str(msg)))
#         bind_socket()
#
#
# def accept_connections():
#     """Accepts the connections that are attempting connection."""
#     number = 9054512999
#     for conn in connection_collection:
#         conn.close()
#
#     del connection_collection[:]
#     del address_collection[:]
#
#     while True:
#         try:
#             conn, address = sockett.accept()
#             sockett.setblocking(1)
#             # this prevents timeout.
#
#             connection_collection.append(conn)
#             address_collection.append(address)
#
#             print("Connection has been established!  ||  {}".format(address[0]))
#         except:
#             print("Error accepting connections.")


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
        print("YA WE CONNNECTED BITCH: {}".format(addr[0]))
        while True:
            thedata = conn.recv(1024)
            if not thedata:
                break
            credentials = thedata.decode("utf-8")
            return credentials
    # while True:
    #     data = sockett.recv(1024)
    #     print(data)
    #     if len(data) > 0:
    #         credentials = data.decode("utf-8")
    #         return credentials

# ---------DATABASE FUNCTIONS-----------


def check_db_status(existence_bool):  # TODO: THIS FUNCTION WOULD NOT ALTER THE EXISTENCE BOOL, ALTER THIS FUNCTION.
    """Checks the existence of a database and connects to a pre-existing database,
    or creates and connects to a new one."""
    name = input("Please enter the name of the database you're connecting with? ").strip().lower()
    if existence_bool:
        try:
            print("Attempting connection to pre-existing database...")
            connect_to_db(name)
            print("Connection secured!")
        except:
            print("Error connecting!")
    else:
        try:
            print("Attempting to create and connect to new database...")
            create_db(name)
            print("Connection secured!")
        except:
            print("Error creating new database!")


def create_db(name):  # MIGHT HAVE TO TAKE THIS OUT OF A FUNCTION AND MAKE IT A LOCALLY EXECUTED CODE BLOCK.
    """Creates the database, if there doesn't exist one already. Returns a cursor object."""
    database_name = name + ".db"
    db_conn = sqlite3.connect(database_name)
    cursor = db_conn.cursor()
    cursor.execute("""CREATE TABLE credential_database(
                        Name text, 
                        Username text, 
                        Password text""")
    return cursor


def connect_to_db(name):
    """Connects to an already existing database. Returns a cursor object."""
    db_name = name + ".db"
    db_conn = sqlite3.connect(db_name)
    cursor = db_conn.cursor()
    return cursor


def add_data(name, username, password, cursor_object):
    """Adds a newly registered user to the database."""
    cursor_object.execute("INSERT INTO credential_database VALUES(?, ?, ?)", (name, username, password))


def check_credentials(given_username, given_password, cursor_object):
    """Checks if the username and password supplied are credible credentials."""
    cursor_object.execute("SELECT * FROM credential_database WHERE username = (?);", (given_username))
    credentials = cursor_object.fetchall()
    for detail in credentials:
        print(detail, end="\n")
    # NEXT PART WOULD NEED SOME CORRECTIONS DEPENDING ON THE USER ENTERED DATA.
    le_password = credentials[1]
    if le_password == given_password:
        return "True"
    else:
        return "False"


def add_new_user(name, username, password, cursor_object):
    """Adds a new user to the database, after checking if the user already exists."""
    cursor_object.execute("SELECT * FROM credential_database WHERE username = (?);", (username))
    data = cursor_object.fetchall()
    if data is None:
        print("Registration initiating...")
        add_data(name, username, password, cursor_object)
    else:
        print("User already exists in the database, login please!")


def check_database(username, password, cursor_object):
    """Checks the database to see if the entered username is already within the database."""
    cursor_object.execute("SELECT * FROM credential_database WHERE username = (?);", (username))
    data = cursor_object.fetchall()
    if data is None:
        name = input("Please enter your name? ").strip()
        add_data(name, username, password, cursor_object)
    else:
        check_credentials(username, password, cursor_object)


if __name__ == "__main__":
    creds = listen_for_data()
    print(creds)
    # response = check_user_creds(creds)
    # send_back_response
