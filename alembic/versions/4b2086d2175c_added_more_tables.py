"""Added more tables

Revision ID: 4b2086d2175c
Revises: 
Create Date: 2023-05-07 00:08:56.124609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b2086d2175c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumni_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('branch', sa.String(), nullable=True),
    sa.Column('batch', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alumni_data_id'), 'alumni_data', ['id'], unique=False)
    op.create_table('faculty_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('designation', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_faculty_data_id'), 'faculty_data', ['id'], unique=False)
    op.create_table('student_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('branch', sa.String(), nullable=True),
    sa.Column('semester', sa.String(), nullable=True),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_data_id'), 'student_data', ['id'], unique=False)
    op.create_table('alumni_experiences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('organization', sa.String(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('alumni_data_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['alumni_data_id'], ['alumni_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alumni_experiences_id'), 'alumni_experiences', ['id'], unique=False)
    op.create_table('faculty_experiences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('organization', sa.String(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('faculty_data_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_data_id'], ['faculty_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_faculty_experiences_id'), 'faculty_experiences', ['id'], unique=False)
    op.drop_index('ix_users_first_name', table_name='users')
    op.drop_index('ix_users_last_name', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_last_name', 'users', ['last_name'], unique=False)
    op.create_index('ix_users_first_name', 'users', ['first_name'], unique=False)
    op.drop_index(op.f('ix_faculty_experiences_id'), table_name='faculty_experiences')
    op.drop_table('faculty_experiences')
    op.drop_index(op.f('ix_alumni_experiences_id'), table_name='alumni_experiences')
    op.drop_table('alumni_experiences')
    op.drop_index(op.f('ix_student_data_id'), table_name='student_data')
    op.drop_table('student_data')
    op.drop_index(op.f('ix_faculty_data_id'), table_name='faculty_data')
    op.drop_table('faculty_data')
    op.drop_index(op.f('ix_alumni_data_id'), table_name='alumni_data')
    op.drop_table('alumni_data')
    # ### end Alembic commands ###
