class DeviceTypeNotFoundException(Exception):
    # Gerätetyp-ID existiert nicht
    def __init__(self, message, errors):
        super().__init__(message)
    
class DeviceNotFoundException(Exception):
    # Gerät (Pin) nicht gefunden
    def __init__(self, message, errors):
        super().__init__(message)
    