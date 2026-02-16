from pydantic import BaseModel, EmailStr

class ProfileCreate(BaseModel):
    full_name: str

class ProfileResponse(BaseModel):
    id: str
    email: EmailStr | None = None
    full_name: str
