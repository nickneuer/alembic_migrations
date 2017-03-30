"""new table

Revision ID: 1586f309b075
Revises: 65f0cd25246c
Create Date: 2017-03-29 21:18:12.355576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1586f309b075'
down_revision = '65f0cd25246c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ARTIST',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('ARTIST_NAME', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ARTIST')
    # ### end Alembic commands ###