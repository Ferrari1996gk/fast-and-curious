# import math
import numpy as np
# import matplotlib.pyplot as plt
from numba import jit


@jit(nopython=True)
def find_launch_angle(mass, velocity, distance, drag_coefficient, cross_section_area):
    '''
    Calculates the launch angle needed to hit a target at a given distance.
    Assumes the required launch angle is between 0 and 45 degrees.
    :param mass: float, The mass of the projectile in kg.
    :param velocity: float, The velocity of the projectile in m/s.
    :param distance: float, The distance to the target in m.
    :param drag_coefficient: float, The drag coefficient of the projectile.
    :param cross_section_area: float, The cross-sectional area of the projectile in m^2.
    :return: float, The launch angle in degrees.
    '''

    # Calculate all the angles to check
    # Every 0.1 degrees from 0 to 45 
    # angles = []
    # for i in range(451):
    #     angles.append(i * 0.1)
    angles = np.linspace(0, 45, 451)

    # Loop over all possible launch angles
    for angle in angles:
        # For the current angle, calculate the range of the projectile
        projectile_range = calculate_distance(mass, velocity, angle, drag_coefficient, cross_section_area)

        # If the range is greater than the target distance, the current angle will be within 1 degree of the correct angle
        if projectile_range > distance:
            # Return the current angle
            return angle
    else:
        # If no angle is found, return None
        return None
        

# @jit(nopython=True)
# def calculate_distance(mass, velocity, angle, drag_coefficient, cross_section_area, dt=0.001):
#     '''
#     Calculates the distance a projectile will travel given certain parameters.
#     :param mass: float, The mass of the projectile in kg.
#     :param velocity: float, The velocity of the projectile in m/s.
#     :param angle: float, The launch angle in degrees.
#     :param drag_coefficient: float, The drag coefficient of the projectile.
#     :param cross_section_area: float, The cross-sectional area of the projectile in m^2.
#     :return: float, The distance the projectile will travel in m.
#     '''
    
#     # Initialise the x and y positions
#     x = 0
#     y = 0

#     # Initialise the x and y velocities
#     v_x = velocity * np.cos(np.radians(angle))
#     v_y = velocity * np.sin(np.radians(angle))

#     # Loop until the projectile hits the ground
#     # Each step represents a time interval of dt seconds
#     while y >= 0:
#         # Update the x and y positions
#         x += v_x * dt
#         y += v_y * dt

#         # Calculate the current speed, angle and rate of deceleration due to air resistance
#         speed = np.sqrt(v_x ** 2 + v_y ** 2)
#         angle = np.arctan(v_y / v_x)
#         deceleration_air_resistance = 1.293 * drag_coefficient * cross_section_area * speed ** 2 / (2 * mass)

#         # Update the x and y velocities
#         v_x -= deceleration_air_resistance * np.cos(angle) * dt
#         v_y -= (deceleration_air_resistance * np.sin(angle) + 9.81) * dt

#     # The loop has ended, so the projectile hit the ground
#     # The x position is the distance the projectile traveled
#     return x

@jit(nopython=True)
def calculate_distance(mass, velocity, angle_deg, drag_coefficient, cross_section_area, dt=0.001):
    angle_rad = np.radians(angle_deg)
    cos_angle = np.cos(angle_rad)
    sin_angle = np.sin(angle_rad)
    x = 0.0
    y = 0.0
    v_x = velocity * cos_angle
    v_y = velocity * sin_angle
    air_density = 1.293
    g = 9.81

    while y >= 0:
        speed_sq = v_x ** 2 + v_y ** 2
        deceleration_air_resistance = air_density * drag_coefficient * cross_section_area * speed_sq / (2 * mass)
        angle = np.arctan2(v_y, v_x)
        cos_angle = np.cos(angle)
        sin_angle = np.sin(angle)

        x += v_x * dt
        y += v_y * dt
        v_x -= deceleration_air_resistance * cos_angle * dt
        v_y -= (deceleration_air_resistance * sin_angle + g) * dt

    return x