"""The client side login-screen file for the MemoPad project."""
# ------------IMPORTS--------------
import socket

# ------------CONSTANTS-------------
sockett = socket.socket()
host = "100.65.251.47"
port = 9996
sockett.connect((host, port))

# -----------FUNCTIONS------------


# def create_socket():
#     """Creates a socket to establish connection between the server and client."""
#     try:
#         global host  # the host IP address
#         global port  # the port over which connection will be done
#         global sockett
#
#         host = ""
#         port = 9997
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
#     while True:
#         try:
#             conn, address = sockett.accept()
#             sockett.setblocking(1)
#             # this prevents timeout.
#
#             # connection_collection.append(conn)
#             # address_collection.append(address)
#
#             print("Connection has been established!  ||  {}".format(address[0]))
#
#             # the line below this comment is new, see if it works:
#             # todo: return conn
#         except:
#             print("Error accepting connection.")
#
#
#
def get_credentials():
    """Gets the credentials of the user."""
    username = input("Please enter your username: ").lower().strip()
    password = input("Please enter your password: ").lower().strip()
    data_packet = username + "|" + password
    # create_socket()
    # bind_socket()
    # accept_connections()
    sockett.sendall(str.encode(data_packet))
    # return data_packet
#
#
# # def check_user_creds(data):
# #     """Checks whether the user entered credentials."""
# #     # the entered data comes in as a tuple.
# #     username = data[0]
# #     pw = data[1]


if __name__ == "__main__":
    get_credentials()
