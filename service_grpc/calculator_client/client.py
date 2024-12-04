"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc

import service_grpc
from service_grpc.proto import calculator_pb2, calculator_pb2_grpc


def add():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    run = service_grpc.run
    if run is None:
        print("Please init the service first.")
        return

    print("Will try to calculate ...")
    with grpc.insecure_channel(run.target) as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response: calculator_pb2.AddResponse = stub.Add(calculator_pb2.AddRequest(a=1, b=2))
    print("Calculator client: 1 + 2 = " + str(response.result))


if __name__ == "__main__":
    logging.basicConfig()
    service_grpc.init()
    add()
