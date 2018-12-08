"""empty message

Revision ID: 83f1a769fc2b
Revises: a020bf35fc99
Create Date: 2018-12-06 23:55:38.272332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83f1a769fc2b'
down_revision = 'a020bf35fc99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catalogues', sa.Column('picture_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('catalogues', 'picture_path')
    # ### end Alembic commands ###
