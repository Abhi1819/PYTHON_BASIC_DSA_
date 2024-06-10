import sys

def create_file(filename):
    file = f'{filename}.py'
    with open(file, 'w') as f:
        f.write(f'#{filename}')
        f.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create.py <filename>")
    else:
        filename = sys.argv[1]
        create_file(filename)
