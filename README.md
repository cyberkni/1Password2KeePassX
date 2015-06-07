# 1Password2KeePassX
Tool to convert a 1password TSV export file in to a KeePassX XML data file.

# Caveats
- This tool is lossy. It does **not** preserve all the data encoded in the 1Password export. It does however translate all the properties than KeepPassX supports.
- All password entries get placed in an *All* group within the exported file. Any organization in 1Password is not carried over.

# Usage
./1pass2kpx.py <input tsv file> <output filename>

To get your input tsv file use the *File -> Export* menu item and pick the plain text format. Please note that the output of this will be unencrypted and contain all of your username and passwords. Treat this file with extreme caution(don't drop it in your Dropbox, Google Drive, or anywhere that could be publicly readable).
