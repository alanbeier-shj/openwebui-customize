"""External resource directory entries."""

from __future__ import annotations

import time
import uuid
from typing import Optional

from open_webui.internal.db import Base, get_async_db_context
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import BigInteger, Boolean, Column, Integer, Text, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class Resource(Base):
    __tablename__ = 'external_resource'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    icon = Column(Text, nullable=True)
    category = Column(Text, nullable=False, default='')
    action_type = Column(Text, nullable=False, default='open_url')
    url = Column(Text, nullable=True)
    contact_name = Column(Text, nullable=True)
    contact_method = Column(Text, nullable=True)
    contact_value = Column(Text, nullable=True)
    manual_url = Column(Text, nullable=True)
    enabled = Column(Boolean, nullable=False, default=True)
    sort_order = Column(Integer, nullable=False, default=0)
    created_at = Column(BigInteger, nullable=False)
    updated_at = Column(BigInteger, nullable=False)


class ResourceModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    description: str | None = None
    icon: str | None = None
    category: str = ''
    action_type: str = 'open_url'
    url: str | None = None
    contact_name: str | None = None
    contact_method: str | None = None
    contact_value: str | None = None
    manual_url: str | None = None
    enabled: bool = True
    sort_order: int = 0
    created_at: int
    updated_at: int


class ResourceForm(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    icon: str | None = Field(default=None, max_length=64)
    category: str = Field(default='', max_length=100)
    action_type: str = Field(default='open_url', max_length=32)
    url: str | None = Field(default=None, max_length=2048)
    contact_name: str | None = Field(default=None, max_length=200)
    contact_method: str | None = Field(default=None, max_length=100)
    contact_value: str | None = Field(default=None, max_length=500)
    manual_url: str | None = Field(default=None, max_length=2048)
    enabled: bool = True
    sort_order: int = 0


class ResourcesTable:
    async def get_resources(self, enabled_only: bool = False, db: AsyncSession | None = None) -> list[ResourceModel]:
        async with get_async_db_context(db) as db:
            query = select(Resource).order_by(Resource.sort_order.asc(), Resource.created_at.asc())
            if enabled_only:
                query = query.where(Resource.enabled.is_(True))
            resources = (await db.scalars(query)).all()
            return [ResourceModel.model_validate(resource) for resource in resources]

    async def get_resource_by_id(self, resource_id: str, db: AsyncSession | None = None) -> ResourceModel | None:
        async with get_async_db_context(db) as db:
            resource = await db.scalar(select(Resource).where(Resource.id == resource_id))
            return ResourceModel.model_validate(resource) if resource else None

    async def insert_resource(self, form_data: ResourceForm, db: AsyncSession | None = None) -> ResourceModel | None:
        now = int(time.time())
        resource = Resource(
            id=str(uuid.uuid4()),
            name=form_data.name,
            description=form_data.description,
            icon=form_data.icon,
            category=form_data.category,
            action_type=form_data.action_type,
            url=form_data.url,
            contact_name=form_data.contact_name,
            contact_method=form_data.contact_method,
            contact_value=form_data.contact_value,
            manual_url=form_data.manual_url,
            enabled=form_data.enabled,
            sort_order=form_data.sort_order,
            created_at=now,
            updated_at=now,
        )
        async with get_async_db_context(db) as db:
            db.add(resource)
            await db.commit()
            await db.refresh(resource)
            return ResourceModel.model_validate(resource)

    async def update_resource(
        self, resource_id: str, form_data: ResourceForm, db: AsyncSession | None = None
    ) -> ResourceModel | None:
        async with get_async_db_context(db) as db:
            resource = await db.get(Resource, resource_id)
            if not resource:
                return None
            values = form_data.model_dump(exclude_unset=False)
            values['updated_at'] = int(time.time())
            await db.execute(update(Resource).where(Resource.id == resource_id).values(**values))
            await db.commit()
            await db.refresh(resource)
            return ResourceModel.model_validate(resource)

    async def delete_resource(self, resource_id: str, db: AsyncSession | None = None) -> bool:
        async with get_async_db_context(db) as db:
            resource = await db.get(Resource, resource_id)
            if not resource:
                return False
            await db.delete(resource)
            await db.commit()
            return True


Resources = ResourcesTable()
