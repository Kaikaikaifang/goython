SERVICE_NAME := calculator

all: build

proto:
	protoc --go_out=. --go_opt=paths=source_relative \
	--go-grpc_out=. --go-grpc_opt=paths=source_relative \
	service_grpc/proto/$(SERVICE_NAME).proto

	mv service_grpc/proto/*.pb.go service_grpc/$(SERVICE_NAME)_server/pkg/proto/

	python3 -m grpc_tools.protoc -Iservice_grpc/proto=service_grpc/proto \
	--python_out=. \
	--pyi_out=. \
	--grpc_python_out=. \
	service_grpc/proto/$(SERVICE_NAME).proto

build:
# CGO_ENABLED=0: 生成的二进制文件不依赖于外部 C 运行时库
	cd service_grpc/$(SERVICE_NAME)_server && CGO_ENABLED=0 go build -o ../bin/$(SERVICE_NAME)_server main.go

test: build
	python mock.py

clean:
# 1. 删除 python 编译产物
	rm -rf build dist *.egg-info
# 2. 删除 go 编译产物
	rm -rf service_grpc/bin
