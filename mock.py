#!/usr/bin/env python
"""The mock of a sdk usage."""
import service_grpc as s

s.init()
s.calculator_client.add()
s.finish()
