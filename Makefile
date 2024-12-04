SERVICE_NAME := calculator

all: build

proto:
	protoc --go_out=. --go_opt=paths=source_relative \
	--go-grpc_out=. --go-grpc_opt=paths=source_relative \
	service_grpc/proto/$(SERVICE_NAME).proto

	python3 -m grpc_tools.protoc -Iservice_grpc/proto=service_grpc/proto \
	--python_out=. \
	--pyi_out=. \
	--grpc_python_out=. \
	service_grpc/proto/$(SERVICE_NAME).proto

build:
# CGO_ENABLED=0: 生成的二进制文件不依赖于外部 C 运行时库
	cd service_grpc && CGO_ENABLED=0 go build -o bin/$(SERVICE_NAME)_server $(SERVICE_NAME)_server/main.go

test: build
	python mock.py

clean:
	rm -rf bin/*
