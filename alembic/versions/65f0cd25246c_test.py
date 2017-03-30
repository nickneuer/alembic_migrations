"""test

Revision ID: 65f0cd25246c
Revises: 
Create Date: 2017-03-29 21:13:53.230824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65f0cd25246c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('COMPANY',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('NAME', sa.TEXT(), nullable=False),
    sa.Column('AGE', sa.INTEGER(), nullable=False),
    sa.Column('ADDRESS', sa.CHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('COMPANY')
    # ### end Alembic commands ###
