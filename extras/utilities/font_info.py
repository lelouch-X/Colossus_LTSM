""" prints out ttf font information """

from fontTools.ttLib import TTFont
import sys

def font_metrics(path):
	font = TTFont(path)

	head = font['head']
	hhea = font['hhea']
	os2 = font['OS/2']

	print("Units per EM:", head.unitsPerEm)
	print("Ascent:", hhea.ascent)
	print("Descent:", hhea.descent)
	print("Line Gap:", hhea.lineGap)
	print("OS/2 Typo Ascent:", os2.sTypoAscender)
	print("OS/2 Typo Descent:", os2.sTypoDescender)

if __name__ == "__main__":
	if len(sys.argv) < 1:
		print("Usage: python font_info.py <fontfile.ttf/otf> ")
	else:
		font_path = sys.argv[1]
		font_metrics(font_path)
