"""Make 'slug' on Corpus unique.

Revision ID: be8f28fccf74
Revises: 2219065cebc7
Create Date: 2016-06-29 12:33:05.557154

"""

# revision identifiers, used by Alembic.
revision = 'be8f28fccf74'
down_revision = '2219065cebc7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'corpus', ['slug'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'corpus', type_='unique')
    ### end Alembic commands ###