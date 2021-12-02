class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if 5 > len(value) or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_lenghtvalid(value) and self.is_upper(value) and self.is_digit(value):
            self.__password = value
            return
        raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')


    def is_lenghtvalid(self, password):
        return len(password) >= 8


    def is_upper(self, password):
        letters = [x for x in password if x.isupper()]
        if letters:
            return True
        return False


    def is_digit(self, password):
        nums = [x for x in password if x.isdigit()]
        if nums:
            return True
        return False


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {(len(self.password)*"*")}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
