# drafty

[![All Contributors](https://img.shields.io/github/all-contributors/blakeNaccarato/drafty?color=ee8449&style=flat-square)](contributors)

A guide to one of the hardest puzzles in Blue Prince, sequenced in such a way that you can solve it gradually and not have to spoil yourself too much as you progress. By surfacing just a few connections that would otherwise go unnoticed, it's much easier to solve this without coming away feeling like you cheated!

:::{toctree}
:hidden:
contributing
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

## Blank books

We will refer back to these books as we progress. Their contents, reproduced below, are revealed after solving [the family core](#the-family-core).

:::::::::{dropdown} *Rosewary*
:name: rosewary-book

My dearest darling son,

I am quite impressed. I didn't expect you to make it this far, yet if these words have reached your eyes, rest assured, the end of the spiral is near! Stay vigilant and rosewary, for the thorns we discover are twice as sharp at the conclusion of each of our journeys.

One final counsel I leave you: The waters of the west spring shall yet reveal more secrets than these mere passages.

I had so many plans but not enough dreams,

Your mother,
Auravei

:::::::::

:::::::::{tab-set}
::::::::{tab-item} Her final counsel
[*Rosewary*](#rosewary-book) contains a passage hinting at a certain part of the map.
::::::::
::::::::{tab-item} It's not about the water
Do not get hung up on "waters", rather focus on the rest of the "passage".
::::::::
::::::::{tab-item} It's all coming together
Lady Auravei suggests we try placing the secret passage beyond the waters of the west spring.
::::::::
:::::::::

:::::::::{dropdown} *Hidden hue*
:name: hidden-hue-book

A HIDDEN HUE  \
FROM PRISM PRISTINE, THREE PATHS CONVENE.  \
THREE LINES OF LIGHT, THREE SHADES FORESEEN.  \
THREE COLOURS TO COUNT, A SUM OF EIGHTEEN.  \
BUT THE ONE LEFT HIDDEN, REMAINS TO BE SEEN.

:::::::::

## Maps

:::::::::{tab-set}

::::::::{tab-item} "Blank" map
I don't consider this {numref}`05-word-map` below to be too much of a spoiler. Who would think that the colors in the corners of the Mora Jai puzzle boxes would matter? But they do! And their use only becomes apparent in combination with other information, so I present them here on this blank map that you can also copy and sketch on as needed.

The next map over gives some more details, including the hallway layout, the colors of lights in the hallways, and the rooms and their orientations. It's fun to map this stuff out yourself, too, but once you've done most of it, it can be tedious to map the rest, and it's easy to make mistakes, especially in the hallway layout!

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/05-word-map.png
:name: 05-word-map
:alt: Alt
Blank map with Mora Jai box colors
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} Room map with lights and Mora Jai colors
Perhaps the most overwhelming part of navigating the Mount Holly Blueprints is all the twists, turns, and dead ends! {numref}`03-map` indicates passable areas in blue, and impassable areas in pink. A pink line crossing a hallway indicates a curtain wall dead end. The smaller colored dots in the corners of each 3x3 room cell give the colors on the corners of the Mora Jai box in that room. Some boxes even feature more than one color on them!

The next map features a spoiler-free reproduction of the drawing pair pictograms in each room. It may be a helpful reference if you're trying to place a few of your screenshots of drawing pairs somewhere on the map.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/03-map.png
:name: 03-map
:alt: Alt
Map of rooms and walls in the Mount Holly Blueprints area with lantern and Mora Jai box colors indicated
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} Drawing pair pictograms (unsolved)
Use {numref}`04-letter-map` to double-check your notes in case you mixed up a few drawing pairs, or to help anchor one of your many screenshots to the map.

The next map reveals the solution to each of the drawing pairs.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/04-letter-map.png
:name: 04-letter-map
:alt: Alt
Map of drawing pairs in each room
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} Solved drawing pairs
{numref}`07-letters` shows the solution for each drawing pair.

The next map shows the words in each of the Mora Jai boxes.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/07-letters.png
:name: 07-letters
:alt: Alt
Map of drawing pairs, overlapping word, and associated letter
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} Words in each Mora Jai box
{numref}`08-words` shows the words in each Mora Jai box.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/08-words.png
:name: 08-words
:alt: Alt
Map of words written on memos inside of Mora Jai boxes
```

:::::
::::::
:::::::
::::::::
:::::::::

## Finding the paths

:::::::::{tab-set}
::::::::{tab-item} The prism
Auravei mentions that the prism is green/violet/yellow/red/blue/orange, as shown in {numref}`01-prism`. Also (not pictured), she writes "THREE PRIMARY COLORS, THREE PRIMARY PATHS" on some paper on the drafting table in the center of the Atelier. We recall that the [*Hidden hue*](#hidden-hue-book) poem also mentions the prism, as well as "three paths". Your initial objective will be to find these "three paths" in the Mount Holly Blueprints.

Another thing that is central to this puzzle is the new Gallery puzzle. The next tab shows the blank gallery puzzle.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/01-prism.jpg
:name: 01-prism
:alt: Alt
The "prism"
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} Gallery (unsolved)
{numref}`06-gallery` shows the blank gallery puzzle.

In my opinion, the single biggest fumble in the design of the Mount Holly Blueprints puzzle is not indicating that the gallery is central to the puzzle. Here are some connections to the gallery that are, in my opinion, impossible to figure out by intuition alone, and will make it more likely that you can solve the rest of this puzzle without tearing your hear out:

- Each word in the gallery puzzle relates to one of the paths.
- Each word in the gallery puzzle relates to one of the busts in Room 46.

If you can manage to solve one of the words in the gallery puzzle by intuition, it may help you find a path. If you find a path, it may help you solve one of the words in the gallery puzzle. Recall the [*Hidden hue*](#hidden-hue-book) poem as you proceed.

The next hint is not much of a spoiler, rather it will give you some practice. I think it's worth revealing what other piece of information links back to "rosewary"...

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/06-gallery.png
:name: 06-gallery
:alt: Alt
Gallery puzzle with only given letters
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} Remember to be rosewary
The rooms indicated on the door to the Mount Holly Blueprints, as shown in {numref}`02-rosewary`, are quite conspicuous. Should we try to duplicate this layout in the house? But what if our Foundation is in the wrong place? Did you know that you can actually banish The Foundation with the room Repellent spray item? But you'll lose The Foundation for over three days before it starts showing up in the draft again.

Before you proceed down that path, I recommend you be [*Rosewary*](#rosewary-book)! How might {numref}`02-rosewary` relate to "rosewary"? If you can find that out, you're starting to understand how you might relate words to rooms.

The next tab shows another screenshot from The Atelier you might want to revisit after you've found at least one of the paths.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/02-rosewary.jpg
:name: 02-rosewary
:alt: Alt
A subset of eight rooms in the test draft
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} A warning about the path
Lady Auravei warns us, "DON'T GO WHERE THE PATH LEADS" in {numref}`12-dont-go`. What might this be referring to? If you've found one of the paths, you might already know. But the [*Hidden hue*](#hidden-hue-book) poem speaks of a special, "hidden" path. What might that mean?

The next tab shows a piece of information that you would probably never have known is related to this puzzle, and I really wish it was clearer, because if you use it correctly, it will help you find the "hidden" path in an intuitive way rather than by brute force.

This information is a message from Mary herself, and suggests that Mary may have walked some of these paths herself! This message is kept safe in a far away place.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/12-dont-go.jpg
:name: 12-dont-go
:alt: Alt
A warning pertaining to certain paths
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} Mary's message
Did you find it? I wouldn't blame you if you didn't. Not only do you have to recall that there's a message scrawled on the wall of the safe house, as shown in {numref}`13-safe-house`, but you also have to notice that it relates to the puzzle at hand!

I'll leave it at that for now, just remember, "WE SEEK WHAT'S IN THE SHADE OF TRUTH".

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/13-safe-house.png
:name: 13-safe-house
:alt: Alt
A relevant message in the Safe House
```

