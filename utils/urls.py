from django.urls import path

from utils import views as util_views


urlpatterns = [
    path('upload_excel/', util_views.CreateTestDataExcelView.as_view(), name='upload_excel_file'),
]
