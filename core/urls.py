from django.urls import path
from .views import (
    analysis_list,
    analysis_create,
    analysis_detail,
    analysis_update,
    analysis_delete,
    data_list,
    data_detail,
    data_create,
    data_update,
    data_delete,
    data_upload,
    data_analysis,
    project_list,
    project_detail,
    project_create,
    project_update,
    project_delete,
    text_analysis,
    dashboard,
    conversion_analytics,
    performance_metrics,
    subscription_analytics,
)

app_name = "core"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("", dashboard, name="dashboard"),
    path("data/", data_list, name="data_list"),
    path("data/create/", data_create, name="data_create"),
    path("data/<int:data_id>/", data_detail, name="data_detail"),
    path("data/<int:data_id>/analysis/", data_analysis, name="data_analysis"),
    path("data/<int:data_id>/text-analysis/", text_analysis, name="text_analysis"),
    path("data/<int:data_id>/subscription-analytics/", subscription_analytics, name="subscription_analytics"),
    path(
        "data/<int:data_id>/performance-metrics/",
        performance_metrics,
        name="performance_metrics",
    ),
    path(
        "data/<int:data_id>/conversion-analytics/",
        conversion_analytics,
        name="conversion_analytics",
    ),
    path("data/<int:data_id>/update/", data_update, name="data_update"),
    path("data/<int:data_id>/upload/", data_upload, name="data_upload"),
    path("data/<int:data_id>/delete/", data_delete, name="data_delete"),
    path("projects/", project_list, name="project_list"),
    path("projects/create/", project_create, name="project_create"),
    path("projects/<int:project_id>/", project_detail, name="project_detail"),
    path("projects/<int:project_id>/update/", project_update, name="project_update"),
    path("projects/<int:project_id>/delete/", project_delete, name="project_delete"),
    path("analysis/", analysis_list, name="analysis_list"),
    path("analysis/create/", analysis_create, name="analysis_create"),
    path("analysis/<int:analysis_id>/", analysis_detail, name="analysis_detail"),
    path("analysis/<int:analysis_id>/update/", analysis_update, name="analysis_update"),
    path("analysis/<int:analysis_id>/delete/", analysis_delete, name="analysis_delete"),
]
