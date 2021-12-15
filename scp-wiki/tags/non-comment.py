import re

f = open("./scp-wiki/tags/tags.md", "r", encoding="utf-8_sig")
data = f.read()
f.close()

f = open('./scp-wiki/tags/tags_commented.md', 'w', encoding="utf-8_sig")
re_data = re.sub(r'(\n)?\[!\-\-(.*?)\-\-\]', '', data, flags=(re.IGNORECASE | re.DOTALL))
f.write(re_data)
f.close()
