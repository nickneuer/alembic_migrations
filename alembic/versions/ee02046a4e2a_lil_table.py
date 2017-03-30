"""lil table

Revision ID: ee02046a4e2a
Revises: b8b1cc7766b3
Create Date: 2017-03-29 22:39:54.073097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee02046a4e2a'
down_revision = 'b8b1cc7766b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('LIL_TABLE',
    sa.Column('T_ID', sa.INTEGER(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('LIL_TABLE')
    # ### end Alembic commands ###