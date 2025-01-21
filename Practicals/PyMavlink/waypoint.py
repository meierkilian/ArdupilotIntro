from pymavlink import mavutil

connection = mavutil.mavlink_connection("tcp:127.0.0.1:14550")

# SEND WAYPOINT
connection.mav.command_int_send(
    1, # (Target system) 
    1, # (Target component)
    mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, # (Frame)
    mavutil.mavlink.MAV_CMD_DO_REPOSITION, # (Command)
    0, # (Unused)
    0, # (Unused)
    0, # (Param 1, Speed) 
    0, # (Param 2, Bitmask)
    0, # (Param 3, Radius [m], only used by plane)
    0, # (Param 4, Yaw [deg])
    int(0.02543594113010138 * 1e7), # (Param 5, Latitude [deg * 1e33)
    int(36.90310516679042 * 1e7), # (Param 6, Longitude [deg * 1e7])
    float(20) # (Param 7, altitude)
)

msg = connection.recv_match(type="COMMAND_ACK",blocking=True)
if msg.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    print("waypoint ACCEPTED")
else:
    print("waypoint FAILED!")
