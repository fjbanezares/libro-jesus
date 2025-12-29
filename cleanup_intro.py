
import re

path = "/Users/fjbanezares/libro sobre mi amigo Jesucristo/output/html/00_introduccion.html"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix literal \n followed by </div> or just \n
# Case 1: \n followed by whitespace and </div>
content = re.sub(r'\\n\s*</div>', '</div>', content)
# Case 2: lone \n literals
content = content.replace('\\n', '')

# Fix double </div> tags if they occurred (though the above might have fixed some)
# Looking at line 571 and 745 in view_file: 
# 570:                 </div>
# 571: \n                </div>
# The sub above should handle the \n part, let's make it more targeted if needed.

# Target specifically: </div>\n                </div> -> </div>
content = re.sub(r'</div>\s*</div>', '</div>', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleanup complete.")
