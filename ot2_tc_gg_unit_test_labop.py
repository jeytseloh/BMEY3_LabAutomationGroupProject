from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'description': 'This protocol is a unit test designed to test thermocycler function and timing using the parameters used in the Golden Gate protocol, written in LabOP',
            'protocolName': 'Thermocycler Golden Gate Unit Test Using LabOP v0'} 

def run(protocol: protocol_api.ProtocolContext):
    p20_single_gen2 = protocol.load_instrument('p20_single_gen2', 'left')
    thermocycler_module = protocol.load_module('thermocycler module', '7')
    thermocycler_module.open_lid()
    labware1 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    p20_single_gen2.tip_racks.append(labware1)
    labware4 = protocol.load_labware('nest_96_wellplate_200ul_flat', '4')
    thermocycler_module.close_lid()
    profile = [{'temperature': 37.0, 'hold_time_seconds': 3600.0}, {'temperature': 60.0, 'hold_time_seconds': 60.0}, {'temperature': 0.0, 'hold_time_seconds': 0.0}]
    thermocycler_module.execute_profile(steps=profile, repetitions=1)
    thermocycler_module.set_block_temperature(4)
