from pymavlink import mavutil

connection = mavutil.mavlink_connection("tcp:127.0.0.1:14550")

# SWITCH TO GUIDED MODE
connection.mav.command_long_send(
    1, # Target system
    1, # Target component
    mavutil.mavlink.MAV_CMD_DO_SET_MODE, # Command
    0, # Confirmation counter
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED, # Param 1 (Mode, for GUIDED, set to CUSTOM)
    4, # Param 2 (Custom mode, GUIDED = 4 for ArduCopter)
    0, # Param 3 (Custom sub-mode, unused for ArduPilot)
    0, # Param 4 (Unused)
    0, # Param 5 (Unused)
    0, # Param 6 (Unused)
    0  # Param 7 (Unused)
)

msg = connection.recv_match(type="COMMAND_ACK",blocking=True)
if msg.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    print("mode switching ACCEPTED")
else:
    print("mode switching FAILED!")
    
# ARM
connection.mav.command_long_send(
    1, # Target system
    1, # Target component
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, # Command
    0, # Confirmation counter
    1, # Param 1 (Arm)
    0, # Param 2 (Force)
    0, # Param 3 (Unused)
    0, # Param 4 (Unused)
    0, # Param 5 (Unused)
    0, # Param 6 (Unused)
    0  # Param 7 (Unused)
)

msg = connection.recv_match(type="COMMAND_ACK",blocking=True)
if msg.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    print("arming ACCEPTED")
else:
    print("arming FAILED!")

# TAKEOFF
connection.mav.command_long_send(
    1, # Target system
    1, # Target component
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, # Command
    0, # Confirmation counter
    0, # Param 1 (Unused)
    0, # Param 2 (Unused)
    0, # Param 3 (Unused)
    0, # Param 4 (Unused)
    0, # Param 5 (Unused)
    0, # Param 6 (Unused)
    20  # Param 7 (Altitude [m])
)

msg = connection.recv_match(type="COMMAND_ACK",blocking=True)
if msg.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    print("takeoff ACCEPTED")
else:
    print("takeoff FAILED!")