# drafty

[![All Contributors](https://img.shields.io/github/all-contributors/blakeNaccarato/drafty?color=ee8449&style=flat-square)](contributors)

Blue Prince.

:::{toctree}
:hidden:
contributing
examples/index
changelog
contributors
apidocs/index
references
:::

## The family core

:::::::::{tab-set}
::::::::{tab-item} Family core
We learn from Blue Tents notes that the family core is located in the family Vault and that it is unlocked by the sum of its digits. Doing so reveals the cipher in {numref}`00-core`. Hints sometimes show up on the shelves of the Lost & Found, and if you look after having unlocked the family core, you'll find a scrap of paper that says ""CLUE = 3". What could that mean?

The piece of information you need to make sense of the cipher, and of `CLUE = 3`, is quite a reach, literally. Where would you go if you wanted to learn your letters and numbers?

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/00-core.png
:name: 00-core
:alt: Alt
The family core
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} ABCs
The colors and placement of letters in the alphabet and counting numbers in the first grade classroom follow the same pattern, which is supposed to suggest that we can substitute A-Z with 1-26 (or vice versa), known as the "a1z26" substitution cipher. With this information, we can transform our Lost & Found `CLUE` hint into `3 12 21 5`.

Now that `CLUE` has become four numbers, what can we do next to get `CLUE = 3`? Well, what operation have you learned that you can perform on four numbers? You must have used it recently, if you're here now!
::::::::
::::::::{tab-item} A familiar operation
Let's try core reduction. We always start with a positive number equal to the leftmost digit in a group of four digits, the nwe must subtract, multiply, or divide our running total by the next digit, then use a different operation on the next digit, then use the last operation on the final digit. We want to arrive at a whole number, and the lowest whole number attainable by any combination of operations is the "reduced" number. We won't need to worry about successive application of core reduction in this puzzle.

So, `CLUE` became "3 12 21 5". If we reduce like `3 * 12 - 21 / 5` (being mindful to apply each operation left-to-right, rather than following order-of-operations), we get `3`!

If you were to try this with each of the words in {numref}`00-core`, you would get a number for each word. But what if you wanted to get a single letter back for each word?
::::::::
::::::::{tab-item} There and back again
The solution to the cipher in {numref}`00-core` involves applying the "a1z26" substitution, reducing the resulting core, then applying "a1z26" again to convert the single resulting number (all cores reduce to numbers less than or equal to 26), which reveals the decoded message: "STILL WATER TINTS BLANK BOOKS". Now, what could that mean?
::::::::
:::::::::

## (Spoilers!) UNDER CONSTRUCTION

::::::::{dropdown}

{numref}`01-prism`
{numref}`02-rosewary`
{numref}`03-map`
{numref}`04-letter-map`
{numref}`05-word-map`
{numref}`06-gallery`
{numref}`07-letters`
{numref}`08-words`
{numref}`09-letter-paths`
{numref}`10-rosewary-letters`
{numref}`11-gallery-paths`
{numref}`12-dont-go`
{numref}`13-safe-house`
{numref}`14-letters-words-safe-house`
{numref}`15-gallery-finished`
{numref}`16-letters-words-safe-house-sw`
{numref}`17-letters-words-safe-house-blue`
{numref}`18-words-actions`
{numref}`19-words-actions-hue`
{numref}`20-words-actions-linked`
{numref}`21-letters-words-true-path`
{numref}`22-map-true-path`

:::::::{grid} 12

::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/01-prism.jpg
:name: 01-prism
:alt: Alt
The "prism"
```

```{figure} _static/02-rosewary.jpg
:name: 02-rosewary
:alt: Alt
A subset of eight rooms in the test draft
```

```{figure} _static/03-map.png
:name: 03-map
:alt: Alt
Map of rooms and walls in the Mount Holly Blueprints area with lantern and Mora Jai box colors indicated
```

```{figure} _static/04-letter-map.png
:name: 04-letter-map
:alt: Alt
Map of drawing pairs in each room
```

```{figure} _static/05-word-map.png
:name: 05-word-map
:alt: Alt
Blank map
```

```{figure} _static/06-gallery.png
:name: 06-gallery
:alt: Alt
Gallery puzzle with only given letters
```

```{figure} _static/07-letters.png
:name: 07-letters
:alt: Alt
Map of drawing pairs, overlapping word, and associated letter
```

```{figure} _static/08-words.png
:name: 08-words
:alt: Alt
Map of words written on memos inside of Mora Jai boxes
```

```{figure} _static/09-letter-paths.png
:name: 09-letter-paths
:alt: Alt
Three paths through the maze overlaid on the drawing pairs
```

```{figure} _static/10-rosewary-letters.png
:name: 10-rosewary-letters
:alt: Alt
Letters associated with rooms indicated in {numref}`02-rosewary`
```

```{figure} _static/11-gallery-paths.png
:name: 11-gallery-paths
:alt: Alt
Three of four Gallery puzzle solutions associated with the three paths
```

```{figure} _static/12-dont-go.jpg
:name: 12-dont-go
:alt: Alt
A warning pertaining to certain paths
```

```{figure} _static/13-safe-house.png
:name: 13-safe-house
:alt: Alt
A relevant message in the Safe House
```

```{figure} _static/14-letters-words-safe-house.png
:name: 14-letters-words-safe-house
:alt: Alt
Subset of only the Mora Jai words (and associated drawing pair letters) that are also in the Safe House message
```

```{figure} _static/15-gallery-finished.png
:name: 15-gallery-finished
:alt: Alt
Full Gallery puzzle solution
```

```{figure} _static/16-letters-words-safe-house-sw.png
:name: 16-letters-words-safe-house-sw
:alt: Alt
Subset of remaining drawing pair letters (and associated Mora Jai words) that could spell SWANSONG
```

```{figure} _static/17-letters-words-safe-house-blue.png
:name: 17-letters-words-safe-house-blue
:alt: Alt
Subset of remaining drawing pair letters which have Blue-only Mora Jai boxes in them and could spell out the Safe House message
```

```{figure} _static/18-words-actions.png
:name: 18-words-actions
:alt: Alt
Mora Jai words with certain important blocks highlighted
```

```{figure} _static/19-words-actions-hue.png
:name: 19-words-actions-hue
:alt: Alt
Mora Jai words with certain important blocks highlighted and hues associated with certain words indicated
```

```{figure} _static/20-words-actions-linked.png
:name: 20-words-actions-linked
:alt: Alt
Mora Jai words with sections containing a hue linked to the action associated with that hue
```

```{figure} _static/21-letters-words-true-path.png
:name: 21-letters-words-true-path
:alt: Alt
Drawing pairs and Mora Jai boxes with the true path indicated
```

```{figure} _static/22-map-true-path.png
:name: 22-map-true-path
:alt: Alt
The true path indicated on the map of the Mount Holly Blueprints
```

```{figure} _static/23-blue-prince-no-spoilers.jpg
:name: 23-blue-prince-no-spoilers
:alt: Alt
This is the last image on this page so that page previews don't spoil the true path
```

:::::
::::::
:::::::
::::::::
