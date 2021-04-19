import faker 

fake = faker.Faker()

class Builder:
    
    def segment_inputs(self, name = None):
        name = fake.name()

        return name

    def campaign_inputs(self, name=None, title=None, text=None):
        name = fake.name()
        title = fake.name()
        text = fake.name()

        return [name, title, text]
