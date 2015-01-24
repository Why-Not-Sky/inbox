"""add message index

Revision ID: 2b288dc444f
Revises: 284227d72f51
Create Date: 2015-01-25 02:41:29.572193

"""

# revision identifiers, used by Alembic.
revision = '2b288dc444f'
down_revision = '284227d72f51'

from alembic import op


def upgrade():
    op.create_index('ix_message_ns_id_is_draft_received_date', 'message',
                    ['namespace_id', 'is_draft', 'received_date'],
                    unique=False)


def downgrade():
    op.drop_index('ix_message_ns_id_is_draft_received_date', table_name='message')
