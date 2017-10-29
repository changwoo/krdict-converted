XDXF = dict.xdxf
MERGED_XML = upstream.xml
UPSTREAM_XML = upstream/0.xml upstream/1.xml

.PHONY:
.PHONY: all build clean

all: build

build: dict.xdxf

clean:
	rm -f $(XDXF)
	rm -f $(INTERMEDIATE_XML)

$(XDXF): $(MERGED_XML)
	xsltproc -o $@ krdict2xdxf.xsl $^

$(MERGED_XML): $(UPSTREAM_XML)
	python3 merge-upstream.py $@ $^
