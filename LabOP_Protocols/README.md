<h1 align="center">
  🧬 Gibson and Golden Gate Protocols - LabOP 🧬
</h1>

## File Contents
- The LabOP protocols are written in *.ipynb* files.
- Upon execution of the LabOP protocols, the following files are generated:
  - A markdown *.md* file.
  - A Python *.py* file to be executed on the OT-2 robot via the [Opentrons Application](https://github.com/Opentrons/opentrons).

## Version Control
### v1
- Initial version of the protocol
- Unable to generate the *.md* and *.py* files due to syntax errors

### v2
- Fixed syntax errors in executing the protocol to generate the *.md* and *.py* files
- Unable to generate the 'hold', 'mix' and 'incubate' commands to work

### v3
- Final version used for Testing with Liquids
- Implemented 8-channel tip, instead of single-channel previously
- Implemented a P300 tip on the right mount
- Replaced the P20 tip with a P10 tip on the left mount
- Implemented custom labware defined
- Implemented additional LabOP helper functions
