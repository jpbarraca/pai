import binascii

data = binascii.unhexlify(
    b"4f1f4d001e0e080000000006100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000181914010708000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003661a00019a140a0a05000000018a0505050505000a000000000000000000000000000010000000100000000a0000000000001200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
)


def test_1():
    assert len(data) == 256


def test_area_block_counter():
    label_eeprom_address_start = 14955  # 0x03C17
    next_label_after_bytes = 107  # 0x6B

    for i in range(0, 9):
        i2 = ((i * next_label_after_bytes) + label_eeprom_address_start) // 256
        print(f"{i}({i2}): {data[i2]}")


def test_zone_block_counter():
    label_eeprom_address_start = 0x00430
    next_label_after_bytes = 16

    for i in range(0, 193):
        i2 = ((i * next_label_after_bytes) + label_eeprom_address_start) // 256
        print(f"{i}({i2}): {data[i2]}")


def test_module_block_counter():
    for i in range(0, 256):
        i2 = ((i * 5) + 0x04E47) // 256
        print(f"{i}({i2}): {data[i2]}")


def test_user_block_counter():
    type_ = "evo"
    for i in range(0, 257):
        if i < 257:
            i2 = ((i * 16) + 0x03E47) // 256
        else:
            i2 = (86416 if type_ == "evohd" else (i * 16) + 20880) // 256
        if i2 < len(data):
            print(f"{i}({i2}): {data[i2]}")


def test_pgm_block_counter():
    for i in range(0, 32):
        i2 = ((i * 32) + 0x07082) // 256
        print(f"{i}({i2}): {data[i2]}")


def test_door_block_counter():
    for i in range(0, 32):
        i2 = ((i * 16) + 0x0345C) // 256
        print(f"{i}({i2}): {data[i2]}")
