import random
import string


class PasswordGenerator:
    charset = string.ascii_letters + string.digits

    def __init__(self, length, charset = charset, count = 1):
        self.length = length
        self.charset = charset
        self.count = count
        self.generated_passwords = 0



    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_passwords >= self.count:
            raise StopIteration
        else:
            password = ""
            for i in range(self.length):
                password += random.choice(self.charset)

            self.generated_passwords += 1
            return password



if __name__ == "__main__":

    password_generator = PasswordGenerator(length=10, count=3)
    for password in password_generator:
        print(password)

    print()
    charset = string.ascii_letters
    password_generator2 = PasswordGenerator(length=5, charset=charset, count=2)
    iterator = iter(password_generator2)

    try:
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
    except StopIteration:
        print("No more passwords to generate.")

    print()
    password_generator3 = PasswordGenerator(length=5, count=2)
    print(next(password_generator3))



    
