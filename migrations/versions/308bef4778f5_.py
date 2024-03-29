"""empty message

Revision ID: 308bef4778f5
Revises: 7539db6a2632
Create Date: 2024-03-29 11:50:04.938949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '308bef4778f5'
down_revision = '7539db6a2632'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
