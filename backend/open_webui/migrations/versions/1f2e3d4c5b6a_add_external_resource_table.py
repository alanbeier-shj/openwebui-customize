"""Add external resource directory table."""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = '1f2e3d4c5b6a'
down_revision: Union[str, None] = 'e42c8f710a36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'external_resource',
        sa.Column('id', sa.Text(), primary_key=True),
        sa.Column('name', sa.Text(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('icon', sa.Text(), nullable=True),
        sa.Column('category', sa.Text(), nullable=False, server_default=''),
        sa.Column('action_type', sa.Text(), nullable=False, server_default='open_url'),
        sa.Column('url', sa.Text(), nullable=True),
        sa.Column('contact_name', sa.Text(), nullable=True),
        sa.Column('contact_method', sa.Text(), nullable=True),
        sa.Column('contact_value', sa.Text(), nullable=True),
        sa.Column('manual_url', sa.Text(), nullable=True),
        sa.Column('enabled', sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column('sort_order', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('created_at', sa.BigInteger(), nullable=False),
        sa.Column('updated_at', sa.BigInteger(), nullable=False),
    )
    op.create_index('ix_external_resource_enabled_sort', 'external_resource', ['enabled', 'sort_order'])


def downgrade():
    op.drop_index('ix_external_resource_enabled_sort', table_name='external_resource')
    op.drop_table('external_resource')
