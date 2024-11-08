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
# userprofile = User(name="jack", email="email@gmail.com", acc_id= -123)

print(userprofile)
print(userprofile.email)
