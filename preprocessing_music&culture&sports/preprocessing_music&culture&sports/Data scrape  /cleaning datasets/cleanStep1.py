input_file = "/Users/zhihanli/Desktop/Pittsburgh_music/music/Cultural Trust/Tickets & Events/Series & Packages.txt"
output_file = "/Users/zhihanli/Desktop/Pittsburgh_music/music/Cultural Trust/Tickets & Events/cleaned.txt"

# Define the start and end markers
start_marker = "Main Page Content:"
end_marker = "rss feed"

remove_sections = [
    ("Subpage: ", "--------------------------------------------------"),
    ("Main Page URL: ", "--------------------------------------------------"),
    ("Subpage: ", "Time left to complete order"),
    ("Follow Us", "--------------------------------------------------"),
    ("Looking for more?", "Join"),
]

def clean_file(input_path, output_path, remove_sections):
    """
    Cleans the input file by removing content between specified start and end markers.

    Args:
        input_path (str): Path to the input file.
        output_path (str): Path to the output file.
        remove_sections (list): List of tuples specifying the start and end markers to remove.
    """
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        skip = False  # Track whether we are in a section to remove
        current_start = None  # Track the current start marker
        
        for line in infile:
            # Check if the line contains any start markers
            for start, end in remove_sections:
                if start in line:
                    skip = True
                    current_start = start
                    break
            
            # Write the line if not skipping
            if not skip:
                outfile.write(line)
            
            # Check if the line contains the corresponding end marker
            if skip and current_start:
                for start, end in remove_sections:
                    if end in line and current_start == start:
                        skip = False  # Stop skipping after the corresponding end marker
                        current_start = None
                        break

    print("Cleaning complete. Check the output file.")

# Call the function
clean_file(input_file, output_file, remove_sections)