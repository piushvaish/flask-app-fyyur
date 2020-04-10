"""empty message

Revision ID: 3f14c9af10c9
Revises: 7a6fb21e2329
Create Date: 2020-04-10 21:58:14.660233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f14c9af10c9'
down_revision = '7a6fb21e2329'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###