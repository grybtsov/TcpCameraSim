import socket


class TcpClient:
    def __init__(self, server_ip_address, server_port_number, connection_timeout, data_length):
        self.socket = socket.socket()
        self.server_ip_address = server_ip_address
        self.server_port_number = server_port_number
        self.connection_timeout = connection_timeout
        self.data_length = data_length

    def connect_to_server(self):
        try:
            self.socket = socket.socket()
            self.socket.settimeout(self.connection_timeout)
            self.socket.connect((self.server_ip_address,
                                 self.server_port_number))

        except socket.gaierror as msg:
            print("Connection socket.error : %s" % msg)
        except socket.error as msg:
            print("Connection socket.error : %s" % msg)

    def get_values(self) -> int:
        received_data_bytes = bytes('', 'utf-8')
        received_data_int32 = 0

        try:
            self.socket.settimeout(self.connection_timeout)
            received_data_bytes = self.socket.recv(self.data_length)  # Get raw data bytes from the server
        except socket.error as msg:
            print("Data reading socket.error : %s" % msg)
            self.connect_to_server()  # Reconnect with server in case of error

        if received_data_bytes:  # If the data was received
            received_data_int32 = int.from_bytes(received_data_bytes,  # Convert raw data to int32 variable
                                                 'little')
            try:
                send_data = (received_data_int32 >> 1)
                self.socket.settimeout(self.connection_timeout)
                self.socket.send(send_data.to_bytes(self.data_length,  # Send received data back to the server
                                                    'little'))
            except socket.error as msg:  # Reconnect with server in case of error
                print("Data sending socket.error : %s" % msg)
                self.connect_to_server()

        return received_data_int32
