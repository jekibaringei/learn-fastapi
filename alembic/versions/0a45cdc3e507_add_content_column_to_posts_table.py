"""add content column to posts table

Revision ID: 0a45cdc3e507
Revises: ba6cee60bfc1
Create Date: 2023-11-24 13:05:37.097054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a45cdc3e507'
down_revision: Union[str, None] = 'ba6cee60bfc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
