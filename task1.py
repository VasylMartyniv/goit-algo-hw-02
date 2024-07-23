import queue
import random
import time

requests_queue = queue.Queue()

request_id = 0


def generate_request():
    global request_id
    request_id += 1
    new_request = f"Request-{request_id}"
    print(f"Generated: {new_request}")

    requests_queue.put(new_request)

    time.sleep(random.uniform(0.5, 2))


def process_request():
    if not requests_queue.empty():
        current_request = requests_queue.get()
        print(f"Processing: {current_request}")

        time.sleep(random.uniform(1, 3))

        requests_queue.task_done()
    else:
        print("Queue is empty")
        time.sleep(1)


if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
