# bordernator
Uses imagemagick to automatically apply a border design to images in a directory

BORDERNATOR

Takes a directory, finds jpgs and applies a scaled border and text label with imagemagick.

1 INPUT
Do you want white or black border (default black)

Store in borderColour variable

2 FILES
Lists all files in directory (using glom maybe?)

3 FOR EACH FILE

Identify x and y resolution, store in variables

Calculate 3% of each for square borders

Calculate 10% of y for cinematic with 1px left and right borders

Is this a cinematic aspect ratio? (Is y/x 1.6 or greater?) then apply Cinema Bars border

Else apply square border

IMAGEMAGICK
Construct command using Python integration that takes the variables calculated for Cinematic or Square for x and y border, also applies a text label that is 67% of the height of x

