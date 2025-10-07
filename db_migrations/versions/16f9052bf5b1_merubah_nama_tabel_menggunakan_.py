"""Merubah nama tabel menggunakan PascalCase style

Revision ID: 16f9052bf5b1
Revises: 95320c65bffc
Create Date: 2025-10-08 02:32:36.043042

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "16f9052bf5b1"
down_revision: Union[str, Sequence[str], None] = "95320c65bffc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("pergerakanharga", "PergerakanHarga")
    op.rename_table("transaksi", "Transaksi")


def downgrade() -> None:
    op.rename_table("PergerakanHarga", "pergerakanharga")
    op.rename_table("Transaksi", "transaksi")
