# bordernator
Bordernator will apply borders and an optional text tag to photos. It is known to run on MACOS and Windows 10.

The border and text label automatically scale with image size, meaning you can have a consistent appearance with differently sized images.

For cinematic aspect ratios it will add cinema bars instead of a border.  

Bordernator can also create and apply a text label using IPTC metadata tags.

Requires GLOB, PILLOW, iptcinfo3, pathlib and logging.

USAGE
Place bordernator.py and Symtext.ttf in the directory with the photos you wish to bordernate. Run bordernator py:

Example 1: python bordernator.py
Example 2: python3 bordernator.py

You could also right-click and execute with IDLE.

Follow the prompts in the terminal, and the output edited photos will be placed in a new folder called 'bordernated'. The original photos are not altered (but remember folks, always back up your data regularly! :-) )


TODO
- add font options / independence / use system fonts? (complex due to differing operating systems)
- add some way to preserve the IPTC title field?
- make installable and add CLI interaction (e.g. make a bordernator command with switches: 'user@sytem:-$:bordernator --black --iptc')


