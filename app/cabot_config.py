
import os

CABOT_FROM_EMAIL = os.environ.get('CABOT_FROM_EMAIL')
GRAPHITE_API = os.environ.get('GRAPHITE_API')
GRAPHITE_USER = os.environ.get('GRAPHITE_USER')
GRAPHITE_PASS = os.environ.get('GRAPHITE_PASS')
JENKINS_API = os.environ.get('JENKINS_API')
JENKINS_USER = os.environ.get('JENKINS_USER')
JENKINS_PASS = os.environ.get('JENKINS_PASS')
HIPCHAT_ALERT_ROOM = os.environ.get('HIPCHAT_ALERT_ROOM')
HIPCHAT_API_KEY = os.environ.get('HIPCHAT_API_KEY')
HIPCHAT_URL = os.environ.get('HIPCHAT_URL')
SMS_PROVIDER = os.environ.get('SMS_PROVIDER', 'TWILIO')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_OUTGOING_NUMBER = os.environ.get('TWILIO_OUTGOING_NUMBER')
CLICKATELL_USERNAME = os.environ.get('CLICKATELL_USERNAME')
CLICKATELL_PASSWORD = os.environ.get('CLICKATELL_PASSWORD')
CLICKATELL_API_ID = os.environ.get('CLICKATELL_API_ID')
CLICKATELL_OUTGOING_NUMBER = os.environ.get('CLICKATELL_OUTGOING_NUMBER')
CALENDAR_ICAL_URL = os.environ.get('CALENDAR_ICAL_URL')
WWW_HTTP_HOST = os.environ.get('WWW_HTTP_HOST')