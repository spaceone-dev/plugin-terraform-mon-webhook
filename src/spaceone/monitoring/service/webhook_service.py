import logging
from spaceone.core.service import *

_LOGGER = logging.getLogger(__name__)

@authentication_handler
@authorization_handler
@event_handler
class WebhookService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @check_required(['options'])
    def init(self, params):
        """ init plugin by options
                """
        return {'metadata': {}}

    @transaction
    @check_required(['options'])
    def verify(self, params):
        """
        Args:
              params:
                - options
        """
        options = params['options']
        return {}