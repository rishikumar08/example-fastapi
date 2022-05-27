"""add content column to posts table

Revision ID: 270a487c68a7
Revises: d997c5c479ab
Create Date: 2022-05-27 11:20:04.819418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '270a487c68a7'
down_revision = 'd997c5c479ab'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
