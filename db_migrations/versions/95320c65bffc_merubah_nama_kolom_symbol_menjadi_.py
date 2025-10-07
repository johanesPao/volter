"""Merubah nama kolom symbol menjadi simbol di tabel PergerakanHarga

Revision ID: 95320c65bffc
Revises:
Create Date: 2025-10-08 02:20:28.810248

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "95320c65bffc"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("pergerakanharga", "symbol", new_column_name="simbol")


def downgrade() -> None:
    op.alter_column("pergerakanharga", "simbol", new_column_name="symbol")
