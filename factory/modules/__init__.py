import click
import os
import sys
import urllib2
import StringIO
import gzip



class File(object):
    
    @staticmethod
    def download(url, location=os.path.dirname(os.path.realpath(__file__))):
        
        outFilePath = location
        response = urllib2.urlopen(url)
        compressedFile = StringIO.StringIO()
        compressedFile.write(response.read())
        #
        # Set the file's current position to the beginning
        # of the file so that gzip.GzipFile can read
        # its contents from the top.
        #
        compressedFile.seek(0)

        decompressedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')

        with open(outFilePath, 'w') as outfile:
            outfile.write(decompressedFile.read())