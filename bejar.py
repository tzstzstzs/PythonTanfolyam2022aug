
import os

def main():
    entries = os.listdir(".")
    # print(entries)
    dirs = sorted([e for e in entries if os.path.isdir(e)])
    # print(dirs)
    files = sorted([e for e in entries if os.path.isfile(e)])
    # print(files)
    for d in dirs:
        print(d)
    print("---")
    for f in files:
        print(f)

##############################################################################

if __name__ == "__main__":
    main()
