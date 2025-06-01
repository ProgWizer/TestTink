from tinkoff.invest import Client, InstrumentIdType
from .config import TINKOFF_TOKEN

def quotation_to_float(q):
    return q.units + q.nano / 1_000_000_000

def get_portfolio_info(user_id: int = None) -> str:
    output = []

    with Client(TINKOFF_TOKEN) as client:
        accounts = client.users.get_accounts()

        for acc in accounts.accounts:
            output.append(f"📂 Счёт: {acc.name or acc.id}")

            portfolio = client.operations.get_portfolio(account_id=acc.id)

            if not portfolio.positions:
                output.append("  🕳 Портфель пуст.")
                continue

            for position in portfolio.positions:
                figi = position.figi
                expected_yield = quotation_to_float(position.expected_yield)

                try:
                    instrument = client.instruments.get_instrument_by(
                        id=figi, id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI
                    )
                    name = instrument.instrument.name
                except Exception:
                    name = f"[FIGI: {figi}]"

                output.append(f"  📈 {name}: доход {expected_yield:.2f} ₽")

    return "\n".join(output)
