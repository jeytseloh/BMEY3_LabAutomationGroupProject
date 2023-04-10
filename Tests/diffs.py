import difflib
import sys

with open('BMEY3_LabAutomationGroupProject\Tests\gibson\labopv3\gibson_labop_v3_runlogs.txt', 'r') as simulate:
    new_lines = simulate.readlines()
    #new_lines = []
    #for line in lines:
    #    if "Transferring" not in line.strip() and "Mixing" not in line.strip():
    #        new_lines.append((line).lstrip())
    
    with open('BMEY3_LabAutomationGroupProject\Tests\gibson\ot2v1\gibson_v1_runlogs.txt', 'r') as run:
        diff = difflib.unified_diff(
            new_lines,
            run.readlines(),
            fromfile='simulate',
            tofile='run',
        )
        match = difflib.SequenceMatcher(new_lines,run.readlines()).get_matching_blocks()
        similarity = difflib.SequenceMatcher(new_lines,run.readlines()).ratio()
        #similarity = difflib.SequenceMatcher(b,a, autojunk=False).ratio()
        for line in diff:
            sys.stdout.write(line)
        print(similarity)
        #
        # print(match)
        #print(new_lines)