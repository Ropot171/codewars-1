def validate_pin(pin):
    if pin.isdigit():
        if len(pin) == 4 or len(pin) == 6:
            return True
    return False