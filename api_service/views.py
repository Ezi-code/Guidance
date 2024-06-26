from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from google_auth_oauthlib.flow import Flow
import os


def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }


# @login_required(login_url=reverse_lazy("accounts:staff_login"))
def oauth_callback(request):
    flow = Flow.from_client_secrets_file(
        "C:\\Users\\USER\\Documents\\code\\Guidance\\api_service\\creds.json",
        scopes=["https://www.googleapis.com/auth/calendar.events"],
        redirect_uri="http://localhost:8000/api/oauth2callback/",
    )

    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials
    request.session["credentials"] = credentials_to_dict(credentials)

    return redirect("staff:requests")


# @login_required(login_url=reverse_lazy("accounts:staff_login"))
def initiate_auth(request):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    flow = Flow.from_client_secrets_file(
        "C:\\Users\\USER\\Documents\\code\\Guidance\\api_service\\creds.json",
        scopes=["https://www.googleapis.com/auth/calendar.events"],
        redirect_uri="http://localhost:8000/api/oauth2callback/",
    )

    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )

    request.session["state"] = state
    return redirect(authorization_url)


def calendar(request):
    return HttpResponse("Calendar")
