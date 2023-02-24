# django imports
from django.urls import path

# local imports
from .views import ReportViewSet

urlpatterns = [
    path("trigger-report/", ReportViewSet.as_view({"get": "trigger_report"})),
    path("get-report/", ReportViewSet.as_view({"get": "get_report"})),
    path("download/<str:filename>/", ReportViewSet.as_view({"get": "download"})),
]
