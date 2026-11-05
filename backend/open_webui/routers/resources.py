"""External resource directory endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status

from open_webui.internal.db import get_async_session
from open_webui.models.resources import ResourceForm, Resources
from open_webui.utils.auth import get_admin_user, get_verified_user
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get('')
async def get_resources(user=Depends(get_verified_user), db: AsyncSession = Depends(get_async_session)):
    return await Resources.get_resources(enabled_only=True, db=db)


@router.get('/all')
async def get_all_resources(user=Depends(get_admin_user), db: AsyncSession = Depends(get_async_session)):
    return await Resources.get_resources(enabled_only=False, db=db)


@router.post('')
async def create_resource(
    form_data: ResourceForm, user=Depends(get_admin_user), db: AsyncSession = Depends(get_async_session)
):
    resource = await Resources.insert_resource(form_data, db=db)
    if not resource:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Failed to create resource')
    return resource


@router.post('/{resource_id}/update')
async def update_resource(
    resource_id: str,
    form_data: ResourceForm,
    user=Depends(get_admin_user),
    db: AsyncSession = Depends(get_async_session),
):
    resource = await Resources.update_resource(resource_id, form_data, db=db)
    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Resource not found')
    return resource


@router.delete('/{resource_id}/delete')
async def delete_resource(
    resource_id: str, user=Depends(get_admin_user), db: AsyncSession = Depends(get_async_session)
):
    result = await Resources.delete_resource(resource_id, db=db)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Resource not found')
    return result
