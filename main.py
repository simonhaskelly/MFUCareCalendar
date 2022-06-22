from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'canvas-mfu-3e4d7e997db5.json'
SUBJECT = 'mfucare@canvas-mfu.iam.gserviceaccount.com'
CALENDARID = '6t2vsu04c2e9k8locl6i2c6cug@group.calendar.google.com'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject(SUBJECT)
service = build('calendar', 'v3', credentials=delegated_credentials)

d = datetime.utcnow().date()
tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
start = tomorrow.isoformat()
end = (tomorrow + timedelta(hours=1)).isoformat()
body={"summary": 'Appointment ABCD',
      "description": 'Another appointment',
      "start": {"dateTime": start, "timeZone": 'Asia/Bangkok'},
      "end": {"dateTime": end, "timeZone": 'Asia/Bangkok'},
     }
event = service.events().insert(calendarId=CALENDARID, body=body).execute()
print(event)