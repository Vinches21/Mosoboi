import random
from data.data import Person
from faker import Faker

faker = Faker(locale='ru_RU')

def generated_person():
    yield Person(
        fio=faker.first_name() + " " + faker.last_name() + " " + faker.middle_name(),
        address=faker.address(),
        phone=random.randint(9000000000, 9999999999),
        email=faker.email(),
        order_number=random.randint(1000, 5000),
        order_date=random.randint(2018, 2022),
        brand=faker.name(),
        collection= faker.name(),
        article=random.randint(111111, 555555),
        part_number=random.randint(1, 15),
        quantity=random.randint(8, 30),
        deffect_quantity=random.randint(1, 5),
        opened_quantity=random.randint(1, 5),
        closed_quantity=random.randint(1, 5),
        used_quantity=random.randint(1, 5),
        message=faker.text(),
        city=faker.city()

    )

def generated_file_jpg():
    path = rf'C:\Users\Home\PycharmProjects\mosoboi\filetest{random.randint(0, 999)}.jpg'
    file = open(path, 'w+')
    file.close()
    return file.name, path

def generated_file_txt():
    path = rf'C:\Users\Home\PycharmProjects\mosoboi\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hi Beach {random.randint(0,10)}!')
    file.close()
    return file.name, path