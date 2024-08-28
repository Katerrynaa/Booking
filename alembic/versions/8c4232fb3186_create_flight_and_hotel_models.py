"""Create flight and hotel models

Revision ID: 8c4232fb3186
Revises: c4a9b17a57cc
Create Date: 2024-08-27 15:39:33.106410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c4232fb3186'
down_revision: Union[str, None] = 'c4a9b17a57cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('depature', sa.String(length=100), nullable=False),
    sa.Column('arrival', sa.String(length=100), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('adults', sa.Integer(), nullable=True),
    sa.Column('children', sa.Integer(), nullable=True),
    sa.Column('bag', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_flights_id'), 'flights', ['id'], unique=False)
    op.create_table('hotels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('checkIn', sa.DateTime(), nullable=False),
    sa.Column('checkOut', sa.DateTime(), nullable=False),
    sa.Column('adults', sa.Integer(), nullable=False),
    sa.Column('children', sa.Integer(), nullable=False),
    sa.Column('payment_currency', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hotels_id'), 'hotels', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_hotels_id'), table_name='hotels')
    op.drop_table('hotels')
    op.drop_index(op.f('ix_flights_id'), table_name='flights')
    op.drop_table('flights')
    # ### end Alembic commands ###
