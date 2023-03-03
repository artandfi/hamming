import re
import random
from hamming import HammingCodec, bits, flip_bit


def bitstr(bits_sequence):
    return "".join([str(b) for b in bits_sequence])


def main():
    print("---Hamming code demo by (c)artandfi---")
    
    n_parity_bits = ""
    while not n_parity_bits.isdigit() or int(n_parity_bits) < 2:
        n_parity_bits = input("Enter the integer number of parity bits k >= 2 for (2^k-1, 2^k-k-1) Hamming code: ")
    n_parity_bits = int(n_parity_bits)

    data = ""
    while not re.match("0|1+", data):
        data = input("Enter the data to be encoded in binary form: ")
    
    data = int(data, 2)
    hc = HammingCodec(n_parity_bits)
    encoded = hc.encode(data)
    block_size = 2 ** n_parity_bits - 1
    data_size = block_size - n_parity_bits

    print(f"Encoded data: {bitstr(bits(encoded, pad_to=block_size))}")
    if random.randint(0, 1):
        data_indices = [i for i in range(len(bits(encoded, pad_to=block_size))) if i & (i + 1)]
        flipped_bit_pos = random.choice(data_indices)
        encoded = flip_bit(encoded, flipped_bit_pos, pad_to=block_size)

        print(f"Flipped bit at position {flipped_bit_pos} in encoded data, which is now {bitstr(bits(encoded, pad_to=block_size))}")


    decoded = hc.decode(encoded)
    print(f"Decoded data: {bitstr(bits(decoded, pad_to=data_size))}")
    print("---------")


if __name__ == "__main__":
    main()
