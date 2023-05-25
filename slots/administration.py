from pylon.core.tools import log, web
from tools import constants as c


class Slot:
    @web.slot('administration_email_invitation_content')
    def administration_email_invitation_content(self, context, slot, payload):
        log.info('SYSYSYYS %s', payload)
        integrations = context.rpc_manager.call.integrations_get_project_integrations_by_name(
            project_id=None,
            integration_name=self.descriptor.name,
            mode=c.ADMINISTRATION_MODE
        )

        integrations = [
            integration for integration in integrations
            if integration.settings['type'] == 'invitational'
        ]

        with context.app.app_context():
            return self.descriptor.render_template(
                'administration/content.html',
                integrations=integrations,
                integrations_url='/~/administration/~/configuration/integrations'
            )

    @web.slot('users_email_invitation_content')
    def users_email_invitation_content(self, context, slot, payload):
        log.info('SYSYSYYS %s', payload)
        available_integrations = context.rpc_manager.call.get_all_integrations_by_name(
            integration_name=self.descriptor.name,
        )

        integrations = [
            integration for integration in available_integrations
            if integration.settings['type'] == 'invitational'
        ]

        with context.app.app_context():
            return self.descriptor.render_template(
                'administration/content.html',
                integrations=integrations,
                integrations_url='/-/configuration/integrations'
            )
