"""
Problem: Compute the parity of a 64-bit word.
Parity is 1 if the number of set bits (1s) is odd, and 0 if even.

Example:
    1011 (binary) has 3 ones => Parity = 1
    10001000 (binary) has 2 ones => Parity = 0

Applications:
    - Error detection in data storage and transmission (e.g., parity bit in memory)
"""

# -------------------------------
# 1. Brute-force Approach (O(n))
# -------------------------------

def parity_brute_force(x: int) -> int:
    """
    Computes parity by checking each bit (Time: O(n), where n = word size)

    Example:
        Input: 0b1011 => 11 in decimal
        Output: 1 (Odd number of 1s)
    """
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# -------------------------------
# 2. Sub-optimal: Erasing Lowest Set Bit (O(k))
# -------------------------------

def parity_drop_lowest_set_bit(x: int) -> int:
    """
    Computes parity using x & (x - 1) trick (Time: O(k), where k = number of 1s)

    Example:
        Input: 0b10001010 => 138 in decimal (3 set bits)
        Output: 1
    """
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # Drops the lowest set bit
    return result


# -------------------------------------------
# 3. Improved: Lookup Table on 16-bit Chunks (O(n/L))
# -------------------------------------------

# Precompute parity for all 16-bit numbers
PRECOMPUTED_PARITY = [parity_brute_force(i) for i in range(1 << 16)]

def parity_lookup(x: int) -> int:
    """
    Computes parity using 4 x 16-bit lookups + XOR

    Time: O(n/L), where L=16 (chunk size)

    Example:
        Input: 0b10000000000000011000000000000001 (32-bit shown for demo)
        Output: depends on number of 1s
    """
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF

    return (
        PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
        PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
        PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
        PRECOMPUTED_PARITY[x & BIT_MASK]
    )


# --------------------------------------------
# 4. Optimal: XOR Folding Method (O(log n))
# --------------------------------------------

def parity_optimized(x: int) -> int:
    """
    Computes parity using XOR and shifting in log(n) steps.

    Example:
        Input: 0b11010111 => 215
        Output: 0 (even number of 1s)
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


# -------------------------------
# Test the functions
# -------------------------------

if __name__ == "__main__":
    test_values = [
        0b1011,              # 3 ones → 1
        0b10001000,          # 2 ones → 0
        0b1111000011110000,  # 8 ones → 0
        0xFFFFFFFFFFFFFFFF,  # 64 ones → 0
        0x8000000000000001,  # 2 ones → 0
        0x0000000000000001   # 1 one → 1
    ]

    print("Testing parity computations:")
    for value in test_values:
        print(f"\nValue: {bin(value)}")
        print(f"Brute-force: {parity_brute_force(value)}")
        print(f"Drop-bit:    {parity_drop_lowest_set_bit(value)}")
        print(f"Lookup:      {parity_lookup(value)}")
        print(f"Optimized:   {parity_optimized(value)}")
