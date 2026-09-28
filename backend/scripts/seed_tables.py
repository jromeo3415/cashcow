import asyncio

from app.database import async_session
from app.models import *

async def seed_tables():
    with async_session as db:
        bra1 = Branch(name="South Tampa Banking", location_region=1, capacity=23, supervisor_id=1)
        bra2 = Branch(name="Beijing Credit Union", location_region=2, capacity=50, supervisor_id=2)
        bra3 = Branch(name="California Finance", location_region=3, capacity=10, supervisor_id=1)

        db.add_all([bra1, bra2, bra3])

        atm1 = ATM(serial_number="ABCD_1001", model="Cash Dispenser 2.0", status=ATMStatus.OPERATIONAL, cash_level=12.9, branch_id=bra1.id)
        atm2 = ATM(serial_number="ABCD_1048", model="Cash Dispenser 2.0", status=ATMStatus.OPERATIONAL, cash_level=100, branch_id=bra1.id)
        atm3 = ATM(serial_number="QX9332", model="Money Distributor 1.0", status=ATMStatus.MAINTENANCE, cash_level=67.1, branch_id=bra2.id)
        atm4 = ATM(serial_number="ABCD_1007", model="Cash Dispenser 2.0", status=ATMStatus.OPERATIONAL, cash_level=2.3, branch_id=bra3.id)
        atm5 = ATM(serial_number="ABCD_2009", model="Cash Dispenser 2.0", status=ATMStatus.MAINTENANCE, cash_level=19.9, branch_id=bra3.id)
        atm6 = ATM(serial_number="QX8430", model="Money Distributor 1.0", status=ATMStatus.OFFLINE, cash_level=10.3, branch_id=bra3.id)

        db.add_all([atm1, atm2, atm3, atm4, atm5, atm6])

if __name__ == "__main__":
    asyncio.run(seed_tables())