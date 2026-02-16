from fastapi import APIRouter, Depends, status
from schemas.profile import ProfileCreate, ProfileResponse
from services.profile_service import (
    create_profile,
    get_profile,
    update_profile,
    delete_profile
)
from auth.dependencies import get_current_user

router = APIRouter(
    prefix="/profiles",
    tags=["Profiles"]
)

@router.post(
    "/",
    response_model=ProfileResponse,
    status_code=status.HTTP_201_CREATED
)
def create(data: ProfileCreate, user=Depends(get_current_user)):
    return create_profile(data, user)


@router.get(
    "/",
    response_model=ProfileResponse
)
def read(user=Depends(get_current_user)):
    return get_profile(user)


@router.put(
    "/",
    response_model=ProfileResponse
)
def update(data: ProfileCreate, user=Depends(get_current_user)):
    return update_profile(data, user)


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(user=Depends(get_current_user)):
    delete_profile(user)
