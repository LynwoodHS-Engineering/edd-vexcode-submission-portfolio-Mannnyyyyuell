import vex

brain = vex.Brain()

def main():
    while True:
        brain.screen.clear_screen()
        width = (potPinE.value() * 180) // 4095  # Changed scaling factor
        brain.screen.set_fill_color(vex.Color.GREEN)
        brain.screen.draw_rectangle(110, 90, width, 40)  # Adjusted position and size
        brain.screen.print_at(15, 25, "Value: %d" % pot.value())  # Adjusted text position
        vex.wait(100, vex.TimeUnits.MSEC)  # Changed wait time

main()
