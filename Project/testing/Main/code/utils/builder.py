import faker 

fake = faker.Faker()

class Builder:
    
    def name(self):
        name = fake.lexify(text='????????')
        return name

    def passw(self):
        passw = fake.password()
        return passw

    def email(self):
        mail = fake.email()
        return mail

    def text(self, num):
        text = fake.lexify(text='?'*num)
        return text