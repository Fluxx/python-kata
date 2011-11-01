import re

class DataLoader:

    EXTRACT_CONTENT = re.compile('<pre>([^<]+)<\/pre>', re.DOTALL)

    def __init__(self, filename, key_col=0, relevant_lines_regex='^\W*\d+'):
        self.filename = filename
        self.key_col = key_col
        self.relevant_lines_regex = relevant_lines_regex
    
    def file_contents(self):
        return open(self.filename, 'r').read()

    def content_lines(self):
        match = self.EXTRACT_CONTENT.search(self.file_contents())
        return match.group(1).split("\n")
    
    def relevant_lines(self):
        return [ line.split() for line in self.content_lines()
                 if re.search(self.relevant_lines_regex, line) ]
    
    def max_diff(self, compare):
        return sorted(self.relevant_lines(), key=compare)[0][self.key_col]
    
print DataLoader('weather.dat', key_col=0).max_diff(
    lambda cols: int(cols[1].strip('*')) - int(cols[2].strip('*'))
)

print DataLoader('football.dat', key_col=1).max_diff(
    lambda cols: abs(int(cols[6]) - int(cols[8]))
)