from utils.builder import Builder

base_url = 'http://notmyapp:8080/welcome/'

builder = Builder()

DEFAULT_USER = {'name': "Alexandr", 'id': 1, 'password': '111111', 'email': 'smth@mail.ru', 'date': '2020-02-03'}

LOGIN_DATA = [
    ('', '', None),
    (' ', ' ', 'Username: Fill username, Password: Fill password'),
    (DEFAULT_USER['name'], '', None),
    (DEFAULT_USER['name'], ' ', 'Fill password'),
    ('', builder.text(6), None),
    (' ', builder.text(6), 'Fill username'),
    (builder.text(6), builder.text(6), 'Invalid username or password')
]


REGISTER_DATA = [
    (' ', ' ', ' ', 'Username: Fill username, Email: Fill email, Password: Fill password'),
    ('', '', '', None),
    (builder.text(6), builder.text(6), builder.text(6), 'Invalid email address'),
    (builder.text(6), ' ', builder.email(), 'Fill password'),
    (' ', builder.text(6), builder.email(), 'Fill username'),
    (builder.text(6), builder.text(6), ' ', 'Fill email'),
    (builder.text(3), builder.text(6), builder.email(), 'Incorrect username length'),
    (builder.text(6), builder.text(3), builder.email(), 'Incorrect password length')
]


NAV_DATA = [
    ('HOME', base_url),
    ('Python', 'https://www.python.org/'),
    ('Linux', base_url),
    ('Network', base_url)
] 


LINK_DATA = [
    ('Python', 'About Flask', 'https://flask.palletsprojects.com/en/1.1.x/#'),
    ('Python', 'Python history', 'https://en.wikipedia.org/wiki/History_of_Python'),
    ('Linux', 'Download Centos7', 'https://www.centos.org/download/'),
    ('Network', 'News', 'https://www.wireshark.org/news/'),
    ('Network', 'Download', 'https://www.wireshark.org/#download'),
    ('Network', 'Examples', 'https://hackertarget.com/tcpdump-examples/'),
] 

CIRCLE_DATA = [
    ('What is an API?', 'https://en.wikipedia.org/wiki/API'),
    ('Future of internet', 'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'),
    ('Lets talk about SMTP?', 'https://ru.wikipedia.org/wiki/SMTP'),
] 
