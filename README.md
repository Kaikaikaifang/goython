# Goython

> 探索 Python 中调用使用 Go 实现的方法

## TODO

- [x] 交叉编译: github action go 多平台编译测试
- [x] 调用测试：python 使用 subprocess 调用 go 生成的可执行文件

## 静态库

> 使用 `Cython` 打包 Go 编译生成的库文件为静态库拓展

测试流程：

```shell
cd lib_static
make
```

## 动态库

> 使用 `ctypes` 调用 Go 编译生成的动态库

测试流程：

```shell
cd lib_dynamic
make
```

## gRPC

> 使用 `Protocol Buffers` 定义接口，使用 `Go` 编写服务端，使用 `Python` 编写客户端

测试流程：

```shell
make test
```

## Build

> 由于用户使用平台的多样性，以及用户可能并未安装 go 的开发环境，我们需要为用户预先编译好，为其提供可直接使用的二进制文件

需要适配的平台有：

1. Linux: `x86_64`, `aarch64`
2. macOS: `x86_64`, `arm64`
3. Windows: `amd64`

Platform 由操作系统 (GOOS) 和指令集架构 (GOARCH) 唯一确定

可选的 `GOOS` 有：

1. `windows`
2. `darwin`
3. `linux`

可选的 `GOARCH` 有：

1. `amd64` & `x86_64` -> `amd64`
2. `arm64` & `aarch64` -> `arm64`

> 💡 为不同平台分发可执行文件可以借助 Github Action 实现

## Mock

> 模拟一个 SDK 的调用流程，进行 Python 与 Go 之间的交互

1. 在 sdk 中启动 tcp server:
	调用 `sdk.init` 时使用 `subprocess.Popen` 启动服务并注册停止服务的相关 `hook`
2. 在 sdk 中关闭 tcp server:
	调用 `sdk.finish` 时通过调用停止服务的 `hook` 向 sock 发送停止信号

> 注意，为了避免用户不执行 `sdk.finish` 导致进程未被杀死，我们需要借助 `atexit` 在程序退出时停止服务进程

## 依赖

1. protoc (如果需要重新编译 `proto` 文件，需要安装)
2. Go with protobuf runtime and grpc tools
3. Python with protobuf runtime and grpc tools

### protoc

1. [Github Release](https://github.com/protocolbuffers/protobuf/releases) 下载所需 `protoc` 版本
2. 解压后查看 `README`
3. 分别将 `bin/*` 与 `include/*` 复制或移动至 `/usr/local/bin/` 与 `/usr/local/include/`

## grpc

### quick start

1. [Go Quick Start](https://grpc.io/docs/languages/go/quickstart/)
2. [Python Quick Start](https://grpc.io/docs/languages/python/quickstart/)

思想：定义服务，指定可以远程调用的方法，并指定参数和响应

接口定义语言（IDL）: Protocol Buffers

```proto
service HelloService {
  rpc SayHello (HelloRequest) returns (HelloResponse);
}

message HelloRequest {
  string greeting = 1;
}

message HelloResponse {
  string reply = 1;
}
```

### Service method

有以下四种可以定义的服务：

1. Unary RPCs
2. Server streaming RPCs: 服务端流式响应
3. Client streaming RPCs: 客户端流式发送
4. Bidirectional streaming RPCs: 双向流

```proto
rpc BidiHello(stream HelloRequest) returns (stream HelloResponse);
```

### Difference between HTTP Restful API

借助 Restful API 实现端到端通信需要定义以下部分：

1. 方法 GET/POST...
2. 路由 /api/:foo/:bar
3. 请求体 SearchParams/Body
4. 响应体 Raw/Text/Json

gRPC 服务需要定义以下部分：

借助 ProtoBuf 定义:

1. 服务 (service)
2. 接口消息数据结构 (message)

> 借助 `protoc` 生成供客户端与服务端使用的方法与数据结构

与 API 调用不同，借助生成的 `stub`，允许在服务端实现 ProtoBuf 中定义的服务，并在客户端直接通过同名方法进行调用。
