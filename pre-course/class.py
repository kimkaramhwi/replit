# Class 를 직접 구현해 보겠습니다.
# Database 라는 이름의 class를 구현해 주세요.
# Database 클래스 내부에 다음의 속성(attribute)들을 선언해주세요.
# name : database의 이름 size : 저장할 수 있는 데이터의 max 사이즈. Size를 넘어서는 데이터를 저장할 수 없다.
# Database 클래스 내부에 다음의 메소드들을 구현해주세요.
# insert select update delete

class Database:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.dict = {}

    def insert(self, field, value):
        if len(self.dict) < self.size:
            self.dict[field] = value
    
    def select(self, field):
        if field in self.dict:
            return self.dict[field]
        else:
            return None
    
    def update(self, field, value):
        if field in self.dict:
            self.dict[field] = value
        
    def delete(self, field):
        if field in self.dict:
            del self.dict[field]