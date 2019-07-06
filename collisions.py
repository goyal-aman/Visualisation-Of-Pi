def reverse_vel(vel):
    '''
    reversing velocity of block
    '''
    vel *= -1
    return vel


def exchange_vel(v1, m1, v2, m2):
    '''
    this function is calculating the new velocity of the block after collision,
    based on law of conservation of momentum and kinetic energy
    '''
    v1 = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2

    return v1  # returning new velocity after collision
