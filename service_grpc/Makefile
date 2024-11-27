SOURCES := $(wildcard *.proto)
SERVICE_NAME := calculator

all: proto

proto: $(SOURCES)
	protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    $(SERVICE_NAME)/$(SERVICE_NAME).proto

	python3 -m grpc_tools.protoc -I $(SERVICE_NAME) \
	--python_out=$(SERVICE_NAME) --pyi_out=$(SERVICE_NAME) \
	--grpc_python_out=$(SERVICE_NAME) \
	$(SERVICE_NAME)/$(SERVICE_NAME).proto

clean:
	go clean
	rm -f $(SERVICE_NAME)/*.pb.go $(SERVICE_NAME)/*.py $(SERVICE_NAME)/*.pyi
