from django.urls import path
from .views import (history_list, history_details, history_post, best_score_by_section)

app_name = "history"

urlpatterns = [
    path('<int:section>', history_list),
    path('<int:section>/best', best_score_by_section),
    path('<int:pk>', history_details, name="detail"),
    path('', history_post)
]
