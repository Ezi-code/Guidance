from django.urls import path
from staff import views


app_name = "staff"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("appointments", views.AppointmentsView.as_view(), name="appointments"),
    path("completed", views.CompletedSessionsView.as_view(), name="completed"),
    path("requests", views.AppointmentRequestView.as_view(), name="requests"),
    path("client-progress", views.ClientProgrssView.as_view(), name="client_progress"),
    path("request/<pk>", views.IndividualRequestsView.as_view(), name="single_request"),
    path(
        "past-session/<uuid>", views.CompletedSessions.as_view(), name="past_sessions"
    ),
    path("previous-notes", views.PreviousNotesView.as_view(), name="previous_notes"),
    path(
        "client-referal/",
        views.ClientReferralView.as_view(),
        name="client_referral",
    ),
    path(
        "complete-session/",
        views.CompleteTaskView.as_view(),
        name="complete_session",
    ),
    path(
        "detail-past-session/<int:pk>",
        views.SinglePastSessionView.as_view(),
        name="detail_past_session",
    ),
    path("refferals", views.RefferalsView.as_view(), name="refferals"),
    path(
        "reffered-client/<uuid>",
        views.ReffereClientView.as_view(),
        name="reffered_client",
    ),
    path("accept-refferals/", views.AcceptRefferal.as_view(), name="accept_refferal"),
]
