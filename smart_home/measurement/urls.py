from django.urls import path
from measurement.views import SensorsViev, MeasurementsViev, SensorDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsViev.as_view()),
    path('sensors/<int:id>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsViev.as_view()),
]
