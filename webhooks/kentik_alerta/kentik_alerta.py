from typing import Any, Dict
import json
from alerta.models.alert import Alert

from alerta.webhooks import WebhookBase

JSON = Dict[str, Any]

class kentikWebhook(WebhookBase):
    """
    Kentik
    https://kb.kentik.com/Gc04.htm#Gc04-JSON_Notification_Settings
    """

    def incoming(self, query_string, payload):

        #Change Kentik alert states into what Alerta Understands

         try:
            resource = query_string['resource']
        except Exception:
            resource = 'kentik'
            # environment
        try:
            environment = query_string['environment']
        except Exception:
            environment = 'Production'
            # severity
        try:
            severity = query_string['severity']
        except Exception:
            severity = 'major'
            # group
        try:
            group = query_string['group']
        except Exception:
            group = 'QueryDefaultGroup'
            # event
        try:
            event = query_string['event']
        except Exception:
            event = 'QueryDefaultEvent'
            # service (Must be an array)
        try:
            service = [query_string['service']]
        except Exception:
            service = ['Kentik']
            # value
        try:
            value = query_string['Description']
        except Exception:
            value = ''
            # text
        try:
            text = query_string['text']
        except Exception:
            text = ''
            # tags (Must be an array)
        try:
            tags = query_string['tags'].split(',')
        except Exception:
            tags = []
            # origin
        try:
            origin = query_string['origin']
        except Exception:
            origin = 'Kentik'
            # timeout
        try:
            timeout = int(query_string['timeout'])
        except Exception:
            timeout = 86400

        return Alert(
            resource=resource,
            event=event,
            environment=environment,
            severity=severity,
            service=service,
            group=group,
            value=value,
            text=text,
            tags=tags,
            origin=origin,
            timeout=timeout,
            raw_data=query_string
        )
