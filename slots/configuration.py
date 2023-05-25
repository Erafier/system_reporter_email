import json

from pylon.core.tools import log, web
import base64

from ..models.integration_pd import IntegrationModel


class Slot:
    integration_name = 'system_reporter_email'
    section_name = 'system'

    @web.slot(f'integrations_{section_name}_content')
    def integration_create_modal_content(self, context, slot, payload):
        default_template = base64.b64decode(IntegrationModel._default_template).decode('utf-8')
        allowed_types = context.rpc_manager.call.system_reporter_email_get_allowed_email_types()
        with context.app.app_context():
            return self.descriptor.render_template(
                'integration/content.html',
                default_template=default_template,
                section_name=Slot.section_name,
                allowed_types=json.dumps(allowed_types)
            )

    @web.slot(f'integrations_{section_name}_scripts')
    def integration_create_modal_scripts(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'integration/scripts.html',
            )
