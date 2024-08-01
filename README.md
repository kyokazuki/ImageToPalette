# ImageToPalette
A simple python script using PIL to convert images to suit a color palette.

## Usage
Clone the repo and copy the images to *ImageToPalette/*. Run *convert.py* followed by the original file name, color palette and the output name. Example: 
```
python convert.py tokyo.jpg gruvbox_l tokyo-gruvbox_l.jpg
```
Without the optional output argument, the converted image will be saved to *[original name]-[color palette].[original extension]*.

## Color Palettes
Color palettes are stored in the *palettes/* folder where the file names are the name of the palette. To create a palette file, put one hex code in each line of the file and **make sure there are no empty lines**.
