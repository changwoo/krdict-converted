XDXF = dict.xdxf.dz
MERGED_XML = merged.xml
UPSTREAM_XML = upstream/0.xml upstream/1.xml

.PHONY:
.PHONY: all build clean

all: build

build: $(XDXF)

clean:
	rm -f $(XDXF)
	rm -f $(MERGED_XML)

dict.xdxf.dz: $(MERGED_XML) krdict2xdxf.xsl
	xsltproc -o dict.xdxf krdict2xdxf.xsl $< && dictzip dict.xdxf

$(MERGED_XML): $(UPSTREAM_XML)
	python3 merge-upstream.py $@ $^
