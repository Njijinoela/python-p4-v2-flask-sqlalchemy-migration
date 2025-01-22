"""rename department

Revision ID: 9220facbb445
Revises: 8f1a6f7ee511
Create Date: 2025-01-22 09:58:52.054655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9220facbb445'
down_revision = '8f1a6f7ee511'
branch_labels = None
depends_on = None




def upgrade():
    # Rename the table 'department' to 'departments'
    op.rename_table('department', 'departments')


def downgrade():
    # Rename the table 'departments' back to 'department'
    op.rename_table('departments', 'department')

