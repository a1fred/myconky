from typing import List, Tuple


class AbstractRepecit:
    @classmethod
    def is_supported(cls) -> bool:
        return True

    def get_info(self) -> List[Tuple[str, str]]:
        raise NotImplementedError
