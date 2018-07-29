"""photo fields

Revision ID: aacde0f57395
Revises: 3db2384567db
Create Date: 2018-07-29 08:14:35.803286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aacde0f57395'
down_revision = '3db2384567db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('photo', sa.String(), nullable=True))
    op.create_index(op.f('ix_item_photo'), 'item', ['photo'], unique=False)
    op.add_column('nonprofit', sa.Column('photo', sa.String(), nullable=True))
    op.create_index(op.f('ix_nonprofit_photo'), 'nonprofit', ['photo'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_nonprofit_photo'), table_name='nonprofit')
    op.drop_column('nonprofit', 'photo')
    op.drop_index(op.f('ix_item_photo'), table_name='item')
    op.drop_column('item', 'photo')
    # ### end Alembic commands ###