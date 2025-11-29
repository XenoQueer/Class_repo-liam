import sys

def read_numbers_from_csv(path):
    """Read numeric values from a CSV file (one value per line).

    BUGS: this function does not correctly handle invalid values or empty lines.
    """
    numbers = []
    with open(path, "r") as f:
        for line in f:
            value = line.strip()
            if line >= 0:
            
            
            # TODO: convert value to float and add to numbers
            # HINT: you should skip values that cannot be converted
             numbers.append(value)
            
    return numbers

def compute_mean(values):
    """Return the mean of a list of numbers.

    BUGS: implementation is incomplete / incorrect.
    """
    total = 0
    t = 0
    for v in values:
        t = t + 1
        total = total + v 
        total / t 
         # BUG: this is wrong -fixed?
    return total

def compute_median(values):
    """Return the median of a list of numbers.
    BUGS: does not handle even-length lists or empty lists correctly.
    """
    for v in values:
     d = v/2
     m = 0 + d
     if m == 0:
        return print('empty list')
    # TODO: implement proper median
    return values[0]

def main():
    if len(sys.argv) < 2:
        print("Usage: python starter.py <data.csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    nums = read_numbers_from_csv(csv_path)
    print("Read values:", nums)

    mean_val = compute_mean(nums)
    median_val = compute_median(nums)

    print("Mean:", mean_val)
    print("Median:", median_val)

if __name__ == "__main__":
    main()

def compute_mode(values):
   a = 0
   b = 0 
   c = 0
   for v in values:
        a = v
        if v == b:
            c= c+1 
        for v in values:
          if b == 0:
       
           if a == v:
          
               b = v
       
          elif b > a:
             b = a
          
        return print(c)
        
