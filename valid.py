from pydantic import BaseModel, validator


class UserText(BaseModel):
    user_text: str

    @validator('user_text')
    def check_input_text(cls, user_text):
        if len(user_text) != 5:
            raise ValueError("Введите слово из 5 букв")
        else:
            return user_text
