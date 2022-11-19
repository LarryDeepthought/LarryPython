# Tool for labeling Blocks
## Requirements
- Extract all puzzles of all the years of Advent of Code
- Split the puzzles in its paragraphs
- Display the paragraphs to the user
- Labeling
- Saving the results in a .csv

## Exact Algorithm
### Protocolls
##### Saving
- File Type: `csv`
- Format: `Year, Day, Paragraph Index, Label`
- Label Abbreviation:

| **Abbreviation** | **Meaning**           |
|------------------|-----------------------|
| e                | Example               |
| s                | Story                 |
| q                | Final Question        |
| a                | Algorithm Description |

##### Scraping
- Order:
	- Paragraphs `<p> ... </p>`
	- Lists `<ul> <li>* </ul>`
- Excluding:
	- Examples `<pre> <code> ... </code> </pre>`

### Pseudocode
```
labels := list of string
for each day, year:
	html := aoc_website(day, year)
	paragraphs := html.find_all('p')
	paragraphs += html.find_all('ul').li
	index := 0
	for each paragraph in paragraphs:
		print(paragraph)
		label := input()
		labels += year, day, index, label
		index += 1

save labels in .csv
```

