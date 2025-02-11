from vex import *

# Begin project code
brain = vex.Brain()

def main():
    while True:
        radius = 10 + (potPina.value() * 90) // 4095
        brain.screen.clear_screen()
        brain.screen.set_pen_color(vex.Color.GREEN)
        brain.screen.draw_circle(240, 136, radius)
        vex.wait(20, vex.TimeUnits.MSEC)

main()
