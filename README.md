# ImageToPalette
A simple python script using PIL to convert images to suit a color palette.

## Usage
Clone the repository with
```
git clone https://github.com/kyokazuki/ImageToPalette
```
and copy the images to *ImageToPalette/*. Run *convert.py* followed by the original file name, color palette and the output name. Example: 
```
python convert.py example.jpg gruvbox_l example-gruvbox_l.jpg
```
Without the optional output argument, the converted image will be saved to *[original name]_[color palette].[original extension]*.

## Color Palettes
Color palettes are stored in *palettes/* where the file names are the name of the palette. To create a palette file, put one hex code in each line of a file and **make sure there are no empty lines**.
