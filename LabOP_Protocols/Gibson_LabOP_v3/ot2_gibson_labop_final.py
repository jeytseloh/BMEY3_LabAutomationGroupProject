from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'description': 'None',
            'protocolName': 'LabOP Opentrons Gibson Assembly Protocol'} 

def run(protocol: protocol_api.ProtocolContext):
    p10_multi = protocol.load_instrument('p10_multi', 'left')
    p300_multi = protocol.load_instrument('p300_multi', 'right')
    thermocycler_module = protocol.load_module('thermocycler module', '7')
    thermocycler_module.open_lid()
    labware1 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    p10_multi.tip_racks.append(labware1)
    labware2 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    p300_multi.tip_racks.append(labware2)
    labware4 = protocol.load_labware('masterblock_96_wellplate_2000ul', '4')
    labware7 = thermocycler_module.load_labware('framestar_96_aluminumblock_200ul')
    thermocycler_module.set_block_temperature(4.0)    # 1. Hold at 4 (ice)
    p300_multi.transfer(16.0, labware4['A2'], labware7['A1'])  # 2. Add 16 ul deionized H2O for assembly reaction
    p300_multi.transfer(36.0, labware4['A2'], labware7['A2'])  # 3. Add 36 ul deionized H2O for negative control
    p300_multi.transfer(20.0, labware4['A1'], labware7['A1'])  # 4. Add 20 ul Gibson Assembly Master Mix for assembly reaction
    p10_multi.transfer(2.0, labware4['A3'], labware7['A1'])  # 5. Add 2 ul DNA fragment 1 for assembly reaction
    p10_multi.transfer(2.0, labware4['A3'], labware7['A2'])  # 6. Add 2 ul DNA fragment 1 for negative control
    p10_multi.transfer(2.0, labware4['A4'], labware7['A1'])  # 7. Add 2 ul DNA fragment 2 for assembly reaction
    p10_multi.transfer(2.0, labware4['A4'], labware7['A2'])  # 8. Add 2 ul DNA fragment 2 for negative control
    
    p300_multi.pick_up_tip(labware2.wells_by_name()['A4']) # added manually due to missing function in LabOP

    p300_multi.mix(5, 20.0, labware7['A1'])    # 9. Mix assembly reaction (volume 20 ul, 5 repetitions)
    p300_multi.drop_tip()
    p300_multi.pick_up_tip(labware2.wells_by_name()['A5'])
    p300_multi.mix(5, 20.0, labware7['A2'])    # 10. Mix negative control (volume 20 ul, 5 repetitions)

    p300_multi.drop_tip() # added manually due to missing function in LabOP

    # 11. Incubate at 50 C for 15 minutes
    thermocycler_module.close_lid()
    thermocycler_module.set_lid_temperature(temperature=60.0)
    thermocycler_module.set_block_temperature(temperature=50.0, hold_time_minutes=1.0)
