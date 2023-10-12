# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorsViev(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        try:
            name = request.data.get('name')
            description = request.data.get('description')

            Sensor(name=name, description=description).save()

            return Response({'status': 'OK'})
        except Exception as ex:
            print(ex)
            return Response({'status': 'ERROR'})
        
    def patch(self, request, id):
        try:
            description = request.data.get('description')

            Sensor.objects.filter(id=id).update(description=description)

            return Response({'status': 'OK'})
        except Exception as ex:
            print(ex)
            return Response({'status': 'ERROR'})


class MeasurementsViev(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        try:
            sensor = Sensor.objects.get(id=int(request.data.get('sensor')))
            temperature = float(request.data.get('temperature'))
            photo = request.data.get('photo')
            
            if photo:
                Measurement(sensor_id=sensor, temperature=temperature, photo=photo).save()
            else:
                Measurement(sensor_id=sensor, temperature=temperature).save()

            return Response({'status': 'OK'})
        except Exception as ex:
            print(ex)
            return Response({'status': 'ERROR'})


class SensorDetailView(APIView):
    def get(self, reuest, id):
        sensors = Sensor.objects.get(id=id)
        ser = SensorDetailSerializer(sensors)

        return Response(ser.data)
