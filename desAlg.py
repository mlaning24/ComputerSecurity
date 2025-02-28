# DES Decryption with Detailed Steps, Key Highlights, and Full S-Boxes

# Permutation tables and shift schedules
KEY_PERM_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 
              10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 
              63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 
              14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

KEY_PERM_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 
              23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 
              41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 
              44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

SHIFT_ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

S_BOXES = [
    #S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

INIT_PERM = [58, 50, 42, 34, 26, 18, 10, 2, 
             60, 52, 44, 36, 28, 20, 12, 4, 
             62, 54, 46, 38, 30, 22, 14, 6, 
             64, 56, 48, 40, 32, 24, 16, 8, 
             57, 49, 41, 33, 25, 17, 9, 1, 
             59, 51, 43, 35, 27, 19, 11, 3, 
             61, 53, 45, 37, 29, 21, 13, 5, 
             63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERM = [40, 8, 48, 16, 56, 24, 64, 32, 
              39, 7, 47, 15, 55, 23, 63, 31, 
              38, 6, 46, 14, 54, 22, 62, 30, 
              37, 5, 45, 13, 53, 21, 61, 29, 
              36, 4, 44, 12, 52, 20, 60, 28, 
              35, 3, 43, 11, 51, 19, 59, 27, 
              34, 2, 42, 10, 50, 18, 58, 26, 
              33, 1, 41, 9, 49, 17, 57, 25]

EXPAND_BLOCK = [32, 1, 2, 3, 4, 5, 
                4, 5, 6, 7, 8, 9, 
                8, 9, 10, 11, 12, 13, 
                12, 13, 14, 15, 16, 17, 
                16, 17, 18, 19, 20, 21, 
                20, 21, 22, 23, 24, 25, 
                24, 25, 26, 27, 28, 29, 
                28, 29, 30, 31, 32, 1]

PERMUTATION_P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Round Keys and Intermediate Values
subkeys = []
C = []
D = []

# Helper Functions
def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)

def rotate_left(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def xor_bits(bits1, bits2):
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bits1, bits2))

# S-Box Substitution
def sbox_substitute(bits):
    output = ''
    for i in range(0, 48, 6):
        block = bits[i:i+6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        output += format(S_BOXES[i//6][row][col], '04b')
    return output

# Feistel Function
def feistel(right, subkey):
    expanded = permute(right, EXPAND_BLOCK)
    xored = xor_bits(expanded, subkey)
    substituted = sbox_substitute(xored)
    permuted = permute(substituted, PERMUTATION_P)
    print(f"Feistel -> Expanded: {expanded}, XORed: {xored}, Substituted: {substituted}, Permuted: {permuted}")
    return permuted

# Key Schedule Generation
def generate_subkeys(master_key):
    key_56 = permute(master_key, KEY_PERM_1)
    left_half = key_56[:28]
    right_half = key_56[28:]
    C.append(left_half)
    D.append(right_half)

    for i in range(16):
        left_half = rotate_left(left_half, SHIFT_ROTATIONS[i])
        right_half = rotate_left(right_half, SHIFT_ROTATIONS[i])
        C.append(left_half)
        D.append(right_half)

        combined = left_half + right_half
        subkey = permute(combined, KEY_PERM_2)
        subkeys.append(subkey)

        # Debug: Display Subkeys
        print(f"Round {i+1} Subkey: {subkey}")


# Convert Binary to Text
def binary_to_text(binary_str):
    text = ''
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        text += chr(int(byte, 2))
    return text

# DES Decryption
def des_decrypt(key, ciphertext):
    generate_subkeys(key)
    permuted = permute(ciphertext, INIT_PERM)
    left, right = permuted[:32], permuted[32:]

    for i in range(15, -1, -1):
        round_key = subkeys[i]
        f_output = feistel(right, round_key)
        new_right = xor_bits(left, f_output)
        left = right
        right = new_right
        print(f"Round {16-i}: L = {left}, R = {right}, f_output = {f_output}")

    combined = right + left
    decrypted_binary = permute(combined, FINAL_PERM)
    decrypted_text = binary_to_text(decrypted_binary)
    print(f"Decrypted Text: {decrypted_text}")

# Inputs
key = "0100110001001111010101100100010101000011010100110100111001000100"
ciphertext = "1100101011101101101000100110010101011111101101110011100001110011"

# Run decryption
des_decrypt(key, ciphertext)
