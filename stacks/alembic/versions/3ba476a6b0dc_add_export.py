"""Add export.

Revision ID: 3ba476a6b0dc
Revises: e07265289e92
Create Date: 2016-07-21 21:58:35.080644

"""

# revision identifiers, used by Alembic.
revision = '3ba476a6b0dc'
down_revision = 'e07265289e92'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('export',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min_year', sa.Integer(), nullable=True),
    sa.Column('max_year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('export')
    ### end Alembic commands ###
