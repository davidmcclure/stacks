"""Add metadata columns to Text.

Revision ID: f6994b159f0f
Revises: bb79aff3199e
Create Date: 2016-06-30 10:17:23.301800

"""

# revision identifiers, used by Alembic.
revision = 'f6994b159f0f'
down_revision = 'bb79aff3199e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('text', sa.Column('author_name_first', sa.String(), nullable=True))
    op.add_column('text', sa.Column('author_name_full', sa.String(), nullable=True))
    op.add_column('text', sa.Column('author_name_last', sa.String(), nullable=True))
    op.add_column('text', sa.Column('plain_text', sa.Text(), nullable=False))
    op.add_column('text', sa.Column('title', sa.String(), nullable=False))
    op.add_column('text', sa.Column('year', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('text', 'year')
    op.drop_column('text', 'title')
    op.drop_column('text', 'plain_text')
    op.drop_column('text', 'author_name_last')
    op.drop_column('text', 'author_name_full')
    op.drop_column('text', 'author_name_first')
    ### end Alembic commands ###