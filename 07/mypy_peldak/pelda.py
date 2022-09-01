#!/usr/bin/env python3

import secret

def main():
    result: int = secret.get_value([5, 7, 3])
    # value = complicated()  # type: ignore

##############################################################################

if __name__ == "__main__":
    main()
