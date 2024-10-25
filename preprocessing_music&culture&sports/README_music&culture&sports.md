The processing files are composed of two parts: python & R.

For the Python files, there are three scripts for data scraping: event.py, main.py, and wiki.py, each targeting different types of content from the websites. The package used is beautifulsoup4.

The main.py script scrapes general information, such as ticket purchasing options and organization staff details.
Since it is more effective for models to learn from structured event data, pages labeled "calendar" or "event" are scraped separately using event.py, which collects detailed event-specific information.
The wiki.py script is dedicated to extracting supplementary information from Wikipedia pages to provide additional context.
All URLs need to be manually input into the scripts by creating variables that store the target website addresses. The scripts also navigate subpages to ensure comprehensive data collection.

In addition to scraping, we have processing code files that remove unnecessary or redundant words, which are often standard texts on websites (e.g., "About Us," "Register Now"). Due to the variety in HTML design, each website and even each subpage has its own default text. We have identified common patterns of such default texts and ensure they are removed from the datasets. Additionally, short or ambiguous words that might be clear in CSV files but confusing in text files are handled carefully. For instance, some websites categorize shows with genre labels like "family," but this can be ambiguous for language models when it appears as a single line. Therefore, these words are removed from the text files but retained in the event CSV files to maintain necessary information.

Two R scripts are included: one for converting event text into structured CSV files and the other for conducting Inter-Annotator Agreement (IAA) analysis.

The script for converting event text organizes the extracted information into tables with columns like event name, time, and location, following the structure typically found on the original websites. For instance, if a website provides brief introductions to events, the corresponding table will have a column labeled "introduction."
The IAA analysis script compares answers to randomly chosen questions from different datasets, calculating similarity scores and checking for accuracy, especially when the answers are numeric.
