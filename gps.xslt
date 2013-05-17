<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="text" />
	
<xsl:template match="/dataset2/Count">
  <xsl:apply-templates select="UTC" /><xsl:apply-templates select="Lat" /><xsl:apply-templates select="Lon" /><xsl:apply-templates select="HGT" />
</xsl:template>

<xsl:template match="UTC">
  <xsl:text>{"time": "</xsl:text>
  <xsl:value-of select="substring-before(. , ',')" />
  <xsl:text> </xsl:text>
  <xsl:value-of select="substring-after(. , ',')" />
  <xsl:text>", </xsl:text>
</xsl:template>

<xsl:template match="Lat">
  <xsl:text>"lat": </xsl:text>
  <xsl:value-of select="."/>
  <xsl:text>, </xsl:text>
</xsl:template>

<xsl:template match="Lon">
  <xsl:text>"lon": </xsl:text>
  <xsl:value-of select="."/>
  <xsl:text>, </xsl:text>
</xsl:template>

<xsl:template match="HGT">
<xsl:text>"hgt": </xsl:text>

  <xsl:choose>
    <xsl:when test=". > -1000">
      <xsl:value-of select="round(3.28084 * .)" />
    </xsl:when>
    <xsl:otherwise>
      <xsl:value-of select="round(3.28084 * (. + 65536))" />
    </xsl:otherwise>
  </xsl:choose>

  <xsl:text>}</xsl:text>
</xsl:template>

</xsl:stylesheet>
