# LarryPython
A Python take on:
## Larry - Long Advent of Rather Regretful Yelling
Larry is a computer program who can solve puzzles of [Advent of Code](https://adventofcode.com). It does this by requesting the selected days' puzzle-website, extracting its puzzle description, processing it and feeding the result into the [Codex API](https://beta.openai.com/docs/guides/code) to produce python code which then is saved, executed and fed with the corresponding input. The generated output is then entered on the puzzle-website to see the puzzle solved.

# How it works
## Partitioning of the Puzzle description
To extract any usable descriptions out of the complete puzzle, the puzzle needs to be partitioned into $Blocks$, with different tags to differentiate the individual content.
We do this by extracting every HTML-Element within the `<article>` element and collecting them in a `list` of tuples, the first element corresponds to the content of the HTML-Element, the second to the type of HTML-Tag.

#### Excluding unnecessary Tags
Because we don't feed ``Codex`` just everything, we can exclude:
- Examples (``<pre>``-Tags)

#### Labeling elements
To determine, which paragraphs and which parts of the description are important, we can look on each element and label it by its content to e.g.:
- Story
- Input format description
- Output format description
- Final question
- Algorithm description
- Inline examples
- ...
For that, multiple rules have to be created to ensure a constant assignments of a label to the content of an element. There are multiple theoretical approaches:
- Trained **Neural Net** / Machine Learning => Needs a big set of training data, may be inconsistent
- Creating a map of all contained words and
	- just check some sums or total values => Easy to do, may be too coarse
	- use a **decision-tree** or a **decision-forest** => Could be hard to set up
To determine the rules, a dataset with possible element-label pairs has to be created, this can be done with a [Tool](LabelingTool/README.md).

#### Deleting unnecessary labels
Now that all elements are labeled, we can remove unnecessary ones, like:
- Examples
- Story

#### Processing elements
Now the labeled elements need to be brought in a different format to be better readable by `Codex`, for this there are multiple approaches:
- Just don't care and feed it anyway
- Cut out words
- Cut our words and rearrange them
- Replace words by other words in its family / with the same implication
- Understand the meaning of the words and the sentence and create another sentence out of it, a simpler sentence for a better understanding