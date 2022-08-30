
def main():
    template = "http://example.com/galleryFX/{n:02}.jpg"
    start = 1
    end = 15
    for i in range(start, end + 1):
        print(template.format(n=i))


##############################################################################

if __name__ == "__main__":
    main()
