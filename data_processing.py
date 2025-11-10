import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data


class Table:
    def __init__(self, data):
        self.data = data

    def head(self, n=5):
        return self.data[:n]

    def filter(self, key, value):
        result = []
        for row in self.data:
            if row.get(key) == value:
                result.append(row)
        return Table(result)

    def unique_count(self, key):
        values = set()
        for row in self.data:
            values.add(row.get(key))
        return len(values)

    def mean(self, key):
        total = 0
        count = 0
        for row in self.data:
            try:
                total += float(row[key])
                count += 1
            except (ValueError, TypeError):
                continue
        if count == 0:
            return 0
        return total / count

    def max(self, key):
        max_value = None
        for row in self.data:
            try:
                value = float(row[key])
                if max_value is None or value > max_value:
                    max_value = value
            except (ValueError, TypeError):
                continue
        return max_value


loader = DataLoader()
data = loader.load_csv("Cities.csv")
table = Table(data)

print("First 5 rows:")
for row in table.head(5):
    print(row)

print("The number of unique countries:")
print(table.unique_count("country"))

print("The average temperature for all the cities in Germany:")
germany = table.filter("country", "Germany")
print(germany.mean("temperature"))

print("The max temperature for all the cities in Italy:")
italy = table.filter("country", "Italy")
print(italy.max("temperature"))
