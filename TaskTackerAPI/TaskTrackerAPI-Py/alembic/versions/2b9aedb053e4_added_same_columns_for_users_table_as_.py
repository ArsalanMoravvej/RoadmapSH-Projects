"""added same columns for users table as well.

Revision ID: 2b9aedb053e4
Revises: efe2156fd3d0
Create Date: 2025-02-14 17:02:49.894722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b9aedb053e4'
down_revision: Union[str, None] = 'efe2156fd3d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    op.add_column('users', sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True))
    op.add_column('users', sa.Column('last_modified_at', sa.TIMESTAMP(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_modified_at')
    op.drop_column('users', 'deleted_at')
    op.drop_column('users', 'is_deleted')
    # ### end Alembic commands ###
