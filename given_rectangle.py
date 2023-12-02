import matplotlib.pyplot as plt
from rotated_rectangle import rotate_square as rotated_rectangle

def given_rectangle(sigma_x, sigma_y, tau_xy, angle):
    start_sigma_x_1_a = -1 if sigma_x >= 0 else -1.65
    start_sigma_x_2_a = 1 if sigma_x >= 0 else 1.65
    end_sigma_x_1_a = -0.5 if sigma_x >= 0 else 0.5
    end_sigma_x_2_a = 0.5 if sigma_x >= 0 else -0.5

    start_sigma_y_1_b = 1 if sigma_y >= 0 else 1.65
    start_sigma_y_2_b = -1 if sigma_y >= 0 else -1.65
    end_sigma_y_1_a = 0.5 if sigma_y >= 0 else -0.5
    end_sigma_y_2_a = -0.5 if sigma_y >= 0 else 0.5

    start_t_x_1_a = -1 if tau_xy >= 0 else 1
    start_t_x_2_a = 1 if tau_xy >= 0 else -1
    end_t_x_1_a = 1.9 if tau_xy >= 0 else -1.9
    end_t_x_2_a = -1.9 if tau_xy >= 0 else 1.9

    start_t_y_1_b = 1 if tau_xy >= 0 else -1
    start_t_y_2_b = -1 if tau_xy >= 0 else 1
    end_t_y_1_a = -1.9 if tau_xy >= 0 else 1.9
    end_t_y_2_a = 1.9 if tau_xy >= 0 else -1.9

    fig, ax = plt.subplots()

    size = 2
    bottom_left_x, bottom_left_y = -1, -1
    square_x = [bottom_left_x, bottom_left_x + size, bottom_left_x + size, bottom_left_x, bottom_left_x]
    square_y = [bottom_left_y, bottom_left_y, bottom_left_y + size, bottom_left_y + size, bottom_left_y]

    ax.plot(square_x, square_y, 'b-')  

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    ax.arrow(start_sigma_x_1_a, 0, end_sigma_x_1_a, 0, head_width=0.05, head_length=0.1, ec='k')
    ax.arrow(start_sigma_x_2_a, 0, end_sigma_x_2_a, 0, head_width=0.05, head_length=0.1, ec='k')
    ax.arrow(0, start_sigma_y_1_b, 0, end_sigma_y_1_a, head_width=0.05, head_length=0.1, ec='k')
    ax.arrow(0, start_sigma_y_2_b, 0, end_sigma_y_2_a, head_width=0.05, head_length=0.1, ec='k')
    ax.arrow(start_t_x_1_a, 1.1, end_t_x_1_a, 0, head_width=0.05, head_length=0.1, ec='k')
    ax.arrow(start_t_x_2_a, -1.1, end_t_x_2_a, 0, head_width=0.05, head_length=0.1, ec='k')
    ax.arrow(-1.1, start_t_y_1_b, 0, end_t_y_1_a, head_width=0.05, head_length=0.1, ec='k')
    ax.arrow(1.1, start_t_y_2_b, 0, end_t_y_2_a, head_width=0.05, head_length=0.1, ec='k')

    ax.axis('equal')


