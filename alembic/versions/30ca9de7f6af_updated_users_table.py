"""Updated users table

Revision ID: 30ca9de7f6af
Revises: a318ae410ee7
Create Date: 2023-05-05 09:46:40.086933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30ca9de7f6af'
down_revision = 'a318ae410ee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('roll_no', sa.String(), nullable=False))
    op.create_index(op.f('ix_users_roll_no'), 'users', ['roll_no'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_roll_no'), table_name='users')
    op.drop_column('users', 'roll_no')
    # ### end Alembic commands ###
