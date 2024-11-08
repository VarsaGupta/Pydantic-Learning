# Json serialization

from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    name: str
    email: EmailStr
    acc_id: int

# custom validation
    @validator("acc_id")
    def validate_acc_id(cls, value):
        if value <= 0:
            raise ValueError(f"acc_id must be positive: {value}")
        return value

userprofile = User(name="jack", email="email@gmail.com", acc_id= 123)
# Json output
user_json_str = userprofile.json()
print(user_json_str)

# dictionary output
user_dict_str = userprofile.dict()
print(user_dict_str)

# convert back to raw data
json_str = '{"name":"jack","email":"email@gmail.com","acc_id":123}'
user = userprofile.parse_raw(json_str)
print(user)