# ImageToPalette :art:
A python script to convert images to your favorite color schemes.

## Prerequisites
This script utilizes the python library Pillow for image processing. Make sure the packages below are installed.
- Python
- [Pillow](https://python-pillow.org/)

## Usage
Clone the repository with
```
git clone https://github.com/kyokazuki/ImageToPalette
```
and make the script executable with
```
chmod +x convert
```
Copy your images to the folder and run *convert* followed by the original file, color palette and the output. Example: 
```
./convert example.jpg kanagawa-dragon example_kanagawa-dragon.jpg
```
The output file argument is optional, by default, the converted image will be saved to *[original name]_[color palette].[original extension]*.

## Color Palettes
Color palettes are stored in *palettes/* where the file names are the name of the palette. To create a palette file, put one hex code in each line of a file and ***make sure there are no empty lines***. For example, the contents of a palette file that recolors to black and white would be:
```
#000000
#ffffff
```

## Examples
- *example.jpg*
![example.jpg](/example.jpg)
- *example_kanagawa-dragon.jpg*
![example_kanagawa-dragon.jpg](/example_kanagawa-dragon.jpg)
- *example_everforest-dark-hard.jpg*
![example_everforest-dark-hard.jpg](/example_everforest-dark-hard.jpg)
- *example_gruvbox-dark.jpg*
![example_gruvbox-dark.jpg](/example_gruvbox-dark.jpg)
