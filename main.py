from take_inputs import get_user_input as getInputs
from mohr_circle import mohr_circle as mohrCircle
from given_rectangle import given_rectangle as givenRectangle
from rotated_rectangle import rotate_square as rotatedRectangle

sigma_x, sigma_y, tau_xy, angle = getInputs()
mohrCircle(sigma_x, sigma_y, tau_xy, angle)
givenRectangle(sigma_x, sigma_y, tau_xy, angle)
rotatedRectangle(sigma_x, sigma_y, tau_xy, angle)



