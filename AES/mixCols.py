def mixColumns(state):
    """
    Performs the MixColumns operation on the state.
    It is a matrix multiplication in GF(2^8).
    """
    mix_column_matrix = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2],
    ]
    return matrix_multiply(mix_column_matrix, state)

def invMixColumns(state):
    """
    Performs the inverse MixColumns operation on the state.
    It is a matrix multiplication in GF(2^8).
    """
    inv_mix_column_matrix = [
        [14, 11, 13, 9],
        [9, 14, 11, 13],
        [13, 9, 14, 11],
        [11, 13, 9, 14],
    ]
    return matrix_multiply(inv_mix_column_matrix, state)

def matrix_multiply(matrix, state):
    """
    Multiplies a 4x4 matrix with the state matrix in GF(2^8).
    """
    result = [[0] * 4 for _ in range(4)]
    for row in range(4):
        for col in range(4):
            for i in range(4):
                result[row][col] ^= gf_multiply(matrix[row][i], state[i][col])
    return result

def gf_multiply(a, b):
    """
    Multiplies two numbers in GF(2^8) using the AES modulus.
    """
    p = 0
    for counter in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x11B  # AES modulus
        b >>= 1
    return p % 256
