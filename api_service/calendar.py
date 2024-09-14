import datetime
from django.shortcuts import redirect
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.utils import timezone
from staff.services import SendEmailNotification


def main(request, appointment):

    if isinstance(appointment.session_date, str):
        session_date = datetime.datetime.strptime(
            appointment.session_date, "%Y-%m-%d"
        ).date()
    else:
        session_date = appointment.session_date

    # Convert session_time to a time object
    if isinstance(appointment.session_time, str):
        session_time = datetime.datetime.strptime(
            appointment.session_time, "%H:%M"
        ).time()
    else:
        session_time = appointment.session_time

    start_datetime = datetime.datetime.combine(session_date, session_time)
    end_datetime = start_datetime + datetime.timedelta(hours=3)

    # if "credentials" not in request.session:
    #     redirect("api_service:initiate_auth")

    # credentials = Credentials(**request.session["credentials"])

    # try:
    #     service = build("calendar", "v3", credentials=credentials)
    #     event = {
    #         "summary": "Counselling Session",
    #         "location": "ROB, SF, Room 19, Counselling Unit, AAMUSTED",
    #         "description": appointment.reason,
    #         "colorId": 6,
    #         "start": {
    #             "dateTime": start_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
    #             "timeZone": str(timezone.get_current_timezone()),
    #         },
    #         "end": {
    #             "dateTime": end_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
    #             "timeZone": str(timezone.get_current_timezone()),
    #         },
    #         "recurrence": ["RRULE:FREQ=DAILY;COUNT=1"],
    #         "attendees": [{"email": appointment.email}],
    #     }
    #     event = service.events().insert(calendarId="primary", body=event).execute()
    return SendEmailNotification.send_appointemt_accepted_email(appointment, request)
    # except HttpError as error:
    #     print(f"An error occurred: {error}")
