<h1 align="center">
  🧬 Lab Automation Group Project 🧬
</h1>
<h2 align="center">
  Year 3 Biomedical Engineering 2022-2023 @ Imperial College London
</h2>
<h3 align="center">
  Aatish Dhawan, Jay Fung, Sonya Kalsi, Jey Tse Loh & Sakshi Singh 
</h3>

## ℹ️ Project Overview
The developments in the Synthetic Biology (SynBio) field are currently hindered by a lack of throughput and reproducibility. The root cause of these issues lies in the manual execution of many frequently used protocols in SynBio and the lack of standardisation in their representation.

To address these issues, we used LabOP (the Laboratory Open Protocol Language), a platform-agnostic framework, to automate two widely used protocols, Golden Gate and Gibson Assembly, on the Opentrons OT-2 Liquid Handling Robot. The efficacy of LabOP was then evaluated and compared with Opentrons’ proprietary framework, the OT-2 API, which we also used to automate the same protocols. While results show that the steps of the original protocols were done in the correct order after automation, further testing on actual reagents would be required to confirm the validity of the automated protocols produced.

Our project focused on the two aims highlighted below:
1.	To automate two DNA Assembly Protocols within SynBio (Golden Gate and Gibson Assembly) using two different automation frameworks (OT-2 Python API and LabOP).
2.	To compare and evaluate the automation frameworks used to assist future researchers in developing automated SynBio workflows.

## 🗂 File Structure
- [LabOP Protocols/](/LabOP%20Protocols/) - protocols written using the LabOP API
  - [Gibson/](/LabOP%20Protocols/Gibson/)
  - [Golden Gate/](/LabOP%20Protocols/Golden%20Gate/)
  - [Tests/](/LabOP%20Protocols/Tests/)
  - [Unit Tests/](/LabOP%20Protocols/Unit%20Tests/)
- [Opentrons/](/Opentrons/) - protocols written using the OT-2 API
  - [Gibson/](/Opentrons/Gibson/)
  - [Golden Gate/](/Opentrons/Golden%20Gate/)
  - [ot2_tests/](/Opentrons/ot2_tests/)
- [Process Mapping JSON Files/](/Process%20Mapping%20JSON%20Files/) - JSON files exported from the Opentrons Protocol Designer App used for process mapping
- [Tests/](/Tests/) - parsed run logs from execution of the unit tests and protocols on the OT-2 robot
- [labop/](/labop%20@%20ceb607d/) - LabOP package with specific modifications for this project (details below)
- [labware/](/labware/) - custom labware defined using the Opentrons Custom Labware Creator
- [.gitignore](/.gitignore)
- [.gitmodules](/.gitmodules)
- [README.md](/README.md)

## 🚀 Setup
### LabOP API
The LabOP package used specifically for this project can be installed by following the steps below.
1.  Clone the 'labop' repository.

```git clone https://github.com/jeytseloh/labop.git```

2. Navigate into the repository and install the package.

```cd labop ```

```pip3 install . ```

The original LabOP package can be found here: [Bioprotocols/labop](https://github.com/Bioprotocols/labop).
Changes made to the LabOP package were mainly to extend the existing functionalities of the OT2Specialization class, which converts the LabOP protocol to the corresponding OT-2 protocol. The following files in the package were modified for this project:
- [labop_convert/opentrons/opentrons_specialization.py](/labop%20@%20ceb607d/labop_convert/opentrons/opentrons_specialization.py)
- [labop/lib/liquid_handling.py](/labop%20@%20ceb607d/labop/lib/liquid_handling.py)
- [labop/lib/plate_handling.py](/labop%20@%20ceb607d/labop/lib/plate_handling.py)
- [labop/container_ontology.ttl](/labop%20@%20ceb607d/labop/container_ontology.ttl)

### Opentrons OT-2 Python API
Note: Python Version between 3.7.0 and 3.9.9 must be used to be able to simulate the protocols.

