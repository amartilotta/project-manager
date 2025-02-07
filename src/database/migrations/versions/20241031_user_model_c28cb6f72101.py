"""user model

Revision ID: c28cb6f72101
Revises: d87a59fb8f8a
Create Date: 2024-10-31 00:02:22.512216

"""

from typing import List, Optional, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c28cb6f72101"
down_revision: Optional[str] = "d87a59fb8f8a"
branch_labels: Optional[Union[str, List[str]]] = None
depends_on: Optional[Union[str, List[str]]] = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "first_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "last_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "password", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###
