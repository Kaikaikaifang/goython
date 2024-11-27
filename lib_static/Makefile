SOURCES := $(wildcard *.go)
LIBRARY := library.a

all: build_ext test

$(LIBRARY): $(SOURCES)
	go build --buildmode=c-archive -o $@ $(SOURCES)

build_ext: $(LIBRARY)
	python setup.py build_ext -i

test: build_ext
	python main.py

clean:
	go clean
	rm -f $(LIBRARY)
	rm -rf build
	rm -f *.so *.c *.h
