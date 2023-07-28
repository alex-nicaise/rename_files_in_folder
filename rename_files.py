import os

def main():

    # REPLACE YOUR FOLDER PATH HERE
    # DO NOT DELETE THE '+ "/"' IN NEXT LINE

    path = "C:/Users/anica/Desktop/images" + "/"

    i = 0

    for file in os.listdir(path):

        # REPLACE PRE-FIX AS YOU LIKE

        prefix = "image_{iterator:x}.jpg".format(iterator = i)

        os.rename(path + file, path + prefix)

        i += 1

if __name__ == "__main__":
    main()