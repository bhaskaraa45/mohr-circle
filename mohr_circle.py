import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def mohr_circle(sigma_x, sigma_y, tau_xy,angle):
    # Formulas for Center and Radius
    center = 0.5 * (sigma_x + sigma_y)
    radius = np.sqrt(((sigma_x - sigma_y) * 0.5) ** 2 + tau_xy ** 2)

    # Principal stresses
    sigma1 = center + radius
    sigma2 = center - radius

    # Maximum shear stress
    tau_max = radius

    # Angles for plotting the circle
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = center + radius * np.cos(theta)
    y = radius * np.sin(theta)

    #points for plotting plane
    xpoints = np.array([sigma_x, sigma_y])
    ypoints = np.array([tau_xy, -tau_xy])

    #rotate the plane by 2theta
    point1 = np.array([sigma_x, tau_xy])  
    point2 = np.array([sigma_y, -tau_xy])

    two_theta = np.radians(2 * angle)

    rotation_mat = np.array([[np.cos(two_theta), -np.sin(two_theta)],
                             [np.sin(two_theta),  np.cos(two_theta)]])

    point1_new = point1 - np.array([center, 0])
    point2_new = point2 - np.array([center, 0])

    rotated_point1 = rotation_mat.dot(point1_new)
    rotated_point2 = rotation_mat.dot(point2_new)

    rotated_point1 += np.array([center, 0])
    rotated_point2 += np.array([center, 0])

    #add curved arrow to show the angle and direction b/w planes
    l = radius/3
    
    value_of_theta_radians = np.pi / 2

    if sigma_x != sigma_y:
        slope_og = 2*tau_xy/(sigma_x-sigma_y)
        value_of_theta_radians = np.arctan(slope_og)

    point_A_x = np.cos(value_of_theta_radians)*l + center
    point_A_y = np.sin(value_of_theta_radians)*l

    point_B_x = np.cos(value_of_theta_radians+two_theta)*l + center
    point_B_y = np.sin(value_of_theta_radians+two_theta)*l

    style = 'arc3,rad=0.75'
    if angle < 0:
        style = 'arc3,rad=-0.75' 

    arrow = FancyArrowPatch(posA=(point_A_x,point_A_y), posB=(point_B_x,point_B_y),
                        arrowstyle='-|>', mutation_scale=20,
                        connectionstyle=style)

    mid_angle = value_of_theta_radians + two_theta / 2
    text_radius = l * 1.5
    text_x = np.cos(mid_angle) * text_radius + center
    text_y = np.sin(mid_angle) * text_radius

    # Plot Mohr's circle
    fig, ax = plt.subplots(figsize=(16,16))
    ax.plot(x, y, 'b-', label=f'Mohr\'s Circle of radius {radius:.2f}')
    ax.set_xlabel('Normal Stress (σ)')
    ax.set_ylabel('Shear Stress (τ)')
    ax.set_title('Mohr\'s Circle')
    ax.grid(True)
    ax.scatter([center],[0],color = 'blue', label = f'Center = ({center:.2f},0)')
    ax.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g-', label='Original Plane')
    ax.plot([rotated_point1[0], rotated_point2[0]], [rotated_point1[1], rotated_point2[1]], 'r--', label='Rotated Plane')
    ax.axhline(0, color='black',linewidth=1)
    ax.axvline(0, color='black',linewidth=1)
    ax.scatter([sigma_x], [tau_xy], color='red', label=f'(σx,τxy) = ({sigma_x},{tau_xy})')
    ax.scatter([sigma_y], [-tau_xy], color='orange', label=f'(σy,-τxy) = ({sigma_y},{-tau_xy})')
    ax.scatter([sigma1], [0], color='green', label=f'Principal Stress 1 = {sigma1:.2f} ')
    ax.scatter([sigma2], [0], color='green', label=f'Principal Stress 2 = {sigma2:.2f}')
    ax.scatter([rotated_point1[0]], [rotated_point1[1]], color='black', label=f'({rotated_point1[0]:.2f}, {rotated_point1[1]:.2f})')
    ax.scatter([rotated_point2[0]], [rotated_point2[1]], color='violet', label=f'({rotated_point2[0]:.2f}, {rotated_point2[1]:.2f})')
    ax.legend()
    ax.axis('equal')
    ax.add_patch(arrow)
    ax.text(text_x, text_y, f'{2*angle}°', fontsize=16, ha='center', va='center')



