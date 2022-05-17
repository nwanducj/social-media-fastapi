"""add content column to post table

Revision ID: a2968310bf45
Revises: 
Create Date: 2022-05-17 15:37:43.752860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2968310bf45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
