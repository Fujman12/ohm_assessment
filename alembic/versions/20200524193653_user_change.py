"""user change

Revision ID: 5ace1ceaf98
Revises: 00000000
Create Date: 2020-05-24 19:36:53.665985

"""

# revision identifiers, used by Alembic.
revision = '5ace1ceaf98'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user
                  SET point_balance = 500.00 WHERE user_id = 1''')

    op.execute('''INSERT INTO rel_user (user_id, rel_lookup, attribute)
        VALUES (2, 'LOCATION', 'USA');
    ''')

    op.execute('''UPDATE user
                  SET tier = 'Silver' 
                  WHERE user_id = 2;  ''')


def downgrade():
    op.execute('''UPDATE user
                  SET point_balance = 0 WHERE user_id = 1''')

    op.execute('''DELETE FROM rel_user
        WHERE user_id = 2;
    ''')

    op.execute('''UPDATE user
                  SET tier = '' 
                  WHERE user_id = 2;  ''')

