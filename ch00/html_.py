import html

html_word_1 = html.escape("This HTML fragment contains a <script> script </script> tag.")
html_word_2 = html.unescape("I &hearts; Python\'s &lt; standard library &gt;.")

print(html_word_1)
print(html_word_2)
