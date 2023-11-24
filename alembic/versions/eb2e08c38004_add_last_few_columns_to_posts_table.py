"""add last few columns to posts table

Revision ID: eb2e08c38004
Revises: 9434e7526525
Create Date: 2023-11-24 13:30:42.936926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb2e08c38004'
down_revision: Union[str, None] = '9434e7526525'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column (
        'published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP (timezone=True), nullable=False, server_default=sa.text
        ('NOW()')), )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
