"""The mock of a sdk module."""
import subprocess
import atexit
import service_grpc.calculator_client as calculator_client
import pathlib
import socket
import grpc
import time

class MockSdk:
    def __init__(self):
        self.process = None
        self.hooks = []
        self.host = "localhost"
        self.port = 50051

    @property
    def target(self):
        """Return the target string."""
        return f"{self.host}:{self.port}"

    def init(self):
        """Start the mock."""
        bin_path = pathlib.Path(__file__).parent / "bin" / "calculator_server"
        command = [str(bin_path)]
        self.process = subprocess.Popen(command)

        # Wait for the port to be open
        if not wait_for_port(self.host, self.port, 10):
            self.process.terminate()
            raise RuntimeError("Service failed to start: port not open")

        # Check if the gRPC channel is ready
        channel = grpc.insecure_channel(self.target)
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            self.process.terminate()
            raise RuntimeError("gRPC channel not ready")
        finally:
            channel.close()

        self.hooks.append(self.process.terminate)
        atexit.register(self.process.terminate)

    def run(self):
        """Client RPC"""
        calculator_client.add()

    def finish(self):
        """Clean up the mock."""
        for hook in self.hooks:
            hook()
            atexit.unregister(hook)

def wait_for_port(host, port, timeout_seconds):
    """Wait until the specified port is open."""
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        if is_port_open(host, port):
            return True
        time.sleep(0.1)
    return False

def is_port_open(host, port):
    """Check if the given host and port are open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error checking port: {e}")
        return False

if __name__ == "__main__":
    s = MockSdk()
    s.init()
    s.run()
    s.finish()
