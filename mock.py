"""The mock of a sdk usage."""
import service_grpc as s

if __name__ == "__main__":
    s.init()
    s.calculator_client.add()
    s.finish()
