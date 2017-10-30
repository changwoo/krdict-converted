XDXF = out/dict.xdxf.dz
MERGED_XML = out/merged.xml
UPSTREAM_XML = upstream/0.xml upstream/1.xml

.PHONY:
.PHONY: all build clean

all: build

build: $(XDXF)

clean:
	-rm -r out
	rm -f $(MERGED_XML)

$(MERGED_XML): $(UPSTREAM_XML)
	@-mkdir out
	python3 merge-upstream.py $@ $^

out/dict.xdxf.dz: $(MERGED_XML) krdict2xdxf.xsl
	@-mkdir out
	xsltproc -o out/dict.xdxf krdict2xdxf.xsl $< && dictzip out/dict.xdxf

