"""add content column to posts table

Revision ID: 47633eb1e264
Revises: e43bb94e9f62
Create Date: 2023-09-26 14:09:53.844126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47633eb1e264'
down_revision: Union[str, None] = 'e43bb94e9f62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
