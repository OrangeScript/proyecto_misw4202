import json
import constants

from rabbitMqConfig import RabbitMQ

if __name__ == "__main__":
    HOST = constants.HOST
    QUEUE = constants.QUEUE_NAME

    rabbitmq = RabbitMQ(HOST, QUEUE)
    print("\nConnection stablish:", "[", HOST, "] [", QUEUE, "]")

    def process_message(body):
        # Usando homólogo de JSON.parse de Js para strings que pueden ser elementos de Python
        """ print("Processing message:", json.loads(body.decode('utf-8'))) """

        decoded_body = body.decode('utf-8')
        try:
            python_object = json.loads(decoded_body)
            print("\nProcessing message:", python_object)
        except json.JSONDecodeError as e:
            print("\nDecoded message:", decoded_body)
            print("Python decoding Error:", e)

    rabbitmq.start_consuming(process_message)

    while True:
        pass
