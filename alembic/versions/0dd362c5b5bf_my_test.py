"""My Test

Revision ID: 0dd362c5b5bf
Revises: 
Create Date: 2019-07-31 10:20:33.478780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dd362c5b5bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='schema_case'
    )
    op.create_index(op.f('ix_schema_case_user_email'), 'user', ['email'], unique=True, schema='schema_case')
    op.create_index(op.f('ix_schema_case_user_full_name'), 'user', ['full_name'], unique=False, schema='schema_case')
    op.create_index(op.f('ix_schema_case_user_id'), 'user', ['id'], unique=False, schema='schema_case')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_schema_case_user_id'), table_name='user', schema='schema_case')
    op.drop_index(op.f('ix_schema_case_user_full_name'), table_name='user', schema='schema_case')
    op.drop_index(op.f('ix_schema_case_user_email'), table_name='user', schema='schema_case')
    op.drop_table('user', schema='schema_case')
    # ### end Alembic commands ###
