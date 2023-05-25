from tools import rpc_tools
from pylon.core.tools import log
from pylon.core.tools import web


class RPC:

    @web.rpc(f'system_reporter_email_get_allowed_email_types')
    @rpc_tools.wrap_exceptions(RuntimeError)
    def get_allowed_email_types(self, **kwargs) -> list:
        return ["invitational", "task_notification"]
