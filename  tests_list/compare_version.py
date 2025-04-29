def compare_version(version1, version2):
    [a1, b1] = version1.split('.')
    [a2, b2] = version2.split('.')

    if  int(a1) > int(a2):
        return 1
    elif int(a1) < int(a2):
        return -1
    elif int(b1) > int(b2):
        return 1
    elif int(b1) < int(b2):
        return -1
    return 0



def test_compare():
    assert compare_version('0.1', '0.2') == -1
    assert compare_version('0.2', '0.1') == 1
    assert compare_version('4.2', '4.2') == 0
    assert compare_version('0.2', '0.12') == -1
    assert compare_version('3.2', '4.12') == -1
    assert compare_version('3.2', '2.12') == 1


