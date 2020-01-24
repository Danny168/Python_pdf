
from tika import parser

raw = parser.from_file("CoD_DD.pdf")
print(raw['content'])