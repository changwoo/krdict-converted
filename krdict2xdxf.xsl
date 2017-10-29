<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <xdxf lang_from="KOR" lang_to="KOR" format="logical" revision="033">
    <meta_info>
      <title>한국어기초사전</title>
      <full_title>한국어기초사전</full_title>
      <description>
	<xsl:value-of select="LexicalResource/GlobalInformation/feat[@att='label']/@val" />
      </description>
      <file_ver>001</file_ver>
      <creation_date>
	<xsl:value-of select="substring(LexicalResource/GlobalInformation/feat[@att='creationDate']/@val, 9, 2)" />-<xsl:value-of select="substring(LexicalResource/GlobalInformation/feat[@att='creationDate']/@val, 6, 2)" />-<xsl:value-of select="substring(LexicalResource/GlobalInformation/feat[@att='creationDate']/@val, 1, 4)" />
      </creation_date>
    </meta_info>
    <lexicon>
      <xsl:for-each select="LexicalResource/Lexicon/LexicalEntry">
	<ar>
	  <k>
	    <xsl:value-of select="Lemma/feat[@att='writtenForm']/@val" />
	  </k>
	  <def>
	    <xsl:for-each select="Sense">
	      <def>
		<gr>
		  <xsl:value-of select="../feat[@att='lexicalUnit']/@val" />
		</gr>
		<gr>
		  <xsl:value-of select="../feat[@att='partOfSpeech']/@val" />
		</gr>
		<tr>
		  <xsl:value-of select="../WordForm/feat[@att='pronunciation']/@val" />
		</tr>
		<deftext>
		  <xsl:value-of select="feat[@att='definition']/@val" />
		</deftext>
		<xsl:for-each select="SenseExample">
		  <ex>
		    <ex_orig>
		      <xsl:value-of select="feat[@att='example']/@val" />
		    </ex_orig>
		  </ex>
		</xsl:for-each>
	      </def>
	    </xsl:for-each>
	  </def>
	</ar>
      </xsl:for-each>
    </lexicon>
  </xdxf>
</xsl:template>

</xsl:stylesheet>
