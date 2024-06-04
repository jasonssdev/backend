from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Jason", surname="Dev", url="https://jasonssdev.com", age=33),
            User(id=2, name="Brais", surname="Dev", url="https://moure.dev", age=34),
            User(id=3, name="Brais", surname="Moure", url="https://mouredev.com", age=35)]

# for i in users_list:
#     print(i)

# for index, saved_user in enumerate(users_list):
#     print(index)
#     print(saved_user)
#     print(saved_user.id)
#     print(saved_user.name)
#     print(saved_user.url)

print(users_list[1])