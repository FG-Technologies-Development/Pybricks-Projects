from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Color, Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.A)

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)
motor = Motor(Port.E)  # For the arm, if needed

robot = DriveBase(right_motor, left_motor, 56, 112)

robot.use_gyro(True)
robot.reset()

robot.settings(
    straight_speed=200,
    straight_acceleration=500,
    turn_rate=100,
    turn_acceleration=300
)

robot.straight(300)
hub.speaker.beep()

robot.turn(90)   # right turn
hub.speaker.beep()

robot.straight(300)
hub.speaker.beep()

robot.turn(90)   # right turn
hub.speaker.beep()

robot.straight(300)
hub.speaker.beep()

robot.turn(90)   # right turn
hub.speaker.beep()

robot.straight(300)
hub.speaker.beep()

