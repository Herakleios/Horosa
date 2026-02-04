from enum import Enum

def get_enum_index(enum_member: Enum) -> int:
    """
    获取枚举成员的索引。

    参数:
        enum_member (Enum): 枚举成员。

    返回:
        int: 枚举成员的索引。
    """
    return list(enum_member.__class__).index(enum_member)

def get_enum_by_index(enum_class: type[Enum], index: int) -> [Enum]:
    """
    通过索引获取枚举成员。

    参数:
        enum_class (type[Enum]): 枚举类。
        index (int): 索引。

    返回:
        Enum: 枚举成员。
    """
    if not issubclass(enum_class, Enum):
        raise TypeError("enum_class must be a subclass of Enum")
    if not isinstance(index, int):
        raise TypeError("index must be an integer")

    enum_members = list(enum_class)
    return enum_members[index]