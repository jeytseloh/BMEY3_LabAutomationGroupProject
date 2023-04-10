from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'description': 'None',
            'protocolName': 'LabOP Golden Gate Assembly Protocol'} 

def run(protocol: protocol_api.ProtocolContext):
    p20_single_gen2 = protocol.load_instrument('p20_single_gen2', 'left')
    thermocycler_module = protocol.load_module('thermocycler module', '7')
    thermocycler_module.open_lid()
    labware1 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    p20_single_gen2.tip_racks.append(labware1)
    labware4 = protocol.load_labware('nest_96_wellplate_200ul_flat', '4')
    labware7 = thermocycler_module.load_labware('biorad_96_wellplate_200ul_pcr')
