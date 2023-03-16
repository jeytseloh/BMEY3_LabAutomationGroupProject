from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'description': 'This protocol is a unit test designed to validate accuracy in aspirating and dispensing 10ul, written in LabOP',
            'protocolName': 'Aspirating/Dispensing Unit Test Using LabOP v0'} 

def run(protocol: protocol_api.ProtocolContext):
    p20_single_gen2 = protocol.load_instrument('p20_single_gen2', 'left')
    labware1 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    p20_single_gen2.tip_racks.append(labware1)
    labware4 = protocol.load_labware('nest_96_wellplate_200ul_flat', '4')
