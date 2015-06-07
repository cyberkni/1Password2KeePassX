# 1Password2KeePassX
Tool to convert a 1password TSV export file in to a KeePassX XML data file.

# Usage
./1pass2kpx.py <input tsv file> <output filename>

To get your input tsv file use the *File -> Export* menu item and pick the plain text format. Please note that the output of this will be unencrypted and contain all of your username and passwords. Treat this file with extreme caution(don't drop it in your Dropbox, Google Drive, or anywhere that could be publicly readable).
