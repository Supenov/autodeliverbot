from .callbacks.shop import rt as shop_rt
from .callbacks.back_to_menu import rt as back_to_menu_rt
from .callbacks.user_profile import rt as profile_rt
from .cmds.start import rt as start_rt


# Список всех роутеров — удобно для импорта
__all_routers__ = [
    start_rt,
    shop_rt,
    profile_rt,
    back_to_menu_rt,
]
