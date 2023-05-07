"""Fixed the answers table

Revision ID: 89858c77e43c
Revises: c3d680efa051
Create Date: 2023-05-07 17:27:18.648755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89858c77e43c'
down_revision = 'c3d680efa051'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'answers', 'users', ['user_id'], ['id'])
    op.drop_column('answers', 'question_user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('question_user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'answers', type_='foreignkey')
    op.drop_column('answers', 'user_id')
    # ### end Alembic commands ###
