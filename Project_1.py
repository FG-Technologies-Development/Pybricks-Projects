from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Color, Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)

robot = DriveBase(left_motor, right_motor, 56, 112)

robot.use_gyro(True)
robot.reset()

robot.settings(
    straight_speed=200,
    straight_acceleration=500,
    turn_rate=100,
    turn_acceleration=300
)

def movement_test():
    print("Running forward")
    robot.straight(100)
    hub.speaker.beep()
    
    print("Turning right")
    robot.turn(90)   # right turn
    hub.speaker.beep()
    
    print("Running forward")
    robot.straight(100)
    hub.speaker.beep()

    print("Running backward")
    robot.straight(-100)
    hub.speaker.beep()

    print("Turning left")
    robot.turn(-90)  # left turn
    hub.speaker.beep()

    print("Running backward")
    robot.straight(-100)
    hub.speaker.beep()

    print("Movement Done")

    motor.run_target(100, 90)
    robot.straight(100)
    motor.run_target(100, 10)
    robot.straight(-200)
    robot.turn(90)
    robot.straight(-100)
    hub.speaker.beep()
    motor.run_target(100, 10)
    robot.straight(250)

    # Start driving forward
    robot.drive(150, 0)

    # Keep going until black is detected
    while True:
        if sensor.reflection() < 20:
           robot.stop()
           hub.speaker.beep()
           break

    motor.run_target(20, 5)
    robot.turn(90)
    robot.straight(200)

def reset_robot():
    robot.stop()
    robot.reset()

def gyro_straight(distance, speed=150, gain=2.0):
    reset_robot()

    if distance > 0:
        while robot.distance() < distance:
            error = hub.imu.heading()
            correction = -error * gain
            robot.drive(speed, correction)
            wait(10)
    else:
        while robot.distance() > distance:
            error = hub.imu.heading()
            correction = -error * gain
            robot.drive(-speed, correction)
            wait(10)

    robot.stop()

def gyro_turn(target_angle, turn_speed=80, turn_gain=2.0):
    reset_robot()

    while True:
        error = target_angle - hub.imu.heading()

        if abs(error) <= 1:
            break

        turn_rate = error * turn_gain

        if turn_rate > turn_speed:
            turn_rate = turn_speed
        if turn_rate < -turn_speed:
            turn_rate = -turn_speed

        robot.drive(0, turn_rate)
        wait(10)

    robot.stop()

'''
# Example
gyro_straight(300)
hub.speaker.beep()

gyro_turn(90)
hub.speaker.beep()

gyro_turn(-90)
hub.speaker.beep()

gyro_straight(-200)
hub.speaker.beep()
'''

movement_test()