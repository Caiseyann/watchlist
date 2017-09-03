"""Update User Model

Revision ID: 9497e0b17278
Revises: 7d08a80b9f72
Create Date: 2017-09-04 02:55:41.490252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9497e0b17278'
down_revision = '7d08a80b9f72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###
