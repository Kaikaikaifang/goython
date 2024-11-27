SOURCES := $(wildcard *.proto)
SERVICE_NAME := calculator

all: proto

proto: $(SOURCES)
	protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    $(SERVICE_NAME)/$(SERVICE_NAME).proto

	python3 -m grpc_tools.protoc -I $(SERVICE_NAME) \
    --python_out=$(SERVICE_NAME)_client --pyi_out=$(SERVICE_NAME)_client \
    --grpc_python_out=$(SERVICE_NAME)_client \
    $(SERVICE_NAME)/$(SERVICE_NAME).proto

clean:
	go clean
	rm -f $(SERVICE_NAME)/*.pb.go $(SERVICE_NAME)_client/*.py $(SERVICE_NAME)_client/*.pyi
