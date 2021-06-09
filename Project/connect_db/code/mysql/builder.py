from mysql.models import Users

class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def fill_user(self, name, pswrd, email, data):
        row = Users(
            username = name,
            password = pswrd,
            email = email,
            access = 1,
            active = 0,
            start_active_time = data
        )
        self.client.session.add(row)
        self.client.session.commit()

