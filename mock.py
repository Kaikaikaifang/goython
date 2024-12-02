"""The mock of a sdk module."""
import subprocess
import atexit
import service_grpc.calculator_client as calculator_client
import pathlib


class MockSdk:
    def __init__(self):
        self.process = None
        self.hooks = []

    def init(self):
        command = [str(pathlib.Path("bin", "calculator_server"))]
        self.process = subprocess.Popen(command)
        self.hooks.append(self.process.terminate)
        atexit.register(self.process.terminate)

    def run(self):
        calculator_client.add()

    def finish(self):
        for hook in self.hooks:
            hook()
            atexit.unregister(hook)


if __name__ == "__main__":
    s = MockSdk()
    s.init()
    s.run()
    s.finish()
