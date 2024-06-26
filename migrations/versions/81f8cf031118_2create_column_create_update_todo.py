"""2create_column_create_update_todo

Revision ID: 81f8cf031118
Revises: 7c58fa9c2e49
Create Date: 2024-05-15 11:53:35.799877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81f8cf031118'
down_revision: Union[str, None] = '7c58fa9c2e49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('create_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    op.add_column('todos', sa.Column('update_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'update_at')
    op.drop_column('todos', 'create_at')
    # ### end Alembic commands ###
