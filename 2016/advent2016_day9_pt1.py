import re
marker_pattern = re.compile(r"\(([0-9]+)x([0-9]+)\)")
decompressed_file_text = ""

with open('day9_input.txt') as compressed_file:
    compressed_text = compressed_file.read().rstrip()
    i = 0
    searching = True
    while searching:
        match = marker_pattern.search(compressed_text, i)
        if match:
            # we have a marker!
            chars = int(match.group(1))
            repeat = int(match.group(2))
            decompressed_file_text += compressed_text[i:match.start()]
            i = match.start() + len(match.group(0))
            compressed_chunk = compressed_text[i:i+chars]
            decompressed_file_text += ''.join([compressed_chunk for r in range(repeat)])
            i += chars
        else:
            # no markers in the rest of the string, wrap it up
            decompressed_file_text += compressed_text[i:]
            searching = False

print(len(decompressed_file_text))
