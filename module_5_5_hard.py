import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha384(password.encode())
        #password = hashlib.sha256(password.encode())
        self.age = age
        print(self.password)
class Video:
    def __init__(self, title, duration,):
        self.title = title # заголовок
        self.duration = duration # продолжительность(в секундах)
        self.time_now = 0   #  секунда остановки
        self.adult_mode = False  #  ограничение по возрасту

class UrTube:
    def __init__(self):
        self.users = ()  #  список объектов User
        self.videos = ()  #  список объектов Video
        #self.current_user = () # текущий пользователь, User

    def log_in(self, nickname, password):
        users = self.users(nickname)
        if users == nickname and password == User(self.password): #hashlib.sha256(password.encode()).hexdigest():
            current_user = nickname
            return print("Есть такой")

# Не могу понять как работать с хэшированнием, и как связывать классы между собой,
# и дальше по пунктам незнаю как их связывать, 





if __name__ == "__main__":
    urtube = UrTube()
    #user = User(input('Логин: '), input('Пароль:'), input('Возраст:'))
    user = User('Timi',"123tre", 20 )



