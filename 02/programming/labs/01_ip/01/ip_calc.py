"""Operations with ip-adresses."""


def get_ip_from_raw_address(raw_address):
    """
    Gets ip from raw adress.
    >>> get_ip_from_raw_address('91.124.230.205/30')
    '91.124.230.205'
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    return raw_address[:raw_address.find("/")]


def get_network_address_from_raw_address(raw_address):
    """
    Gets network address from raw address.
    >>> get_network_address_from_raw_address('91.124.230.205/30')
    '91.124.230.204'
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    address = list(map(int, get_ip_from_raw_address(raw_address).split('.')))
    mask = list(map(int, binary_to_decimal(get_binary_mask_from_raw_address
                                           (raw_address)).split('.')))
    result = []

    for each in range(len(address)):
        result.append(str(address[each] & mask[each]))

    return ".".join(result)


def get_broadcast_address_from_raw_address(raw_address):
    """
    Gets broadcast address from raw address.
    >>> get_broadcast_address_from_raw_address('91.124.230.205/30')
    '91.124.230.207'
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    mask = get_binary_mask_from_raw_address(raw_address)
    new_mask = ''

    for each in mask:
        if each == ".":
            new_mask += each
        else:
            new_mask += str(1 ^ int(each))

    address = list(map(int, get_ip_from_raw_address(raw_address).split('.')))
    mask = list(map(int, binary_to_decimal(new_mask).split('.')))
    result = []

    for each in range(len(address)):
        result.append(str(address[each] | mask[each]))

    return ".".join(result)


def get_binary_mask_from_raw_address(raw_address):
    """
    Gets binary mask from raw address.
    >>> get_binary_mask_from_raw_address('91.124.230.205/30')
    '11111111.11111111.11111111.11111100'
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    return '00000000.00000000.00000000.00000000'.\
        replace('0', '1', int(raw_address[raw_address.find("/") + 1:]))


def get_first_usable_ip_address_from_raw_address(raw_address):
    """
    Gets first usable ip address from raw address.
    >>> get_first_usable_ip_address_from_raw_address\
        ('91.124.230.205/30')
    '91.124.230.205'
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    network = decimal_to_binary(get_network_address_from_raw_address
                                (raw_address)).split(".")
    network[3] = str(bin(int(network[3], 2)+1))[2:]
    first_ip = list(map(lambda x: str(int(x, 2)), network))

    return ".".join(first_ip)


def get_penultimate_usable_ip_address_from_raw_address(raw_address):
    """
    Gets penultimate usable ip address from raw address.
    >>> get_penultimate_usable_ip_address_from_raw_address\
        ('91.124.230.205/30')
    '91.124.230.205'
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    broadcast = decimal_to_binary(get_broadcast_address_from_raw_address
                                  (raw_address)).split(".")
    broadcast[3] = str(bin(int(broadcast[3], 2)-2))[2:]
    penultimate_ip = list(map(lambda x: str(int(x, 2)), broadcast))

    return ".".join(penultimate_ip)


def get_number_of_usable_hosts_from_raw_address(raw_address):
    """
    Gets number of usable hosts from raw address.
    >>> get_number_of_usable_hosts_from_raw_address\
        ('91.124.230.205/30')
    2
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    return 2**(32-int(raw_address[raw_address.find("/") + 1:]))-2


def get_ip_class_from_raw_address(raw_address):
    """
    Gets ip class from raw address.
    >>> get_ip_class_from_raw_address('91.124.230.205/30')
    'A'
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    num = int(raw_address[:raw_address.find(".")])
    if num in range(1, 127):
        return 'A'
    if num in range(128, 192):
        return 'B'
    if num in range(192, 224):
        return 'C'
    if num in range(224, 240):
        return 'D'
    if num in range(240, 248):
        return 'E'


def check_private_ip_address_from_raw_address(raw_address):
    """
    Checks private ip address from raw address.
    >>> check_private_ip_address_from_raw_address('91.124.230.205/30')
    False
    """
    if check_input(raw_address) != raw_address:
        return check_input(raw_address)

    short = raw_address

    if short.startswith("10.") or short.startswith("172.16.") \
            or short.startswith("172.31.") or short.startswith("192.168."):
        return True

    return False


def decimal_to_binary(address):
    """
    Converts decimal to binary.
    >>> decimal_to_binary('91.124.230.205')
    '01011011.01111100.11100110.11001101'
    """
    return ".".join(list(map(lambda x: str(bin(int(x)))[2:].zfill(8),
                             address.split('.'))))


def binary_to_decimal(address):
    """
    Converts binary to decimal.
    >>> binary_to_decimal('01011011.01111100.11100110.11001101')
    '91.124.230.205'
    """
    return ".".join(list(map(lambda x: str(int(x, 2)),
                             address.split('.'))))


def check_input(raw_address):
    """
    Checks if input is correct.
    >>> check_input('91.124.230.205')
    'Missing prefix'
    >>> check_input('91.124.230.205/30')
    '91.124.230.205/30'
    """
    if "/" not in raw_address or len(raw_address.split("/")[1]) == 0:
        return "Missing prefix"
    if len(raw_address.split("/")[1]) <= 0 or not raw_address.\
            split("/")[1].isdigit() or raw_address.count(".") != 3:
        return "Error"
    for each in raw_address.split("/")[0].split("."):
        if not each.isdigit():
            return "Error"
        if int(each) not in range(0, 256):
            return "Error"
    return raw_address


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
