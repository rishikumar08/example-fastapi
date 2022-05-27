"""add foreign key to post table

Revision ID: 4623fdbbbbd3
Revises: f401ae87d1ae
Create Date: 2022-05-27 11:29:41.327601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4623fdbbbbd3'
down_revision = 'f401ae87d1ae'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
