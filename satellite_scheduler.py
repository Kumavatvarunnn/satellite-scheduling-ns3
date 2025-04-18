# satellite_scheduler.py
# Simulates basic data packet scheduling for LEO satellite constellation

import heapq
import random
import time

class SatelliteNode:
    def __init__(self, node_id, latency):
        self.node_id = node_id
        self.latency = latency  # in milliseconds

    def transmit_data(self, data):
        print(f"Transmitting '{data}' from Satellite {self.node_id} with latency {self.latency}ms")

class Scheduler:
    def __init__(self):
        self.queue = []

    def add_packet(self, satellite, data):
        heapq.heappush(self.queue, (satellite.latency, satellite, data))

    def process_packets(self):
        while self.queue:
            latency, satellite, data = heapq.heappop(self.queue)
            time.sleep(latency / 1000.0)  # simulate latency
            satellite.transmit_data(data)

# Simulate network
satellites = [SatelliteNode(i, random.randint(50, 200)) for i in range(1, 6)]
scheduler = Scheduler()

# Simulate incoming packets
for i in range(10):
    sat = random.choice(satellites)
    scheduler.add_packet(sat, f"Data-{i}")

scheduler.process_packets()
