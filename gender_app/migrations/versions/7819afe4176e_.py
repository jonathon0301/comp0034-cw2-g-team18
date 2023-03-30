"""empty message

Revision ID: 7819afe4176e
Revises: 63c42cc92d9a
Create Date: 2023-03-23 15:00:44.355931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7819afe4176e'
down_revision = '63c42cc92d9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_Gender_pay', sa.Column('EmployerSizeMedian', sa.String(length=128), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_Gender_pay', 'EmployerSizeMedian')
    # ### end Alembic commands ###
