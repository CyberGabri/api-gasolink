from typing import Dict
from fastapi import HTTPException, status

fake_db: Dict[str, dict] = {}

def create_profile(data, user):
    user_id = user["sub"]

    if user_id in fake_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile já existe"
        )

    profile = {
        "id": user_id,
        "email": user.get("email"),
        "full_name": data.full_name
    }

    fake_db[user_id] = profile
    return profile


def get_profile(user):
    user_id = user["sub"]
    profile = fake_db.get(user_id)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile não encontrado"
        )

    return profile


def update_profile(data, user):
    user_id = user["sub"]
    profile = fake_db.get(user_id)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile não encontrado"
        )

    profile["full_name"] = data.full_name
    return profile


def delete_profile(user):
    user_id = user["sub"]

    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile não encontrado"
        )

    fake_db.pop(user_id)
