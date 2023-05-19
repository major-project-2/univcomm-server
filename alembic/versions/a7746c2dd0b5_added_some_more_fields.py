"""Added some more fields

Revision ID: a7746c2dd0b5
Revises: 89b162ddc39d
Create Date: 2023-05-19 09:07:24.434911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7746c2dd0b5'
down_revision = '89b162ddc39d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('announcement_files', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('announcement_files', 'name')
    # ### end Alembic commands ###