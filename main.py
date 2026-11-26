#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Prints exactly one original fortune-cookie line for a liquidated trader.
Deterministic: no randomness, no network, no time, no I/O beyond stdout.
"""

FORTUNE = (
    "Your lucky numbers are 100x leverage, zero margin, and one very patient "
    "liquidation bot that has already eaten your lunch — twice."
)


def main() -> None:
    print(FORTUNE)


if __name__ == "__main__":
    main()
