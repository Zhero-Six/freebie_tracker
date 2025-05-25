"""Create freebies table

Revision ID: 1234567890ab
Revises: 
Create Date: 2025-05-26 00:45:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1234567890ab'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_name', sa.String, nullable=False),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('dev_id', sa.Integer, sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=False)
    )

def downgrade():
    op.drop_table('freebies')