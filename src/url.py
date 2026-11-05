import requests



class UrlRepository:
    
    def __init__(self, url: str):
        self.url = url
        
    def get_text(self) -> str:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text
    
    
    
    