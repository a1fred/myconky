import argparse
from typing import List, Iterator

from myconky.core.receipt import AbstractRepecit
from myconky.core.utils import table
from myconky.receipts import RECEIPTS_MAPPING


def get_receipts(receipts: List[str]) -> Iterator[AbstractRepecit]:
    for r_str in receipts:
        r_klass = RECEIPTS_MAPPING[r_str]
        if not r_klass.is_supported():
            raise SystemError("%s is not supported on your OS." % r_str)
        yield r_klass()


def get_cells(receipts: List[str]):
    for r in get_receipts(receipts):
        for n, g in r.get_info():
            yield (n, g)
        yield ("", "")


def main():
    parser = argparse.ArgumentParser('myconky')
    parser.add_argument('receipts', nargs="+", choices=list(RECEIPTS_MAPPING.keys()))
    args = vars(parser.parse_args())

    print(table(cellgrid=get_cells(**args)))
