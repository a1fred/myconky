from typing import Iterable

from monotable.table import MonoTable


def gauge(percentile, width=20, filled_char='#', empty_char=' ', summary=None):
    fill_length = int((percentile/100)*width)
    filled = filled_char * fill_length

    empty_length = width - fill_length
    empty = empty_char * empty_length

    if summary is None:
        summary = "%s%%" % str(int(percentile))

    return '[%s%s] %s' % (
        filled, empty, summary
    )


def bytes_fmt(num, suffix='b'):
    for unit in ['', 'k', 'm', 'g', 't', 'p', 'e', 'z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def table(headings: Iterable[str]=(),
          formats: Iterable[str]=(),
          cellgrid: Iterable[Iterable[object]]=((),),
          title: str='',
          ):
    # type: (...) -> str
    """Wrapper to :py:meth:`monotable.table.MonoTable.table`."""
    tbl = MonoTable()
    tbl.guideline_chars = ''
    return tbl.table(headings, formats, cellgrid, title)
