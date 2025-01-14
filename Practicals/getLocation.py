from pymavlink import mavutil

connection = mavutil.mavlink_connection("tcp:127.0.0.1:14550")
while True:
    message = connection.recv_match(type="GLOBAL_POSITION_INT", blocking=True).to_dict()
    print(message)