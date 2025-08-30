from .callbacks.open_profile_callback import router as open_profile_callback_router
from .callbacks.return_to_menu_callback import router as return_to_menu_callback_router
from .callbacks.ai_setup.choose_model_callback import router as choose_model_callback_router

from .cmds.cmd_menu import router as cmd_menu_router
from .cmds.cmd_start import router as cmd_start_router

# Список всех роутеров — удобно для импорта
__all_routers__ = [
    return_to_menu_callback_router,
    open_profile_callback_router,
    cmd_start_router,
    cmd_menu_router,
]

__ai_setup_routers__ = [
    choose_model_callback_router,

]