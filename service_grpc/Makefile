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

test: proto
# 1. 管理 tmux 会话
	@if ! tmux has-session -t $(SERVICE_NAME) 2>/dev/null; then \
		tmux new -s $(SERVICE_NAME) -d; \
		tmux split-window -h -t $(SERVICE_NAME); \
	fi
# 2. 启动服务端
	tmux send-keys -t $(SERVICE_NAME).0 'go run $(SERVICE_NAME)_server/main.go' C-m
# 3. 启动客户端
	tmux send-keys -t $(SERVICE_NAME).1 'python $(SERVICE_NAME)_client/main.py'
# 4. 进入 tmux 会话
	tmux attach -t $(SERVICE_NAME)

clean:
	go clean
	rm -f $(SERVICE_NAME)/*.pb.go
	find $(SERVICE_NAME)_client -type f \( -name "*.py" -o -name "*.pyi" \) -not -name "main.py" -exec rm -f {} \;
	rm -rf $(SERVICE_NAME)_client/__pycache__
