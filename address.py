import re

class Address:
    
    pattern = r'(?:(?:[0-9]|[1-9][0-9]|[1][0-9]{2}|[2][0-4][0-9]|[2][0-5][0-5])\.){3}(?:[0-9]|[1-9][0-9]|[1][0-9]{2}|[2][0-4][0-9]|[2][0-5][0-5])'

    def __init__(self):
        pass

    def address_validation(self, address) -> bool: 
        match = re.fullmatch(self.pattern, address)
        if match:
            return True
        return False
    
    
    def get_all(self,text: str) -> list[str]:
        return re.findall(self.pattern, text)
    
    
    
    