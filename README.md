# ImageToPalette :art:
A python script to convert images to your favorite color schemes.
Some nice wallpapers created with this tool are in [wallpapers/](/wallpapers).

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
Copy your images to the folder and run ``convert`` followed by the original file, color palette and the output. Example: 
```
./convert example.jpg kanagawa-dragon example_kanagawa-dragon.jpg
```
The output file argument is optional, by default, the converted image will be saved to ``[original name]_[color palette].[original extension]``.

## Color Palettes
Color palettes are stored in ``palettes/[palette name].py``. Currently includes color schemes from:
- [Catppuccin](https://github.com/catppuccin/catppuccin)
- [Everforest](https://github.com/sainnhe/everforest)
- [Gruvbox](https://github.com/morhetz/gruvbox)
- [Kanagawa](https://github.com/rebelot/kanagawa.nvim)
- [TokyoNight](https://github.com/folke/tokyonight.nvim)

To create a palette file, define a list ``palette`` and store the hex codes as strings. For example, the contents of a palette file that recolors to black and white could simply be:
```
palette = [
    '#000000',
    '#ffffff'
]
```

## Examples
- example.jpg
![example.jpg](/example.jpg)
- example_everforest-dark-hard.jpg
![example_everforest-dark-hard.jpg](/example_everforest-dark-hard.jpg)
- example_gruvbox-dark.jpg
![example_gruvbox-dark.jpg](/example_gruvbox-dark.jpg)
- example_kanagawa-dragon.jpg
![example_kanagawa-dragon.jpg](/example_kanagawa-dragon.jpg)
