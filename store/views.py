# python imports
import csv

# django imports
from django.conf import settings
from django.http.response import HttpResponse
from django.utils import timezone

# external imports
from django_q.models import Schedule, Task
from django_q.tasks import schedule
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

# local imports
from .utils import generate_key


class ReportViewSet(ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def trigger_report(self, request):
        report_id = generate_key()
        func = "store.tasks.generate_report"
        schedule(
            func,
            filename=report_id,
            name=report_id,
            schedule_type="O",
            next_run=timezone.now() + timezone.timedelta(seconds=1),
        )
        return Response(data={"report_id": report_id}, status=HTTP_200_OK)

    def get_report(self, request):
        report_id = request.data.get("report_id")
        if not report_id:
            return Response(
                data={"error": "required field: 'report_id'"},
                status=HTTP_400_BAD_REQUEST,
            )

        sch = Schedule.objects.filter(name=report_id)
        if sch.exists():
            return Response(data={"status": "Running"}, status=HTTP_200_OK)
        task = Task.objects.filter(group=report_id, success=True)

        file_path = settings.BASE_DIR.joinpath(f"store/export/{report_id}.csv")
        if task.exists() and file_path.is_file():
            return Response(
                data={
                    "status": "success",
                    "file": f"https://{settings.WEBHOST}/store/download/{report_id}/",
                },
                status=HTTP_200_OK,
            )
        return Response(data={"error": "File not found."}, status=HTTP_400_BAD_REQUEST)

    def download(self, request, filename):
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="report.csv"'},
        )
        file_path = settings.BASE_DIR.joinpath(f"store/export/{filename}.csv")
        with open(file_path, "r") as file:
            writer = csv.writer(response)
            writer.writerows(csv.reader(file))
        return response
