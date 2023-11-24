"""add users table

Revision ID: 32cc0cdbad52
Revises: 0a45cdc3e507
Create Date: 2023-11-24 13:14:04.044110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32cc0cdbad52'
down_revision: Union[str, None] = '0a45cdc3e507'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa. Integer (), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP (timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
