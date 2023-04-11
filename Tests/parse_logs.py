import json

#Define output filename
testname = 'test'
save_output = testname + '_runlogs.txt'


#Load .json run logs
path_to_file = 'BMEY3_LabAutomationGroupProject/Tests/transfer/SD20181230A10_Transfer Unit Test v0.2_2023-03-20T09_22_30.789Z.json'
with open(path_to_file, 'r') as f:
  data = json.load(f)


#Map each command type and Labware name in the json to the correct output display text
command_map = {
    'pickUpTip': "Picking up tip from ",
    'aspirate' : "Aspirating",
    'dispense' : "Dispensing",
    'dropTip' : "Dropping tip into ",
    #'framestar_96_aluminumblock_200ul' : "Framestar 96 Aluminum Block 200 Â\u00b5L on Thermocycler Module GEN1",
    'framestar_96_aluminumblock_200ul' : "Destination Plate on Thermocycler Module GEN1",
    'opentrons_96_tiprack_10ul' : "Opentrons 96 Tip Rack 10 Â\u00b5L",
    'opentrons_96_tiprack_300ul' : "Opentrons 96 Tip Rack 300 Â\u00b5L",
    'masterblock_96_wellplate_2000ul' : "Masterblock 96 Well Plate 2000 Â\u00b5L",
    'fixedTrash' : 'Opentrons Fixed Trash',
    'opentrons_96_tiprack_20ul' : "Opentrons 96 Tip Rack 20 Â\u00b5L",
    "opentrons_1_trash_1100ml_fixed" : 'Opentrons Fixed Trash',
    'nest_96_wellplate_200ul_flat' : 'NEST 96 Well Plate 200 Â\u00b5L Flat'

}

commands = data['commands']

with open(save_output, 'w') as f: #opens file to write logs to
    
    for step in commands:
        if step["commandType"] in command_map.keys(): 
            #Matches labware used to the display name in command_map
            for i in range(0,len(data["labware"])):    
                if step["params"]["labwareId"] == data["labware"][i]["id"]:
                    labware = command_map[data["labware"][i]["loadName"]]
                    try:
                        lab_slot = data["labware"][i]["location"]["slotName"] 
                    except:
                        lab_slot = data["modules"][0]["location"]["slotName"]

            if "volume" in step["params"]: # filters commands to create logs for aspirating and dispensing command types only
                #Define direction of pipetting for each command
                if step["commandType"] == 'aspirate':
                    direction = ' from '
                elif step["commandType"] == 'dispense':
                    direction = ' into '   
                #Create log with required parameters    
                log = command_map[step["commandType"]] + " "+str(step["params"]["volume"]) + '.0 uL' + direction 
                + step["params"]["wellName"] +" of "+ labware + " on " + lab_slot +  " at " 
                + str(step["params"]["flowRate"]) + '.0 uL/sec' 

            #For all other command types:
            else:       
                #Create log with required parameters     
                log = command_map[step["commandType"]] + step["params"]["wellName"] + " of " +labware+ " on " + lab_slot 

            #Writes log to file
            f.write(str(log))
            f.write('\n')

        elif "legacyCommandText" in step["params"]:  # Filters only thermocycler functions
            log = step["params"]["legacyCommandText"] #Assigns log pre-defined in json file
            #Writes log to file
            f.write(str(log))
            f.write('\n')

        

