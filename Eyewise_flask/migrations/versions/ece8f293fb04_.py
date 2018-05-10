"""empty message

Revision ID: ece8f293fb04
Revises: 76c6442afb22
Create Date: 2018-04-30 09:14:29.559638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece8f293fb04'
down_revision = '76c6442afb22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    "just for the indent"
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.create_foreign_key(None, 'order', 'user', ['user_id'], ['id'])
    op.drop_column('order', 'cart_id')
    op.drop_index(op.f('ix_cart_user_id'), table_name='cart')
    op.drop_table('cart')
    # ### end Alembic commands ###