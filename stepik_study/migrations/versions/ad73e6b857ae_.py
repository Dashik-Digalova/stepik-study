"""empty message

Revision ID: ad73e6b857ae
Revises: 
Create Date: 2020-06-24 20:44:10.981239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad73e6b857ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('date', sa.String(), nullable=False))
    op.add_column('requests', sa.Column('goal', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requests', 'goal')
    op.drop_column('requests', 'date')
    # ### end Alembic commands ###
