"""Updated user table to include username and password columns

Revision ID: a89d335bed1c
Revises: 3b806c7838c1
Create Date: 2023-12-13 12:28:35.597430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a89d335bed1c'
down_revision = '3b806c7838c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