:::::
::::::
:::::::
::::::::
:::::::::

## SPOILERS BELOW

::::::::::{dropdown}
:::::::::{tab-set}
::::::::{tab-item} letter-paths
Hint about {numref}`09-letter-paths`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/09-letter-paths.png
:name: 09-letter-paths
:alt: Alt
Three paths through the maze overlaid on the drawing pairs
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} rosewary-letters
Hint about {numref}`10-rosewary-letters`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/10-rosewary-letters.png
:name: 10-rosewary-letters
:alt: Alt
Letters associated with rooms indicated in {numref}`02-rosewary`
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} gallery-paths
Hint about {numref}`11-gallery-paths`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/11-gallery-paths.png
:name: 11-gallery-paths
:alt: Alt
Three of four Gallery puzzle solutions associated with the three paths
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} letters-words-safe-house
Hint about {numref}`14-letters-words-safe-house`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/14-letters-words-safe-house.png
:name: 14-letters-words-safe-house
:alt: Alt
Subset of only the Mora Jai words (and associated drawing pair letters) that are also in the Safe House message
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} gallery-finished
Hint about {numref}`15-gallery-finished`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/15-gallery-finished.png
:name: 15-gallery-finished
:alt: Alt
Full Gallery puzzle solution
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} letters-words-safe-house-sw
Hint about {numref}`16-letters-words-safe-house-sw`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/16-letters-words-safe-house-sw.png
:name: 16-letters-words-safe-house-sw
:alt: Alt
Subset of remaining drawing pair letters (and associated Mora Jai words) that could spell SWANSONG
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} letters-words-safe-house-blue
Hint about {numref}`17-letters-words-safe-house-blue`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/17-letters-words-safe-house-blue.png
:name: 17-letters-words-safe-house-blue
:alt: Alt
Subset of remaining drawing pair letters which have Blue-only Mora Jai boxes in them and could spell out the Safe House message
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} words-actions
Hint about {numref}`18-words-actions`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/18-words-actions.png
:name: 18-words-actions
:alt: Alt
Mora Jai words with certain important blocks highlighted
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} words-actions-hue
Hint about {numref}`19-words-actions-hue`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/19-words-actions-hue.png
:name: 19-words-actions-hue
:alt: Alt
Mora Jai words with certain important blocks highlighted and hues associated with certain words indicated
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} words-actions-linked
Hint about {numref}`20-words-actions-linked`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/20-words-actions-linked.png
:name: 20-words-actions-linked
:alt: Alt
Mora Jai words with sections containing a hue linked to the action associated with that hue
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} letters-words-true-path
Hint about {numref}`21-letters-words-true-path`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/21-letters-words-true-path.png
:name: 21-letters-words-true-path
:alt: Alt
Drawing pairs and Mora Jai boxes with the true path indicated
```

:::::
::::::
:::::::
::::::::
::::::::{tab-item} map-true-path
Hint about {numref}`22-map-true-path`.

:::::::{grid} 12
::::::{grid-item}
:columns: 12

:::::{grid} 1

```{figure} _static/22-map-true-path.png
:name: 22-map-true-path
:alt: Alt
The true path indicated on the map of the Mount Holly Blueprints
```

:::::
::::::
:::::::
::::::::
:::::::::
::::::::::

```{figure} _static/23-blue-prince-no-spoilers.jpg
:name: 23-blue-prince-no-spoilers
:alt: Alt
This is the last image on this page so that page previews don't spoil the true path
```
