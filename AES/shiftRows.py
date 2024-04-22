def shiftRows(state):
    """
    Performs the ShiftRows operation on the state.
    Each row of the state is shifted cyclically a certain number of steps.
    """
    for r in range(1, 4):
        state[r] = state[r][r:] + state[r][:r]
    return state

def invShiftRows(state):
    """
    Performs the inverse ShiftRows operation on the state.
    Each row of the state is shifted cyclically in the opposite direction.
    """
    for r in range(1, 4):
        state[r] = state[r][-r:] + state[r][:-r]
    return state
