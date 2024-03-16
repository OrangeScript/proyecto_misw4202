import json
import constants
from requests import get

from rabbitMqConfig import RabbitMQ

if __name__ == "__main__":
    HOST = constants.HOST
    QUEUE = constants.QUEUE_NAME

    rabbitmq = RabbitMQ(HOST, QUEUE)
    print("\nConnection stablish:", "[", HOST, "] [", QUEUE, "]")

    def new_location_alert(user_location, request_location):
        print("\nAlerta, nueva ubicación de usuario registrada:")
        print("Ubicación de usuario registrada: [", user_location,
              "], ubicación de la petición[", request_location, "]")

    def new_ip_alert(user_ip, request_ip):
        print("\nAlerta, nueva Ip de usuario registrada:")
        print("Ip de usuario registrada: [", user_ip,
              "], Ip de la petición[", request_ip, "]")

    def process_message(body):
        # Usando homólogo de JSON.parse de Js para strings que pueden ser elementos de Python
        """ print("Processing message:", json.loads(body.decode('utf-8'))) """

        decoded_message = body.decode('utf-8')
        try:
            response = get(
                f'http://localhost:5001/socio/1').json()

            message = json.loads(decoded_message)

            equal_city_validation = message["ciudad"] != response["ciudad"]

            ip_validation = message["ip"] != response["ip"]

            if equal_city_validation:
                new_location_alert(response["ciudad"], message["ciudad"])
            elif ip_validation:
                new_ip_alert(response["ip"], message["ip"])

            print("\nProcessing message:", message)

        except json.JSONDecodeError as e:
            print("\nDecoded message:", decoded_message)
            print("Python decoding Error:", e)

    rabbitmq.start_consuming(process_message)

    while True:
        pass
