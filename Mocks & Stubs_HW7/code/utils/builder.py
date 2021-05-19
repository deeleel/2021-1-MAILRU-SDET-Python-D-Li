import faker

fake = faker.Faker()


class Builder:

    def name():
        get_name = fake.first_name()
        return get_name

    def surname():
        get_surname = fake.last_name()
        return get_surname
    