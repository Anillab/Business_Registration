"""empty message

Revision ID: edd25f8319cc
Revises: 83f1a769fc2b
Create Date: 2018-12-07 12:36:05.577732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edd25f8319cc'
down_revision = '83f1a769fc2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('businessesid', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'businesses', ['businessesid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'businessesid')
    # ### end Alembic commands ###
