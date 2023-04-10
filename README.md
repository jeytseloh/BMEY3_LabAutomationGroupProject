<h1 align="center">
  🧬 Automation of Laboratory Protocols in Synthetic Biology 🧬
</h1>
<h2 align="center">
  Year 3 Biomedical Engineering 2022-2023 Group Project @ Imperial College London
</h2>
<h3 align="center">
  Aatish Dhawan, Jay Fung, Sonya Kalsi, Jey Tse Loh & Sakshi Singh 
</h3>

## ℹ️ Project Overview
The developments in the Synthetic Biology (SynBio) field are currently hindered by a lack of throughput and reproducibility. The root cause of these issues lies in the manual execution of many frequently used protocols in SynBio and the lack of standardisation in their representation.

To address these issues, we used [**LabOP (the Laboratory Open Protocol Language)**](https://bioprotocols.github.io/labop/), a platform-agnostic framework, to automate two widely used protocols, **Golden Gate and Gibson Assembly**, on the Opentrons OT-2 Liquid Handling Robot. The efficacy of LabOP was then evaluated and compared with Opentrons’ framework, the **OT-2 API**, which we also used to automate the same protocols. While results show that the steps of the original protocols were done in the correct order after automation, further testing on actual reagents would be required to confirm the validity of the automated protocols produced.

Our project focused on the two aims highlighted below:
1.	To automate two DNA Assembly Protocols within SynBio (Golden Gate and Gibson Assembly) using two different automation frameworks (OT-2 Python API and LabOP).
2.	To compare and evaluate the automation frameworks used to assist future researchers in developing automated SynBio workflows.

More information on our project can be found on our Wiki page: [Year 3 BME Group Project 22-23: Automation of Laboratory Protocols](https://openwetware.org/wiki/Year_3_BME_Group_Project_22-23:_Automation_of_Laboratory_Protocols).

## 🗂 File Structure
- [Custom_Labware/](/Custom_Labware/) - custom labware defined using the [Opentrons Custom Labware Creator](https://labware.opentrons.com/create/)
- [LabOP_Protocols/](/LabOP_Protocols/) - protocols written using the LabOP API
  - [Gibson_LabOP_v1/](/LabOP_Protocols/Gibson_LabOP_v1/)
  - [Gibson_LabOP_v2/](/LabOP_Protocols/Gibson_LabOP_v2/)
  - [Gibson_LabOP_v3/](/LabOP_Protocols/Gibson_LabOP_v3/)
  - [Golden_Gate_LabOP_v1/](/LabOP_Protocols/Golden_Gate_LabOP_v1/)
  - [Golden_Gate_LabOP_v2/](/LabOP_Protocols/Golden_Gate_LabOP_v2/)
  - [Golden_Gate_LabOP_v3/](/LabOP_Protocols/Golden_Gate_LabOP_v3/)
  - [LabOP_Examples/](/LabOP_Protocols/LabOP_Examples/)
  - [LabOP_Unit_Tests/](/LabOP_Protocols/LabOP_Unit_Tests/)
  - [README.md](/LabOP_Protocols/README.md)
- [Opentrons/](/Opentrons/) - protocols written using the OT-2 API
  - [Gibson_OT2_v0/](/Opentrons/Gibson_OT2_v0/)
  - [Gibson_OT2_v1/](/Opentrons/Gibson_OT2_v1/)
  - [Golden_Gate_OT2_v0/](/Opentrons/Golden_Gate_OT2_v0/)
  - [Golden_Gate_OT2_v1/](/Opentrons/Golden_Gate_OT2_v1/)
  - [OT2_Examples](/Opentrons/OT2_Examples/)
  - [OT2_Unit_Tests/](/Opentrons/OT2_Unit_Tests/)
  - [README.md](/Opentrons/README.md)
- [Process_Mapping_Files/](/Process_Mapping_Files/) - JSON files exported from the [Opentrons Protocol Designer App](https://designer.opentrons.com/) used for process mapping
- [Tests/](/Tests/) - parsed run logs from execution of the unit tests and protocols on the OT-2 robot
- [labop/](https://github.com/jeytseloh/labop/tree/ceb607dec429ce8576aba8da9d3825fd7e147c23) - LabOP package (git sub-module) with specific modifications for this project (details below)
- [.gitignore](/.gitignore)
- [.gitmodules](/.gitmodules)
- [README.md](/README.md)

Note: Version control of both LabOP and OT2 protocols can be found within the [LabOP_Protocols](/LabOP_Protocols/) and [Opentrons/](/Opentrons/) folders.

## 🚀 Setup
### LabOP API
The LabOP package used specifically for this project can be installed by following the steps below.
1.  Clone and install the 'labop' repository.

```git clone https://github.com/jeytseloh/labop.git```

```cd labop ```

```pip3 install . ```

2. Ensure that the 'container-ontology' repository has been installed. Otherwise, clone and install it in its respective directory within 'labop'.

```git clone https://github.com/Bioprotocols/container-ontology.git```

```cd container-ontology```

```pip3 install .```

The original LabOP package can be found here: [Bioprotocols/labop](https://github.com/Bioprotocols/labop).

Changes made to the LabOP package were mainly to extend the existing functionalities of the OT2Specialization class, which converts the LabOP protocol to the corresponding OT-2 protocol. The following files in the package were modified for this project:
- [labop_convert/opentrons/opentrons_specialization.py](https://github.com/jeytseloh/labop/blob/ceb607dec429ce8576aba8da9d3825fd7e147c23/labop_convert/opentrons/opentrons_specialization.py)
- [labop/lib/liquid_handling.py](https://github.com/jeytseloh/labop/blob/ceb607dec429ce8576aba8da9d3825fd7e147c23/labop/lib/liquid_handling.py)
- [labop/lib/plate_handling.py](https://github.com/jeytseloh/labop/blob/ceb607dec429ce8576aba8da9d3825fd7e147c23/labop/lib/plate_handling.py)
- [labop/container_ontology.ttl](https://github.com/jeytseloh/labop/blob/ceb607dec429ce8576aba8da9d3825fd7e147c23/labop/container-ontology.ttl)

### Opentrons OT-2 Python API
Python 3.7 or higher is required. However, **Python 3.10** currently does not allow for protocol simulation. It is recommended to use a version between 3.7.0 and 3.9.9. More information can be found [here](https://support.opentrons.com/s/article/Simulating-OT-2-protocols-on-your-computer?).

The OT-2 Python API V2 documentation can be found here: [OT-2 Python API V2](https://docs.opentrons.com/v2/)
