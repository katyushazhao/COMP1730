import robot

robot.init()

current_pos=0

def movex(x):
    i=0
    global current_pos
    if x < 0:
        x=-1*x
        while i < x:
            robot.drive_left()
            current_pos=current_pos-1
            i = i+1
    if x > 0:
        while i <x:
            robot.drive_right()
            current_pos=current_pos+1
            i = i+1

def reset():
    robot.gripper_to_open()
    robot.lift_up()
    movex(-1*current_pos)
    robot.gripper_to_folded()
    robot.lift_down()


def swap_left_and_middle():
    movex(1)
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    movex(2)
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    movex(-2)
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    movex(2)
    robot.lift_down()
    reset()
