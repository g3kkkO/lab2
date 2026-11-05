import re

class Address:
    
    valid_pattern = r'(?:(?:[2][0-5][0-5]|[2][0-4][0-9]|[1][0-9]{2}|[1-9][0-9]|[0-9])\.){3}(?:[2][0-5][0-5]|[2][0-4][0-9]|[1][0-9]{2}|[1-9][0-9]|[0-9])'
    
    def __init__(self):
        pass

    @classmethod
    def address_validation(self, address) -> bool: 
        match = re.fullmatch(self.valid_pattern, address)
        if match:
            return True
        return False
    
    @classmethod
    def get_all(self,text: str) -> list[str]:
        return re.findall(self.valid_pattern, text)
    
    
    
    