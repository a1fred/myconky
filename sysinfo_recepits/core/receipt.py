from typing import List, Tuple


class AbstractRepecit:
    def get_info(self) -> List[Tuple[str, str]]:
        raise NotImplementedError
