class DBExistsException(Exception):
    # Currently unused – reserved for future DB init checks
    def __init__(self, message, errors):            
        super().__init__(message)
        self.errors = errors

class DeviceTypeNotFoundException(Exception):
    # Device type ID does not exist
    def __init__(self, message, errors):
        super().__init__(message)
    
class DeviceNotFoundException(Exception):
    # Device (pin) not found
    def __init__(self, message, errors):
        super().__init__(message)
    