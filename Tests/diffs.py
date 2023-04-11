import difflib
import sys

with open('BMEY3_LabAutomationGroupProject\Tests\gibson\labopv3\gibson_labop_v3_runlogs.txt', 'r') as simulate:
    
    #Use this block for comparing simulated to executed logs
    lines = simulate.readlines() # Reads simulated run logs
    new_lines = []
    for line in lines:
        if "Transferring" not in line.strip() and "Mixing" not in line.strip(): # Filters out higher level Transfer and Mix lines not present in run logs
            new_lines.append((line).lstrip()) # Adds remaining lines to list
    
    # Use the line below for comparing 2 executed run logs
    #new_lines = simulate.readlines()

    with open('BMEY3_LabAutomationGroupProject\Tests\gibson\ot2v1\gibson_v1_runlogs.txt', 'r') as run:
        diff = difflib.unified_diff(
            new_lines,
            run.readlines(),
            fromfile='simulate',
            tofile='run',) #Runs the diff function between simulated and executed run logs
        
        
        similarity = difflib.SequenceMatcher(new_lines,run.readlines()).ratio() # Calculates a similarity ratio - not accurate so not used for this project

        for line in diff:
            sys.stdout.write(line) #outputs unique lines with 3 lines of context
        print(similarity)
        