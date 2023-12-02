import numpy as np
import matplotlib.pyplot as plt

def rotate_point(point, angle_radians):
    rotation_matrix = np.array([
        [np.cos(angle_radians), -np.sin(angle_radians)],
        [np.sin(angle_radians), np.cos(angle_radians)]
    ])
    return np.dot(point, rotation_matrix)


def rotate_square(sigma_x, sigma_y, tau_xy, angle_degrees):
    size = 2
    bottom_left_x, bottom_left_y = -1, -1
    square_coords = np.array([
        [bottom_left_x, bottom_left_y],
        [bottom_left_x + size, bottom_left_y],
        [bottom_left_x + size, bottom_left_y + size],
        [bottom_left_x, bottom_left_y + size],
        [bottom_left_x, bottom_left_y] 
    ])
    arrow_length = 0.5
    arrow_properties = {'head_width': 0.05, 'head_length': 0.1, 'fc': 'k', 'ec': 'k'}

    arrows = [
        [np.array([-1 if sigma_x>=0 else -1.65, 0]), np.array([-arrow_length if sigma_x >= 0 else arrow_length, 0])],
        [np.array([1 if sigma_x>=0 else 1.65, 0]), np.array([arrow_length if sigma_x >= 0 else -arrow_length, 0])],
        [np.array([0, 1 if sigma_y>=0 else 1.65]), np.array([0, arrow_length if sigma_y >= 0 else -arrow_length])],
        [np.array([0, -1 if sigma_y>=0 else -1.65]), np.array([0, -arrow_length if sigma_y >= 0 else arrow_length])]
    ]

    angle_radians = np.radians(angle_degrees)
    rotated_square_coords = np.array([rotate_point(coord, angle_radians) for coord in square_coords])
    rotated_arrows = [[rotate_point(start, angle_radians), rotate_point(start + end, angle_radians) - rotate_point(start, angle_radians)] for start, end in arrows]

    fig, ax = plt.subplots()

    ax.plot(square_coords[:, 0], square_coords[:, 1], 'b--', label='Original Square')
    ax.plot(rotated_square_coords[:, 0], rotated_square_coords[:, 1], 'r-', label='Rotated Square')

    for start, end in rotated_arrows:
        ax.arrow(start[0], start[1], end[0], end[1], **arrow_properties)

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_title(f"Rotated plane by {angle_degrees}°")

    ax.axis('equal')
    plt.show()

