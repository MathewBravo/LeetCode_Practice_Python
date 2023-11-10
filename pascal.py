from typing import List
def generate(numRows: int) -> List[List[int]]:
    triangle = []

    for rowNum in range(numRows):
        row = []
        if rowNum == 0:
            row = [1]
        else:
            # Calculate the current row based on the previous row
            prevRow = triangle[rowNum - 1]
            row.append(1)  # First element is always 1
            for j in range(1, rowNum):
                row.append(prevRow[j - 1] + prevRow[j])
            row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
    
if __name__ == "__main__":
    print(generate(5))