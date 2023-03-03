from hamming import HammingCodec, flip_bit


def test_hamming1():
    hc = HammingCodec(4)
    data = 0b01010110010
    encoded = hc.encode(data)

    assert encoded == 0b100110110110010
    assert hc.decode(encoded) == data


def test_hamming2():
    hc = HammingCodec(4)
    data = 0b01010110010
    encoded = hc.encode(data)

    assert encoded == 0b100110110110010

    encoded = flip_bit(encoded, 0)
    assert hc.decode(encoded) == data


def test_hamming3():
    hc = HammingCodec(3)
    data = 0b11                 # should be padded w/ 2 leading zeroes to achieve length 4: 0b0011
    encoded = hc.encode(data)

    assert encoded == 0b1000011
    assert hc.decode(encoded) == data
