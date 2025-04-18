import heapq
import random
import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Encryption Stub for QKD (Basic Simulation)
def encrypt_data(data, key):
    """Simulate encryption using QKD-generated key."""
    return f"{data} | ENCRYPTED with {key}"

def decrypt_data(data, key):
    """Simulate decryption."""
    return f"{data.split(' | ')[0]} | DECRYPTED with {key}"

# Satellite Node Class
class SatelliteNode:
    def __init__(self, node_id, latency):
        self.node_id = node_id
        self.latency = latency  # in milliseconds
        self.transmit_count = 0  # To track packet transmission count

    def transmit_data(self, packet_id, data):
        self.transmit_count += 1
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Satellite {self.node_id} sending Packet {packet_id} ➜ {data}")

    def generate_qkd_key(self):
        """Generate a unique quantum key"""
        return f"QKDKEY_{self.node_id}_{random.randint(10000, 99999)}"

# Scheduler Class
class Scheduler:
    def __init__(self):
        self.queue = []
        self.latency_stats = []  # To store latency statistics for plotting

    def add_packet(self, satellite, packet_id, data):
        heapq.heappush(self.queue, (satellite.latency, satellite, packet_id, data))

    def process_packets(self):
        while self.queue:
            latency, satellite, packet_id, data = heapq.heappop(self.queue)
            time.sleep(latency / 1000.0)  # Simulate transmission delay
            self.latency_stats.append(latency)  # Track latency for stats
            satellite.transmit_data(packet_id, data)

# Simulation of Satellite Network with QKD Integration
def simulate_satellite_network():
    # Create Satellite Nodes with random latencies between 50-200ms
    satellites = [SatelliteNode(i, random.randint(50, 200)) for i in range(1, 6)]
    scheduler = Scheduler()

    for i in range(10):
        sat = random.choice(satellites)
        packet_id = f"PKT-{i}-{datetime.now().strftime('%H%M%S')}"
        key = sat.generate_qkd_key()
        encrypted_data = encrypt_data(f"Data {i}", key)
        scheduler.add_packet(sat, packet_id, encrypted_data)

    scheduler.process_packets()

    return scheduler.latency_stats

# Visualize Latency Stats
def plot_latency_distribution(latency_stats):
    """Plot the distribution of latency in satellite data transmission."""
    plt.hist(latency_stats, bins=5, color='skyblue', edgecolor='black')
    plt.title('Latency Distribution in Satellite Communication')
    plt.xlabel('Latency (ms)')
    plt.ylabel('Frequency')
    plt.show()

# Main function to run the simulation and plotting
def main():
    latency_stats = simulate_satellite_network()  # Run simulation
    plot_latency_distribution(latency_stats)  # Plot latency distribution

main()
