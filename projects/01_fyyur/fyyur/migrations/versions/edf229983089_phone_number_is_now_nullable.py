"""Phone Number is now NULLABLE

Revision ID: edf229983089
Revises: ffbca4f8599e
Create Date: 2022-02-07 07:30:45.107008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edf229983089'
down_revision = 'ffbca4f8599e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'phone',existing_type=sa.VARCHAR(length=120),nullable=False),
    op.add_column('shows', sa.Column('artist_id', sa.Integer(),nullable=True)),
    op.add_column('shows', sa.Column('venue_id', sa.Integer(),nullable=True)),
    op.add_column('venues', sa.Column('show_id', sa.Integer(),nullable=True)),
    op.add_column('artists', sa.Column('venue_id', sa.Integer(),nullable=True))
               
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###