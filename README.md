# ImageToPalette
A python script to convert images to your favorite color schemes.

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
./convert *example.jpg* *kanagawa-dragon* *example_kanagawa-dragon.jpg*
```
Without the optional output argument, the converted image will be saved to *[original name]_[color palette].[original extension]*.

## Color Palettes
Color palettes are stored in *palettes/* where the file names are the name of the palette. To create a palette file, put one hex code in each line of a file and **make sure there are no empty lines**.
