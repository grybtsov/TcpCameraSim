import datetime
import socket
from tcp_client import TcpClient

SERVER_IP_ADDRESS = '127.0.0.1'
SERVER_PORT_NUMBER = 2010
CONNECTION_TIMEOUT = 1  # Connection timeout in seconds
DATA_LENGTH = 4  # Number of bytes to send/receive

if __name__ == '__main__':
    tcp_client = TcpClient(SERVER_IP_ADDRESS,
                           SERVER_PORT_NUMBER,
                           CONNECTION_TIMEOUT,
                           DATA_LENGTH)

    tcp_client.connect_to_server()

    while True:
        received_data_int32 = tcp_client.get_values()
        sign_of_life = bool(received_data_int32 & 1)  # Check sign of life bit 0
        received_data_value = received_data_int32 >> 1  # Get value without sign of life bit
        timestamp = datetime.datetime.now()
        print('{}   Value: {},   Sign of life: {}'.format(timestamp, received_data_value, sign_of_life))
