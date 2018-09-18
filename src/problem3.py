"""
Exam 1, problem 3.

Authors: David Mutchler, Vibha Alangar, Valerie Galluzzi, Mark Hays,
         Amanda Stouder, their colleagues and Jacob Pinney.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem3  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(10, 20), 200, 25, window)
    window.close_on_mouse_click()

    # TWO tests on ONE window.
    title = 'Tests 2, 3 and 4 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(15, 30), 100, 20, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 10), 90, 45, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 125), 80, 45, window)
    window.close_on_mouse_click()


def problem3(point, length, delta, window):
    """
    See   problem3_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Point.
      -- Two positive integers
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given rg.RoseWindow:

      -- A VERTICAL rg.Line for which:
           -- Its topmost point is the given point.
           -- Its length is the given length.
           -- Its color is 'black'.
           -- Its thickness is 3.

      -- Several HORIZONTAL rg.Lines such that:
           -- All the horizontal lines have their leftmost point
                on the vertical line.  SEE THE PICTURES.
           -- For the FIRST of these HORIZONTAL lines:
                -- Its leftmost point is the given point.
                -- Its length is the given length.
           -- Each SUBSEQUENT HORIZONTAL rg.Line is  delta  pixels
                directly below the previous rg.Line (where delta is a parameter)
                and 20 pixels longer than the previous rg.Line.
           -- All the HORIZONTAL lines have thickness 3.
           -- The 1st, 4th, 7th, etc rg.Lines have color 'magenta',
              The 2nd, 5th, 8th, etc rg.Lines have color 'cyan'
              The 3rd, 6th, 9th, etc rg.Lines have color 'spring green'

      NOTE: The NUMBER of lines to draw is determined by the facts that:
        -- The vertical line has the given length.
        -- All horizontal lines have their left endpoint on the vertical line.
        -- The distance between horizontal lines is the given delta.

      Must render but   ** NOT close **   the window.

    Type hints:
      :type point:   rg.Point
      :type length:  int
      :type delta:   int
      :type window:  rg.RoseWindow
    """
    # --------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    # DONE (continued):  IMPORTANT: Use this ITERATIVE ENHANCEMENT PLAN:
    # DONE (continued):    1. Make the sole VERTICAL line appear,
    # DONE (continued):         with thickness 3.
    # DONE (continued):    2. Make the FIRST horizontal line appear.
    # DONE (continued):    3. Make MORE horizontal lines appear,
    # DONE (continued):         each delta below the previous one.
    # DONE (continued):    4. Make each successive horizontal line
    # DONE (continued):         20 pixels longer than the previous one.
    # DONE (continued):    5. Make the right NUMBER of horizontal lines.
    # DONE (continued):    6. Make the horizontal lines each have thickness 3
    # DONE (continued):         and colors per the specified pattern.
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------

    main_start_point = rg.Point(point.x, point.y)
    main_end_point = rg.Point(point.x, point.y + length)

    line = rg.Line(main_start_point, main_end_point)
    line.thickness = 3
    line.attach_to(window)

    r = ((main_end_point.y - point.y) // delta) + 1

    color_id = 0  # 0 = magenta, 1 = cyan, 2 = spring green

    for k in range(r):
        start_point_x = point.x
        start_point_y = point.y + (delta * k)

        end_point_x = point.x + length + (20 * k)
        end_point_y = start_point_y

        start_point = rg.Point(start_point_x, start_point_y)
        end_point = rg.Point(end_point_x, end_point_y)

        rainbow_line = rg.Line(start_point, end_point)
        rainbow_line.thickness = 3

        if color_id == 0:
            rainbow_line.color = "magenta"
        elif color_id == 1:
            rainbow_line.color = "cyan"
        elif color_id == 2:
            rainbow_line.color = "spring green"

        if color_id == 2:
            color_id = 0
        else:
            color_id = color_id + 1

        rainbow_line.attach_to(window)
    window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
