"""empty message

Revision ID: e50c661794b7
Revises: 14bdd204a317
Create Date: 2018-12-08 11:49:56.937070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e50c661794b7'
down_revision = '14bdd204a317'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('businessesid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['businessesid'], ['businesses.id'], name='category_businessesid_fkey'),
    sa.PrimaryKeyConstraint('id', name='category_pkey')
    )
    # ### end Alembic commands ###
