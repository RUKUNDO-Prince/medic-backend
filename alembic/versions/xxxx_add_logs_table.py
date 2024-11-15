"""add logs table

Revision ID: xxxx
Revises: previous_revision
Create Date: 2024-xx-xx

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'logs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('message', sa.String(), nullable=False),
        sa.Column('method', sa.String(), nullable=True),
        sa.Column('path', sa.String(), nullable=True),
        sa.Column('status_code', sa.Integer(), nullable=True),
        sa.Column('ip_address', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_logs_id'), 'logs', ['id'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_logs_id'), table_name='logs')
    op.drop_table('logs') 