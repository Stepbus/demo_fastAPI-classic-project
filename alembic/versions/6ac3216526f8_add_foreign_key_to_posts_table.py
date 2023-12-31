"""add foreign-key to posts table

Revision ID: 6ac3216526f8
Revises: 7ea310b515d3
Create Date: 2023-09-26 14:30:14.768789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ac3216526f8'
down_revision: Union[str, None] = '7ea310b515d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('owner_id', sa.Integer(),
                                     nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts',
                          referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
