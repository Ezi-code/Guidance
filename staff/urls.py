from django.urls import path
from staff import views


app_name = "staff"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("appointments", views.AppointmentsView.as_view(), name="appointments"),
    path("completed", views.CompletedView.as_view(), name="completed"),
    path("requests", views.RequestsView.as_view(), name="requests"),
    path("client-progress", views.ClientProgrssView.as_view(), name="client_progress"),
    path("request/<uuid>", views.SingeleRequests.as_view(), name="single_request"),
    path(
        "past-session/<uuid>", views.CompletedSessions.as_view(), name="past_sessions"
    ),
    path("previous-notes", views.PreviousNotes.as_view(), name="previous_notes"),
    path("client-referal", views.ClientReferralView.as_view(), name="client_referral"),
    path(
        "complete-session/<uuid>", views.CompleteTask.as_view(), name="complete_session"
    ),
    path(
        "detail-past-session/<int:pk>",
        views.SinglePastSession.as_view(),
        name="detail_past_session",
    ),
]
