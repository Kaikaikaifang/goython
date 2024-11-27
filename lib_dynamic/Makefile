SOURCES := $(wildcard *.go)
LIBRARY := library.so

all: $(LIBRARY) test

$(LIBRARY): $(SOURCES)
	go build --buildmode=c-shared -o $@ $(SOURCES)

test: $(LIBRARY)
	python main.py

clean:
	go clean
	rm -f $(LIBRARY)
	rm -f *.so *.h
