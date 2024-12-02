# Goython

> 探索 Python 中调用使用 Go 实现的方法

## TODO

- [ ] 交叉编译: github action go 多平台编译测试 (不同平台 python sdk 中的可执行文件不同)
- [x] 调用测试：python 使用 subprocess 调用 go 生成的可执行文件
- [ ] 可观测性：为 grpc 接入 openTelemetry 进行链路追踪测试

## 静态库

> 使用 `Cython` 打包 Go 编译生成的库文件为静态库拓展

测试流程：

```shell
cd lib_static
pip install Cython
make
```

## 动态库

> 使用 `ctypes` 调用 Go 编译生成的动态库

测试流程：

```shell
cd lib_dynamic
pip install ctypes
make
```

## gRPC

> 使用 `Protocol Buffers` 定义接口，使用 `Go` 编写服务端，使用 `Python` 编写客户端

测试流程：

```shell
make
python mock.py
```

## 依赖

1. protoc
2. Go with protobuf runtime and grpc tools
3. Python with protobuf runtime and grpc tools

### protoc

1. [Github Release](https://github.com/protocolbuffers/protobuf/releases) 下载所需 `protoc` 版本
2. 解压后查看 `README`
3. 分别将 `bin/*` 与 `include/*` 复制或移动至 `/usr/local/bin/` 与 `/usr/local/include/`

### grpc

1. [Go Quick Start](https://grpc.io/docs/languages/go/quickstart/)
2. [Python Quick Start](https://grpc.io/docs/languages/python/quickstart/)