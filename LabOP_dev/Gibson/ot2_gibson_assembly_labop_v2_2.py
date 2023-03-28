from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'description': 'None',
            'protocolName': 'LabOP Opentrons Gibson Assembly Protocol'} 

def run(protocol: protocol_api.ProtocolContext):
    p20_single_gen2 = protocol.load_instrument('p20_single_gen2', 'left')
    thermocycler_module = protocol.load_module('thermocycler module', '7')
    thermocycler_module.open_lid()
    labware1 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    p20_single_gen2.tip_racks.append(labware1)
    labware4 = protocol.load_labware('nest_96_wellplate_200ul_flat', '4')
    labware7 = thermocycler_module.load_labware('biorad_96_wellplate_200ul_pcr')
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['A1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['B1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['C1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['D1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['E1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['F1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['G1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['H1'])  # 2. Add deionized H2O for assembly reaction (first transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['A1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['B1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['C1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['D1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['E1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['F1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['G1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['H1'])  # 2. Add deionized H2O for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['A2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['B2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['C2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['D2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['E2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['F2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['G2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['H2'])  # 3. Add deionized H2O for negative control (first transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['A2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['B2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['C2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['D2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['E2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['F2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['G2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(6.0, labware4['A2'], labware7['H2'])  # 3. Add deionized H2O for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['A1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['B1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['C1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['D1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['E1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['F1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['G1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['H1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['A1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['B1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['C1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['D1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['E1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['F1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['G1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A1'], labware7['H1'])  # 4. Add Gibson Assembly Master Mix for assembly reaction (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['A2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['B2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['C2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['D2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['E2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['F2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['G2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['H2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (first transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['A2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['B2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['C2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['D2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['E2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['F2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['G2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(10.0, labware4['A2'], labware7['H2'])  # 5. Add deionized H2O instead of Gibson Assembly Master Mix for negative control (second transfer)
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['A1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['B1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['C1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['D1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['E1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['F1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['G1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['H1'])  # 6. Add DNA fragment 1 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['A2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['B2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['C2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['D2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['E2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['F2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['G2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A3'], labware7['H2'])  # 7. Add DNA fragment 1 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['A1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['B1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['C1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['D1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['E1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['F1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['G1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['H1'])  # 8. Add DNA fragment 2 for assembly reaction
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['A2'])  # 9. Add DNA fragment 2 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['B2'])  # 9. Add DNA fragment 2 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['C2'])  # 9. Add DNA fragment 2 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['D2'])  # 9. Add DNA fragment 2 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['E2'])  # 9. Add DNA fragment 2 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['F2'])  # 9. Add DNA fragment 2 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['G2'])  # 9. Add DNA fragment 2 for negative control
    p20_single_gen2.transfer(2.0, labware4['A4'], labware7['H2'])  # 9. Add DNA fragment 2 for negative control
