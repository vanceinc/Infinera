##### Syntax: ```ABT-CMD:[TID]::[CTAG]::[<CMDTAG>]; ```
##### Parameters
Attribute | Description
|---
CMDTAG|This is the CTAG of the command that should be aborted. If omitted, the default ctag of "1" is used for the CMDTAG. CMDTAG is a String. The default value is ""1"".

##### Syntax: ```ACT-PROTN-BWCLINK:[TID]:<WorkLinkBwcAid>,<ProtLinkBwcAid>:[CTAG]; ```
##### Parameters
Attribute | Description
|---
WorkLinkBwcAid|Working BWC Link AID. This is the AID of the source (from) endpoint of the Working (as opposed to Protection) video bandwidth constraint link on the STS transport path. It must not identify the endpoint which is common to both the Working and Protection Virtual Circuits. WkgBwcLinkAid is the address of the port which transmits the working traffic, which is also the port which is receiving the protection traffic (and is hence the protection side of the facility protection group). WorkLinkBwcAid is the AID NvmLinkBwcAid.
ProtLinkBwcAid|Protection BWC Link AID. This is the AID of the source (from) endpoint of the Protection (as opposed to Working) video bandwidth constraint link on the STS transport path. It must not identify the endpoint which is common to both the Working and Protection Virtual Circuits. ProtBwcLinkAid is the address of the port which transmits the protection traffic, which is also the port which is receiving the working traffic (and is hence the working side of the facility protection group). ProtLinkBwcAid is the AID NvmLinkBwcAid.

##### Syntax: ```ACT-PROTN-VC:[TID]:<WorkSrcVcAid>,<ProtSrcVcAid>:[CTAG]:::[PC=<PC>]; ```
##### Parameters
Attribute | Description
|---

WorkSrcVcAid|Working Source Virtual Circuit Access Identifier. This is the AID of the source (from) endpoint of the Working (as opposed to Protection) Virtual Circuit for the connection. It must not identify the endpoint which is common to both the Working and Protection Virtual Circuits. Rather, it identifies the first point which is unique to the Working Virtual Circuit. Note that for a unidirectional ring, WorkSrcVcAid is the address of the port which transmits the working traffic, which is also the port which is receiving the protection traffic (and is hence the protection side of the facility protection group). WorkSrcVcAid is the AID VcId2.
ProtSrcVcAid|Protection Source Virtual Circuit Access Identifier. This is the AID of the source (from) endpoint of the Protection (as opposed to Working) Virtual Circuit for the connection. It must not identify the endpoint which is common to both the Working and Protection Circuits. Rather, it identifies the first point which is unique to the Protection Virtual Circuit. ProtSrcVcAid is the AID VcId2.
PC|Protection Class - Indicates whether the cross connect is uses Bridged or UnBridged protection. PC is of type ProtClassAny and can be one of the following values: "BR", "DEFAULT", "UNBR".

##### Syntax: ```ACT-PROTN-VP:[TID]:<WorkSrcVpAid>,<ProtSrcVpAid>:[CTAG]:::[PC=<PC>]; ```

##### Parameters
Attribute | Description
|---

WorkSrcVpAid|Working Source Virtual Path Access Identifier. This is the AID of the source (from) endpoint of the Working (as opposed to Protection) Virtual Path for the connection. It must not identify the endpoint which is common to both the Working and Protection Paths. Rather, it identifies the first point which is unique to the Working Virtual Path. WorkSrcVpAid is the AID VpAid.
ProtSrcVpAid|Protection Source Virtual Path Access Identifier. This is the AID of the source (from) endpoint of the Protection (as opposed to Working) Virtual Path for the connection. It must not identify the endpoint which is common to both the Working and Protection Paths. Rather, it identifies the first point which is unique to the Protection Virtual Path. ProtSrcVpAid is the AID VpAid.
PC|Protection Class - Indicates whether the cross connect is uses Bridged or UnBridged protection. PC is of type ProtClassAny and can be one of the following values: "BR", "DEFAULT", "UNBR".

##### Syntax: ```ACT-USER:[TID]:<UID>:[CTAG]::<PID>; ```

##### Parameters
Attribute | Description
|---

UID|User Identifier. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination of alphanumeric characters 4 to 10 characters long and is case-sensitive. UID is a String.
PID|The password must conform to the rules provisioned via ED-SYS-SECU. PID is a String.

##### Syntax: ```ALW-CMD-RESTR:[TID]::[CTAG]; ```


##### Syntax: ```ALW-MSG-ALL:[TID]::[CTAG]::[<NTFCNCDE>]; ```

##### Parameters
Attribute | Description
|---

NTFCNCDE|Notification Code. This parameter identifies the notification code of the alarms which the user wants to inhibit. Alarms of a less severe notification code are also inhibited. NTFCNCDE is of type NotificationInh. The default value is "ALL".

##### Syntax: ```ALW-MSG-SECU:[TID]::[CTAG]; ```


##### Syntax: ```ALW-STBY-UPGRD:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---

ShelfAid|Shelf Access Identifier. The address of the shelf where the automatic upgrade of the standby is to be allowed again. ShelfAid is the AID ShelfAid.

##### Syntax: ```ALW-SWDX-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---

EqptAid|Equipment Access Identifier. The address of the equipment which is to be switched. EqptAid is the AID SlotCsAid.

##### Syntax: ```ALW-SWDX-GR303:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|Data Link Access Identifier. The address of the data link which is now allowed to provide protection and can now be switched into, either automatically or manually. DataLinkSwAid is the AID IgLinkSwAid.

##### Syntax: ```ALW-SWDX-T1TG:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|Data Link Access Identifier. The address of the data link which is now allowed to provide protection and can now be switched into, either automatically or manually. DataLinkSwAid is the AID IgLinkSwAid.

##### Syntax: ```ALW-SWTOPROTN-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Protection Access Identifier. The address of the protection equipment unit which is to be allowed to accept the load from any of the working units that have been configured to be protected by it. EqptAid is the AID SlotLuAid.

##### Syntax: ```ALW-SWTOWKG-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Working Access Identifier. The address of the working equipment unit which is to be allowed to carry the load. EqptAid is the AID SlotLuAid.

##### Syntax: ```ALW-USER-SECU:[TID]::[CTAG]::<UIDLIST>; ```

##### Parameters
Attribute | Description
|---
UIDLIST|User Identifier. A list of one or more non-confidential identifiers that uniquely identifies which users will have session privileges re-instated (separated by &s). UIDLIST is a String.

##### Syntax: ```CANC-CID-SECU:[TID]:<CID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
CID|CID is the AID CID.

##### Syntax: ```CANC-PPPOESESS:[TID]:<MACAID>:[CTAG]::[<ACSESS>]:SCOPE=<SCOPE>,[HOSTMAC=<HOSTMAC>]; ```

##### Parameters
Attribute | Description
|---
MACAID|This is the Ethernet Address of the AC as learned from the PPPoE Discovery packet. If ALL is specified, the ACSESS must be NULL. MACAID is the AID MacRngAid.
ACSESS|The Session Id is a 16 bit number produced by the AC during the discovery phase. If ACSESS is null, all sessions for the access concentrator will be cancelled. ACSESS is a Integer.
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1.
HOSTMAC|This is the Ethernet Address of the Host as learned from the PPPoE Discovery packet HOSTMAC is the AID MacAid.

##### Syntax: ```CANC-SES-SECU:[TID]:<MsAid>:[CTAG]::<UIDLIST>; ```

##### Parameters
Attribute | Description
|---
MsAid|Maintenance Slot Access Identifier. The address of the maintenance slot where the user's session was retrieved. MsAid is the AID MsAid.
UIDLIST|User Identifier. A list of one or more non-confidential identifiers that uniquely identifies which users will have session privileges re-instated (separated by &s). UIDLIST is a String.

##### Syntax: ```CANC-USER:[TID]:<UID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
UID|User Identifier. The user's identifier for session to be cancelled. User Identifier. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination of alphanumeric characters 4 to 10 characters long and is case-sensitive. UID is a String.

##### Syntax: ```CHG-SPLIT:[TID]:<TapAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TapAid|Test Access Path (TAP) Access Identifier. The test access path number selected. The assigned TAP number is echoed back in the response of the initial CONN-LPACC-MET (Connect Loop Around Access Metallic) message. Thereafter, TAP is used to identify all messages between the TSC and NE until the access point is released. TapAid is the AID TapAid.

##### Syntax: ```CONN-FPACC-MET:[TID]:<MetAid>:[CTAG]::<TAP>:[[CNFGN=<CNFGN>,][TMOUT=<TMOUT>]]; ```

##### Parameters
Attribute | Description
|---
MetAid|Metallic Port Access Identifier. The address of the metallic port which is to be connected to the test bus. MetAid is the AID TwentyFourPortLuAid.
TAP|Test Access Path (TAP) Identifier. The test access path selected. If the requested TAP is not available, the command will be rejected. This parameter must be provided. TAP is the AID TapAid.
CNFGN|Configuration Code. For metallic access, it defines the access point lead-pair usage configuration. CNFGN is of type ConfigurationFP. The default value is "2WA".
TMOUT|Time Out. The amount of time the test should be established for. If the period of time expires, then if the test is still established is should be torn down. TMOUT is of type TimeOutTesting. The default value is "5".

##### Syntax: ```CONN-LPACC-MET:[TID]:<MetAid>:[CTAG]::<TAP>:[CNFGN=<CNFGN>]; ```

##### Parameters
Attribute | Description
|---
MetAid|Metallic Port Access Identifier. The address of the metallic port which is to be connected to the test bus. MetAid is the AID TwentyFourPortLuAid.
TAP|Test Access Path (TAP) Identifier. The test access path number selected. If the requested TAP is not available, the command will be rejected. TAP is the AID TapAid.
CNFGN|Configuration Code. For metallic access, this defines the access point lead-pair usage configuration. CNFGN is of type Configuration. The default value is "2WA".

##### Syntax: ```CONN-MON:[TID]:<TapAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TapAid|TapAid is the AID TapAid.

##### Syntax: ```CONN-TACC-MET:[TID]:<TapAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TapAid|Test Access Path (TAP) Identifier. The test access path number selected. The assigned TAP number which was echoed back in the response of the initial CONN-LPACC-MET (Connect Loop Around Access Metallic) message. TapAid is the AID TapAid.

##### Syntax: ```DISC-FPACC-MET:[TID]:<TapAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TapAid|Test Access Path (TAP) Identifier. The test access path which was selected for the test. TapAid is the AID TapAid.

##### Syntax: ```DISC-TACC:[TID]:<TapAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TapAid|Test Access Path (TAP) Identifier. The test access path which is to be disconnected. The assigned TAP number which was echoed back in the response of the initial CONN-LPACC-MET (Connect Loop Around Access Metallic) message. TapAid is the AID TapAid.

##### Syntax: ```DLT-<OCN>:[TID]:<OcNAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Access Identifer. The address of the port being deleted. OcNAid is the AID FourPortLuAndRapRngAid and is listable and rangeable.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a port even if it will delete an active Calix LINK. INCL is of type BoolYN.

##### Syntax: ```DLT-<STSN>:[TID]:<StsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS12C Access Identifer. The access identifier for the STSnC path being deleted. StsAid is the AID StsRngAid and is listable and rangeable.

##### Syntax: ```DLT-ADSL:[TID]:<AdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AdslAid|Asymmetric Digital Subscriber Access Identifer. The access identifier for the DSL entity being deleted. AdslAid is the AID TwentyFourPortLuRngAid and is listable and rangeable.

##### Syntax: ```DLT-ALM-SHELF:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf whose alarms are being deleted. ShelfAid is the AID ShelfAid.

##### Syntax: ```DLT-AP:[TID]:<ApAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid.

##### Syntax: ```DLT-AP-T1:[TID]:<ApAid>:[CTAG]::[<PLOCN>]:[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid.
PLOCN|Physical Location. This is the AID of the associated T1 or HDSL port. PLOCN is the AID TwelvePortLuAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced removal of the association in case the T1 port provisioning is missing a reference to the AP. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-AVO:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Analog Video Overlay Port Access Identifer. The address of the AVO port being deleted. The port number must be equal to 1. OntPortAid is the AID OntPortRngAid.

##### Syntax: ```DLT-BWC:[TID]:<BwcAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
BwcAid|Bandwidth Constraint Access Identifier. Identifier of the Bandwidth Constraint to be operated upon. BwcAid is the AID BwcProvAid.
INCL|INCLusive. This flag allows an internal bandwidth constraint to be forcibly deleted. This is a restricted parameter. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-BWCLINK:[TID]:<LinkBwcAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
LinkBwcAid|Link Bandwidth Constraint Access Identifier. Identifies the Link Bandwidth Constraint to be operated upon. LinkBwcAid is the AID BwclinkId.
INCL|Include flag. This flag is used to do a force delete on internally created Bandwidth Constraint links. INCL is of type BoolYN.

##### Syntax: ```DLT-CFG-ONT:[TID]:<CfgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
CfgAid|Aid of ONT configuration file. CfgAid is the AID CfgAid.

##### Syntax: ```DLT-CRS-<STSN>:[TID]:<SrcStsAid>,[<DstStsAid>]:[CTAG]:::[[SCOPE=<SCOPE>,][PATH=<PATH>,][INTERNAL=<INTERNAL>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
SrcStsAid|Source Access Identifier. The address of the source (from) STS endpoint of the cross-connect being deleted. SrcStsAid is the AID StsCrsAid.
DstStsAid|Destination Access Identifier. The address of the destination (to) STS endpoint of the cross-connect being deleted. DstStsAid is the AID StsCrsAid.
SCOPE|SCOPE of deletion. This will indicate how far to delete the cross-connect. SCOPE is of type Scope. The default value is "NTWK".
PATH|Path on which to follow the cross-connect. PATH is of type Path. The default value is "Any provisioned".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the deletion of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. The default value is "NONE".
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a cross-connect even though the cross-connect is restricted (owned by an application within the C7 system). INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-CRS-DCC:[TID]:<CrsDccSrcAid>,[<CrsDccDestAid>]:[CTAG]:::[[SCOPE=<SCOPE>,][PATH=<PATH>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
CrsDccSrcAid|Source Access Identifier. The address of the source (from) SDCC endpoint of the cross-connect being deleted. SDCC denotes a section DCC. LDCC denotes a line DCC. LDCC(1-3) denotes one byte in the line DCC overhead. CrsDccSrcAid is the AID DccAid.
CrsDccDestAid|Destination Access Identifier. The address of the destination (to) SDCC endpoint of the cross-connect being deleted. SDCC denotes a section DCC. LDCC denotes a line DCC. LDCC(1-3) denotes one byte in the line DCC overhead. CrsDccDestAid is the AID DccAid.
SCOPE|SCOPE of deletion. This will indicate how far to delete the cross-connect. SCOPE is of type Scope. The default value is "NTWK".
PATH|Path on which to follow the cross-connect. PATH is of type Path. The default value is "Any provisioned".
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a cross-connect even though the cross-connect is restricted (owned by an application within the C7 system). INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-CRS-T0:[TID]:<SrcDs0Aid>,[<DstDs0Aid>]:[CTAG]:::[[SCOPE=<SCOPE>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
SrcDs0Aid|Source Access Identifier. The access identifier of the source (from) endpoint of the cross-connect being deleted. SrcDs0Aid is the AID CrsT0SrcAid and is listable and rangeable.
DstDs0Aid|Destination Access Identifier. The access identifier of the destination (to) endpoint of the cross-connect being deleted. DstDs0Aid is the AID CrsT0DstAid.
SCOPE|SCOPE of deletion. This will indicate how far to delete the cross-connect. SCOPE is of type Scope. The default value is "NTWK".
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a T0 cross-connect when the remote shelf is unreachable. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-CRS-T1:[TID]:<SrcDs1Aid>,[<DstDs1Aid>]:[CTAG]:::[[SCOPE=<SCOPE>,][PATH=<PATH>,][INTERNAL=<INTERNAL>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
SrcDs1Aid|Source Access Identifier. The access identifier of the source (from) endpoint of the cross-connect being deleted. SrcDs1Aid is the AID T1CrsAid.
DstDs1Aid|Destination Access Identifier. The access identifier of the destination (to) endpoint of the cross-connect being deleted. DstDs1Aid is the AID T1CrsAid.
SCOPE|SCOPE of deletion. This will indicate how far to delete the cross-connect. SCOPE is of type Scope. The default value is "NTWK".
PATH|Path on which to follow the cross-connect. PATH is of type Path. The default value is "Any provisioned".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the deletion of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. The default value is "NONE".
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a cross-connect even though the cross-connect is restricted (owned by an application within the C7 system). INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-CRS-VC:[TID]:<SrcVcAid>,[<DstVcAid>]:[CTAG]:::[[SCOPE=<SCOPE>,][PATH=<PATH>,][INTERNAL=<INTERNAL>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVcAid|Source Access Identifier. The access identifier of the source (from) endpoint of the cross-connect being deleted. SrcVcAid is the AID VcId6.
DstVcAid|Destination Access Identifier. The access identifier of the destination (to) endpoint of the cross-connect being deleted. DstVcAid is the AID VcId12.
SCOPE|SCOPE of deletion. This will indicate how far to delete the cross-connect. SCOPE is of type Scope. The default value is "NTWK".
PATH|Path on which to follow the cross-connect. PATH is of type Path. The default value is "Any provisioned".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the deletion of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. The default value is "NONE".
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a cross-connect even though the cross-connect is restricted (owned by an application within the C7 system). INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-CRS-VIDVC:[TID]:<SrcVcAid>,<DstVcAid>:[CTAG]:::IRCAID=<IrcAid>,[[INTERNAL=<INTERNAL>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVcAid|Source Access Identifier. The access identifier of the source (from) endpoint of the cross-connect being deleted. SrcVcAid is the AID VidvcId1.
DstVcAid|Destination Access Identifier. The access identifier of the destination (to) endpoint of the cross-connect being deleted. DstVcAid is the AID VidvcId1.
IrcAid|Slot address of the IRC. IrcAid is the AID SlotLuAid.
INTERNAL|Internal Cross Connects. If present, this parameter specifies the deletion of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. The default value is "NONE".
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a video cross-connect from the IRC when the cross-connect does not exist in the RAPs database. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-CRS-VP:[TID]:<SrcVpAid>,[<DstVpAid>]:[CTAG]:::[[SCOPE=<SCOPE>,][PATH=<PATH>,][INTERNAL=<INTERNAL>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVpAid|Source Access Identifier. The access identifier of the source (from) endpoint of the cross-connect being deleted. SrcVpAid is the AID VpAid.
DstVpAid|Destination Access Identifier. The access identifier of the destination (to) endpoint of the cross-connect being deleted. DstVpAid is the AID VpAid.
SCOPE|SCOPE of deletion. This will indicate how far to delete the cross-connect. SCOPE is of type Scope. The default value is "NTWK".
PATH|Path on which to follow the cross-connect. PATH is of type Path. The default value is "Any provisioned".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the deletion of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. The default value is "NONE".
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a cross-connect even though the cross-connect is restricted (owned by an application within the C7 system). INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-CVIDREG:[TID]:<CVidRegAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
CVidRegAid|CVID Registration Table Entry Access Identifier. CVidRegAid is the AID CVidRegAid.

##### Syntax: ```DLT-DHCP-OUI:[TID]:<OUIAID>:[CTAG]:::RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
OUIAID|Organizationally Unique Identifier. The OUI is first 3 octets of the MAC address and identifies the vendor OUIAID is the AID OuiAid.
RTRAID|Router AID - target Virtual Router, or IRC slot address. RTRAID is the AID RouterAid.

##### Syntax: ```DLT-DHCPSVR:[TID]:<IP>:[CTAG]:::RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
IP|DHCP Server IP Address. IP is the AID IpAid.
RTRAID|RTRAID is the AID RouterAid.

##### Syntax: ```DLT-EC1:[TID]:<Ec1Aid>:[CTAG]::[LBO=<LBO>]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|Access Identifier. The access identifier of the EC1 being deleted. Ec1Aid is the AID TwelvePortLuAid.
LBO|LineBuildOut. LBO is a Integer.

##### Syntax: ```DLT-EOAM-FMP:[TID]:<FMPAID>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
FMPAID|FMPAID is the AID EthOamFmpAid.

##### Syntax: ```DLT-EOAM-MEG:[TID]:<MEGAID>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid.
INCL|INCL is of type BoolYN.

##### Syntax: ```DLT-EOAM-MEP:[TID]:<MEPAID>:[CTAG]:::[IFAID=<IFAID>]; ```

##### Parameters
Attribute | Description
|---
MEPAID|MEPAID is the AID EthOamMepAid.
IFAID|IFAID is the AID MepId1.

##### Syntax: ```DLT-EOAM-MIP:[TID]:<MIPAID>:[CTAG]:::[MEGAID=<MEGAID>]; ```

##### Parameters
Attribute | Description
|---
MIPAID|MIPAID is the AID OntPortAid.
MEGAID|MEGAID is the AID MegAid.

##### Syntax: ```DLT-EOAM-RMEP:[TID]:<RMEPAID>:[CTAG]:::[RMEPIDLIST=<RMEPIDLIST>]; ```

##### Parameters
Attribute | Description
|---
RMEPAID|RMEPAID is the AID EthOamMepAid.
RMEPIDLIST|RMEPIDLIST is of type OneTo8191.

##### Syntax: ```DLT-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The access identifier for the equipment entity being deleted. EqptAid is the AID EquipmentId and is listable.

##### Syntax: ```DLT-ERPS:[TID]:<ErpsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsAid.

##### Syntax: ```DLT-ETH:[TID]:<EthPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Access Identifier. EthPortAid is the AID EthId1.

##### Syntax: ```DLT-ETH-ACL:[TID]:<EthPortAid>:[CTAG]::[[MAC=<MAC>,][MMSK=<MMSK>]]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Port Access Identifier. EthPortAid is the AID TwelvePortLuAid.
MAC|MAC address MAC is the AID MacAid.
MMSK|Mac address mask MMSK is the AID MacAid.

##### Syntax: ```DLT-FFP-<OCN>:[TID]:<WrkOcNAid>,[<ProtOcNAid>]:[CTAG]; ```

##### Parameters
Attribute | Description
|---
WrkOcNAid|Working OCn Access Identifier. The address of the port which receives the traffic from the working fiber in the facility protection group. WrkOcNAid is the AID FourPortLuAndRapAid.
ProtOcNAid|Protection Access Identifier. The address of the port which receives the traffic from the protect fiber in the facility protection group. ProtOcNAid is the AID FourPortLuAndRapAid.

##### Syntax: ```DLT-FTP:[TID]:<FTPAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
FTPAID|FTP server AID. FTPAID is the AID FtpAid.

##### Syntax: ```DLT-GOS-<OCN>:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the OCn Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-<STSN>:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the STS1 Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-ADSL:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the ADSL Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-AP:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-EC1:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the EC1 Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-ETH:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-GRPXDSL:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the GRPXDSL Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-HDSL:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the EC1 Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-IMA:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-IMALINK:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Link Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-ONT:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-PW:[TID]:<GosAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
GosAid|PW Grade of Service Aid pattern. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-T1:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the T1 Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-T3:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The access identifier of the T3 Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GOS-XDSL:[TID]:<GosAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the XDSL Grade of Service table entry. GosAid is the AID GosProvAid.

##### Syntax: ```DLT-GR303:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Interface Group Access Identifier. The address of the GR-303 Interface Group within a shelf. IgAid is the AID IgAid.

##### Syntax: ```DLT-GR8:[TID]:<SlotIgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SlotIgAid|GR-8 Interface Group Access Identifier. This is the address of the GR-8 Interface Group which is being deleted. SlotIgAid is the AID SlotIgAid.

##### Syntax: ```DLT-GRPXDSL:[TID]:<GroupAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GroupAid is the AID DslGrpAid.

##### Syntax: ```DLT-GW-VOIP:[TID]:<VOIPGWAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VOIPGWAID|AID of the VoIP Gateway VOIPGWAID is the AID VoIPGWONTAid.

##### Syntax: ```DLT-H248:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|H.248 Interface Group Access Identifier. This is the address of the H.248 Interface Group which is being deleted. IgAid is the AID IgAid.

##### Syntax: ```DLT-HDSL:[TID]:<HdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Access Identifer. The access identifier for the HDSL port being deleted. HdslAid is the AID SixPortLuRngAid and is listable and rangeable.

##### Syntax: ```DLT-IG-CRV:[TID]:<CrvAid>:[CTAG]::[<PLOCN>]; ```

##### Parameters
Attribute | Description
|---
CrvAid|Call Reference Value Access Identifier. The address of the call reference value within a GR-303 interface group. CrvAid is the AID CrvAid.
PLOCN|Physical Location. The physical location of the subscriber line associated with the Call Reference Value within the C7 network. This parameter only needs to be entered if there is an inconsistency in the database at either the IG shelf or the CRV shelf. PLOCN is the AID T0CrvAid.

##### Syntax: ```DLT-IG-CSHELF:[TID]:<IgAid>:[CTAG]::<SHELF>:[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The Interface Group AID. IgAid is the AID IgAid.
SHELF|The associated subscriber shelf. SHELF is the AID ShelfAid.
INCL|Force flag. If the specified Shelf is not reachable, INCL=Y is required to force the deletion. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-IG-DS1:[TID]:<IgDs1Aid>:[CTAG]::[<PLOCN>],[<CMDMODE>]; ```

##### Parameters
Attribute | Description
|---
IgDs1Aid|Interface Group Digital Signal 1 (DS1) Access Identifier. The address of the DS1 within an interface group. IgDs1Aid is the AID IgDs1Aid.
PLOCN|Physical Location. The physical location of the DS1 port associated with the IG. This parameter only needs to be entered if there is an inconsistency in the database at the IG shelf. PLOCN is the AID TwelvePortLuAid.
CMDMODE|Command Mode. This parameter should only be used when there is an inconsistency in the database and the IG shelf is not currently reachable. This parameter will allow the database on the reachable end to be modified without the other end being modified. CMDMODE is of type CommandMode.

##### Syntax: ```DLT-IG-VDS1:[TID]:<IgDs1Aid>:[CTAG]::[<PLOCN>],[<CMDMODE>]; ```

##### Parameters
Attribute | Description
|---
IgDs1Aid|The address of the logical DS1 within a VCG interface group. IgDs1Aid is the AID IgDs1Aid.
PLOCN|Physical Location. The "physical location" of the virtual DS1 port associated with the IG. This parameter only needs to be entered if there is an inconsistency in the database at the IG shelf. PLOCN is the AID Vds1Aid.
CMDMODE|Command Mode. This parameter should only be used when there is an inconsistency in the database and the IG shelf is not currently reachable. This parameter will allow the database on the reachable end to be modified without the other end being modified. CMDMODE is of type CommandMode.

##### Syntax: ```DLT-IG-VSP:[TID]:<IgVspAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgVspAid|The address of the logical VSP within a H.248 interface group. IgVspAid is the AID IgVspAid.

##### Syntax: ```DLT-IGMP-JOIN:[TID]:<IP>:[CTAG]:::IRCAID=<IRCAID>,[[VP=<VP>,][VC=<VC>]],L2IFAID=<L2IFAID>; ```

##### Parameters
Attribute | Description
|---
IP|IP address of the EPG channel or Multicast IP address for video. IP is the AID IpAid and is listable.
IRCAID|IRCAid - address of the IRC slot IRCAID is the AID SlotLuAid.
VP|VP - VPI number of the single VC used to aggregate all the EPG channels. VP is of type VPRange.
VC|VCI number of the singel VC used to aggregate all the EPG channels. VC is of type VCRange.
L2IFAID|L2IFAID is the AID VbPortAid.

##### Syntax: ```DLT-IMA:[TID]:<ImaAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA AID. This is the address of the IMA Interface Group that is being deleted. The slot number of this AID must be that of the T1 lines which are to be included in the group. ImaAid is the AID ImaGrpAid.

##### Syntax: ```DLT-IMA-PORT:[TID]:<ImaAid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
ImaAid|Ima Aid. This is the address of the IMA Interface Group that is being deleted. The slot number of this AID must be that of a T1 line which is a member of the group. ImaAid is the AID ImaGrpAid.
PLOCN|Physical LOCatioN of the port. This specifies the location of the T1 port. It must specify the same slot as that of the IMA group. PLOCN is the AID PortId.

##### Syntax: ```DLT-IP-HOST:[TID]:<IP>:[CTAG]:::[[RTRAID=<RTRAID>,][BRIDGE=<BRIDGE>,][L2IFAID=<L2IFAID>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP Address. The static IP address of the Host to be deleted. IP is the AID IpAid.
RTRAID|RTRAID is the AID RouterAid.
BRIDGE|BRIDGE is the AID BridgeProvAid.
L2IFAID|Layer 2 Interface Access Identifier - This is the port address or the VC AID on which the host can be found. The system will use an IP VC if it is the only IP VC on the specified PORT. If the IP VC hasn't been provisioned yet, the system will use the first one upon its creation. IP HOST creation to a PON port is not allowed. IP HOST creation between an IRC PP1 and GE-2p VB port is not allowed. Hosts may be identified by enabling ARP between the IRC and Ge2p. L2IFAID is the AID HostId.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a DHCP or ARP entry. Normally DHCP and ARP host entries are created and deleted by the C7 system. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-IP-HOSTID:[TID]:<IPHostIdAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
IPHostIdAid|IP HostId AID on 8/12-port line-unit. IPHostIdAid is the AID IPHostIdAid.

##### Syntax: ```DLT-IP-IF:[TID]:<IP>:[CTAG]:::[[L2IFAID=<L2IFAID>,][RTRAID=<RTRAID>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP address. The IP address may not be all zeros. The IP address anded with the IPMSK may not equal zero. The IP address anded with the compliment of the IPMSK may not be zero IP is the AID IpAid.
L2IFAID|L2IFAID is the AID IpIfAid.
RTRAID|RTRAID is required for a virtual router and optional for IRC. RTRAID is the AID RouterAid.
INCL|INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-IP-ROUTE:[TID]:<IPMASK>:[CTAG]:::RTRAID=<RTRAID>,[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
IPMASK|IP/MASK - Destination subnet IP Address and destination subnet IP address Mask used to define the IP Route. IPMASK is the AID IpMask.
RTRAID|RTRAID is the AID RouteId1.
INCL|INCLUSIVE. This parameter provides a way for the user to force delete the default route with INCL=Y. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-IPIF-PORT:[TID]:<IP>:[CTAG]:::INTERFACE=<INTERFACE>,RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
IP|IP address to associate the lower layer interface. IP is the AID IpAid.
INTERFACE|Lower Layer Interface. This can be a Virtual Bridge, Virtual Router VC, VLAN etc. INTERFACE is the AID IpIfPortAid.
RTRAID|Router Access Identifier.- This is the address of the virtual router for the IP interface. RTRAID is the AID VrAid.

##### Syntax: ```DLT-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 12 groups are supported on a single slot, and up to 4 on a single VB. LinkAggAid is the AID LinkAggAid.

##### Syntax: ```DLT-LSWITCH:[TID]:<LSwitchAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LSwitchAid|Logical Switch Access Identifier. LSwitchAid is the AID LSwitchAid.

##### Syntax: ```DLT-LSWITCH-PORT:[TID]:<LSwitchPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LSwitchPortAid|Logical Switch Port Access Identifier. LSwitchPortAid is the AID LSwitchPortAid.

##### Syntax: ```DLT-MACHOST:[TID]:<MACAID>:[CTAG]:::VLAN=<VLAN>,[[BRIDGE=<BRIDGE>,][L2IFAID=<L2IFAID>,][STATIC=<STATIC>]]; ```

##### Parameters
Attribute | Description
|---
MACAID|MAC Address. MACAID is the AID MacRngAid.
VLAN|VLAN is the AID IfId1.
BRIDGE|BRIDGE is the AID VbAid.
L2IFAID|L2IFAID is the AID MachostId1.
STATIC|Indicates whether the MACHOST entry was STATICally provisioned or dynamically learned. STATIC is of type BoolYN. The default value is "Y".

##### Syntax: ```DLT-NODE:[TID]:<NodeAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
NodeAid|The AID of the node to be deleted. NodeAid is the AID NodeAid.

##### Syntax: ```DLT-ONT:[TID]:<OntAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntAid|The AID of the ONT being deleted. OntAid is the AID OntAid.

##### Syntax: ```DLT-ONT-QUAR:[TID]:<QuarOntAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
QuarOntAid|QuarOntAid is the AID QuarOntAid.

##### Syntax: ```DLT-PON:[TID]:<PonAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PonAid|The PON Port Access Identifier. PonAid is the AID FourPortLuRngAid and is listable and rangeable.

##### Syntax: ```DLT-PP:[TID]:<PpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpAid|The PseudoPort AID. PpAid is the AID PpAid.

##### Syntax: ```DLT-PPPOEAC:[TID]:<MAC>:[CTAG]:::SCOPE=<SCOPE>,[VLAN=<VLAN>]; ```

##### Parameters
Attribute | Description
|---
MAC|MAC Address : This is the Ethernet Address of the AC as learned from the PPPoE Discovery packet MAC is the AID MacAid and is listable.
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1.
VLAN|The request may be filtered to a specific VLAN. VLAN is the AID VlanIndexAid.

##### Syntax: ```DLT-PPPOEHOST:[TID]:<MACAID>:[CTAG]:::SCOPE=<SCOPE>,[[L2IFAID=<L2IFAID>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
MACAID|This is the Ethernet Address of the Host as learned from the PPPoE Discovery packet MACAID is the AID MacAid and is listable.
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1.
L2IFAID|Layer 2 Interface Access Identifier - This can be one of the following : - subscriber port on which this Host was discovered OR - AID of the remote endpoint (on an access LU card) of the subscriber VC. L2ifAid is required parameter for PPPOA and optional for PPPOE. L2IFAID is the AID PppoehostId1.
INCL|This is an input parameter to the delete command. It determines whether any open sessions should be terminated (sent a PADT packet) before deleting the AC record. INCL=Y : any active session is terminated before the Host Record is deleted. INCL=N: the Host Record will not be deleted if there is an active session. Session termination entails sending a PADT packet to both the AC and the Host, and removing all associated fast-path forwarding entries from the Network Processing subsystem. INCL is of type BoolYN.

##### Syntax: ```DLT-PROF-ACS:[TID]:<ACSPROFAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ACSPROFAID|The ACSProf Access Identifier. ACSPROFAID is the AID AcsProfAid.

##### Syntax: ```DLT-PROF-ETH:[TID]:<EthProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EthProfAid|Ethernet Profile Number. EthProfAid is the AID EthProfAid.

##### Syntax: ```DLT-PROF-ETHBW:[TID]:<BwpProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
BwpProfAid|This identifies which profile is being operated on. BwpProfAid is the AID BwpProfAid.

##### Syntax: ```DLT-PROF-MATCHLIST:[TID]:<MatchListAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
MatchListAid|A unique network wide ID. MatchListAid is the AID MatchListAid.

##### Syntax: ```DLT-PROF-MATCHRULE:[TID]:<RuleAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
RuleAid|A C7 Network unique number identifying the rule. RuleAid is the AID MatchRuleId.

##### Syntax: ```DLT-PROF-MCAST:[TID]:<McastProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
McastProfAid|McastProfAid is the AID McastProfAid.

##### Syntax: ```DLT-PROF-MCASTRANGE:[TID]:<McastRangeProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
McastRangeProfAid|Multicast Range Profile AID. McastRangeProfAid is the AID McastRangeProfAid.

##### Syntax: ```DLT-PROF-MVR:[TID]:<MvrProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
MvrProfAid|MvrProfAid is the AID MvrProfAid.

##### Syntax: ```DLT-PROF-ONT:[TID]:<OntProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntProfAid|ONT profile number. OntProfAid is the AID OntProfAid.

##### Syntax: ```DLT-PROF-SIPDIAL:[TID]:<SipDialAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SipDialAid|System scoped Dial Plan for SIP Gateways. SipDialAid is the AID DialPlanAid.

##### Syntax: ```DLT-PROF-SIPSVC:[TID]:<SipSvcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SipSvcAid|System scoped SIP Profile. SipSvcAid is the AID SipSvcAid.

##### Syntax: ```DLT-PROF-TRF:[TID]:<TrfProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TrfProfAid|Traffic Profile Access Identifier. The access identifier of the Traffic Profile table entry being deleted. TrfProfAid is the AID AtmTrfProfProvAid.

##### Syntax: ```DLT-PW:[TID]:<PwAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
PwAid|PW Aid pattern. PwAid is the AID PwRangeAid.

##### Syntax: ```DLT-RFVID:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Rf-Video Port Access Identifer. The address of the RFVID port being deleted. The port number must be equal to 1. OntPortAid is the AID OntPortRngAid.

##### Syntax: ```DLT-RMTDEV:[TID]:<RmtDevAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
RmtDevAid|Remote Device Access Identifier. RmtDevAid is the AID RmtDevAid.

##### Syntax: ```DLT-SIP:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Access Identifier for the SIP Group. IgAid is the AID IgAid.

##### Syntax: ```DLT-SIPT0:[TID]:<T0Port>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Port|T0Port is the AID SipT0PortAid.

##### Syntax: ```DLT-SIPVCG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Ig Number within a shelf. IgAid is the AID IgAid.

##### Syntax: ```DLT-SNMP-ACL:[TID]::[CTAG]:::IP=<IP>,IPMSK=<IPMSK>; ```

##### Parameters
Attribute | Description
|---
IP|IP Address. The IP address of the SNMP manager that is allowed to make requests to the C7 network. IP is the AID IpAid.
IPMSK|IP Address Mask. The mask to apply to the IP address, allowing for a range of IP addresses to be considered. IPMSK is the AID IpAid.

##### Syntax: ```DLT-SUBIF-BINDING:[TID]:<PHYSLOC>:[CTAG]:::RTRAID=<RTRAID>,IP=<IP>; ```

##### Parameters
Attribute | Description
|---
PHYSLOC|PHYSLOC is the AID SubIfBindingAid.
RTRAID|RTRAID is the AID SlotLuAid.
IP|IP is the AID IpAid.

##### Syntax: ```DLT-T0:[TID]:<T0Aid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Access Identifer. The access identifier for the T0 port being deleted. T0Aid is the AID TwentyFourPortLuRngAid and is listable and rangeable.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a port even if it is in the RDLD state. INCL is of type BoolYN.

##### Syntax: ```DLT-T1:[TID]:<Ds1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Access Identifer. The access identifier for the T1 port being deleted. Ds1Aid is the AID TwelvePortLuRngAid and is listable and rangeable.

##### Syntax: ```DLT-T1TG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Interface Group AID. This parameter specifies the interface group to which is to be deleted. IgAid is the AID IgAid.

##### Syntax: ```DLT-T3:[TID]:<Ds3Aid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|DS3 Access Identifer. The address of the port being deleted. Ds3Aid is the AID T3RngAid and is listable and rangeable.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a port even if it will delete an active Calix LINK. INCL is of type BoolYN.

##### Syntax: ```DLT-TDMGW:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgAid.

##### Syntax: ```DLT-TGRP:[TID]:<MsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
MsAid|Management/Maintenance Slot Access Identifier. The address of the Management/Maintenance Slot where the Administration and Maintenance Processor (AMP) card of the test group was located. MsAid is the AID MsAid.

##### Syntax: ```DLT-TMPLT-ADSL:[TID]:<DslProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslProfAid|ADSL Profile Access Identifier. The address of the specific entry in ADSL Profile table. DslProfAid is the AID DslProfProvAid.

##### Syntax: ```DLT-TMPLT-PW:[TID]:<PwTmpltAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
PwTmpltAid|PW template Aid pattern. PwTmpltAid is the AID PwTmpltAid.

##### Syntax: ```DLT-TMPLT-SECU:[TID]:<SecuTmpltAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SecuTmpltAid|This is the AID of the template to be deleted. Only the numbered security templates may be deleted. SecuTmpltAid is the AID SecuTmpltProvAid.

##### Syntax: ```DLT-TMPLT-VLANIF:[TID]:<VlanIfTmpltAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VlanIfTmpltAid|VlanIfTmpltAid is the AID VlanPortTmpltAid.

##### Syntax: ```DLT-TMPLT-XDSL:[TID]:<DslProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslProfAid|DSL Configuration Template Number DslProfAid is the AID DslProfProvAid.

##### Syntax: ```DLT-USER-ACL:[TID]::[CTAG]:::IP=<IP>,IPMSK=<IPMSK>; ```

##### Parameters
Attribute | Description
|---
IP|IP Address. The IP address of the TL1 or iMS client. IP is the AID IpAid.
IPMSK|IP Address Mask. The mask to apply to the IP address, allowing for a range of IP addresses to be considered. IPMSK is the AID IpAid.

##### Syntax: ```DLT-USER-SECU:[TID]:<UID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
UID|User Identifier. The user's identifier for session to be cancelled. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination of alphanumeric characters 4 to 10 characters long and is case-sensitive. UID is the AID UserAid.

##### Syntax: ```DLT-VB:[TID]:<VbAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VbAid|Virtual Bridge Access Identifier. VbAid is the AID VbAid.

##### Syntax: ```DLT-VBPORT:[TID]:<VbPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|Virtual Bridge Port Aid - This is either the physical port or the VC end point associated with the virtual bridge. VbPortAid is the AID VirtualBridgePortId4.

##### Syntax: ```DLT-VCG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|The address of the VCG being deleted. IgAid is the AID IgAid.

##### Syntax: ```DLT-VCGLINK:[TID]:<IgAid>:[CTAG]::<LINK>:[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The address of the Voice Concentration Group. IgAid is the AID IgAid.
LINK|LINK is the AID VcglinkId.
INCL|INCL/Force. This flag can be used to force deletion when an endpoint is on an unreachable shelf. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VEP:[TID]:<VepAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VepAid|Voice Endpoint AID of POTs port on ONT or C7 Line Unit VepAid is the AID VepAid.

##### Syntax: ```DLT-VID-CHAN:[TID]:<IP>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IP|IP Address. IP is the AID IpAid.

##### Syntax: ```DLT-VID-FILTER:[TID]:<VidSrcAid>:[CTAG]:::IP=<IP>,IPMSK=<IPMSK>; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source Index AID. VidSrcAid is the AID VidSrcAid.
IP|IP Address. This is the Multicast IP address of the channel. IP is the AID IpAid.
IPMSK|IP MASK. This is used to indicate which range of IP addresses should be included or excluded from Channel auto-detection on the specified video source. IPMSK is the AID IpAid.

##### Syntax: ```DLT-VID-IRCLOC:[TID]:<VidServAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VidServAid|Video Service Access Identifier. The AID of the Video Service that contains the IRC. VidServAid is the AID VidServAid.

##### Syntax: ```DLT-VID-SOURCE:[TID]:<VidSrcAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source Index AID. VidSrcAid is the AID VidSrcAid.
INCL|INCLusive Flag. This flag is needed when deleting video source with channel associations. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VID-SUB:[TID]:<VidSubAid>:[CTAG]:::RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
VidSubAid|Video Subscriber Access Identifier - The port or channel to which subscribers are connected. Usually an ADSL Channel or ONT (or vdsl in the future) port. VidSubAid is the AID SubId1.
RTRAID|Target Router Access Identifier (IRC) RTRAID is the AID SlotLuAid.

##### Syntax: ```DLT-VID-SVC:[TID]:<VidSvcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VidSvcAid|Video Service Access Identifier. VidSvcAid is the AID VidSvcAid.

##### Syntax: ```DLT-VLAN:[TID]:<VLanAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VLanAid|Virtual LAN Access Identifier. VLanAid is the AID VlanId.

##### Syntax: ```DLT-VLAN-IF:[TID]:<IfAid>:[CTAG]:::VLAN=<VLAN>,[BRIDGE=<BRIDGE>]; ```

##### Parameters
Attribute | Description
|---
IfAid|Interface Aid. IfAid is the AID IfId11.
VLAN|Packet VLAN Access Identifier. Only VLAN number AID is allowed since R7.0. VLAN is the AID IfId1.
BRIDGE|VB access identifier. BRIDGE is the AID IfId8.

##### Syntax: ```DLT-VLAN-PORT:[TID]:<VLanPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VLanPortAid|VLAN port Access Identifier. VLanPortAid is the AID VLanPortAid.

##### Syntax: ```DLT-VLAN-VBPORT:[TID]:<VbPortAid>:[CTAG]:::VLAN=<VLAN>,[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|VbPortAid is the AID VirtualBridgePortId4.
VLAN|VLAN Access Identifier associated with the port. VLAN is the AID PacketVlanAid.
INCL|INCLusive. This parameter provides a way for the user to request a deletion of all CVIDREG entries that may be associated with this VLAN VBPORT. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VODCLNT:[TID]:<IpAid>:[CTAG]:::IRCAID=<IRCAID>,[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
IpAid|IP Address. The IP address of the VOD Client. IpAid is the AID IpAid.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a VOD Client. Normally VOD Clients are created and deleted by the C7 system. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VODDSTLU:[TID]:<EqptAid>:[CTAG]:::IRCAID=<IRCAID>,[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|VOD Destination LU Access Identifier. The address of the VOD Destination Line Unit. EqptAid is the AID EquipmentId3.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a VOD Destination LU. The VODDSTLU is created by ENT-VODDSTLU operation command. If not in use, it can be deleted without INCL flag. However, if some active VOD flow is using the VODDSTLU, the INCL flag must be provided and the affected active flow will be torn down. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VODFLOW:[TID]:<VodFlowId>:[CTAG]:::IRCAID=<IRCAID>,[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
VodFlowId|VOD Flow Access Identifier. Number of the VOD flow. VodFlowId is the AID VodFlowAid.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a VOD Flow. Normally VOD Flows are created and deleted by the C7 system. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VODSRCLU:[TID]:<EqptAid>:[CTAG]:::IRCAID=<IRCAID>,[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|VOD Source LU Access Identifier. The address of the VOD Source Line Unit. EqptAid is the AID VodsrcluId.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a VOD Source LU. Normally VOD Source LUs are created and deleted by the C7 system. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VODSVR:[TID]:<IpAid>:[CTAG]:::IRCAID=<IRCAID>,[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
IpAid|IP Address. The IP address of the VOD Server. IpAid is the AID IpAid.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced deletion of a VOD Server. Normally VOD Servers are created and deleted by the C7 system. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```DLT-VR:[TID]:<VrAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrAid|Virtual Router Access Identifier. VrAid is the AID VrAid.

##### Syntax: ```DLT-VRP:[TID]:<VrpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrpAid|Video Return Path Access Identifier. VrpAid is the AID VrpAid.

##### Syntax: ```DLT-VRPORT:[TID]:<VrPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrPortAid|Virtual Router Port Identifier - This is the Endpoint index id associated with a virtual router. VrPortAid is the AID VrEpIdxAid.

##### Syntax: ```DLT-VSP:[TID]:<VspAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VspAid|The AID of the VSP port. VspAid is the AID VspPortAid.

##### Syntax: ```DLT-XDSL:[TID]:<DslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslAid|Digital Subscriber Line Access Identifer. The access identifier for the DSL entity being deleted. DslAid is the AID TwentyFourPortLuRngAid.

##### Syntax: ```DLT-XLAN:[TID]:<XLanAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
XLanAid|EXtended LAN Access Identifier. XLanAid is the AID XLanAid.

##### Syntax: ```ED-<OCN>:[TID]:<OcAid>:[CTAG]:::[[TXS1=<TXS1>,][RXS1=<RXS1>,][LSREN=<LSREN>,][EXT=<EXT>,][FEPM=<FEPM>,][ALMPROF=<ALMPROF>,][SDBER=<SDBER>,][SFBER=<SFBER>,][GOS=<GOS>,][PDOM=<PDOM>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OcAid|OCn Access Identifer. The address of the OCn port being modified. OcAid is the AID FourPortLuAndRapAid.
TXS1|Transmit S1. This parameter is set to Y if the sync status nibble indicates the source of timing. It is set to N if the nibble is set to Do not Use for Synchronization (DUS). TXS1 is of type BoolYN.
RXS1|Receive S1. This parameter is set to Y if the received S1 sync status is to be acted uppon. It is set to N if it is to be ignored. RXS1 is of type BoolYN.
LSREN|LaSeR ENable. This parameter is set to Y to enable transmitting a signal over this facility. If the facility is to be used for receiving only, the value should be set to N. LSREN is of type BoolYN.
EXT|External Interface. This indicates if the OCn port is an internal or external path in the network. The value should be set to "Y" when the port is an external interface. It should be set to "N" when the port is connected to other shelves within a network of C7s. Note that EXT cannot be set to "N" on Sonet-only cards. Also note that this parameter must be changed independently of others, ie. a separate ED-OCn command is required. EXT is of type BoolYN.
FEPM|Far End Performance Monitoring. When this parameter is set to "N", the Far End Performance Monitoring data is not collected. When retrieving Far End PM, the Monitored Values (MONVAL) field will contain '0' and the Validity (VLDTY) field will contain 'INVLD'. When this parameter is set to "Y", data collection for Far End Performance Monitoring is enabled. The default value is "N". FEPM is of type BoolYN.
ALMPROF|Alarm Profile. The set of alarm Notification codes to be associated with this entity. ALMPROF is the AID AlmProfileAid.
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD.
SFBER|Signal Failed Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Failed Signal. SFBER is of type BitErrorRateSF.
GOS|Grade of service. This identifies the OCn grade of service for performance monitoring (PM) which will be applied to the OCn port. GOS is the AID GosAid.
PDOM|Protection domain. This is an integer that is used to associate a transport facility into a protection domain that is used for A to Z connection provisioning. The PDOM for each domain must be a unique non-zero integer. The value of 0 is reserved to indicate that the facility is not to be used for A to Z connections. PDOM is of type Pdom.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-<STSN>:[TID]:<StsAid>:[CTAG]:::[[STSMAP=<STSMAP>,][TIMDET=<TIMDET>,][EXPTRC=<EXPTRC>,][TRC=<TRC>,][FEPM=<FEPM>,][ALMPROF=<ALMPROF>,][SDBER=<SDBER>,][SFBER=<SFBER>,][GOS=<GOS>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path being modified. StsAid is the AID StsAid.
STSMAP|STS Mapping. This parameter indicates the type of mapping supported by the STS-p SPE. STSMAP is of type StsMap.
TIMDET|Trace Identifier Mismatch Detection. This parameter indicates whether to turn on or off the trace identifer mismatch detection for the expected trace. TIMDET is of type OnOff.
EXPTRC|Expected Path Trace. This parameter is the expected Path Trace (J1) content. The maximum length of the string is 62 characters. The system will automatically add a carriage return (CR) and line feed (LF) to end of string to make it 64 characters. EXPTRC is a String.
TRC|Transmit Path Trace. This parameter indicates the path trace to be transmitted. The maximum length of the string is 62 characters. The system will automatically add a carriage return (CR) and line feed (LF) to end of string to make it 64 characters. TRC is a String.
FEPM|Far End Performance Monitoring. When this parameter is set to "N", the Far End Performance Monitoring data is not collected. When retrieving Far End PM, the Monitored Values (MONVAL) field will contain '0' and the Validity (VLDTY) field will contain 'INVLD'. When this parameter is set to "Y", data collection for Far End Performance Monitoring is enabled. The default value is "N". FEPM is of type BoolYN.
ALMPROF|Alarm Profile. The set of alarm Notification codes to be associated with this entity. ALMPROF is the AID AlmProfileStsAid.
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Path's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD.
SFBER|Signal Failed Bit Error Rate. The threshold value above which the Path's bit error rate constitutes a Failed Signal. Note that the valid SFBER threshold can currently be only 4 or 5; ``` a value of 3 is not valid for STS12c. SFBER is of type BitErrorRateSF.
GOS|Grade of Service Access Identifier. This identifies the specific Grade of Service for Performance Monitoring (PM) which will be applied to the STSnC facility. GOS is the AID GosAid.
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. It applies only to UNI and NNI interfaces, in which case it defaults to 'Y'. PYLDSCRM is of type BoolYN.
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. ATMMON is of type BoolYN.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-ADSL:[TID]:<AdslAid>:[CTAG]::[<SRVTYPE>],[<CHNL0>],[<CHNL1>]:[[PROF=<PROF>,][XDSR0=<XDSR0>,][MDSR0=<MDSR0>,][XUSR0=<XUSR0>,][MUSR0=<MUSR0>,][XDSR1=<XDSR1>,][MDSR1=<MDSR1>,][XUSR1=<XUSR1>,][MUSR1=<MUSR1>,][DSEXR=<DSEXR>,][USEXR=<USEXR>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][DSLAT=<DSLAT>,][USLAT=<USLAT>,][TC=<TC>,][RAMODEDS=<RAMODEDS>,][RAMODEUS=<RAMODEUS>,][RAUMDS=<RAUMDS>,][RADMDS=<RADMDS>,][RAUTDS=<RAUTDS>,][RADTDS=<RADTDS>,][RAUMUS=<RAUMUS>,][RADMUS=<RADMUS>,][RAUTUS=<RAUTUS>,][RADTUS=<RADTUS>,][AHC=<AHC>,][PMMODE=<PMMODE>,][L0TIME=<L0TIME>,][L2TIME=<L2TIME>,][L2ATPR=<L2ATPR>,][L2MINR=<L2MINR>,][L2EXITR=<L2EXITR>,][L2ENTRYR=<L2ENTRYR>,][L2ENTRYT=<L2ENTRYT>,][DSST=<DSST>,][DSET=<DSET>,][USST=<USST>,][USET=<USET>,][GOS=<GOS>,][MININPDS=<MININPDS>,][MININPUS=<MININPUS>,][REPTRMVRST=<REPTRMVRST>,][INCL=<INCL>,][ENABLENOTCH=<ENABLENOTCH>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
AdslAid|Asymmetric Digital Subscriber Line (ADSL) Access Identifier. The address of the ADSL port which is being modified. AdslAid is the AID TwentyFourPortLuAid.
SRVTYPE|Service Type. This parameter specifies the ADSL operating modes that dictate the ADSL handshaking protocol, channel capacity, and other physical line characteristics based on ADSL specifications. SRVTYPE is of type AdslType.
CHNL0|Channel 0 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (4 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL0 is of type ChnlSelect0.
CHNL1|Channel 1 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (2 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL1 is of type ChnlSelect1.
PROF|ADSL Profile. This specifies the ADSL profile which is to set the initial values for the confirguration parameters for the ADSL line. These parameters may be over-ridden by the values specified in the other parameters of the ED-ADSL command. PROF is the AID DslProfAid.
XDSR0|Maximum Downstream Rate - Channel 0 (kbps). XDSR0 is of type DwnStreamRate.
MDSR0|Minimum Downstream Rate - Channel 0 (kbps). MDSR0 is of type DwnStreamRate.
XUSR0|Maximum Upstream Rate - Channel 0 (kbps). XUSR0 is of type UpStreamRate.
MUSR0|Minimum Upstream Rate - Channel 0 (kbps). MUSR0 is of type UpStreamRate.
XDSR1|Maximum Downstream Rate - Channel 1 (kbps). XDSR1 is of type DwnStreamRate.
MDSR1|Minimum Downstream Rate - Channel 1 (kbps). MDSR1 is of type DwnStreamRate.
XUSR1|Maximum Upstream Rate - Channel 1 (kbps). XUSR1 is of type UpStreamRate.
MUSR1|Minimum Upstream Rate - Channel 1 (kbps). MUSR1 is of type UpStreamRate.
DSEXR|Downstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. (Values in kbps) DSEXR is of type ExcessRate.
USEXR|Upstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. (Values in kbps) USEXR is of type ExcessRate.
TMDS|Target Downstream SNR Margin. This parameter specifies the desired downstream signal to noise ratio margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. Actual connection margins may be greater than or less than the desired target margin based on the configured maximum and minimum downstream bit rates. Higher connect margins will result when maximum configured data rates are lower than the maximum achievable data rates. Lower connect margins will result when the minimum configured data rate is not achievable at the desired margin. TMDS is of type SnrTargetMargins.
XMDS|Maximum Downstream SNR Margin. This parameter specifies the maximum downstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-C. It may not always be possible to reduce the actual connection margin for short loops and lower bit rate configuration. As a result, a connect margin greater than the specified maximum margin is possible. The maximum downstream SNR margin must be greater than the target downstream SNR margin. XMDS is of type SnrMaxMargins.
MMDS|Minimum Downstream SNR Margin. This parameter specifies the minimum downstream signal to noise ratio margin in dB. This margin specifies the minimum threshold allowed for modem operation. The connection will fail if the operating downstream margin falls below the specified minimum for more than 20 seconds and a modem retrain will be attempted. The minimum downstream margin must be less than the target downstream margin. MMDS is of type SnrMinMargins.
TMUS|Target Upstream SNR Margin. This parameter specifies the desired upstream signal to noise ratio (SNR) margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. Actual connection margins may be greater than or less than the desired target margin based on the configured maximum and minimum upstream bit rates. Higher connect margins will result when maximum configured data rates are lower than the maximum achievable data rates. Lower connect margins will result when the minimum configured data rate is not achievable at the desired margin. TMUS is of type SnrTargetMargins.
XMUS|Maximum Upstream SNR Margin. This parameter specifies the maximum upstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-R. It may not always be possible to reduce the actual connection margin for short loops and lower bit rate configuration. As a result, a connect margin greater than the specified maximum margin is possible. The maximum upstream SNR margin must be greater than the target upstream SNR margin. XMUS is of type SnrMaxMargins.
MMUS|Minimum Upstream SNR Margin. This parameter specifies the minimum upstream signal to noise ratio (SNR) margin in dB. This margin specifies the minimum threshold allowed for modem training. The connection will fail if the operating upstream margin falls below the specified minimum for more than 20 seconds. The minimum upstream margin must be less than the target upstream margin MMUS is of type SnrMinMargins.
DSLAT|Downstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. If either DSLAT or USLAT is set to AUTO, both will be set to AUTO in h/w. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. DSLAT is of type Latency.
USLAT|Upstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. If either DSLAT or USLAT is set to AUTO, both will be set to AUTO in h/w. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. USLAT is of type Latency.
TC|Trellis Coding. Enables trellis coding to improve the DSL system performance. Trellis coding is an encoding scheme for piggybacking bits onto the electrical signal on the twisted pair. TC is of type TrellisCoding.
RAMODEDS|Rate Adaptation MODE DownStream. RAMODEDS is of type RateAdaptationMode.
RAMODEUS|Rate Adaptation MODE UpStream. RAMODEUS is of type RateAdaptationMode.
RAUMDS|Rate Adaptation Upshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RAUMDS is of type SnrMaxMargins.
RADMDS|Rate Adaptation Downshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RADMDS is of type SnrMaxMargins.
RAUTDS|Rate Adaptation Upshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RAUTDS is of type RateAdaptationMarginSeconds.
RADTDS|Rate Adaptation Downshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RADTDS is of type RateAdaptationMarginSeconds.
RAUMUS|Rate Adaptation Upshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RAUMUS is of type SnrMaxMargins.
RADMUS|Rate Adaptation Downshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RADMUS is of type SnrMaxMargins.
RAUTUS|Rate Adaptation Upshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RAUTUS is of type RateAdaptationMarginSeconds.
RADTUS|Rate Adaptation Downshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RADTUS is of type RateAdaptationMarginSeconds.
AHC|Compression of the ATM header results to improve throughput. AHC is of type BoolYN.
PMMODE|Power Management MODE. PMMODE is of type AdslPowerMgmtStates.
L0TIME|Minimum L0 Time interval between L2 exit and next L2 entry. (0-255 seconds) L0TIME is a Integer.
L2TIME|Minimum L2 time interval between L2 entry and first L2 trim. (0-255 seconds) L2TIME is a Integer.
L2ATPR|Maximum Aggregate Transmit Power Reduction per L2 trim. (dB) L2ATPR is of type SnrMaxMargins.
L2MINR|Minimum Data Rate in Low Power Mode (L2). This parameter specifies the minimum net data rate (in Kbps) during the low power state. If the actual user data rate is lower than L2MINR, raw cells will be injected to maintain the provisioned value. The value can range from 256 to 1024 Kbps. L2MINR is a Integer.
L2EXITR|L2 Exit Rate Threshold. This parameter specifies the downstream datarate threshold (in Kbps), which triggers exit from low power state (L2). The value ranges between 1 and 1024, and must be less than L2MINR. L2EXITR is a Integer.
L2ENTRYR|L2 Entry Rate Threshold. This parameter specifies the downstream data rate threshold (in Kbps), which triggers autonomous entry into low power state (L2). The value can range from 1 to 1024, and must be less or equal to L2EXITR. L2ENTRYR is a Integer.
L2ENTRYT|L2 Entry Time Threshold. This parameter specifies minimum interval of time (in seconds) that the net data rate should stay below L2ENTRYR before autonomous entry into low power state (L2). The value can range from 900 to 65535 seconds. L2ENTRYT is a Integer.
DSST|DownStream Start Tone index. DSST must be less than or equal to DSET. DSST is a Integer.
DSET|DownStream End Tone index. DSET must be greater than or equal to DSST. DSET is a Integer.
USST|UpStream Start Tone index. USST must be less than or equal USET. USST is a Integer.
USET|UpStream End Tone index. USET must be greater than or equal to USST. USET is a Integer.
GOS|Grade of service. This identifies the ADSL grade of service for performance monitoring (PM) which will be applied to the ADSL port. GOS is the AID GosAid.
MININPDS|The Downstream Minimum Impulse Noise Protection. MININPDS is of type SymbolProtection.
MININPUS|The Upstream Minimum Impulse Noise Protection. MININPUS is of type SymbolProtection.
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the port. Note that RMV/RST are reported upon every modem retrain and can clutter the event logs if enabled. REPTRMVRST is of type BoolYN.
INCL|INCLusive. INCL is of type BoolYN. The default value is "N".
ENABLENOTCH|Enable notching for adsl. ENABLENOTCH is of type BoolYN.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-ADV-PW:[TID]:<PwAid>:[CTAG]:::[[PYLDS=<PYLDS>,][PKTSINSYN=<PKTSINSYN>,][PKTSOUTSYN=<PKTSOUTSYN>,][HOLDOFF=<HOLDOFF>,][FILLP=<FILLP>,][FILL=<FILL>,][RTPPTTX=<RTPPTTX>,][RTPPTRX=<RTPPTRX>,][SSRCTX=<SSRCTX>,][SSRCRX=<SSRCRX>]]; ```

##### Parameters
Attribute | Description
|---
PwAid|PW Aid pattern. PwAid is the AID PwAid.
PYLDS|Selecting Yes means suppression is allowed. Payload MAY be omitted in order to conserve bandwidth. Otherwise, no suppression under any condition. PYLDS is of type BoolYN.
PKTSINSYN|The number of packets required to exit the LOPS state. PKTSINSYN is of type PktsInSyn.
PKTSOUTSYN|The number of consecutive packets missed required to enter LOPS state. PKTSOUTSYN is of type PktsOutSyn.
HOLDOFF|Hold-off timer to declare PW down when a PW is setup (refer RFC5604). HOLDOFF is of type NonNegativeInteger.
FILLP|Policy to be applied when the CE-bound Jitter buffer is overflow/ underflow for any reason. FILLP is of type TdmFillPolicy.
FILL|User Defined Fill Pattern to be used towards the T1 port. FILL is of type FillerRange.
RTPPTTX|RTP Payload type to be used to transmit and received PW packets. RTPPTTX is of type RtpPayloadType.
RTPPTRX|RTP Payload expected to be received from the far-end PW.For Ont PWE3, Calix ONT only accepts RTPPTRX=0. RTPPTRX is of type RtpPayloadType.
SSRCTX|SSRC value to be transmitted on towards PSN. For Ont PWE3, Calix ONT uses hard-coded 100. SSRCTX is of type NonNegativeInteger.
SSRCRX|SSRC value expected to be received at the near-end. It's not applicable for ONT PW. SSRCRX is of type NonNegativeInteger.

##### Syntax: ```ED-ADV-XDSL:[TID]:<DslAid>:[CTAG]:::[[PTMOVER=<PTMOVER>,][RAMODEDS=<RAMODEDS>,][RAMODEUS=<RAMODEUS>,][RAUMDS=<RAUMDS>,][RADMDS=<RADMDS>,][RAUTDS=<RAUTDS>,][RADTDS=<RADTDS>,][RAUMUS=<RAUMUS>,][RADMUS=<RADMUS>,][RAUTUS=<RAUTUS>,][RADTUS=<RADTUS>,][AHC=<AHC>,][EINP=<EINP>,][PMMODE=<PMMODE>,][L0TIME=<L0TIME>,][L2TIME=<L2TIME>,][L2ATPR=<L2ATPR>,][L2MINR=<L2MINR>,][L2ENTRYT=<L2ENTRYT>,][PHYRUS=<PHYRUS>,][PHYRDS=<PHYRDS>]]; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DslAid is the AID TwentyFourPortLuAid.
PTMOVER|This parameter overrides the default encapsulation selection and forces the line to use PTM encapsulation regardless of mode. PTMOVER is of type BoolYN. The default value is "N".
RAMODEDS|The Rate Adaptation Mode for Downstream. RAMODEDS is of type RateAdaptationMode. The default value is "INIT".
RAMODEUS|The Rate Adaptation Mode for Upstream. RAMODEUS is of type RateAdaptationMode. The default value is "INIT".
RAUMDS|The Rate Adaptation Upshift Margin Downstream in dB. RAUMDS is of type SnrMaxMargins. The default value is "9".
RADMDS|The Rate Adaptation Downshift Margin Downstream in dB. RADMDS is of type SnrMaxMargins. The default value is "3".
RAUTDS|The Rate Adaptation Upshift Time Downstream in seconds. RAUTDS is of type RateAdaptationMarginSeconds. The default value is "60".
RADTDS|The Rate Adaptation Downshift Time Downstream in seconds. RADTDS is of type RateAdaptationMarginSeconds. The default value is "60".
RAUMUS|The Rate Adaptation Upshift Margin Upstream in dB. RAUMUS is of type SnrMaxMargins. The default value is "9".
RADMUS|The Rate Adaptation Downshift Margin Upstream in dB. RADMUS is of type SnrMaxMargins. The default value is "3".
RAUTUS|The Rate Adaptation Upshift Time Upstream in seconds. RAUTUS is of type RateAdaptationMarginSeconds. The default value is "60".
RADTUS|The Rate Adaptation Downshift Time Upstream in seconds. RADTUS is of type RateAdaptationMarginSeconds. The default value is "60".
AHC|Compression of the ATM header results to improve throughput. AHC is of type BoolYN. The default value is "N".
EINP|This allows the caller to enable enhanced impulse noise protection. Several technology specific mechanisms are supported. EINP is of type INPType.
PMMODE|Power Management Mode. PMMODE is of type AdslPowerMgmtStates. The default value is "L0".
L0TIME|The Minimum L0 Time interval between L2 exit and next L2 entry. Units are seconds. L0TIME is a Integer.
L2TIME|The Minimum L2 time interval between L2 entry and first L2 trim. Units are seconds. L2TIME is a Integer.
L2ATPR|Maximum Aggregate Transmit Power Reduction per L2 trim in dB. L2ATPR is of type SnrMaxMargins.
L2MINR|The Minimum Data Rate in Low Power Mode specifies the minimum net data rate (in Kbps) during the low power state. L2MINR is a Integer. The default value is "1024".
L2ENTRYT|This is the minimum number of consecutive seconds that the line rate must be at or below L2MINR in order to trigger a transition into L2. L2ENTRYT is a Integer. The default value is "1800".
PHYRUS|PhyR Upstream. PHYRUS is of type BoolYN. The default value is "N".
PHYRDS|PhyR Downstream. PHYRDS is of type BoolYN. The default value is "N".

##### Syntax: ```ED-AP:[TID]:<ApAid>:[CTAG]:::[[ATMMAP=<ATMMAP>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][PDOM=<PDOM>,][GOS=<GOS>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid.
ATMMAP|When payload signal is a form that may be altered at the ATM Resource port, this parameter specifies the mapping. ATMMAP is of type AtmMap.
PYLDSCRM|This parameter is set to Y to enable the scrambling of ATM cells. It is only applicable when ATMMAP is UNI or NNI. PYLDSCRM is of type BoolYN.
ATMMON|This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to NNI and UNI interfaces ATMMON is of type BoolYN.
PDOM|Protection Domain. This is an integer that is used to associate a transport facility into a protection domain that is used for A to Z connection provisioning. The PDOM for each domain must be a unique non-zero integer. The value of 0 is reserved to indicate that the facility is not to be used for A to Z connections PDOM is of type Pdom.
GOS|Grade of Service. This identifies the AP grade of service for performance monitoring (PM) which will be applied to the AP port. GOS is the AID GosAid.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-ARP:[TID]:<RTRAID>:[CTAG]:::[AGE=<AGE>]; ```

##### Parameters
Attribute | Description
|---
RTRAID|RTRAID is the AID RouterAid.
AGE|ARP age time in seconds. Allow user to adjust ARP aging of routes. AGE is of type ArpAgeRange.

##### Syntax: ```ED-AVO:[TID]:<OntPortAid>:[CTAG]:::[[OMI=<OMI>,][RFRTRN=<RFRTRN>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Analog Video Overlay Port Access Identifer. The address of the AVO port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortAid.
OMI|The per-channel Optical Modulation Index of the RF-Video content that is being carried in the Analog Video Overlay signal. This parameter is only applied to ONTs that return an OMI value during initialization.
The value is a percentage, and must be between 3.2 and 3.8 (%). OMI is a String.

RFRTRN|This will directly control the operation of the RF-Return function of the ONT, instead of enabling RF-Return only when RF-Video services are enabled. RFRTRN is of type RfRtrnAdminState.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-BWC:[TID]:<BwcAid>:[CTAG]:::DESC=<DESC>; ```

##### Parameters
Attribute | Description
|---
BwcAid|Bandwidth Constraint Access Identifier. Identifier of the Bandwidth Constraint to be operated upon. BwcAid is the AID BwcProvAid.
DESC|DESCription. A user-settable description field for the contraint, up to 31 characters. DESC is a String.

##### Syntax: ```ED-BWCLINK:[TID]:<LinkBwcAid>:[CTAG]:::[[RXLMT=<RXLMT>,][RXNTFY=<RXNTFY>,][TXLMT=<TXLMT>,][TXNTFY=<TXNTFY>]]; ```

##### Parameters
Attribute | Description
|---
LinkBwcAid|Link Bandwidth Constraint Access Identifier. Identifies the Link Bandwidth Constraint to be operated upon. LinkBwcAid is the AID LinkBwcAid.
RXLMT|Receive Limit. Bandwidth reserved for the constraint in the ingress or receive direction on the link in kbps. RXLMT is a Integer.
RXNTFY|Receive Notification Threshold. This parameter sets the percent threshold at which the RXBWNTFY condition is raised. This condition indicates that bandwidth usage for the constraint in the receive direction exceeds this value. If this is set to OFF, no condition is raised. RXNTFY is of type BwcNtfyThrRange.
TXLMT|Transmit Limit. Bandwidth reserved for the constraint in the egress or transmit direction on the link in kbps. TXLMT is a Integer.
TXNTFY|Transmit Notification Threshold. This parameter sets the percent threshold at which the TXBWNTFY condition is raised. This condition indicates that bandwidth usage for the constraint in the receive direction exceeds this value. If this is set to OFF, no condition is raised. TXNTFY is of type BwcNtfyThrRange.

##### Syntax: ```ED-CFG-ONT:[TID]:<CfgAid>:[CTAG]:::[STATUS=<STATUS>]; ```

##### Parameters
Attribute | Description
|---
CfgAid|Aid of ONT configuration file. CfgAid is the AID CfgAid.
STATUS|Status of instance. STATUS is of type CFGONTEDSTAT.

##### Syntax: ```ED-CRS-<STSN>:[TID]:<SrcStsAid>,<DstStsAid>:[CTAG]:::[[DROP=<DROP>,][DLTDROP=<DLTDROP>]]; ```

##### Parameters
Attribute | Description
|---
SrcStsAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being edited. SrcStsAid is the AID StsCrsAid.
DstStsAid|Destination (To) Access Identifier. This identifies address of the destination (to) endpoint of the cross-connect being modified. It does NOT indicate a new destination for the source identified. DstStsAid is the AID StsCrsAid.
DROP|Drop Location. This parameter indicates the location where the cross-connect is to be dropped along the path to the endpoint. This is used in drop-and-continue applications. DROP is the AID StsCrsAid.
DLTDROP|Delete Drop Location. This parameter indicates the location where the cross-connect is no longer to be dropped along the path to the endpoint. This is used to delete a drop in drop-and-continue applications. DLTDROP is the AID StsCrsAid.

##### Syntax: ```ED-CRS-VC:[TID]:<SrcVcAid>,<DstVcAid>:[CTAG]:::[[DROP=<DROP>,][DROPPPL=<DROPPPL>,][DLTDROP=<DLTDROP>,][INTERNAL=<INTERNAL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVcAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being edited. SrcVcAid is the AID VcId18.
DstVcAid|Destination (To) Access Identifier. This identifies address of the destination (to) endpoint of the cross-connect being modified. It does NOT indicate a new destination for the source identified. DstVcAid is the AID VcId18.
DROP|DROP location. This parameter indicates the location where the cross-connect is to be dropped along the path to the endpoint. This is used in drop-and-continue applications. DROP is the AID VcId3.
DROPPPL|Drop Path Protection Label. This parameter indicates the PPL association for the cross-connect drop end-point being added, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. DROPPPL is the AID PplId1.
DLTDROP|DeLeTe DROP location. This parameter indicates the location where the cross-connect is no longer to be dropped along the path to the endpoint. This is used to delete a drop in drop-and-continue applications. DLTDROP is the AID VcId3.
INTERNAL|Internal Cross Connects. If present, this parameter specifies the editing of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. The default value is "NONE".

##### Syntax: ```ED-CRS-VIDVC:[TID]:<SrcVcAid>,<DstVcAid>:[CTAG]:::IRCAID=<IrcAid>,[[ARP=<ARP>,][PARP=<PARP>,][DROP=<DROP>,][DROPPPL=<DROPPPL>,][DLTDROP=<DLTDROP>,][INTERNAL=<INTERNAL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVcAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being edited. SrcVcAid is the AID VidvcId2.
DstVcAid|Destination (To) Access Identifier. This identifies address of the destination (to) endpoint of the cross-connect being modified. It does NOT indicate a new destination for the source identified. DstVcAid is the AID VidvcId2.
IrcAid|The slot address of the IRC. IrcAid is the AID SlotLuAid.
ARP|ARP Enabled. This option is only valid on VCs with a traffic profile containing the IP application ID. If set to Y, the IRC will answer ARP requests on this VC, thus creating dynamic ARP entries. ARP is of type BoolYN.
PARP|Proxy ARP Enabled. This option is only valid on VCs with a traffic profile containing the IP application ID. PARP is of type BoolYN.
DROP|DROP location. This parameter indicates the location where the cross-connect is to be dropped along the path to the endpoint. This is used in drop-and-continue applications. DROP is the AID VidvcId.
DROPPPL|Drop Path Protection Label. This parameter indicates the PPL association for the cross-connect drop end-point being added, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. DROPPPL is the AID PplId1.
DLTDROP|DeLeTe DROP location. This parameter indicates the location where the cross-connect is no longer to be dropped along the path to the endpoint. This is used to delete a drop in drop-and-continue applications. DLTDROP is the AID VidvcId.
INTERNAL|Internal Cross Connects. If present, this parameter specifies the editing of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. The default value is "NONE".

##### Syntax: ```ED-CRS-VP:[TID]:<SrcVpAid>,<DstVpAid>:[CTAG]:::[[DROP=<DROP>,][DLTDROP=<DLTDROP>,][DROPPPL=<DROPPPL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVpAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being edited. SrcVpAid is the AID VpAid.
DstVpAid|Destination (To) Access Identifier. This identifies address of the destination (to) endpoint of the cross-connect being modified. It does NOT indicate a new destination for the source identified. DstVpAid is the AID VpAid.
DROP|DROP location. This parameter indicates the location where the cross-connect is to be dropped along the path to the endpoint. This is used in drop-and-continue applications. DROP is the AID VpAid.
DLTDROP|DeLeTe DROP location. This parameter indicates the location where the cross-connect is no longer to be dropped along the path to the endpoint. This is used to delete a drop in drop-and-continue applications. DLTDROP is the AID VpAid.
DROPPPL|Drop Path Protection Label. This parameter indicates the PPL association for the cross-connect drop end-point being added, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. DROPPPL is the AID PplId1.

##### Syntax: ```ED-CVIDREG:[TID]:<CVidRegAid>:[CTAG]:::[PRIO=<PRIO>]; ```

##### Parameters
Attribute | Description
|---
CVidRegAid|CVID Registration Table Entry Access Identifier. CVidRegAid is the AID CVidRegAid.
PRIO|802.1q Priority Bits Policy. PRIO is of type PrioBits.

##### Syntax: ```ED-DAT:[TID]::[CTAG]::[<DATE>],[<TIME>]; ```

##### Parameters
Attribute | Description
|---
DATE|Date. Change the date of the C7 network to this value. DATE is the current date in a format of: [YY(YY)-]MM-DD, where YY is the last two digits of the year ranging from 00 to 99 (or YYYY is the full 4-digit representation of the current year; ``` either format is acceptable), MM is the month of the year ranging from 01 to 12, and DD is the day of the month ranging from 01 to 31. If the year is omitted, it is interpreted as YY=0. DATE is a Date.
TIME|Time. Change the time of the C7 network to this value. The time format is: HH-MM[-SS] where HH is the hour in a 24 hour format ranging from 00 to 23, MM is the minute ranging from 00 to 59, and SS is the second ranging from 00 to 59. If seconds are omitted, it is interpreted as SS=0. TIME is a Time.

##### Syntax: ```ED-DHCPSVR:[TID]:<IP>:[CTAG]:::[[RTRAID=<RTRAID>,][OPTION82=<OPTION82>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP Address of the DHCP Server. This is must match an existing DHCP Server address IP is the AID IpAid.
RTRAID|RTRAID is the AID RouterAid.
OPTION82|DHCP Option 82 - This feature adds a unique identifier in the relay agent information option. OPTION82 is of type Option82.

##### Syntax: ```ED-DLPROF:[TID]:<DLProfileAid>:[CTAG]:::[[MAXIFRAME=<MAXIFRAME>,][N200=<N200>,][T200=<T200>,][T203=<T203>]]; ```

##### Parameters
Attribute | Description
|---
DLProfileAid|Data Link Profile Access Identifier. The address of the GR-303 data link profile entity. DLProfileAid is the AID DLProfileAid.
MAXIFRAME|Maximum Information Frames. This specifies the maximum number of information (I) frames that may be outstanding at Layer 2 using LAPD. MAXIFRAME is of type MaxIFrames.
N200|N200. This specifies the maximum number of retransmissions for a frame at Layer 2 using LAPD. N200 is of type N200.
T200|T200. This specifies the maximum length of time in milliseconds that a data link layer entity will wait for acknowledgement of a transmitted frame. T200 is of type T200.
T203|T203. This specifies the maximum time in seconds that a data link is allowed to remain idle before verifying the path between the IDT and the RDT. T203 is of type T203.

##### Syntax: ```ED-EC1:[TID]:<Ec1tAid>:[CTAG]:::[[FEPM=<FEPM>,][ALMPROF=<ALMPROF>,][SDBER=<SDBER>,][SFBER=<SFBER>,][GOS=<GOS>,][LBO=<LBO>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
Ec1tAid|Access Identifier. The address of the EC1 for which the parameters are being modified. Ec1tAid is the AID TwelvePortLuAid.
FEPM|Far End Performance Monitoring. When this parameter is set to "N", the Far End Performance Monitoring data is not collected. When retrieving Far End PM, the Monitored Values (MONVAL) field will contain '0' and the Validity (VLDTY) field will contain 'INVLD'. When this parameter is set to "Y", data collection for Far End Performance Monitoring is enabled. The default value is "N". FEPM is of type BoolYN.
ALMPROF|Alarm Profile. The set of alarm Notification codes to be associated with this entity. ALMPROF is the AID AlmProfileAid.
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD.
SFBER|Signal Failed Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Failed Signal. Only values of 3 and 4 are valid for EC1. SFBER is of type BitErrorRateSF.
GOS|Grade of service. This identifies the EC1 grade of service for performance monitoring (PM) which is applied to the EC1 port. GOS is the AID GosAid.
LBO|Line Build Out. LBO is a Integer.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-EOAM-CFG:[TID]::[CTAG]:::[[OAMENABLED=<OAMENABLED>,][SENDERID=<SENDERID>,][CCSENDERID=<CCSENDERID>,][CCPORTSTATUS=<CCPORTSTATUS>,][CCIFSTATUS=<CCIFSTATUS>,][LBSENDERID=<LBSENDERID>,][LBDATASTATUS=<LBDATASTATUS>,][LTSENDERID=<LTSENDERID>]]; ```

##### Parameters
Attribute | Description
|---
OAMENABLED|OAMENABLED is of type BoolYN.
SENDERID|SENDERID is of type EthOamSenderId.
CCSENDERID|CCSENDERID is of type BoolYN. The default value is "Y".
CCPORTSTATUS|CCPORTSTATUS is of type BoolYN. The default value is "N".
CCIFSTATUS|CCIFSTATUS is of type BoolYN. The default value is "N".
LBSENDERID|LBSENDERID is of type BoolYN. The default value is "Y".
LBDATASTATUS|LBDATASTATUS is of type BoolYN. The default value is "N".
LTSENDERID|LTSENDERID is of type BoolYN. The default value is "Y".

##### Syntax: ```ED-EOAM-FMP:[TID]:<FMPAID>:[CTAG]:::[[FRMSIZE=<FRMSIZE>,][DELAYRATE=<DELAYRATE>,][LOSSRATE=<LOSSRATE>,][LOSSMEASTYPE=<LOSSMEASTYPE>,][LOSSFRMTYPE=<LOSSFRMTYPE>]]; ```

##### Parameters
Attribute | Description
|---
FMPAID|FMPAID is the AID EthOamFmpOrDfltAid.
FRMSIZE|FRMSIZE is a Integer.
DELAYRATE|DELAYRATE is of type EthOamFmpSamplePeriod.
LOSSRATE|LOSSRATE is of type EthOamFmpSamplePeriod.
LOSSMEASTYPE|LOSSMEASTYPE is of type EthOamLossMsType.
LOSSFRMTYPE|LOSSFRMTYPE is of type EthOamLossFrameType.

##### Syntax: ```ED-EOAM-MEG:[TID]:<MEGAID>:[CTAG]:::[[CCMINT=<CCMINT>,][AUTODISC=<AUTODISC>,][AUTODISCTMO=<AUTODISCTMO>,][MINCCDEFECT=<MINCCDEFECT>,][ALMTIME=<ALMTIME>,][ALMCLRTIME=<ALMCLRTIME>]]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid.
CCMINT|CCMINT is of type CcmInterval.
AUTODISC|AUTODISC is of type BoolYN.
AUTODISCTMO|AUTODISCTMO is of type ThrityFiveTo100.
MINCCDEFECT|MINCCDEFECT is of type MinCcDefect.
ALMTIME|ALMTIME is of type AlmTimeRng.
ALMCLRTIME|ALMCLRTIME is of type AlmClrTimeRng.

##### Syntax: ```ED-EOAM-MEP:[TID]:<MEPAID>:[CTAG]:::[[IFAID=<IFAID>,][DIRN=<DIRN>,][CONTCHK=<CONTCHK>,][CCMLTMPRIO=<CCMLTMPRIO>,][FRMMEASPROF=<FRMMEASPRIO>,][DLYLOSSMAC=<DLYLOSSMAC>,][DLYMEASUREMENT=<DLYMEASUREMENT>,][LOSSMEASUREMENT=<LOSSMEASUREMENT>,][CFGPST=<CFGPST>,][CFGSST=<CFGSST>]]; ```

##### Parameters
Attribute | Description
|---
MEPAID|MEPAID is the AID EthOamMepAid.
IFAID|IFAID is the AID MepId1.
DIRN|DIRN is of type MepDirn.
CONTCHK|CONTCHK is of type BoolYN.
CCMLTMPRIO|CCMLTMPRIO is of type CcmLtmPrio.
FRMMEASPRIO|FRMMEASPRIO is the AID FrmMeasProf.
DLYLOSSMAC|DLYLOSSMAC is the AID MacAid.
DLYMEASUREMENT|DLYMEASUREMENT is of type BoolYN.
LOSSMEASUREMENT|LOSSMEASUREMENT is of type BoolYN.
CFGPST|CFGPST is of type PrimaryStateChg.
CFGSST|CFGSST is of type SecondaryState.

##### Syntax: ```ED-EOAM-MIP:[TID]:<MIPAID>:[CTAG]:::[[MEGAID=<MEGAID>,][MIPENABLED=<MIPENABLED>]]; ```

##### Parameters
Attribute | Description
|---
MIPAID|MIPAID is the AID OntPortAid.
MEGAID|MEGAID is the AID MegAid.
MIPENABLED|MIPENABLED is of type BoolYN.

##### Syntax: ```ED-EQPT:[TID]:<EqptAid>:[CTAG]::[<TYPE>]:[[PROTN=<PROTN>,][RVRTV=<RVRTV>,][RNPRTY=<RNPRTY>,][PWR=<PWR>,][LINERATE=<LINERATE>,][IMAIDLECELL=<IMAIDLECELL>,][UBRBWRES=<UBRBWRES>,][DBA=<DBA>,][ECCONFIG=<ECCONFIG>,][BANDPLAN=<BANDPLAN>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the Equipment entity being modified. EqptAid is the AID EquipmentId.
TYPE|Equipment Type. This parameter identifies the type of equipment which can be plugged into the slot. The provisioned equipment type must be the exact equipment card type. Examples of card types are RPOTS-24, OC12-4-IR, etc. Note that if the equipment has provisioned services, the following conditions must be met in order to change the provisioned equipment type: 1) the equipment must be in either the MEA or UEQ state. In other words, the card must be physically changed before changing it's provisioned value. 2) Only the conversions given in the table above are permitted by the system. 3) The card is not the active RAP. TYPE is of type EqptTypeProv.
PROTN|Protection Unit Access Identifier. This is the address of the equipment which is to provide protection for this card. If the equipment being modified is to provide protection for other cards in the system, then PROTN should be specified as the equipment's own address. The equipment providing protection must be provisioned before the equipments that use it as their protection. This is an optional parameter on the ED-EQPT command and the value will not change if not provided. NONE should be specified to disable an existing protection configuration. PROTN is the AID EquipmentId6.
RVRTV|Revertive. This parameter indicates if the protection requested is to be revertive or non-revertive. The parameter value can be either Y = revertive or N = non-revertive. This parameter is only applicable in a 1:1 protection scheme. In a 1:n protection scheme, the equipment protection is always revertive. RAP cards are always non-revertive and cannot be provisioned to be revertive. This is an optional parameter on the ED-EQPT command and the value will not change if not provided. This parameter is only applicable if this is the protection card unit. It is not provided when this is the protected card. RVRTV is of type BoolYN.
RNPRTY|Redundancy Priority. This parameter only applies in a 1:n protection scheme. It gives the priority of this working equipment versus other working equipment protected by the same protection card. Equipment given a smaller RNPRTY number will pre-empt any protection already in effect for equipment given a larger RNPRTY number. When equipment fails with the same RNPRTY number as the already protected equipment, no protection switch will occur. RNPRTY is of type ProtnPriority.
PWR|Power Category. The system shall minimize the power dissipation during power failure (battery backup). Following power failure the system needs to enter a power-save mode. Upon entering this mode, the C7 turns off the DSL cards. The period in which the system enters power-save mode after a power failure shall be a user provisionable interval. To accomplish this task three power categories are created: Category 1 that do not get shut down during battery back up (AC power failure). Category 2 cards that get shut down after 2 hours. Category 3 card that get shut down after the period of time specified by PWRCAT3 (up to a maximum of 30 minutes - see ED-SHELF). The system defaults are that POTS, DS1, DS3, and optics are category 1 and ADSL are category 3. Presently, no Category 2 cards are supported. PWR is of type PowerCategory.
LINERATE|Line Rate. This parameter only applies when provisioning RAP-OC cards. This is the configurable line speed of the equipment. When decreasing the linerate, there can be no STS provisioned outside the acceptable range of the new rate. As well, the current packet bandwidth used by the port must not exceed the new maximum bandwidth. NOTE: The card will reboot if this parameter is changed when it has provisioned services! LINERATE is of type LineRate.
IMAIDLECELL|This indicates how IMA idle cells will be transmitted by all IMA groups on this card. IMAIDLECELL is of type ImaIdleCellType.
UBRBWRES|UBR BandWidth REServed. Amount of backplane bandwidth reserved for UBR bandwidth by user in kbps. This parameter takes value of zero and values greater than or equal to 128 kbps in increments of 128. This is a restricted parameter and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. UBRBWRES is a Integer. The default value is "0". UBRBWRES is a Integer.
DBA|Enable/Disable Dynamic Bandwidth Allocation on all PONs on the OLTG card. Applicable to OLTG card only. DBA is of type BoolYN.
ECCONFIG|Indicates the type of echo cancellation filtering to be used on all VSPs or VSD1s on the equipment. This parameter is only applicable to VGP and VIPR line units. ECCONFIG is of type EqptEcConfig.
BANDPLAN|This parameter only applies when provisioning COMBO2-24V or VDSL2-24 cards. It selects which VDSL2 profiles are available for provisioning. When set to �3BAND�, 8a, 8b, 8c and 8d profiles are available for provisioning each of 24 ports. BANDPLAN set to �5BAND� extends the available profile selection to 8a, 8b, 8c, 8d, 12a, 12b and 17a but limits usable ports to 12. BANDPLAN is of type BandPlan.
PST|Primary Service State. This is the service state which the user wants the equipment to transition into. The equipment can be put into service or out of service with the ED-EQPT command. PST is of type PrimaryStateChg.

##### Syntax: ```ED-ERPS:[TID]:<ErpsAid>:[CTAG]:::[[PRIM=<PRIM>,][SEC=<SEC>,][CVLAN=<CVLAN>,][HMF=<HMF>,][RMF=<RMF>,][ISMASTER=<ISMASTER>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsAid.
PRIM|The primary interface for this ERPS domain. If the domain is of role 'MASTER', then this is the primary interface. Otherwise, it is just one of the 2 interfaces. The only modification allowed to PRIM and SEC is to interchange the two assignments. PRIM is the AID RapEthPortAid.
SEC|This is the secondary interface for this ERPS domain. If the domain is of role 'MASTER', then this is the secondary interface. Otherwise, it is just one of the 2 interfaces. The only modification allowed to PRIM and SEC is to interchange the two assignments. SEC is the AID RapEthPortAid.
CVLAN|This is the VLAN on which the control messages will be sent. This VLAN will be reserved from the VLAN pool and unavailable for use. CVLAN is the AID ErpsVlanIndexAid.
HMF|The frequency (in seconds) at which health messages will be sent. The valid range is 1-10. HMF is a Integer.
RMF|The frequency (in seconds) at which recover messages are sent. The valid range is 1-10. RMF is a Integer.
ISMASTER|Indicate this is master or not. ISMASTER is of type BoolYN.
DESC|The name of the ERPS domain. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-ETH:[TID]:<EthPortAid>:[CTAG]:::[[SPD=<SPD>,][DPLX=<DPLX>,][TAGGED=<TAGGED>,][MTU=<MTU>,][POLICE=<POLICE>,][LSREN=<LSREN>,][VIDTXMODE=<VIDTXMODE>,][ENONBAT=<EONBAT>,][GOS=<GOS>,][AHDISCENABLE=<AHDISCENABLE>,][AHLPBKACCEPT=<AHLPBKACCEPT>,][PRIO=<PRIO>,][LACPTMOUT=<LACPTMOUT>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Access Identifier. EthPortAid is the AID EthId.
SPD|Speed. SPD is of type Speed.
DPLX|Duplex. DPLX is of type Duplex.
TAGGED|Tagged. TAGGED is of type BoolYN.
MTU|Max Transmission Unit. Varies by equipment type. GE-2P/EGW: must be 2048. RAP10 : must be within [1518,9022], default 2048. GE-4S and FE-12S: must be within [1518, 9022], default 1522. ONT: MTU is not settable. (For ONT ETH ports, MTU can be retrieved with RTRV-STAT-ETH) MTU is of type Mtu.
POLICE|Policing. POLICE is of type BoolYN.
LSREN|LaSeR ENable - Laser On/Off. Applies to GE ports only. LSREN is of type BoolYN.
VIDTXMODE|For ONT ports, allows conversion of multicast video streams to unicast streams to the specific Set Top Boxes that have joined the associated stream. VIDTXMODE is of type OntEthVidTxMode.
EONBAT|For ONT ports, this parameter specifies the behavior the port when the ONT is running on battery backup, and overrides the default (ONTETHONBAT) specified by ED-SYS. EONBAT is of type OntPortPwrOpt.
GOS|GOS is the AID GosAid.
AHDISCENABLE|AHDISCENABLE is of type BoolYN.
AHLPBKACCEPT|AHLPBKACCEPT is of type BoolYN.
PRIO|Lacp Priority. Only effective for cross-card LinkAgg. PRIO is of type One264K.
LACPTMOUT|Timeout for LACP when operating in Protection mode. LACPTMOUT is of type LacpTmout.
DESC|DESCription. A user-settable description field, up to 63 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-FFP-<OCN>:[TID]:<OcAid>:[CTAG]:::[[BDCST=<BDCST>,][PSDIRN=<PSDIRN>,][RVRTV=<RVRTV>,][PDIP=<PDIP>,][WTR=<WTR>,][APSOP=<APSOP>]]; ```

##### Parameters
Attribute | Description
|---
OcAid|OCn Access Identifier. The address of a port which is either the working or the protection unit in the facility protection group. OcAid is the AID FourPortLuAndRapAid.
BDCST|Broadcast. This parameter is set to Y if the signal is to be broadcast over the protected (main) and the protecting (protection) channels simultaneously for a 1+1 protection scheme. It is set to N if the signal is only to be sent over the active channel. BDCST is of type BoolYN.
PSDIRN|Protection Switch Direction. Specifies whether both directions of a bi-directional connection are to be switched together. PSDIRN is of type ProtnSwDirection.
RVRTV|Revertive. This parameter is set to Y if the traffic normally is to revert to working when the condition which triggered the switch to protection has cleared. This parameter is applicable in a 1:1 or 1+1 protection scheme. The parameter value can be either Y = revertive or N = non-revertive. RVRTV is of type BoolYN.
PDIP|Payload Defect Indication. This parameter indicates whether to switch on a PDI-P defect. This parameter is applicable only when MODE = CLOSED. PDIP is of type BoolYN.
WTR|Wait to Restore. The amount of time in minutes to wait before restoring a revertive protection switch. Does not apply to non-revertive protection switch. WTR is of type WaitToRestore.
APSOP|Automatic Protection Switch Operation. This parameter may be set to N to disable the execution of the Automatic Protection Switching (APS) protocol (processing of K-bytes). This option is useful for Ring Management when new Nodes are added/deleted in a BLSR which allows the ring maps to be updated for all the existing nodes in a ring. In the case of a Linear protection configuration, the addition/deletion of a new NE in an existing span will require that APS operation be temporarily turned off, while traffic re-configuration is in progress. NOTE: This parameter has been deprecated and will be ignored by the C7. APSOP is of type BoolYN.

##### Syntax: ```ED-FPACC:[TID]:<ShelfAid>:[CTAG]:::CHAP=<CHAP>; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the front panel is connected. ShelfAid is the AID ShelfAid.
CHAP|Channel Access Privileges. This parameter indicates the privileges for testing with the front panel. CHAP is of type CidAccess.

##### Syntax: ```ED-FTP:[TID]:<FTPAID>:[CTAG]:::[[FTPIP=<FTPIP>,][FTPUID=<FTPUID>,][FTPPID=<FTPPID>,][LOCN=<LOCN>]]; ```

##### Parameters
Attribute | Description
|---
FTPAID|FTP server AID. FTPAID is the AID FtpAid.
FTPIP|IP address of the FTP server. FTPIP is the AID IpAid.
FTPUID|User ID of the FTP server. FTPUID is a String.
FTPPID|Password on the FTP server. FTPPID is a String.
LOCN|Location of the C7 Gateway from which FTP functions will be performed. LOCN is the AID FtpGatewayAid.

##### Syntax: ```ED-GOS-<OCN>:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][UASL=<UASL>,][CVS=<CVS>,][ESS=<ESS>,][SESS=<SESS>,][SEFSS=<SEFSS>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the STS12 Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVL is of type CVThreshRange.
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 12 and for 1-DAY is 200. ESL is of type SecondsThreshRange.
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 3 and for 1-DAY is 7. SESL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 10. UASL is of type SecondsThreshRange.
CVS|Coding Violations Threshold Section. The threshold value for the coding violations for the section. This parameter does not apply to far end provisioning. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVS is of type CVThreshRange.
ESS|Errored Seconds Threshold Section. The threshold value for the errored seconds for the section. This parameter does not apply to far end provisioning. The default threshold for 15-MIN is 12 and for 1-DAY is 200. ESS is of type SecondsThreshRange.
SESS|Severely Errored Seconds Threshold Section. The threshold value for the severely errored seconds for the section. This parameter does not apply to far end provisioning. The default threshold for 15-MIN is 3 and for 1-DAY is 7. This parameter does not apply to far end provisioning. SESS is of type SecondsThreshRange.
SEFSS|Severely Errored Framing Seconds Threshold Section. The threshold value for the severely errored framing seconds for the section. This parameter does not apply to far end provisioning. Default threshold for 15-MIN interval and 1-DAY interval is 10 SEFSS is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-<STSN>:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SESP=<SESP>,][UASP=<UASP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the STS1 Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end PM registers are being edited. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. CVP is of type CVThreshRange.
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. ESP is of type SecondsThreshRange.
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. SESP is of type SecondsThreshRange.
UASP|Un-Available seconds path. This is the threshold value for the un-available seconds for the path. UASP is of type SecondsThreshRange.
PERUPE|Percent Utilization - Path, Egress. PERUPE is of type Percentage.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-ADSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVFL=<CVFL>,][CVIL=<CVIL>,][ECFL=<ECFL>,][ECIL=<ECIL>,][ECSL=<ECSL>,][ESL=<ESL>,][SESL=<SESL>,][UASL=<UASL>,][LOSSL=<LOSSL>,][PERU=<PERU>,][PERUE=<PERUE>,][LOSC=<LOSC>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the ADSL Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end PM registers are being edited. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVFL|Coding violations fast - line. The threshold value for the coding violations fast for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVFL is of type CVAdslThreshRange.
CVIL|Coding violations interleaved - line. The threshold value for the coding violations interleaved for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVIL is of type CVAdslThreshRange.
ECFL|Forward error correction count fast - line. The threshold value for the forward error correction count fast for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100 ECFL is of type ECThreshRange.
ECIL|Forward error correction count interleaved - line. The threshold value for the forward error correction count interleaved for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100 ECIL is of type ECThreshRange.
ECSL|Forward error correction count second - line. The threshold value for the forward error correction count second for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100 ECSL is of type SecondsThreshRange.
ESL|Errored seconds - line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESL is of type SecondsThreshRange.
SESL|Severely errored seconds - line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 65. UASL is of type SecondsThreshRange.
LOSSL|LOS Seconds Threshold Line. The threshold value for the LOS seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 10. LOSSL is of type SecondsThreshRange.
PERU|Percent Utilization, Ingress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERU is of type Percentage.
PERUE|Percent Utilization, Egress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERUE is of type Percentage.
LOSC|Loss of Signal Count (Near End only). This indicates the number of times a LOS condition was set, and also represents the number of modem retrains in the time period. The default threshold for 15-MIN is 3 and for 1-DAY is 10. LOSC is a Integer.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-AP:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[PERUP=<PERUP>,][PERUPE=<PERUPE>,][IVIMA=<IVIMA>,][OIFIMA=<OIFIMA>,][SESIMA=<SESIMA>,][UASIMA=<UASIMA>,][TXUUSIMA=<TXUUSIMA>,][RXUUSIMA=<RXUUSIMA>,][TXFC=<TXFC>,][RXFC=<RXFC>,][TXSTUFFIMA=<TXSTUFFIMA>,][RXSTUFFIMA=<RXSTUFFIMA>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
PERUP|Percent Utilization - Path, Ingress (Near End only). PERUP is of type Percentage.
PERUPE|Percent Utilization - Path, Egress (Near End only). PERUPE is of type Percentage.
IVIMA|ICP Violations. Count of errored, invalid, or missing ICP cells, except during seconds where a SES-IMA or UAS-IMA condition is reported (Near End only). IVIMA is of type SecondsThreshRange.
OIFIMA|Out of IMA Frame (Near End only). Count of OIF anomalies except during SES-IMA or UAS-IMA conditions. OIFIMA is of type SecondsThreshRange.
SESIMA|Severely Errored Seconds. Count of 1-second intervals containing >= 30% of the ICP cells counted as IV-IMAs, or one or more near-end link defects (facility, LIF, or LODS) during non-UAS-IMA intervals. The number of IV-IMA counts required to meet the 30% criteria will depend on the facility line rate and the IMA frame size (M). SESIMA is of type SecondsThreshRange.
UASIMA|Unavailable seconds at NE. The NE unavailability begins at the onset of 10 contiguous SES-IMA including the first 10 seconds to enter the UAS-IMA condition, and ends at the onset of 10 contiguous second with no SES-IMA, excluding the last 10 seconds to exit the UAS-IMA condition. UASIMA is of type SecondsThreshRange.
TXUUSIMA|Transit Unusable Seconds (Near End only). Count of Tx Unusable seconds at the Tx NE Link State Machine (LSM). TXUUSIMA is of type SecondsThreshRange.
RXUUSIMA|Receive Unusable Seconds (Near End only). Count of Rx Unusable seconds at the Rx NE LSM. RXUUSIMA is of type SecondsThreshRange.
TXFC|Transit Failure Count. Count of the number of NE Transmit Link failure alarm entrances. The possible NE Tx link failure alarm conditions are: Tx-Mis-Connected and Tx-Fault. TXFC is of type SecondsThreshRange.
RXFC|Receive Failure Count. Count of the number of NE Receive Link failure alarm entrances. The possible NE Rx link failure alarm conditions are: LIF, LODS, and Rx-Fault. RXFC is of type SecondsThreshRange.
TXSTUFFIMA|Transmit Stuff Events (Near End only). Count of stuff events inserted in the transmited direction. TXSTUFFIMA is of type ImaLinkStuff.
RXSTUFFIMA|Receive Stuff Events (Near End only). Count of stuff events inserted in the receive direction, except during SES-IMA and UAS-IMA conditions. RXSTUFFIMA is of type ImaLinkStuff.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-EC1:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][UASL=<UASL>,][CVS=<CVS>,][ESS=<ESS>,][SESS=<SESS>,][SEFSS=<SEFSS>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the EC1 Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line. CVL is of type CVThreshRange.
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. ESL is of type SecondsThreshRange.
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. SESL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. UASL is of type SecondsThreshRange.
CVS|Coding Violations Threshold Section. The threshold value for the coding violations for the section. This parameter does not apply to far end provisioning. CVS is of type CVThreshRange.
ESS|Errored Seconds Threshold Section. The threshold value for the errored seconds for the section. This parameter does not apply to far end provisioning. ESS is of type SecondsThreshRange.
SESS|Severely Errored Seconds Threshold Section. The threshold value for the severely errored seconds for the section. This parameter does not apply to far end provisioning. SESS is of type SecondsThreshRange.
SEFSS|Severely Errored Framing Seconds Threshold Section. The threshold value for the severely errored framing seconds for the section. This parameter does not apply to far end provisioning. SEFSS is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-ETH:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[FCSERROR=<FCSERROR>,][XSCOLL=<XSCOLL>,][LATECOLL=<LATECOLL>,][TOOLONG=<TOOLONG>,][INBUFOVFL=<INBUFOVFL>,][OUTBUFOVFL=<OUTBUFOVFL>,][SQETEST=<SQETEST>,][DEFERRED=<DEFERRED>,][ALIGNERR=<ALIGNERR>,][RXINTERR=<RXINTERR>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location and can be one of the following values: "NEND".
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
FCSERROR|FCS Error Counter. FCSERROR is a Integer.
XSCOLL|Excessive Collision Counter. XSCOLL is a Integer.
LATECOLL|Late Collision Counter. LATECOLL is a Integer.
TOOLONG|FrameTooLongs. TOOLONG is a Integer.
INBUFOVFL|Buffer Overflows on Receive. INBUFOVFL is a Integer.
OUTBUFOVFL|Buffer Overflows on Transmit. OUTBUFOVFL is a Integer.
SQETEST|SQE Counter. SQETEST is a Integer.
DEFERRED|Deferred Transmission Counter. DEFERRED is a Integer.
ALIGNERR|Alignment Error Counter. ALIGNERR is a Integer.
RXINTERR|Internal MAC Receive Error Counter. RXINTERR is a Integer.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-GRPXDSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[FC=<FC>,][MDSRFS=<MDSRFS>,][MUSRFS=<MUSRFS>,][PERU=<PERU>,][PERUE=<PERUE>,][UAS=<UAS>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the GRPXDSL Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end PM registers are being edited. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
FC|Failure Count FC is a Integer.
MDSRFS|Min Downstream Failure Seconds MDSRFS is of type SecondsThreshRange.
MUSRFS|Min Uptream Failure Seconds MUSRFS is of type SecondsThreshRange.
PERU|Percent Utilization, Ingress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERU is of type Percentage.
PERUE|Percent Utilization, Egress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERUE is of type Percentage.
UAS|Unavailable Seconds UAS is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-HDSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SESP=<SESP>,][CSSP=<CSSP>,][UASP=<UASP>,][CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][LOSWSL=<LOSWSL>,][UASL=<UASL>,][RTRN=<RTRN>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the DS1 Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end PM registers are being edited. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. The default threshold for 15-MIN is 13,296 and for 1-DAY is 132,960. CVP is of type CVThreshRange.
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESP is of type SecondsThreshRange.
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESP is of type SecondsThreshRange.
CSSP|Controlled Slip Seconds Path. The threshold value for the controlled slip seconds path. The default threshold for 15-MIN is 1 and for 1-DAY is 4. CSSP is of type SecondsThreshRange.
UASP|Unavailable Seconds Threshold Path. The threshold value for the unavailable seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 10. UASP is of type SecondsThreshRange.
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line (Near End only). The default threshold for 15-MIN is 13,340 and for 1-DAY is 133,400. CVL is of type CVThreshRange.
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line (Near End only). The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESL is of type SecondsThreshRange.
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line(Near End only). The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange.
LOSWSL|Loss of Sync Word Seconds Line (Near End). The default threshold for 15-MIN is 30 seconds and for 1-DAY is 120 seconds. LOSWSL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. The default threshold for 15-MIN is 60 seconds and for 1-DAY is 120 seconds. UASL is of type SecondsThreshRange.
RTRN|ReTRaiN count (Near End only). The threshold value for number of retrains on either loop (individually). The default threshold for 15-MIN is 3 retrains and for 1-DAY is 10 retrains RTRN is a Integer.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-IMA:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[GRFC=<GRFC>,][GRUASIMA=<GRUASIMA>,][PERUP=<PERUP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
GRFC|Group failure count. GRFC is of type SecondsThreshRange.
GRUASIMA|Count of seconds where IMA GTSM is down (Near End only). GRUASIMA is of type SecondsThreshRange.
PERUP|Percent Utilization - Path, Ingress (Near End only). PERUP is of type Percentage.
PERUPE|Percent Utilization - Path, Egress (Near End only). PERUPE is of type Percentage.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-IMALINK:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[IVIMA=<IVIMA>,][SESIMA=<SESIMA>,][UASIMA=<UASIMA>,][TXUUSIMA=<TXUUSIMA>,][RXUUSIMA=<RXUUSIMA>,][TXFC=<TXFC>,][RXFC=<RXFC>,][TXSTUFFIMA=<TXSTUFFIMA>,][RXSTUFFIMA=<RXSTUFFIMA>,][OIFIMA=<OIFIMA>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Link Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
IVIMA|ICP Violations. Count of errored, invalid, or missing ICP cells, except during seconds where a SES-IMA or UAS-IMA condition is reported (Near End only). IVIMA is of type SecondsThreshRange.
SESIMA|Severely Errored Seconds. Count of 1-second intervals containing >= 30% of the ICP cells counted as IV-IMAs, or one or more near-end link defects (facility, LIF, or LODS) during non-UAS-IMA intervals. The number of IV-IMA counts required to meet the 30% criteria will depend on the facility line rate and the IMA frame size (M). SESIMA is of type SecondsThreshRange.
UASIMA|Unavailable seconds at NE. The NE unavailability begins at the onset of 10 contiguous SES-IMA including the first 10 seconds to enter the UAS-IMA condition, and ends at the onset of 10 contiguous second with no SES-IMA, excluding the last 10 seconds to exit the UAS-IMA condition. UASIMA is of type SecondsThreshRange.
TXUUSIMA|Transit Unusable Seconds (Near End only). Count of Tx Unusable seconds at the Tx NE Link State Machine (LSM). TXUUSIMA is of type SecondsThreshRange.
RXUUSIMA|Receive Unusable Seconds (Near End only). Count of Rx Unusable seconds at the Rx NE LSM. RXUUSIMA is of type SecondsThreshRange.
TXFC|Transit Failure Count. Count of the number of NE Transmit Link failure alarm entrances. The possible NE Tx link failure alarm conditions are: Tx-Mis-Connected and Tx-Fault. TXFC is of type SecondsThreshRange.
RXFC|Receive Failure Count. Count of the number of NE Receive Link failure alarm entrances. The possible NE Rx link failure alarm conditions are: LIF, LODS, and Rx-Fault. RXFC is of type SecondsThreshRange.
TXSTUFFIMA|Transmit Stuff Events (Near End only). Count of stuff events inserted in the transmited direction. TXSTUFFIMA is of type ImaLinkStuff.
RXSTUFFIMA|Receive Stuff Events (Near End only). Count of stuff events inserted in the receive direction, except during SES-IMA and UAS-IMA conditions. RXSTUFFIMA is of type ImaLinkStuff.
OIFIMA|Out of IMA Frame (Near End only). Count of OIF anomalies except during SES-IMA or UAS-IMA conditions. OIFIMA is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-ONT:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[BIP8=<BIP8>,][BES=<BES>,][SES=<SES>,][UAS=<UAS>,][MISSING=<MISSING>,][MES=<MES>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
BIP8|BIP8 errors detected on PON transport. NE is OLT detected, FE is ONT detected BIP8 is a Integer.
BES|Number of seconds during the period when a BIP8 error was detected. For the FE case, the granularity is 5 seconds rather than 1 second. BES is a Integer.
SES|For NEND this is the count of seconds where either the BIP8 count has exceeded a threshold or where the number of missing bursts equals the number of possible bursts for the ONT.
For FEND this is the count of seconds where the BIP8 count has exceeded a threshold. For the FE case the granularity is 5 seconds rather than 1 second. SES is a Integer.

UAS|This is defined a N consecutive SES. Once unavailable, N consecutive seconds must pass without SES before coming available again. In the FEND case this is a 5 second granularity rather than 1 second. UAS is a Integer.
MISSING|Count of missed bursts (no received traffic from ONT in allocated timeslot). NEND Only. MISSING is a Integer.
MES|Number of seconds during the period when a missing error was detected. NEND only. MES is a Integer.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.

##### Syntax: ```ED-GOS-PW:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[MISSPKTS=<MISSPKTS>,][JBUFUR=<JBUFUR>,][MFPKT=<MFPKT>,][PKTLOSRT=<PKTLOSRT>,][ES=<ES>,][SES=<SES>,][UAS=<UAS>,][FC=<FC>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|GOS Provisioning Access Identifier. GosAid is the AID GosProvAid.
LOCN|This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
MISSPKTS|Threshold of Missing Packet. MISSPKTS is a Integer.
JBUFUR|Number of times a packet need to be played out and the jitter buffer was empty. JBUFUR is a Integer.
MFPKT|Any packet which contains improper format that is unexpected size or bad header. MFPKT is a Integer.
PKTLOSRT|Packet Loss Rate Threshold. PKTLOSRT is of type Percentage.
ES|The number of seconds during which at least one discarded, LOPS, malformed and like. ES is a Integer.
SES|Counter associated with the number of severely errored seconds. SES is a Integer.
UAS|Counter associated with the number of UAS encountered. Any consecutive 10 seconds of SES are counted as one Unavailable Seconds (UAS).
Once a sequence of 10 consecutive SES, these counter increments each second until 10 consecutive seconds without SES. UAS is a Integer.

FC|The number of failure events. A failure event begins when the LOPS failure is detected and it ends when the failure is detected. FC is a Integer.
DESC|Description. DESC is a String.

##### Syntax: ```ED-GOS-T1:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SESP=<SESP>,][SASP=<SASP>,][CSSP=<CSSP>,][UASP=<UASP>,][CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][PERUP=<PERUP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the DS1 Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end PM registers are being edited. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. CVP is of type CVThreshRange.
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. ESP is of type SecondsThreshRange.
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. SESP is of type SecondsThreshRange.
SASP|Severely Errored Framing/Alarm Indication Signal Second Count. The threshold value for the severely errored framing/alarm indication signal second count. SASP is of type SecondsThreshRange.
CSSP|Controlled Slip Seconds Path. The threshold value for the controlled slip seconds path. CSSP is of type SecondsThreshRange.
UASP|Unavailable Seconds Threshold Path. The threshold value for the unavailable seconds for the path. UASP is of type SecondsThreshRange.
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line. CVL is of type CVThreshRange.
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. ESL is of type SecondsThreshRange.
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange.
PERUP|Percent Utilization - Path, Ingress (Near End only). PERUP is of type Percentage.
PERUPE|Percent Utilization - Path, Egress (Near End only). PERUPE is of type Percentage.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-T3:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SESP=<SESP>,][SASP=<SASP>,][UASP=<UASP>,][CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][PERUP=<PERUP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the T3 Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end PM registers are being edited. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. Note also that the corresponding CP parameter (CVCP) is set via this same field, since they have the same thresholds. CVP is of type CVThreshRange.
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. Note also that the corresponding CP parameter (ESCP) is set via this same field, since they have the same thresholds. ESP is of type SecondsThreshRange.
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. Note also that the corresponding CP parameter (SESCP) is set via this same field, since they have the same thresholds. SESP is of type SecondsThreshRange.
SASP|Severely Errored Framing/Alarm Indication Signal Second Count. The threshold value for the severely errored framing/alarm indication signal second count. Note also that the corresponding CP parameter (SASCP) is set via this same field, since they have the same thresholds. SASP is of type SecondsThreshRange.
UASP|Unavailable Seconds Threshold Path. The threshold value for the unavailable seconds for the path. Note also that the corresponding CP parameter (UASCP) is set via this same field, since they have the same thresholds. Note also that the corresponding CP parameter (UASCP) is set via this same field, since they have the same thresholds. UASP is of type SecondsThreshRange.
CVL|Coding Violations Threshold Line. The threshold value for the unavailable seconds for the line. CVL is of type CVThreshRange.
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. ESL is of type SecondsThreshRange.
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. This parameter does not apply to far end provisioning. SESL is of type SecondsThreshRange.
PERUP|Percent Utilization - Path, Ingress (Near End only). PERUP is of type Percentage.
PERUPE|Percent Utilization - Path, Egress (Near End only). PERUPE is of type Percentage.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GOS-XDSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVL=<CVL>,][ECL=<ECL>,][ECSL=<ECSL>,][ESL=<ESL>,][LOSC=<LOSC>,][LOSSL=<LOSSL>,][PERU=<PERU>,][PERUE=<PERUE>,][SESL=<SESL>,][UASL=<UASL>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the XDSL Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVL|Coding violations - line. The threshold value for the coding violations for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVL is of type CVAdslThreshRange.
ECL|Forward error correction count - line. The threshold value for the forward error correction count for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. ECL is of type ECThreshRange.
ECSL|Forward error correction count second - line. The threshold value for the forward error correction count second for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. ECSL is of type SecondsThreshRange.
ESL|Errored seconds - line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESL is of type SecondsThreshRange.
LOSC|Loss of Signal Count (Near End only). This indicates the number of times a LOS condition was set, and also represents the number of modem retrains in the time period. LOSC is a Integer.
LOSSL|LOS Seconds Threshold Line. The threshold value for the LOS seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 10. LOSSL is of type SecondsThreshRange.
PERU|Percent Utilization, Ingress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERU is of type Percentage.
PERUE|Percent Utilization - Path, Egress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERUE is of type Percentage.
SESL|Severely errored seconds - line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 65. UASL is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-GR303:[TID]:<IgAid>:[CTAG]:::[[PRIOP=<PRIOP>,][SECOP=<SECOP>,][SWTYPE=<SWTYPE>,][T308=<T308>,][T303=<T303>,][T396=<T396>,][T397=<T397>,][EOCALARM=<EOCALARM>,][EOCUPSST=<EOCUPSST>,][FLOWTHROUGH=<FLOWTHROUGH>]]; ```

##### Parameters
Attribute | Description
|---
IgAid|Interface Group Access Identifier. This is the address of the GR-303 Interface Group which is being modified. IgAid is the AID IgAid.
PRIOP|Primary Operations Processor. This parameter identifies the primary Operations Processor which will terminate the EOC channel. This must be a Maintenance/Administration Slot (MS). PRIOP is the AID MsNoneAid.
SECOP|Secondary Operations Processor. This parameter identifies the Secondary Operations Processor which will terminate the EOC channel. This must be a Maintenance/Administration Slot (MS). SECOP is the AID MsNoneAid.
SWTYPE|Switch type. This parameter identifies the type of switch to which the interface is connected. SWTYPE is of type SwitchType.
T308|T308 Timer. Identifies timer T308 used at Layer 3 and specifies the maximum length of time in seconds the RDT will wait for a reply to a RELEASE message. T308 is of type T308.
T303|T303 Timer. Identifies time T303 used at Layer 3 for the TMC and defines the maximum length of time in milliseconds that the RDT will wait for a reply to a SETUP message. T303 is of type T303.
T396|T396 Timer. This parameter specifies the length of time in milliseconds that the RDT will wait for a reply to a SETUP message following the initial expiration of time T303. T396 is of type T396.
T397|T397 Timer. This parameter specifies the maximum length of time in seconds the RDT will wait for the IDT to acknowledge an INFORMATION message that indicated that a customer who had been generating a permanent signal has returned on-hook. T397 is of type T397.
EOCALARM|EOC Alarms. This parameter indicates which alarms are to be reported through the EOC interface. The EOC can report alarms for either the shelf IG, the entire network, or no alarms at all. EOCALARM is of type EOCAlarmReport.
EOCUPSST|EOC Up Send Service States. Although service state changes are always sent to the switch when the IG is in normal operation, they are not reported to the switch when the EOC link is down. Some switches, such as the DMS100, do not audit the CRVs when the EOC link comes up, so the switch continues to have the incorrect service state. This can result in the switch thinking that a CRV is down so no traffic is able to be carried. When set to "Y", this parameter will send service state notifications for all provisioned CRVs when the EOC link comes up. EOCUPSST is of type BoolYN.
FLOWTHROUGH|Flow through provisioning (also referred to as 'RDT provisioning'). This is a provisionable option that exists in a Class-5 switch which when enabled causes the switch to send provisioning messages over the EOC of a given GR303 interface group for the purposes of managing analogLineTerminations in the RDT. The switch will Create, Delete, Remove from Service, and audit each CRV in the RDT when this option is enabled. The RDT needs to be aware of how this option is set in the switch for the purposes of issuing service state notifications. If an analogLineTermination is not 'switch created' and flow through provisioning is enabled, then the RDT should not issue any service state notifications to the switch for that line. If flow through provisioning is disabled, then the RDT should always issue service state notifications for all lines. FLOWTHROUGH is of type BoolYN.

##### Syntax: ```ED-GR8:[TID]:<SlotIgAid>:[CTAG]:::[SWTYPE=<SWTYPE>]; ```

##### Parameters
Attribute | Description
|---
SlotIgAid|GR-8 Interface Group Access Identifier. This is the address of the GR-8 Interface Group which is being modified. SlotIgAid is the AID SlotIgAid.
SWTYPE|Switch Type. The parameter indicate the type of switch which the GR-8 interface group will be connected to. SWTYPE is of type SwitchType.

##### Syntax: ```ED-GRPXDSL:[TID]:<GroupAid>:[CTAG]:::[[ADDMEM=<ADDMEM>,][REMMEM=<REMMEM>,][PKTMODE=<PKTMODE>,][FALLBACKVPI=<FALLBACKVPI>,][FALLBACKVCI=<FALLBACKVCI>,][MRDS=<MRDS>,][XRDS=<XRDS>,][MRUS=<MRUS>,][XRUS=<XRUS>,][DIFDS=<DIFDS>,][DIFUS=<DIFUS>,][GOS=<GOS>,][REPTRMVRST=<REPTRMVRST>,][PROMOTEALARMS=<PROMOTEALARMS>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
GroupAid|Access Identifier of the Group. GroupAid is the AID DslGrpAid.
ADDMEM|This parameter identifies the AID of member port(s) to be added to the group. The number of members should be 0, 1, 2, 4, 8, 12. ADDMEM is the AID DslPortAid and is listable.
REMMEM|This parameter identifies the AID of member port(s) to be removed from the group. The number of members should be 0, 1, 2, 4, 8, 12. REMMEM is the AID DslPortAid and is listable.
PKTMODE|Packet mode defines if this port is to operate in packet or ATM VC mode. It could not be set to N when the service type of any group memeber is VDSL2 or VDSL2MM or when PTMOVER attribute of any group memeber is Y. PKTMODE is of type BoolYN. The default value is "Y".
FALLBACKVPI|The VPI value to use on the singular VC in packet mode. FALLBACKVPI is of type VPRange.
FALLBACKVCI|The VCI value to use on the singular VC in packet mode. FALLBACKVCI is of type VCBndGrpRange.
MRDS|Minimum aggregate downstream rate. MRDS is of type DwnStreamRateGrp.
XRDS|Maximum aggregate downstream rate. XRDS is of type DwnStreamRateGrp.
MRUS|Minimum aggregate upstream rate. MRUS is of type UpStreamRateGrp.
XRUS|Maximum aggregate upstream rate. XRUS is of type UpStreamRateGrp.
DIFDS|The differential delay for the downstream direction in milliseconds. DIFDS is a Integer.
DIFUS|The differential delay for the upstream direction in milliseconds. DIFUS is a Integer.
GOS|This is the related Grade of Service for GRPXDSL that is to be applied to the group. GOS is the AID GosAid.
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the Group. Note that RMV/RST are reported upon every modem retrain and can clutter the event logs if enabled. REPTRMVRST is of type BoolYN.
PROMOTEALARMS|It depends on this toggle to raise alarms or events for the following CondType. If N, raise as event. If Y, raise as alarm _CondTypeMinRateFailUs_ = 547, // Aggregate US train rate below mininum _CondTypeMinRateFailDs_ = 548, // Aggregate DS train rate below mininum _CondTypeDiffDlyFailUs_ = 551, // Diff. delay US between members exceeded _CondTypeDiffDlyFailDs_ = 552, // Diff. delay DS between members exceeded _CondTypeLinkRateFailUs_ = 553, // Ratio between low/high rates US exceeded _CondTypeLinkRateFailDs_ = 554, // Ratio between low/high rates DS exceeded _CondTypeLinkTcModeMismatch_= 605, // VDSL PTM Bonding: Mismatch of the TC mode between group members _CondTypeMemDown_ = 546, // Group Member Down PROMOTEALARMS is of type BoolYN.
DESC|Description. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-GW-VOIP:[TID]:[<VOIPGWAID>]:[CTAG]:::[[IGAID=<IGAID>,][FQDN=<FQDN>,][HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
VOIPGWAID|AID of the VoIP Gateway. VOIPGWAID is the AID VoIPGWONTAid.
IGAID|Interface Group identifying the type and parameters of the VoIP Gateway. IGAID is the AID IgAid.
FQDN|Fully Qualified Domain Name for the VoIP Gateway. FQDN is a String.
HOSTPROTO|Determines whether static or Dynamic (DHCP) IP addressing will be performed for the VoIP Gateway IP Address. HOSTPROTO is of type GwHostProto.
IP|Statically Provisioned IP Address of VoIP Gateway. IP is the AID IpAid.
IPMSK|Network Address Mask of Gateway IP Address. IPMSK is the AID IpAid.
GADDR|IP Address of Network Gateway. GADDR is the AID IpAid.
PST|Operational Service State of the VoIP Gateway. PST is of type PrimaryStateChg.

##### Syntax: ```ED-H248:[TID]:<IgAid>:[CTAG]:::[[SWTYPE=<SWTYPE>,][MGIP=<MGIP>,][MG2IP=<MG2IP>,][MGUDP=<MGUDP>,][MGC1IP=<MGC1IP>,][MGC1UDP=<MGC1UDP>,][MGC2IP=<MGC2IP>,][MGC2UDP=<MGC2UDP>,][MGC2SWTYPE=<MGC2SWTYPE>,][MGC2ESA=<MGC2ESA>,][TERMPREFIX=<TERMPREFIX>,][EPHEMTERMID=<EPHEMTERMID>,][TMAX=<TMAX>,][MWD=<MWD>,][EPHEMAUDITDELAY=<EPHEMAUDITDELAY>,][FIRSTDIGWAIT=<FIRSTDIGWAIT>,][LONGDIGWAIT=<LONGDIGWAIT>,][SHORTDIGWAIT=<SHORTDIGWAIT>,][LONGDIGDUR=<LONGDIGDUR>,][MINFLASH=<MINFLASH>,][MAXFLASH=<MAXFLASH>,][MAXACTCALLS=<MAXACTCALLS>,][RFC2833ENABLED=<RFC2833ENABLE>,][ECENABLE=<ECENABLE>,][EPCD=<EPCD>,][ECTAIL=<ECTAIL>,][MGC1FQDN=<MGC1FQDN>,][MGC2FQDN=<MGC2FQDN>,][RTPUDP=<RTPUDP>,][APPMODE=<APPMODE>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|IG number within a shelf. IgAid is the AID IgAid.
SWTYPE|SWitch TYPE The parameter indicate the type of switch which the H.248 interface group will be connected to. The only switches supported for primary switch type are: CS2K, META9020, SONUS. SWTYPE is of type H248SwitchType.
MGIP|Media Gateway's IP address for control message transport. MGIP is the AID IpAid.
MG2IP|Secondary MGC IP address for control message transport. MG2IP is the AID IpAid.
MGUDP|MGUDP is a Integer.
MGC1IP|Primary Media Gateway Controller's IP address. MGC1IP is the AID IpAid.
MGC1UDP|MGC1UDP is a Integer.
MGC2IP|Secondary Media Gateway Controller's IP address. A value of 0.0.0.0 indicates there is none. MGC2IP is the AID IpAid.
MGC2UDP|MGC2UDP is a Integer.
MGC2SWTYPE|Secondary MGC Switch Type. When MGC2ESA is set to N(by default), the only switches supported for secondary switch type are: CS2K, META9020, SONUS, NONE; ``` When MGC2ESA is set to Y, the only switches supported for secondary switch type are: GBANDG2, GBANDG6, NONE. MGC2SWTYPE is of type H248SwitchType.
MGC2ESA|This parameter indicates whether the secondary MGC is ESA MGC2ESA is of type BoolYN.
TERMPREFIX|Prefix on Termination Ids. This is a string of up to 11 characters. TERMPREFIX is a String.
EPHEMTERMID|H248 Ephemeral Termination ID. Used to allow the media gateway to properly interpret the string sent by the media gateway controller. Default value is NONE, max length is 30. EPHEMTERMID is a String.
TMAX|Maximum delay in seconds between first transmission and final retransmission of a message before declaring a communication failure with the MGC.
A value of 0 for TMAX disables the declaring of a MGC communication failure due to a message timeout, including a timeout waiting for a heartbeat message. TMAX is a Integer.

MWD|Maximum delay in seconds [0,60] before announcing MG presence to MGC. MWD is a Integer.
EPHEMAUDITDELAY|The number of seconds between repetitions of reporting of a stranded "ephemeral termination" (Network trunk). The value should be in the range 0-3600. The value 0 indicates that the audit is not to be performed. EPHEMAUDITDELAY is a Integer.
FIRSTDIGWAIT|Default number of seconds to wait for the start of dialing. The valid range is 0-60 (0 disables the timer). FIRSTDIGWAIT is a Integer.
LONGDIGWAIT|Default value in seconds of the long inter-digit timer. The valid range is 1-60. LONGDIGWAIT is a Integer.
SHORTDIGWAIT|Default value in seconds of the short inter-digit timer. The valid range is 1-60. SHORTDIGWAIT is a Integer.
LONGDIGDUR|Default minimum duration, in seconds, of a long digit event. The valid range is 1-60. LONGDIGDUR is a Integer.
MINFLASH|Default minimum on-hook duration in milliseconds for a flash. The value range is 100-4900. MINFLASH is a Integer.
MAXFLASH|Default maximum on-hook duration in milliseconds for a flash. The value range is 100-4900. MAXFLASH is a Integer.
MAXACTCALLS|Maximum number of concurrent calls (up to 384) for this IG. MAXACTCALLS is a Integer.
RFC2833ENABLE|RFC2833ENABLE is of type BoolYN.
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN.
EPCD|Echo Path Change Detection. EPCD=Y is only effective when ECCONFIG=SPARSE on the supporting equipement (VGP/VIPR). Enabling EPCD improves the ability to track changes in the echo path, but reduces channel density. EPCD is of type BoolYN.
ECTAIL|Integer: 64ms to 128ms in steps of 8ms. The maximum echo delay that the echo canceller is able to eliminate. If ECCONFIG=DUAL, increasing ECTAIL may further reduce channel density. If ECCONFIG=SPARSE, increasing ECTAIL does not impact channel density. ECTAIL is a Integer.
MGC1FQDN|None is a special value to unset its previous value. MGC1FQDN is a String.
MGC2FQDN|None is a special value to unset its previous value. MGC2FQDN is a String.
RTPUDP|RTPUDP is a Integer.
APPMODE|Application Mode. APPMODE is of type H248AppMode.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-HDSL:[TID]:<HdslAid>:[CTAG]:::[[LINETYPE=<LINETYPE>,][T1MAP=<T1MAP>,][FMT=<FMT>,][TERM=<TERM>,][SNRTHR=<SNRTHR>,][ATTHR=<ATTHR>,][PWR=<PWR>,][GOS=<GOS>,][TMGMODE=<TMGMODE>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port being entered. HdslAid is the AID SixPortLuAid.
LINETYPE|HDSL Line Type: 2- or 4-wire mode. In 4-wire mode, two consecutive port addresses are required for one HDSL port. LINETYPE is of type HdslLineType.
T1MAP|MAPping of the payload signal. When payload signal is a form that may be altered at the T1 port, this parameter specifies the mapping. Otherwise, its value should be NA. T1MAP is of type T1MapHdsl.
FMT|DS1 Format. This parameter indicates DS1 signal format. FMT is of type FormatSignal.
TERM|TERMinal Unit Type TERM is of type HdslTermType.
SNRTHR|Signal-to-Noise Margin Threshold (near-end), in dB. (0 == OFF) SNRTHR is of type SnrTargetMargins.
ATTHR|Loop Attenuation Threshold (near-end), in dB. (0 == OFF) ATTHR is of type HdslLoopAttenThresh.
PWR|Line PoWeRing. This parameter indicates whether the line is to supply power. PWR is of type T1Pwr.
GOS|Grade of Service Access Identifier. This is the HDSL Grade of Service which is to be applied to the port. GOS is the AID GosAid.
TMGMODE|Timing Mode. This parameter selects the timing source for the T1 port transmit signal. For T1MAP other than UNI or NNI, C7 will default TMGMODE to LOOP when FMT=UF, SOURCE otherwise. TMGMODE is of type T1TimingMode.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-IFCONFIG:[TID]:<IfConfigAid>:[CTAG]:::[[CHAP=<CHAP>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>,][ENCAP=<ENCAP>,][VLAN=<VLAN>]]; ```

##### Parameters
Attribute | Description
|---
IfConfigAid|Interface Configuration Access Identifier. The address of an interface configuration which is being modified. IfConfigAid is the AID IfConfigAid.
CHAP|Channel Access Privilege. This parameter identifies the access privileges for the ethernet port on which a user can establish a session. At system initialization the default value is FULLACC for all ethernet ports. CHAP is of type CidSecurity.
IP|IP address. IP ADDRess. This parameter identifies the IP address used when accessing the ethernet port. Entering an IP address of 0.0.0.0 will tear down the interface and unbind the associated IfConfigAid from it. Some older Amp cards only support two active interfaces, so this allows the user to bind either E2 or E3 to the desired IP, depending on application needs. IP is the AID IpAid.
IPMSK|IP address mask. This parameter identifies the the mask used on the IP Address. IPMSK is the AID IpAid.
GADDR|Gateway IP address. Only one of the gateway addresses per shelf (interface E1 or E2) can be nonzero. Additional static routes can be created with ENT-IP-ROUTE. GADDR is the AID IpAid.
ENCAP|ATM Encapsulation Type. This parameter is applicable only for the Inband Management (E3) interface. ENCAP is of type E3EncapType.
VLAN|Packet VLAN Access Identifier. This parameter is applicable only for the Inband Management (E4) interface. VLAN is the AID IfconfigId.

##### Syntax: ```ED-IG-CSHELF:[TID]:<IgAid>:[CTAG]::<SHELF>:[[NVDS1=<NVDS1>,][CAPALMTHR=<CAPALMTHR>]]; ```

##### Parameters
Attribute | Description
|---
IgAid|The Interface Group AID. IgAid is the AID IgAid.
SHELF|The associated subscriber shelf. SHELF is the AID ShelfAid.
NVDS1|The number of Virtual DS1s allocated for this association. This determines the call capacity for the IG to the associated shelf. NVDS1 is a Integer.
CAPALMTHR|Call Capacity Alarm Threshold. If the number of active calls reaches or exceeds this percentage of total, an alarm is raised. CAPALMTHR is of type Percentage.

##### Syntax: ```ED-IGMP:[TID]:<IgmpAid>:[CTAG]:::[[QINT=<QINT>,][QRINT=<QRINT>,][SQINT=<SQINT>,][SQCNT=<SQCNT>,][LMQINT=<LMQINT>,][LMQCNT=<LMQCNT>,][CTLMODE=<CTLMODE>,][MACFLTR=<MACFLTR>,][PROXY=<PROXY>,][LOCALIZE=<LOCALIZE>]]; ```

##### Parameters
Attribute | Description
|---
IgmpAid|IP Route processor Card Access IDentifier. IgmpAid is the AID SlotLuAid.
QINT|Query Interval. The interval in seconds between General Queries sent by the requestor. The valid range is 1 - 255 seconds. QINT is a Integer. The default value is "125".
QRINT|Query Response Interval. The Max Response Time in milliseconds inserted into the periodic General. The valid range is 100 - 25000 milliseconds. QRINT is a Integer. The default value is "20000".
SQINT|Startup Query Interval. The interval in seconds between General Queries sent by a requestor on startup. The valid range is 1 - 255 seconds. SQINT is a Integer. The default value is "30".
SQCNT|Startup Query Count. The number of Queries sent out on startup, separated by the Startup Query Interval. The valid range is 1 - 10. SQCNT is a Integer. The default value is "2".
LMQINT|Last Member Query Interval. The Max Response Time in milliseconds inserted into Group-Specific Queries sent in response to Leave Group messages, and is also the amount of time between Group-Specific Query messages. The valid range is 1 - 1000 milliseconds. LMQINT is a Integer. The default value is "100".
LMQCNT|Last Member Query Count. The number of Group-Specific Queries sent before the router assumes there are no local members. The valid range is 1 - 10. LMQCNT is a Integer. The default value is "1".
CTLMODE|Control Mode. Determines how IGMP clients are expected to behave. 'Normal' for RFC 2336 support and 'Fast' supports the customized IGMP client, which requires each client to send reports and leaves [For the first release, it implies a deployment of similar STBs, in future release, can be overridden by a device level setting]. CTLMODE is of type IgmpCtlMode. The default value is "NORMAL".
MACFLTR|MAC Filtering. Mac address filtering provides added security when set to TRUE. Extra checks validate the channel changers source MAC address. MACFLTR is of type BoolYN. The default value is "N".
PROXY|Igmp PROXY Mode. IRC operates in IGMP Proxy Mode when set to TRUE by sending reports and leaves upstream to the video head end. When set to 'N', all multicast video channels are always flowing from the video head end. PROXY is of type BoolYN. The default value is "N".
LOCALIZE|When it's 'Y', IGMP localization is turned on. When it's 'N' IGMP localization is off and joins and leaves are sent on all uplinks. LOCALIZE is of type BoolYN. The default value is "N".

##### Syntax: ```ED-IMA:[TID]:<ImaAid>:[CTAG]:::[[IMAMAP=<IMAMAP>,][MLINKS=<MLINKS>,][XDIFDLY=<XDIFDLY>,][INH=<INH>,][FRMLEN=<FRMLEN>,][ALTV1_0=<ALTV1_0>,][EXT=<EXT>,][PDOM=<PDOM>,][GOS=<GOS>,][LINKGOS=<LINKGOS>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][TMGMODE=<TMGMODE>,][TXIMAGRPID=<TXIMAGRPID>,][TXIMAGRPVER=<TXIMAGRPVER>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. The address of the IMA group being modified. ImaAid is the AID ImaGrpAid.
IMAMAP|IMA Mapping. This parameter indicates how the internal fixed length packets are to be mapped at the IMA interface. IMAMAP is of type ImaMap.
MLINKS|Minimum links. Minimum number of links required to be Active for the IMA group to be in the Up state. MLINKS is of type ImaLinks.
XDIFDLY|Maximum Differential Delay. The maximum number of milliseconds of differential delay among the links that will be tolerated. XDIFDLY is of type ImaDiffDelay.
INH|Inhibited. Configures whether the group is allowed to become operational and carry ATM data. INH is of type BoolYN.
FRMLEN|Frame Length. The IMA frame length to be used by the IMA group. FRMLEN is of type ImaFrm.
ALTV1_0|Alternative V1.0. The C7 IMA interface uses the IMA version 1.1 specification as default to interoperate with other IMA interfaces, this is normally backward compatible with older v1.0 interfaces. However, there are recognized interoperability issues with some older IMA interfaces. This parameter enables/disables the IMA group to use the alternative v1.0 IMA specification that should avoid these interoperability problems. For example, the parameter should be set in a group that is interoperating with an older Cisco IMA interface. Please see Atm Forum: Inverse Multiplexing for ATM Specification Version 1.1(AF-PHY-0086.001) - Abstract for further details. ALTV1_0 is of type BoolYN.
EXT|External Interface. This indicates if the IMA group is an internal or external path in the network. The value should be set to "Y" when the group is an external interface. It should be set to "N" when the group is connected to other shelves within a network of C7s. This parameter is valid only if IMAMAP is NNI. Note that this parameter must be changed independently of others, ie. a separate ED-IMA command is required. EXT is of type BoolYN.
PDOM|Protection DOMain. This is an integer that is used to associate a transport facility into a protection domain that is used for A to Z connection provisioning. The PDOM for each domain must be a unique non-zero integer. The value of 0 is reserved to indicate that the facility is not to be used for A to Z connections. PDOM is of type Pdom.
GOS|Grade of Service Access Identifier. This is the Grade of Service that is to be applied to the IMA group. GOS is the AID GosAid.
LINKGOS|Link Grade of Service Access Identifier. This is the Grade of Service that is to be applied to the IMA links. LINKGOS is the AID GosAid.
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. PYLDSCRM is of type BoolYN.
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. ATMMON is of type BoolYN.
TMGMODE|Timing Mode. This parameter selects the timing source. TMGMODE is of type T1TimingMode.
TXIMAGRPID|Specifies the transmit IMA Group ID, a value between 1 and 255. TXIMAGRPID is a Integer.
TXIMAGRPVER|Specifies the transmitted IMA version. TXIMAGRPVER is of type ImaVersion.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-IP-HOSTID:[TID]:<IPHostIdAid>:[CTAG]:::[[IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>]]; ```

##### Parameters
Attribute | Description
|---
IPHostIdAid|IP HostId AID on 8/12-port line-unit only. IPHostIdAid is the AID IPHostIdAid.
IP|IP Address of Host. IP is the AID IpAid.
IPMSK|IP mask. IPMSK is the AID IpAid.
GADDR|Gateway Address. GADDR is the AID IpAid.

##### Syntax: ```ED-IPIF-PORT:[TID]:<IP>:[CTAG]:::INTERFACE=<INTERFACE>,RTRAID=<RTRAID>,[DHCPIPIF=<DHCPIPIF>]; ```

##### Parameters
Attribute | Description
|---
IP|IP is the AID IpAid.
INTERFACE|INTERFACE is the AID IpIfPortAid.
RTRAID|RTRAID is the AID VrAid.
DHCPIPIF|Indicates that this IPIF-PORT's interface is used for relaying DHCP requests. For DHCP requests to be relayed, exactly one IP interface for a given layer-2 interface must have DHCPIPIF=Y.
A given virtual bridge may have at most one IPIF-PORT, attached at the VB level, with the DHCPIPIF set to Y. Each VLAN, independent of the virtual bridge attachments, may also have at most one attached IP-Interface with DHCPIPIF set to Y. DHCPIPIF is of type BoolYN.


##### Syntax: ```ED-LAG:[TID]:<LinkAggAid>:[CTAG]:::[[ADDMEM=<ADDMEM>,][REMMEM=<REMMEM>,][LACPMODE=<LACPMODE>,][MTU=<MTU>,][RVRTV=<RVRTV>,][SYSPRIO=<SYSPRIO>,][PARTNERACTSTBY=<PARTNERACTSTBY>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 12 groups are supported on a single slot, and up to 4 on a single VB. LinkAggAid is the AID LinkAggAid.
ADDMEM|This is the AID of the member port to be added. ADDMEM is the AID LagId2 and is listable.
REMMEM|This is the AID of the member port to be removed. REMMEM is the AID LagId2 and is listable.
LACPMODE|Only effective for Rap. LACPMODE is of type LacpMode.
MTU|Max Transmission Unit. MTU is of type Mtu.
RVRTV|Revertive. This parameter indicates if the protection requested is to be revertive or non-revertive. This parameter is only applicable for RAP10G Active/Standby mode. Non-revertive prevents the link from switching back to the active members when a link is restored. RVRTV is of type BoolYN.
SYSPRIO|Used between two systems connected by the LAG to dertermine which should be controlling the LAG. The lower value takes priority. Typically, the upstream side of the LAG is configured for the LAG master (lower value). SYSPRIO is of type Zero264k.
PARTNERACTSTBY|Y - Suppress alarms consistent with Active/Standby operation. N - Do not supress alarms. PARTNERACTSTBY is of type BoolYN.
DESC|The name of the LinkAgg. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-LINK:[TID]:<DataLinkAid>:[CTAG]::<LINKTYPE>,[<ICCVC>]; ```

##### Parameters
Attribute | Description
|---
DataLinkAid|Data Link Access Identifier. The address of the port which is to carry the datalink. DataLinkAid is the AID DataLinkAid.
LINKTYPE|Link Type. This parameter indicates whether the Section Data Communication Channel (SDCC), Link Data Communications Channel (LDCC), or Internal Communication Channel (ICC) in a facility payload should be used to communicate with the other nodes in the system. LINKTYPE is of type LinkType.
ICCVC|Internal Communications Channel Virtual Circuit. When an Internal Communications Channel within a facility payload is used to carry the internal datalink, this parameter is used to specify the full address of the Virtual Circuit in the payload. If no value is provided, the default of VP0, VC24 will be set. For a Sonet port, C7 will assume the first STS, which MUST be ATMNNI or the command will be rejected. ICCVC is the AID LinkId.

##### Syntax: ```ED-MACHOST:[TID]:<MACAID>:[CTAG]:::VLAN=<VLAN>,[[BRIDGE=<BRIDGE>,][L2IFAID=<L2IFAID>]]; ```

##### Parameters
Attribute | Description
|---
MACAID|MAC Address. MACAID is the AID MacAid.
VLAN|VLAN is the AID IfId1.
BRIDGE|BRIDGE is the AID VbAid.
L2IFAID|Layer 2 Access Identifier. This is the port address or the VC Aid on which the host can be found. L2IFAID is the AID MachostId1.

##### Syntax: ```ED-NODE:[TID]:<NodeAid>:[CTAG]::[<SID>]:[[NODEAMP=<NODEAMP>,][ALMCONT=<ALMCONT>,][MOUNT=<MOUNT>,][LAT=<LAT>,][LONG=<LONG>]]; ```

##### Parameters
Attribute | Description
|---
NodeAid|Node Access Identifier. The node number of the node which is to be updated. NodeAid is the AID NodeAid.
SID|System identification code (SID). If specified, this is the new SID to be assigned to the the node. It is the SID which will be used to identify the node in the TID field of any subsequent TL1 commands issued by TL1 users who do not specify a Node Number in their AIDs. The value of SID may be any valid simple or compound TL1 identifier or text string. It is limited to 24 characters. The recommended value for this parameter is the node's CLLI. SID is a String.
NODEAMP|Node AMP. This is the AID of the AMP or ATP which is to report alarms for all shelves within the node. It must be in a shelf within the node. NODEAMP is the AID MsNoneAid.
ALMCONT|ALarM CONTact. This parameter determines whether alarm contacts can be scoped to reflect just the node or can be scoped report for the network. ALMCONT is of type AlarmContact.
MOUNT|Mount Type. This describes how the Node of C7's is mounted, such as a Rack or Outdoor Cabinet. MOUNT is of type MountType.
LAT|Latitude. This is the Latitude in real world coordinates. LAT is a Integer.
LONG|Longitude. This is the Longitude in real world coordinates. LONG is a Integer.

##### Syntax: ```ED-ONT:[TID]:<OntAid>:[CTAG]:::[[ONTNUM=<ONTNUM>,][REGID=<REGID>,][ONTPROF=<ONTPROF>,][VCG=<VCG>,][BATPROV=<BATPROV>,][ONTPID=<ONTPID>,][SDBER=<SDBER>,][GOS=<GOS>,][ADRMODE=<ADRMODE>,][RGALWRMT=<RGALWRMT>,][RGCFGINST=<RGCFGINST>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OntAid|The ONT Port Access Identifier. OntAid is the AID OntAid.
ONTNUM|The ONT Number for the ONT. This can be physical serial number of the unit or an assigned number programmed into the ONT. The ONT Number is entered as string of at most 8 hexidecimal digits, optionally preceeded by "0x". ONTNUM is a String.
REGID|Registration Id. This is a string of up to 10 printable ASCII characters (Space is disallowed), that can be used instead of ONTNUM for remote ONT registration. When an ONT has been ranged and associated with a matching REGID in the database, the ONTNUM will be automatically recorded in the C7 database and service to the ONT enabled. REGID is a String.
ONTPROF|ONT profile conversion is allowed provided there are no provisioned services incompatible with the new profile. ONTPROF is the AID OntId2.
VCG|The Voice Concentration Group used to support T0 cross-connects from this ONT. VCG is the AID OntId.
BATPROV|This parameter indicates the expected Battery Backup capability. BATPROV is of type BoolYN.
ONTPID|The ONT Password is a string of up to 10 characters that can be used to verify the authenticity of an arriving ONT. A password cannot be provided when using a Calix defined ONT Profile. ONTPID is a String.
SDBER|The threshold value above which the PON Interface bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD.
GOS|GOS is the AID GosAid.
ADRMODE|ADRMODE is of type AdrMode.
RGALWRMT|This parameter specifies a timeout which enables the RG remote management. This would only be allowed for ONTs with a NUMRG=1 profile. RGALWRMT is of type RgAlwRmtTimeOut.
RGCFGINST|RGCFGINST is of type ONTCFGINST.
DESC|DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-PID:[TID]:<UID>:[CTAG]::<OLDPID>,<NEWPID>; ```

##### Parameters
Attribute | Description
|---
UID|User Identifier. The user's identifier for session to be cancelled. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination of alphanumeric characters 4 to 10 characters long and is case-sensitive. UID is the AID UserAid.
OLDPID|Old password. The user's old password or private identifier. OLDPID is a String.
NEWPID|User's new password. The password must conform to the rules provisioned via ED-SYS-SECU. The new password must be distinct from the old password. NEWPID is a String.

##### Syntax: ```ED-PON:[TID]:<PonAid>:[CTAG]:::[[SDBER=<SDBER>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
PonAid|The PON Port Access Identifier. PonAid is the AID FourPortLuAid.
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-PROF-ACS:[TID]:<ACSPROFAID>:[CTAG]:::[[ACSURL=<ACSURL>,][USER=<USER>,][PID=<PID>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
ACSPROFAID|The ACSProf Aid. ACSPROFAID is the AID AcsProfAid.
ACSURL|The ACSURL is a string of up to 63 characters. It must begin with "http://". ACSURL is a String.
USER|The ACS user is a string of up to 31 characters. USER is a String.
PID|The ACS password is a string of up to 25 characters. PID is a String.
DESC|DESC is a String.

##### Syntax: ```ED-PROF-ETHBW:[TID]:<ProfileId>:[CTAG]:::[DESC=<DESC>]; ```

##### Parameters
Attribute | Description
|---
ProfileId|This identifies which profile is being operated on. ProfileId is the AID BwpProfAid.
DESC|A string describing the profile or its use. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ED-PROF-MATCHLIST:[TID]:<MatchListAid>:[CTAG]:::[[ADDMATCHRULE=<ADDMATCHRULE>,][REMMATCHRULE=<REMMATCHRULE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
MatchListAid|A unique network wide ID. MatchListAid is the AID MatchListAid.
ADDMATCHRULE|The ID of a match rule to be added in this match list. ADDMATCHRULE is the AID MatchRuleId and is listable.
REMMATCHRULE|The ID of a match rule to be removed from this match list. REMMATCHRULE is the AID MatchRuleId and is listable.
DESC|An 11 character string description of the MatchList. DESC is a String.

##### Syntax: ```ED-PROF-MATCHRULE:[TID]:<RuleAid>:[CTAG]:::[DESC=<DESC>]; ```

##### Parameters
Attribute | Description
|---
RuleAid|Match rule AID RuleAid is the AID MatchRuleId.
DESC|An 11 character string description of the MatchRule. DESC is a String.

##### Syntax: ```ED-PROF-MCAST:[TID]:<McastProfAid>:[CTAG]:::[[MVRPROF=<MVRPROF>,][MAXSTREAMS=<MAXSTREAMS>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
McastProfAid|McastProfAid is the AID McastProfAid.
MVRPROF|This identifies an existing Multicast Vlan Registration profile entry. MVRPROF is the AID McastId1.
MAXSTREAMS|Maximum number of video streams that can be joined. "NONE" means no maximum. MAXSTREAMS is of type McastProfMaxStreams.
DESC|User string. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ED-PROF-MCASTRANGE:[TID]:<McastRangeProfAid>:[CTAG]:::[[ADDRANGE=<ADDRANGE>,][REMSTART=<REMSTART>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
McastRangeProfAid|Multicast Range Profile AID. McastRangeProfAid is the AID McastRangeProfAid.
ADDRANGE|This is a Multicast Address range to be added to the profile. Both a start and an end must be provided. The address range must not overlap existing ranges within the profile. ADDRANGE is the AID IpAid and is listable and rangeable.
REMSTART|This is a Multicast Address range to be removed from the profile. Only the start address of the range is needed. REMSTART is the AID IpAid and is listable.
DESC|User String. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ED-PROF-MVR:[TID]:<MvrProfAid>:[CTAG]:::[[ADDVLAN=<ADDVLAN>,][REMVLAN=<REMVLAN>,][ADDRANGEPROF=<ADDRANGEPROF>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
MvrProfAid|MvrProfAid is the AID MvrProfAid.
ADDVLAN|This parameter can be used to add a list of VLANs to this profile. Up to 4 VLANs may be associated with one profile. ADDVLAN is the AID VlanIndexAid and is listable.
REMVLAN|This parameter can be used to remove a list of VLANs from this profile. At least one VLAN must remain in the profile. REMVLAN is the AID VlanIndexAid and is listable.
ADDRANGEPROF|The Multicast Range profile ID added to a VLAN. The number of Range profile specified must match the number of ADDVLAN specified. ADDRANGEPROF is the AID McastRangeProfAid and is listable.
DESC|User string. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ED-PROF-ONT:[TID]:<OntProfAid>:[CTAG]:::[[VENDOR=<VENDOR>,][NUMPOTS=<NUMPOTS>,][NUMDS1=<NUMDS1>,][NUMGETH=<NUMGETH>,][NUMETH=<NUMETH>,][NUMHPNA=<NUMHPNA>,][NUMRFVID=<NUMRFVID>,][GEMONLY=<GEMONLY>,][AUXPWR=<AUXPWR>,][PWE3=<PWE3>,][NUMRG=<NUMRG>,][NUMBR=<NUMBR>,][DFLTRG=<DFLTRG>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
OntProfAid|ONT profile number. OntProfAid is the AID OntProfAid.
VENDOR|The Vendor ID for ONTs using this profile. This is a string up to 4 characters long. VENDOR is a String.
NUMPOTS|The number of POTS ports supported on the ONT; ``` the supported values are 0,2,4 and 8. NUMPOTS is a Integer.
NUMDS1|The number of DS1 ports supported on the ONT. {0-12} NUMDS1 is a Integer.
NUMGETH|The number of Gigabit Ethernet ports supported on the ONT. {0-8} NUMGETH is a Integer.
NUMETH|The number of Fast Ethernet ports supported on the ONT. {0-8} NUMETH is a Integer.
NUMHPNA|The number of HPNA Ethernet ports supported on the ONT. {0-2} NUMHPNA is a Integer.
NUMRFVID|The number of RF Video (COAX) output ports supported on the ONT. {0-12} NUMRFVID is a Integer.
GEMONLY|This ONT has GEM /IP only capability. GEMONLY is of type BoolYN.
AUXPWR|This ONT Auxiliary Power capability. AUXPWR is of type BoolYN.
PWE3|PWE3 Capability. PWE3 is of type BoolYN.
NUMRG|The number of RG ports supported on the ONT; ``` the supported values are 0 and 1. NUMRG is a Integer.
NUMBR|The number of BR ports supported on the ONT; ``` the supported values are 0 and 1. NUMBR is a Integer.
DFLTRG|The default mode of the ONT. DFLTRG is of type BoolYN.
DESC|A user-settable description field for this profile, of up to 31 characters. DESC defaults to be the template address/index number. DESC is a String.

##### Syntax: ```ED-PROF-SIPDIAL:[TID]:<SipDialAid>:[CTAG]:::[[ADDRULE=<ADDRULE>,][DELRULE=<DELRULE>,][SHDIGTIM=<SHDIGTIM>,][LNDIGTIM=<LNDIGTIM>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
SipDialAid|System scoped Dial Plan for SIP Gateways SipDialAid is the AID DialPlanAid.
ADDRULE|A string specifying a rule to add to the dial plan. ADDRULE is a String.
DELRULE|A string specifying a rule to delete from the dial plan. DELRULE is a String.
SHDIGTIM|The timeout, in seconds, for digit collection when no match exists. SHDIGTIM is of type STimeOut.
LNDIGTIM|The timeout, in seconds, for digit collection when no match exists. LNDIGTIM is of type LTimeOut.
DESC|A string describing this Profile. DESC is a String.

##### Syntax: ```ED-PROF-SIPSVC:[TID]:<SipSvcAid>:[CTAG]:::[[PRIPROXYADR=<PRIPROXYADR>,][SECPROXYADR=<SECPROXYADR>,][PROXYNAME=<PROXYNAME>,][PROXYPORT=<PROXYPORT>,][CODEC=<CODEC>,][PKTRATE=<PKTRATE>,][RTPPORT=<RTPPORT>,][RTPPRIO=<RTPPRIO>,][RTPDSCP=<RTPDSCP>,][TIMER_T1=<TIMER_T1>,][TIMER_T2=<TIMER_T2>,][SIPREGPER=<SIPREGPER>,][DTMFMODE=<DTMFMODE>,][CWSTRING=<CWSTRING>,][DISTRINGPREFIX=<DISTRINGPREFIX>,][UAHOOKFLASHCTRL=<UAHOOKFLASHCTRL>,][DNSSRV=<DNSSRV>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
SipSvcAid|System scoped SIP Profile. SipSvcAid is the AID SipSvcAid.
PRIPROXYADR|Primary SIP proxy server. PRIPROXYADR is the AID IpAid.
SECPROXYADR|Secondary SIP proxy server. SECPROXYADR is the AID IpAid.
PROXYNAME|FQDN of next hop Proxy Server for forwarding SIP messages.It should be 5 to 63 characters. PROXYNAME is a String.
PROXYPORT|UDP Port to use for SIP Proxy messaging. PROXYPORT is of type PortRange.
CODEC|Codec to use for digitization CODEC is of type Codec.
PKTRATE|Sample period to use for digitization. PKTRATE is of type PacketRate.
RTPPORT|Base UDP port to be used for RTP streams. RTPPORT is of type RTPPORT.
RTPPRIO|802.1p priority value to be used for RTP frames. RTPPRIO is of type EthPrio.
RTPDSCP|IP DSCP Value to be used for RTP PDUs. RTPDSCP is the AID DscpAid.
TIMER_T1|SIP RTT estimate. TIMER_T1 is of type TimerRange.
TIMER_T2|SIP max retransmit interval. TIMER_T2 is of type TimerRange.
SIPREGPER|Default lifetime of SIP registrations. SIPREGPER is of type TimerRange.
DTMFMODE|Enable out of band encoding of DTMF signals. DTMFMODE is of type DtmfMode.
CWSTRING|String used to identify Call Waiting tone in SIP messages. CWSTRING is a String.
DISTRINGPREFIX|text string used to identify distinctive ring in SIP messages N/A. It is up to 20 characters. DISTRINGPREFIX is a String.
UAHOOKFLASHCTRL|Handle Hook Flash events at the SIP UA (true) or send Hook Flash notification to switch (false). UAHOOKFLASHCTRL is of type BoolYN.
DNSSRV|DNS SRV control flag. DNSSRV is of type BoolYN.
DESC|A string description of the profile. DESC is a String.

##### Syntax: ```ED-PROF-TRF:[TID]:<TrfProfAid>:[CTAG]:::[[ACTIVE=<ACTIVE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
TrfProfAid|Traffic Profile Access Identifier. The address of the specific entry in Traffic Profile table. TrfProfAid is the AID AtmTrfProfProvAid.
ACTIVE|This parameter indicates that the profile may be used for new cross-connect provisioning. Setting ACTIVE=N will prevent the VOD Flow Manager from selecting a traffic profile for flow VC creation when the operator is attempting to "age out" a profile and later delete it. ACTIVE is of type BoolYN.
DESC|Description. A string description of this object, up to 11 characters in length. The string is intended to help users track profiles they create. DESC is a String.

##### Syntax: ```ED-PSD-XDSL:[TID]:<DslAid>:[CTAG]:::[[US0PSD=<US0PSD>,][VNSTART1=<VNSTART1>,][VNSTOP1=<VNSTOP1>,][VNSTART2=<VNSTART2>,][VNSTOP2=<VNSTOP2>,][VNSTART3=<VNSTART3>,][VNSTOP3=<VNSTOP3>,][VNSTART4=<VNSTART4>,][VNSTOP4=<VNSTOP4>,][VRSTART1=<VRSTART1>,][VRSTOP1=<VRSTOP1>,][VRSTART2=<VRSTART2>,][VRSTOP2=<VRSTOP2>,][VRSTART3=<VRSTART3>,][VRSTOP3=<VRSTOP3>,][VRSTART4=<VRSTART4>,][VRSTOP4=<VRSTOP4>,][VRSTART5=<VRSTART5>,][VRSTOP5=<VRSTOP5>,][VRSTART6=<VRSTART6>,][VRSTOP6=<VRSTOP6>,][VRSTART7=<VRSTART7>,][VRSTOP7=<VRSTOP7>,][VRSTART8=<VRSTART8>,][VRSTOP8=<VRSTOP8>,][VRSTART9=<VRSTART9>,][VRSTOP9=<VRSTOP9>,][VRSTART10=<VRSTART10>,][VRSTOP10=<VRSTOP10>,][VRSTART11=<VRSTART11>,][VRSTOP11=<VRSTOP11>,][VRSTART12=<VRSTART12>,][VRSTOP12=<VRSTOP12>,][VRSTART13=<VRSTART13>,][VRSTOP13=<VRSTOP13>,][VRSTART14=<VRSTART14>,][VRSTOP14=<VRSTOP14>,][VRSTART15=<VRSTART15>,][VRSTOP15=<VRSTOP15>,][VRSTART16=<VRSTART16>,][VRSTOP16=<VRSTOP16>]]; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all XDSL line units. This AID uniquely identifies which XDSL port is to be acted upon. DslAid is the AID TwentyFourPortLuAid.
US0PSD|Upstream Power Spectral Density Mask. US0PSD is of type US0PSD.
VNSTART1|The beginning frequency for the first band to skip. Value range for this parameter is [0-65535]kHz. VNSTART1 is of type RfiBand.
VNSTOP1|The ending frequency for the first band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP1 is of type RfiBand.
VNSTART2|The beginning frequency for the second band to skip. Value range for this parameter is [0-65535]kHz. VNSTART2 is of type RfiBand.
VNSTOP2|The ending frequency for the second band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP2 is of type RfiBand.
VNSTART3|The beginning frequency for the third band to skip. Value range for this parameter is [0-65535]kHz. VNSTART3 is of type RfiBand.
VNSTOP3|The ending frequency for the third band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP3 is of type RfiBand.
VNSTART4|The beginning frequency for the fourth band to skip. Value range for this parameter is [0-65535]kHz. VNSTART4 is of type RfiBand.
VNSTOP4|The ending frequency for the fourth band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP4 is of type RfiBand.
VRSTART1|The beginning frequency for the first low power band. Value range for this parameter is [0-65535]kHz. VRSTART1 is of type RfiBand.
VRSTOP1|The ending frequency for the first low power band. Value range for this parameter is [0-65535]kHz. VRSTOP1 is of type RfiBand.
VRSTART2|The beginning frequency for the second low power band. Value range for this parameter is [0-65535]kHz. VRSTART2 is of type RfiBand.
VRSTOP2|The ending frequency for the second low power band. Value range for this parameter is [0-65535]kHz. VRSTOP2 is of type RfiBand.
VRSTART3|The beginning frequency for the third low power band. Value range for this parameter is [0-65535]kHz. VRSTART3 is of type RfiBand.
VRSTOP3|The ending frequency for the third low power band. Value range for this parameter is [0-65535]kHz. VRSTOP3 is of type RfiBand.
VRSTART4|The beginning frequency for the fourth low power band. Value range for this parameter is [0-65535]kHz. VRSTART4 is of type RfiBand.
VRSTOP4|The ending frequency for the fourth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP4 is of type RfiBand.
VRSTART5|The beginning frequency for the fifth low power band. Value range for this parameter is [0-65535]kHz. VRSTART5 is of type RfiBand.
VRSTOP5|The ending frequency for the fifth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP5 is of type RfiBand.
VRSTART6|The beginning frequency for the sixth low power band. Value range for this parameter is [0-65535]kHz. VRSTART6 is of type RfiBand.
VRSTOP6|The ending frequency for the sixth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP6 is of type RfiBand.
VRSTART7|The beginning frequency for the seventh low power band. Value range for this parameter is [0-65535]kHz. VRSTART7 is of type RfiBand.
VRSTOP7|The ending frequency for the seventh low power band. Value range for this parameter is [0-65535]kHz. VRSTOP7 is of type RfiBand.
VRSTART8|The beginning frequency for the eighth low power band. Value range for this parameter is [0-65535]kHz. VRSTART8 is of type RfiBand.
VRSTOP8|The ending frequency for the eighth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP8 is of type RfiBand.
VRSTART9|The beginning frequency for the ninth low power band. Value range for this parameter is [0-65535]kHz. VRSTART9 is of type RfiBand.
VRSTOP9|The ending frequency for the ninth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP9 is of type RfiBand.
VRSTART10|The beginning frequency for the tenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART10 is of type RfiBand.
VRSTOP10|The ending frequency for the tenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP10 is of type RfiBand.
VRSTART11|The beginning frequency for the eleventh low power band. Value range for this parameter is [0-65535]kHz. VRSTART11 is of type RfiBand.
VRSTOP11|The ending frequency for the eleventh low power band. Value range for this parameter is [0-65535]kHz. VRSTOP11 is of type RfiBand.
VRSTART12|The beginning frequency for the twelfth low power band. Value range for this parameter is [0-65535]kHz. VRSTART12 is of type RfiBand.
VRSTOP12|The ending frequency for the twelfth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP12 is of type RfiBand.
VRSTART13|The beginning frequency for the thirdth low power band. Value range for this parameter is [0-65535]kHz. VRSTART13 is of type RfiBand.
VRSTOP13|The ending frequency for the thirdth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP13 is of type RfiBand.
VRSTART14|The beginning frequency for the forteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART14 is of type RfiBand.
VRSTOP14|The ending frequency for the forteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP14 is of type RfiBand.
VRSTART15|The beginning frequency for the fifteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART15 is of type RfiBand.
VRSTOP15|The ending frequency for the fifteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP15 is of type RfiBand.
VRSTART16|The beginning frequency for the sixteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART16 is of type RfiBand.
VRSTOP16|The ending frequency for the sixteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP16 is of type RfiBand.

##### Syntax: ```ED-PW:[TID]:<PwAid>:[CTAG]:::[[TMPLT=<TMPLT>,][STARTDS0=<STARTDS0>,][NDS0=<NDS0>,][IPHOSTID=<IPHOSTID>,][DSTIP=<DSTIP>,][SRCUDP=<SRCUDP>,][DSTUDP=<DSTUDP>,][RTPTS=<RTPTS>,][RTPTSMODE=<RTPTSMODE>,][FPP=<FPP>,][PYLDSIZE=<PYLDSIZE>,][JBUFDEPTH=<JBUFDEPTH>,][GOS=<GOS>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
PwAid|PW Aid pattern. PwAid is the AID PwAid.
TMPLT|Includes all the following attributes after UDP. TMPLT is the AID PwTmpltAid.
STARTDS0|First DS0 timeslot in the range of consecutive DS0 timeslots associated with the PWUSTRUCT PW. STARTDS0 is of type PwDs0TimeSlot.
NDS0|Number of consecutive DS0 timeslots associated with the PWUSTRUCT PW starting at STARTDS0. NDS0 is of type PwDs0TimeSlot.
IPHOSTID|IP Host of the PW bundle at the near-end. Slot scope IP Host identifier. IPHOSTID is the AID IPHostIdAid.
DSTIP|Destination IP address of the PW. DSTIP is the AID IpAid.
SRCUDP|Source UDP Port# identifying this PW at the given IP address. SRCUDP is of type PwUdpPort.
DSTUDP|Destination UDP Port# identifying this PW at the given IP address. DSTUDP is of type PwUdpPort.
RTPTS|Allows enabling RTP timestamp. RTPTS can only be Y when TMGMODE is set to DIFF. RTPTS is of type BoolYN.
RTPTSMODE|Timestamp generation mode -ignored if RTPTS=N. When RTPTS is enabled, if TMGMODE is set to ADAPT/LOOP/SOURCE, RTPTSMODE must be ABS; ``` and if TMGMODE is set to DIFF, RTPTSMODE must be DIFF. RTPTSMODE is of type RtpTsMode.
FPP|Number of T1 frames per packet for structured service. Packet interval is computed in the range of 0.5ms to 7.5ms. FPP is of type T1FrmsPerPkt.
PYLDSIZE|This is the size of the PWE3 payload. For PWUNSTRUCT only. PYLDSIZE must be in multiples of 32 when the container T1 port is enabled with TMGMODE as either ADAPT or DIFF. PYLDSIZE is of type PayloadSize.
JBUFDEPTH|The size of the buffer to absorb the PDV. Jitter buffer latency is based on the FramesPerPacket. Its max value for ONT PW is limited to 250000. JBUFDEPTH is of type JitBufSize.
GOS|This identifies the grade of service for performance monitoring (PM) which will be applied to the PW. GOS is the AID GosAid.
DESC|A user-settable description field, up to 31 characters. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisonable is SB. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-PWR-ADSL:[TID]:<DslAid>:[CTAG]:::[[DPBOEPSDBP1TONE=<DPBOEPSDBP1TONE>,][DPBOEPSDBP1PSD=<DPBOEPSDBP1PSD>,][DPBOEPSDBP2TONE=<DPBOEPSDBP2TONE>,][DPBOEPSDBP2PSD=<DPBOEPSDBP2PSD>,][DPBOEPSDBP3TONE=<DPBOEPSDBP3TONE>,][DPBOEPSDBP3PSD=<DPBOEPSDBP3PSD>,][DPBOEPSDBP4TONE=<DPBOEPSDBP4TONE>,][DPBOEPSDBP4PSD=<DPBOEPSDBP4PSD>,][DPBOEPSDBP5TONE=<DPBOEPSDBP5TONE>,][DPBOEPSDBP5PSD=<DPBOEPSDBP5PSD>,][DPBOEPSDBP6TONE=<DPBOEPSDBP6TONE>,][DPBOEPSDBP6PSD=<DPBOEPSDBP6PSD>,][DPBOEPSDBP7TONE=<DPBOEPSDBP7TONE>,][DPBOEPSDBP7PSD=<DPBOEPSDBP7PSD>,][DPBOEPSDBP8TONE=<DPBOEPSDBP8TONE>,][DPBOEPSDBP8PSD=<DPBOEPSDBP8PSD>,][DPBOEPSDBP9TONE=<DPBOEPSDBP9TONE>,][DPBOEPSDBP9PSD=<DPBOEPSDBP9PSD>,][DPBOEPSDBP10TONE=<DPBOEPSDBP10TONE>,][DPBOEPSDBP10PSD=<DPBOEPSDBP10PSD>,][DPBOEPSDBP11TONE=<DPBOEPSDBP11TONE>,][DPBOEPSDBP11PSD=<DPBOEPSDBP11PSD>,][DPBOEPSDBP12TONE=<DPBOEPSDBP12TONE>,][DPBOEPSDBP12PSD=<DPBOEPSDBP12PSD>,][DPBOEPSDBP13TONE=<DPBOEPSDBP13TONE>,][DPBOEPSDBP13PSD=<DPBOEPSDBP13PSD>,][DPBOEPSDBP14TONE=<DPBOEPSDBP14TONE>,][DPBOEPSDBP14PSD=<DPBOEPSDBP14PSD>,][DPBOEPSDBP15TONE=<DPBOEPSDBP15TONE>,][DPBOEPSDBP15PSD=<DPBOEPSDBP15PSD>,][DPBOEPSDBP16TONE=<DPBOEPSDBP16TONE>,][DPBOEPSDBP16PSD=<DPBOEPSDBP16PSD>,][DPBOESEL=<DPBOESEL>,][DPBOESCMA=<DPBOESCMA>,][DPBOESCMB=<DPBOESCMB>,][DPBOESCMC=<DPBOESCMC>,][DPBOMUS=<DPBOMUS>,][DPBOFMIN=<DPBOFMIN>,][DPBOFMAX=<DPBOFMAX>]]; ```

##### Parameters
Attribute | Description
|---
DslAid|DslAid is the AID TwentyFourPortLuAid.
DPBOEPSDBP1TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP1TONE is of type Tone.
DPBOEPSDBP1PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, PSD value. The valid range is from -127 to 0. DPBOEPSDBP1PSD is a Integer.
DPBOEPSDBP2TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP2TONE is of type Tone.
DPBOEPSDBP2PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, PSD value. The valid range is from -127 to 0. DPBOEPSDBP2PSD is a Integer.
DPBOEPSDBP3TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP3TONE is of type Tone.
DPBOEPSDBP3PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, PSD value. The valid range is from -127 to 0. DPBOEPSDBP3PSD is a Integer.
DPBOEPSDBP4TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP4TONE is of type Tone.
DPBOEPSDBP4PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, PSD value. The valid range is from -127 to 0. DPBOEPSDBP4PSD is a Integer.
DPBOEPSDBP5TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP5TONE is of type Tone.
DPBOEPSDBP5PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, PSD value. The valid range is from -127 to 0. DPBOEPSDBP5PSD is a Integer.
DPBOEPSDBP6TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP6TONE is of type Tone.
DPBOEPSDBP6PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, PSD value. The valid range is from -127 to 0. DPBOEPSDBP6PSD is a Integer.
DPBOEPSDBP7TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP7TONE is of type Tone.
DPBOEPSDBP7PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, PSD value. The valid range is from -127 to 0. DPBOEPSDBP7PSD is a Integer.
DPBOEPSDBP8TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP8TONE is of type Tone.
DPBOEPSDBP8PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, PSD value. The valid range is from -127 to 0. DPBOEPSDBP8PSD is a Integer.
DPBOEPSDBP9TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP9TONE is of type Tone.
DPBOEPSDBP9PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, PSD value. The valid range is from -127 to 0. DPBOEPSDBP9PSD is a Integer.
DPBOEPSDBP10TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP10TONE is of type Tone.
DPBOEPSDBP10PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, PSD value. The valid range is from -127 to 0. DPBOEPSDBP10PSD is a Integer.
DPBOEPSDBP11TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP11TONE is of type Tone.
DPBOEPSDBP11PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, PSD value. The valid range is from -127 to 0. DPBOEPSDBP11PSD is a Integer.
DPBOEPSDBP12TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP12TONE is of type Tone.
DPBOEPSDBP12PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, PSD value. The valid range is from -127 to 0. DPBOEPSDBP12PSD is a Integer.
DPBOEPSDBP13TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP13TONE is of type Tone.
DPBOEPSDBP13PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, PSD value. The valid range is from -127 to 0. DPBOEPSDBP13PSD is a Integer.
DPBOEPSDBP14TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP14TONE is of type Tone.
DPBOEPSDBP14PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, PSD value. The valid range is from -127 to 0. DPBOEPSDBP14PSD is a Integer.
DPBOEPSDBP15TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP15TONE is of type Tone.
DPBOEPSDBP15PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, PSD value. The valid range is from -127 to 0. DPBOEPSDBP15PSD is a Integer.
DPBOEPSDBP16TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP16TONE is of type Tone.
DPBOEPSDBP16PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, PSD value. The valid range is from -127 to 0. DPBOEPSDBP16PSD is a Integer.
DPBOESEL|Downstream Power Back Off, Exchange-side Electrical Length. The valid range is from 0 to 255. DPBOESEL is a Integer.
DPBOESCMA|Downstream Power Back Off, Exchange-side Cable Model Parameter A. DPBOESCMA is of type Escm.
DPBOESCMB|Downstream Power Back Off, Exchange-side Cable Model Parameter B. DPBOESCMB is of type Escm.
DPBOESCMC|Downstream Power Back Off, Exchange-side Cable Model Parameter C. DPBOESCMC is of type Escm.
DPBOMUS|Downstream Power Back Off, Minimum Usable PSD Mask. The valid range is from -127 to 0. DPBOMUS is a Integer.
DPBOFMIN|Downstream Power Back Off, Frequency Min. DPBOFMIN is of type Fmin.
DPBOFMAX|Downstream Power Back Off, Frequency Max. DPBOFMAX is of type Fmax.

##### Syntax: ```ED-PWR-XDSL:[TID]:<DslAid>:[CTAG]:::[[UPBOUS1PSDA=<UPBOUS1PSDA>,][UPBOUS1PSDB=<UPBOUS1PSDB>,][UPBOUS2PSDA=<UPBOUS2PSDA>,][UPBOUS2PSDB=<UPBOUS2PSDB>,][UPBOUS3PSDA=<UPBOUS3PSDA>,][UPBOUS3PSDB=<UPBOUS3PSDB>,][UPBOUS4PSDA=<UPBOUS4PSDA>,][UPBOUS4PSDB=<UPBOUS4PSDB>,][UPBOELELEN=<UPBOELELEN>,][DPBOEPSDBP1TONE=<DPBOEPSDBP1TONE>,][DPBOEPSDBP1PSD=<DPBOEPSDBP1PSD>,][DPBOEPSDBP2TONE=<DPBOEPSDBP2TONE>,][DPBOEPSDBP2PSD=<DPBOEPSDBP2PSD>,][DPBOEPSDBP3TONE=<DPBOEPSDBP3TONE>,][DPBOEPSDBP3PSD=<DPBOEPSDBP3PSD>,][DPBOEPSDBP4TONE=<DPBOEPSDBP4TONE>,][DPBOEPSDBP4PSD=<DPBOEPSDBP4PSD>,][DPBOEPSDBP5TONE=<DPBOEPSDBP5TONE>,][DPBOEPSDBP5PSD=<DPBOEPSDBP5PSD>,][DPBOEPSDBP6TONE=<DPBOEPSDBP6TONE>,][DPBOEPSDBP6PSD=<DPBOEPSDBP6PSD>,][DPBOEPSDBP7TONE=<DPBOEPSDBP7TONE>,][DPBOEPSDBP7PSD=<DPBOEPSDBP7PSD>,][DPBOEPSDBP8TONE=<DPBOEPSDBP8TONE>,][DPBOEPSDBP8PSD=<DPBOEPSDBP8PSD>,][DPBOEPSDBP9TONE=<DPBOEPSDBP9TONE>,][DPBOEPSDBP9PSD=<DPBOEPSDBP9PSD>,][DPBOEPSDBP10TONE=<DPBOEPSDBP10TONE>,][DPBOEPSDBP10PSD=<DPBOEPSDBP10PSD>,][DPBOEPSDBP11TONE=<DPBOEPSDBP11TONE>,][DPBOEPSDBP11PSD=<DPBOEPSDBP11PSD>,][DPBOEPSDBP12TONE=<DPBOEPSDBP12TONE>,][DPBOEPSDBP12PSD=<DPBOEPSDBP12PSD>,][DPBOEPSDBP13TONE=<DPBOEPSDBP13TONE>,][DPBOEPSDBP13PSD=<DPBOEPSDBP13PSD>,][DPBOEPSDBP14TONE=<DPBOEPSDBP14TONE>,][DPBOEPSDBP14PSD=<DPBOEPSDBP14PSD>,][DPBOEPSDBP15TONE=<DPBOEPSDBP15TONE>,][DPBOEPSDBP15PSD=<DPBOEPSDBP15PSD>,][DPBOEPSDBP16TONE=<DPBOEPSDBP16TONE>,][DPBOEPSDBP16PSD=<DPBOEPSDBP16PSD>,][DPBOESEL=<DPBOESEL>,][DPBOESCMA=<DPBOESCMA>,][DPBOESCMB=<DPBOESCMB>,][DPBOESCMC=<DPBOESCMC>,][DPBOMUS=<DPBOMUS>,][DPBOFMIN=<DPBOFMIN>,][DPBOFMAX=<DPBOFMAX>]]; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all XDSL line units. This AID uniquely identifies which XDSL port is to be acted upon. DslAid is the AID TwentyFourPortLuAid.
UPBOUS1PSDA|Upstream power back off reference PSD parameter A for US1. UPBOUS1PSDA is of type PsdA.
UPBOUS1PSDB|Upstream power back off reference PSD parameter B for US1. UPBOUS1PSDB is of type PsdB.
UPBOUS2PSDA|Upstream power back off reference PSD parameter A for US2. UPBOUS2PSDA is of type PsdA.
UPBOUS2PSDB|Upstream power back off reference PSD parameter B for US2. UPBOUS2PSDB is of type PsdB.
UPBOUS3PSDA|Upstream power back off reference PSD parameter A for US3. UPBOUS3PSDA is of type PsdA.
UPBOUS3PSDB|Upstream power back off reference PSD parameter B for US3. UPBOUS3PSDB is of type PsdB.
UPBOUS4PSDA|Upstream power back off reference PSD parameter A for US4. UPBOUS4PSDA is of type PsdA.
UPBOUS4PSDB|Upstream power back off reference PSD parameter B for US4. UPBOUS4PSDB is of type PsdB.
UPBOELELEN|Upstream power back off electrical length. UPBOELELEN is the AID EleLenAid.
DPBOEPSDBP1TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, Tone Value. DPBOEPSDBP1TONE is of type Tone.
DPBOEPSDBP1PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, PSD value. The valid range is from -127 to 0. DPBOEPSDBP1PSD is a Integer.
DPBOEPSDBP2TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, Tone Value. DPBOEPSDBP2TONE is of type Tone.
DPBOEPSDBP2PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, PSD value. The valid range is from -127 to 0. DPBOEPSDBP2PSD is a Integer.
DPBOEPSDBP3TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, Tone Value. DPBOEPSDBP3TONE is of type Tone.
DPBOEPSDBP3PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, PSD value. The valid range is from -127 to 0. DPBOEPSDBP3PSD is a Integer.
DPBOEPSDBP4TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, Tone Value. DPBOEPSDBP4TONE is of type Tone.
DPBOEPSDBP4PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, PSD value. The valid range is from -127 to 0. DPBOEPSDBP4PSD is a Integer.
DPBOEPSDBP5TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, Tone Value. DPBOEPSDBP5TONE is of type Tone.
DPBOEPSDBP5PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, PSD value. The valid range is from -127 to 0. DPBOEPSDBP5PSD is a Integer.
DPBOEPSDBP6TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, Tone Value. DPBOEPSDBP6TONE is of type Tone.
DPBOEPSDBP6PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, PSD value. The valid range is from -127 to 0. DPBOEPSDBP6PSD is a Integer.
DPBOEPSDBP7TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, Tone Value. DPBOEPSDBP7TONE is of type Tone.
DPBOEPSDBP7PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, PSD value. The valid range is from -127 to 0. DPBOEPSDBP7PSD is a Integer.
DPBOEPSDBP8TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, Tone Value. DPBOEPSDBP8TONE is of type Tone.
DPBOEPSDBP8PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, PSD value. The valid range is from -127 to 0. DPBOEPSDBP8PSD is a Integer.
DPBOEPSDBP9TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, Tone Value. DPBOEPSDBP9TONE is of type Tone.
DPBOEPSDBP9PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, PSD value. The valid range is from -127 to 0. DPBOEPSDBP9PSD is a Integer.
DPBOEPSDBP10TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, Tone Value. DPBOEPSDBP10TONE is of type Tone.
DPBOEPSDBP10PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, PSD value. The valid range is from -127 to 0. DPBOEPSDBP10PSD is a Integer.
DPBOEPSDBP11TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, Tone Value. DPBOEPSDBP11TONE is of type Tone.
DPBOEPSDBP11PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, PSD value. The valid range is from -127 to 0. DPBOEPSDBP11PSD is a Integer.
DPBOEPSDBP12TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, Tone Value. DPBOEPSDBP12TONE is of type Tone.
DPBOEPSDBP12PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, PSD value. The valid range is from -127 to 0. DPBOEPSDBP12PSD is a Integer.
DPBOEPSDBP13TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, Tone Value. DPBOEPSDBP13TONE is of type Tone.
DPBOEPSDBP13PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, PSD value. The valid range is from -127 to 0. DPBOEPSDBP13PSD is a Integer.
DPBOEPSDBP14TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, Tone Value. DPBOEPSDBP14TONE is of type Tone.
DPBOEPSDBP14PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, PSD value. The valid range is from -127 to 0. DPBOEPSDBP14PSD is a Integer.
DPBOEPSDBP15TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, Tone Value. DPBOEPSDBP15TONE is of type Tone.
DPBOEPSDBP15PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, PSD value. The valid range is from -127 to 0. DPBOEPSDBP15PSD is a Integer.
DPBOEPSDBP16TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, Tone Value. DPBOEPSDBP16TONE is of type Tone.
DPBOEPSDBP16PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, PSD value. The valid range is from -127 to 0. DPBOEPSDBP16PSD is a Integer.
DPBOESEL|Downstream Power Back Off, Exchange-side Electrical Length. The valid range is from 0 to 255. DPBOESEL is a Integer.
DPBOESCMA|Downstream Power Back Off, Exchange-side Cable Model Parameter A. DPBOESCMA is of type Escm.
DPBOESCMB|Downstream Power Back Off, Exchange-side Cable Model Parameter B. DPBOESCMB is of type Escm.
DPBOESCMC|Downstream Power Back Off, Exchange-side Cable Model Parameter C. DPBOESCMC is of type Escm.
DPBOMUS|Downstream Power Back Off, Minimum Usable PSD Mask. The valid range is from -127 to 0. DPBOMUS is a Integer.
DPBOFMIN|Downstream Power Back Off, Frequency Min. DPBOFMIN is of type Fmin.
DPBOFMAX|Downstream Power Back Off, Frequency Max. DPBOFmax must be no less than (DPBOFmin+2). DPBOFMAX is of type Fmax.

##### Syntax: ```ED-RADIUS:[TID]::[CTAG]:::[[AMP=<AMP>,][AMP2=<AMP2>,][RADIP=<RADIP>,][RADPORT=<RADPORT>,][RAD2IP=<RAD2IP>,][RAD2PORT=<RAD2PORT>,][SECRET=<SECRET>,][TMOUT=<TMOUT>,][RETRIES=<RETRIES>]]; ```

##### Parameters
Attribute | Description
|---
AMP|Primary AMP to be used as a RADIUS client. This AMP should have IP connectivity to the RADIUS server. AMP is the AID MsAid. The default value is "NONE".
AMP2|Alternate (fallback) AMP to use for RADIUS client. This AMP should have IP connectivity to the RADIUS server. AMP2 is the AID MsNoneAid. The default value is "NONE".
RADIP|IP address of the primary RADIUS server. RADIP is the AID IpAid. The default value is "0.0.0.0".
RADPORT|UDP port for the primary RADIUS server. RADPORT is a Integer. The default value is "1812".
RAD2IP|IP address of the alternate (fallback) RADIUS server. RAD2IP is the AID IpAid. The default value is "0.0.0.0".
RAD2PORT|UDP port for the alternate (fallback) RADIUS server. RAD2PORT is a Integer. The default value is "1812".
SECRET|The "shared secret" known to both RADIUS client and server. This is an ascii string of up to 16 characters. SECRET is a String. The default value is """".
TMOUT|Timeout in seconds when waiting for a response from the RADIUS server. The timeout must be in the interval [5,60]. TMOUT is a Integer. The default value is "8".
RETRIES|Number of times to retry a request after timeout. Retries must be in the interval [0,5]. RETRIES is a Integer. The default value is "2".

##### Syntax: ```ED-RFVID:[TID]:<OntPortAid>:[CTAG]:::[[ENONBAT=<EONBAT>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Rf-Video Port Access Identifer. The address of the RFVID port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortAid.
EONBAT|For ONT ports, this parameter specifies the behavior the port when the ONT is running on battery backup, and overrides the default (ONTRFVIDONBAT) specified by ED-SYS. EONBAT is of type OntPortPwrOpt.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-RMTDEV:[TID]:<RmtDevAid>:[CTAG]:::[[SERIAL=<SERIAL>,][DEVNAME=<DEVNAME>,][DEVTYPE=<DEVTYPE>,][MGMTIP=<MGMTIP>,][PLOCN=<PLOCN>,][SAMENODE=<SAMENODE>,][SIPVCG=<SIPVCG>]]; ```

##### Parameters
Attribute | Description
|---
RmtDevAid|Remote Device Access Identifier. RmtDevAid is the AID RmtDevAid.
SERIAL|The remote device serial number. This may correspond to a backplane identifier, or some other means of identifying the physical piece of equipment. SERIAL is a String.
DEVNAME|The name of the remote device. This could be the CLLI code of a network element, or an arbitrary name assigned to the device DEVNAME is a String.
DEVTYPE|The type of the Remote Device. DEVTYPE is of type RmtDeviceType.
MGMTIP|The IP address(es) of the device to which an operator or the CMS can connect. MGMTIP is the AID IpAid.
PLOCN|The identifier(s) of the physical port(s) to which the remote device is connected. This can include in-band ports such as a GE or OCn port, or a port on the AMP. PLOCN is the AID RmtDevDiscAid.
SAMENODE|This indicates if the device is considered part of the same node for management purposes. In a general sense, a node refers to co-located equipment of performing a collective function. SAMENODE is of type BoolYN.
SIPVCG|The SIP VCG created for managing SIP-based subscribers. The SIP VCG is required if this device will use a PSTN gateway capabilities of the C7 SIPVCG is the AID IgAid.

##### Syntax: ```ED-SERIAL:[TID]:<SerialPortAid>:[CTAG]::[<PARITY>],[<STOPB>],[<BRATE>],[<DATABITS>]:[CHAP=<CHAP>]; ```

##### Parameters
Attribute | Description
|---
SerialPortAid|Serial Port Access Identifier. The address of the serial port to be set. SerialPortAid is the AID SerialPort.
PARITY|Parity. This parameter indicate the parity for the serial port. If parameter is not entered, then value does not change from current values. PARITY is of type Parity. The default value is "NONE".
STOPB|STOP Bits. The number of stop bits used for this port. STOPB is of type StopBits. The default value is "1".
BRATE|Baud RATE. This parameter indicates the baud rate for the serial port. If parameter is not entered, then value does not change from current values. BRATE is of type BaudRate. The default value is "38400".
DATABITS|DATA BITS. The number of data bits allowed. DATABITS is of type DataBits. The default value is "8".
CHAP|Channel Access Privileges. This parameter indicates the privileges which are allowed on the serial port. At system initialization the default value is FULLACC for all serial ports. CHAP is of type CidSecurity. The default value is "FULLACC".

##### Syntax: ```ED-SHELF:[TID]:<ShelfAid>:[CTAG]::[<BackplaneNo>]:[[PWRCAT3=<PWRCAT3>,][DCIN=<DCIN>,][EXPRESSLINKS=<EXPRESSLINKS>,][DEFAULTVB=<DEFAULTVB>,][ROGDTCT=<ROGDTCT>,][AUTOQUAR=<AUTOQUAR>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. If a BackplaneNo is NOT specified, this is the address of the shelf where the shelf parameters are to be modified. If a BackplaneNo is specified, this is the new Shelf AID to be assigned to the shelf with this backplane number. ShelfAid is the AID ShelfAid.
BackplaneNo|If specified, this is the serial number of the backplane for the shelf to be edited. The shelf will have its Shelf AID updated to the one given in the ShelfAid field. If this field is not given the command is applied to the shelf identified in the ShelfAid field. Note that to input a HEX-value, the leading 2 characters shoule be 0x (zero x). Otherwise, the value will be processed as a Decimal-value. BackplaneNo is a String.
PWRCAT3|Power Category 3 Shutdown time. This is the time equipment assigned to power category 3 is allowed to remain powered up after the system switches to emergency backup power. PWRCAT3 is of type PowerCat3Time.
DCIN|DC Inputs. This parameter indicates the type of DC power being supplied to the shelf. DCIN is of type DCIN.
EXPRESSLINKS|Express Links. When set to Y, this will cause the system will attempt to save bandwidth on cross-connects the following criteria: 1) Connection is of type T0, T1, VP or VC. 2) Connection is on an intermediate transport shelf that is ATM-capable. 3) Source and destination are on slots 9-12, CSA and CSB. 4) Connection is bi-directional, or a unicast VOD connection. 5) Connection is unprotected or is going to an unprotected destination. Note that INCL=Y must also be specified when changing this parameter, as the shelf will reboot as a result! EXPRESSLINKS is of type BoolYN.
DEFAULTVB|Default VB number for this shelf. DEFAULTVB is of type VbNum.
ROGDTCT|System will enable rogue detection on PONs by default. ROGDTCT is of type BoolYN.
AUTOQUAR|System will auto quarantine Rogue ONTs. AUTOQUAR is of type BoolYN.
INCL|Inclusive. This parameter must be specified to force changing the value of EXPRESSLINKS. INCL is of type BoolYN.

##### Syntax: ```ED-SIP:[TID]:<IgAid>:[CTAG]:::[[PRICFGURL=<PRICFGURL>,][SECCFGURL=<SECCFGURL>,][HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>,][MAXACTCALLS=<MAXACTCALLS>,][OPTION82=<OPTION82>,][DNSSVR=<DNSSVR>,][SECDNSSVR=<SECDNSSVR>,][ETHPRIO=<ETHPRIO>,][ECENABLE=<ECENABLE>,][DSCP=<DSCP>,][VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][ECTAIL=<ECTAIL>,][SIPSVCPROF=<SIPSVCPROF>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|Access Identifier for the SIP Group. IgAid is the AID IgAid.
PRICFGURL|PRImary ConFiGuration Uniform Resource Locator. URL of the configuration needed to access the SIP network. Currently TFTP access and direct registration with the SIP registrar are supported. The value can take following 1 of 2 formats: "TFTP: //IP address of TFTP server/Path to Config File" or "REGISTER SIP: IP address of SIP registrar" PRICFGURL is a String.
SECCFGURL|SECondary ConFiGuration Uniform Resource Locator. URL of backup network access configuration. The value takes the same format as PRICFGURL. SECCFGURL is a String.
HOSTPROTO|Protocol to be used to obtain the IP address for the host for SIP lines in the group. HOSTPROTO is of type SipHostProto.
IP|IP address. Statically assigned IP address associated with the group. IP is the AID IpAid.
IPMSK|Subnet IP MASK. IPMSK is the AID IpAid.
GADDR|Subnet IP GATEWAY Address. Statically assigned IP address associated with the group's gateway. GADDR is the AID IpAid.
MAXACTCALLS|Maximum number of concurrent calls (up to 384) for this IG. MAXACTCALLS is a Integer.
OPTION82|Indicates whether DHCP Relay Option 82 is enabled.This field is only used for C7 SIP service. It has been deprecated since C7 9.0. OPTION82 is of type Option82.
DNSSVR|IP Address of Primary DNS Server. DNSSVR is the AID IpAid.
SECDNSSVR|IP Address of Secondary DNS Server. SECDNSSVR is the AID IpAid.
ETHPRIO|802.1p priority value to be used for SIP messages. ETHPRIO is of type EthPrio.
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN.
DSCP|IP DSCP Value to be used for SIP messages. DSCP is the AID DscpAid.
VLAN|The integer value of the VLAN. VLAN is the AID VlanIndexAid.
BRIDGE|The virtual bridge providing Ethernet services. BRIDGE is the AID BridgeProvAid.
ECTAIL|ECTAIL. ECTAIL is of type Ectail.
SIPSVCPROF|SIP service profile index. SIPSVCPROF is the AID SipSvcAid.
PST|PST is of type PrimaryStateChg.

##### Syntax: ```ED-SIPT0:[TID]:<T0Aid>:[CTAG]:::[[SIPIG=<SIPIG>,][USER=<USER>,][AOR=<AOR>,][PID=<PID>,][HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>]]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0Aid is the AID SipT0PortAid.
SIPIG|SIP Group AID. SIPIG is the AID IgAid.
USER|User Name. User name for the subscriber. This string is used to form the UserId field toe the left of the @ in the SIP URL. It is also used as the username for authentication protocols. The value is a character string up to 20 bytes. It must be the AID of a legacy telephony interface provided by a C7. USER is a String.
AOR|Address Of Record. This is an alphanumeric string that describes the phone number used to reference a user in the network. The value is a character string up to 32 bytes. AOR is a String.
PID|Password. Password for authorization of the subscriber. The value is a character string up to 20 bytes. PID is a String.
HOSTPROTO|HOSTPROTO is of type SipT0HostProto.
IP|IP is the AID IpAid.
IPMSK|IPMSK is the AID IpAid.
GADDR|GADDR is the AID IpAid.

##### Syntax: ```ED-SIPVCG:[TID]:<IgAid>:[CTAG]:::[[CTLIP=<CTLIP>,][MAXACTCALLS=<MAXACTCALLS>,][ECENABLE=<ECENABLE>,][EPCD=<EPCD>,][ECTAIL=<ECTAIL>,][VSPIP=<VSPIP>,][VSPUDP=<VSPUDP>,][SUBNET=<SUBNET>,][RTRAID=<RTRAID>,][VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][PKTRATE=<PKTRATE>,][RETRYTMR=<RETRYTMR>,][UDPSTART=<UDPSTART>,][LEASETIME=<LEASETIME>,][FORCERENEW=<FORCERENEW>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|Ig Number within a shelf. IgAid is the AID IgAid.
CTLIP|Control IP Address. IP address for control message transport. This IP address is used to contact both the SIP registrar and the SIP user agents associated with the IG. CTLIP is the AID IpAid.
MAXACTCALLS|MAXACTCALLS is a Integer.
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN.
EPCD|Echo Path Change Detection. EPCD=Y is only effective when ECCONFIG=SPARSE on the supporting equipement (VGP/VIPR). Enabling EPCD improves the ability to track changes in the echo path, but reduces channel density. EPCD is of type BoolYN.
ECTAIL|ECTAIL is a Integer.
VSPIP|This parameter is only applicable when the associated VSP resource resides on an EGW. VSPIP is the AID IpAid.
VSPUDP|This parameter is only applicable when the associated VSP resource resides on an EGW. Allowable values are 49408, 53504, 57600, and 61696. VSPUDP is a Integer.
SUBNET|SUBNET is the AID IpAid.
RTRAID|RTRAID is the AID VrAid.
VLAN|The integer value of the VLAN. VLAN is the AID VlanIndexAid.
BRIDGE|LOCAL is not valid for this command. BRIDGE is the AID BridgeProvAid.
PKTRATE|PKTRATE is a Integer.
RETRYTMR|RETRYTMR is a Integer.
UDPSTART|UDPSTART is restricted to the values 49408, 53504, 57600, and 61696 UDPSTART is a Integer.
LEASETIME|LEASETIME is a Integer.
FORCERENEW|FORCERENEW is of type BoolYN.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "OOS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-SNMP:[TID]::[CTAG]:::[[SNMPVER=<SNMPVER>,][ROCOMMSTRING=<ROCOMMSTRING>,][TRAPPORT=<TRAPPORT>]]; ```

##### Parameters
Attribute | Description
|---
SNMPVER|SNMP Version. SNMPVER is of type SnmpVersion and is listable.
ROCOMMSTRING|Read-Only Community String. This identifies the Community String (up to 20 characters) that must be used by the SNMP manager when performing SNMP Get operations on the C7 network. ROCOMMSTRING is a String. The default value is "public".
TRAPPORT|The Management port through which Traps are emitted. TRAPPORT is the AID IfConfigAidNone.

##### Syntax: ```ED-SNMP-TRAP:[TID]:<TrapAid>:[CTAG]:::[[IP=<IP>,][UDPPORT=<UDPPORT>,][COMMSTRING=<COMMSTRING>,][SNMPVER=<SNMPVER>,][PID=<PID>]]; ```

##### Parameters
Attribute | Description
|---
TrapAid|SNMP Trap Access Identifier. This identifies a particular trap recipient. TrapAid is the AID TrapAid.
IP|Recipient IP address. IP is the AID IpAid.
UDPPORT|UDP Port. This parameter identifies the port where the trap is to be sent. UDPPORT is of type UdpPort.
COMMSTRING|Community String. This identifies the Community String (up to 20 characters) to be used when sending traps. COMMSTRING is a String.
SNMPVER|SNMP Version. SNMPVER is of type SnmpVersion.
PID|Password, up to 20 characters. This parameter is applicable only if the SNMPVER is V3. PID is not displayed on retrieval. PID is a String.

##### Syntax: ```ED-SSH:[TID]::[CTAG]:::[[HASH=<HASH>,][CIPHER=<CIPHER>]]; ```

##### Parameters
Attribute | Description
|---
HASH|The allowed hashes or MACs (Message Authentication Codes). HASH is of type SshHash and is listable.
CIPHER|The allowed encryption schemes. CIPHER is of type SshCipher and is listable.

##### Syntax: ```ED-STP-GROUP:[TID]:<StpGroupAid>:[CTAG]:::[[HELLOTMR=<HELLOTMR>,][FWDDLYTMR=<FWDDLYTMR>,][MAXAGETMR=<MAXAGETMR>,][PRIO=<PRIO>]]; ```

##### Parameters
Attribute | Description
|---
StpGroupAid|Spanning Tree Group Access Identifier. StpGroupAid is the AID StpGroupAid.
HELLOTMR|Value range is [1, 2]. HELLOTMR is a Integer.
FWDDLYTMR|Monitors the time spent by a port in the learning and listening states. The timeout value is the forward delay parameter of the switches. This value is in Seconds. Value range is [4, 30]. FWDDLYTMR is a Integer.
MAXAGETMR|Measures the age of the received protocol information recorded for a port and ensure that this information is discarded when its age limit exceeds the value to the maximum age parameter recorded by the switch. The timeout value for this timer is the maximum age parameter of the switches. This values is in Seconds. Value range is [6, 40]. MAXAGETMR is a Integer.
PRIO|Priority of the Spanning Tree Group. The value must be a multiple of 4096 in the range [0-61140]. PRIO is a Integer.

##### Syntax: ```ED-SYS:[TID]::[CTAG]:::[[ADMIN=<ADMIN>,][TDMBWC=<TDMBWC>,][DEFONTPROF=<DEFONTPROF>,][VCPOOL=<VCPOOL>,][VPPOOL=<VPPOOL>,][PROVLOCK=<PROVLOCK>,][VIDPROV=<VIDPROV>,][NTWKNAME=<NTWKNAME>,][REVERTENABLED=<REVERTENABLED>,][ONTETHONBAT=<ONTETHONBAT>,][ONTRFVIDONBAT=<ONTRFVIDONBAT>,][RSVDVLANSTART=<RSVDVLANSTART>]]; ```

##### Parameters
Attribute | Description
|---
ADMIN|Administrative Master. The Administrative Master is the location where data which is required to be maintained across the network is controlled. ADMIN is the AID ShelfAid.
TDMBWC|Enable TDM bandwidth constraint. If set to Y, this will require that all TDM connections created using the ENT-CRS-T0 command to be routed via links that have some bandwidth reserved for the TDM Bandwidth Constraint Id. TDMBWC is of type BoolYN.
DEFONTPROF|Default ONT Profile. If set, this ONT profile will be used when not specified in ENT-ONT. DEFONTPROF is the AID SystemId1.
VCPOOL|VCPOOL : Protected VC Label Space. The value for VCPOOL is an VPI number between 1 and 4094. VC Label space is defaulted to 4094 if no value is specified. This value can be modified to any available VPI number. Once VCPOOL is modified, the modified value will be used for subsequent protected connections, but will not modify any existing connections. VCPOOL is a Integer.
VPPOOL|VPPOOL : Protected VP Label Space.
This label space range is used for internal VP creation. The values entered represent the start and end of the label space range and it can be any available range of VPI numbers.

Once VPPOOL is modified, the modified values will be used for subsequent protected connections, but will not modify any existing connections. The default range for VPPOOL is 4000&&4090. VPPOOL is a Integer and is rangeable.

PROVLOCK|Provisioning Lock PROVLOCK is of type BoolYN.
VIDPROV|Video Provisioning Mode in network. Video Transport can either be provisioned using Video VC cross-connects or using aggregated bandwidth constraint links. VIDPROV is of type VidProvMode.
NTWKNAME|Network Name - 20 character string. NTWKNAME is a String.
REVERTENABLED|This parameter is deprecated in C7 release 7.0. Revert Enabled. The C7 periodically determines whether or not there is enough flash space available to support an upgrade and a full revert. If the C7 determines that there is not enough flash space available, the PROVCAPTHR or PROVCAPOVF alarm is raised. These alarms may be cleared by disabling the full revert capability by setting this flag to 'N'. REVERTENABLED is of type BoolYN.
ONTETHONBAT|This is the system default for determining if ONT ETH ports should remain enabled when the ONT is operating on battery backup. The default can be overridden on a per ONT port basis. ONTETHONBAT is of type BoolYN.
ONTRFVIDONBAT|This is the system default for determining if ONT RFVID ports should remain enabled when the ONT is operating on battery backup. The default can be overridden on a per ONT port basis. ONTRFVIDONBAT is of type BoolYN.
RSVDVLANSTART|C7 reserves 4 VLANs for internal use. These are consecutive VLANs, beginning with the value identified with this field. In order to change this value, there must not be any current provisioning in this range on any shelf. RSVDVLANSTART is the AID VlanRsvdIndexStart.

##### Syntax: ```ED-SYS-SECU:[TID]::[CTAG]:::[[PIDLEN=<PIDLEN>,][SPECIAL=<SPECIAL>,][NONALPHA=<NONALPHA>,][SUBSTR=<SUBSTR>,][MXINV=<MXINV>,][SSH=<SSH>,][AUTH=<AUTH>,][AMPROUTER=<AMPROUTER>]]:[<BANNER>]; ```

##### Parameters
Attribute | Description
|---
PIDLEN|PID LENgth. Minimum number of password characters - an integer in the range [4,16]. PIDLEN is a Integer. The default value is "6".
SPECIAL|SPECIAL characters. Minimum number of special characters (i.e. "@ # $ % [ ] ~ ! _ | ?" ) Range is from 0-16. SPECIAL is a Integer. The default value is "1".
NONALPHA|NON-ALPHAnumeric characters. Minimum number of non-alpha characters (special or numeric). Range is from 0-16. NONALPHA is a Integer. The default value is "2".
SUBSTR|SUBSTRing. Is the UID allowed as a substring of the PID ? SUBSTR is of type BoolYN. The default value is "N".
MXINV|MaXimum INValid login attempts. A telnet session will be dropped upon this number of successive login failures. 2 <= MXINV <= 6. MXINV is a Integer. The default value is "3".
SSH|Activate Secure Shell for all login channels. SSH is of type BoolYN. The default value is "N".
AUTH|User Authentication Mode. AUTH is of type UserAuthMode. The default value is "LOCAL".
AMPROUTER|AMP as ROUTER. If enabled, static routes provisioned on an AMP will be used to route incoming packets from one management interface to another. If disabled, the AMP functions only as an IP host. AMPROUTER is of type BoolYN. The default value is "N".
BANNER|BANNER String of up to 79 characters displayed upon each login. BANNER is a String. The default value is "*** WELCOME TO THE CALIX C7. AUTHORIZED ACCESS ONLY. *** ".

##### Syntax: ```ED-T0:[TID]:<T0Aid>:[CTAG]:::[[GSFN=<GSFN>,][RTLP=<RTLP>,][TTLP=<TTLP>,][Z=<Z>,][EBSLVL=<EBSLVL>,][EFTT=<EFTT>,][RATE=<RATE>,][EC=<EC>,][ZCS=<ZCS>,][SC=<SC>,][TIMEOUT=<TIMEOUT>,][LLBE=<LLBE>,][DDSTEST=<DDSTEST>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Port Access Identifier. The address of the T0 port for which the parameters are being modified. T0Aid is the AID TwentyFourPortLuAid.
GSFN|General Signaling Function. This indicates the signaling used by the T0 port, such as loop start, ground start, etc. Note: 4DU is valid for the OCUDPx6 line unit. 4D0 is valid for the DS0DPx6 line unit. GSFN is of type GenSigFunction.
RTLP|Receive Transmission Loss Plan. Transmission level point for receiving from the equipment. The transmission level point is the decibel value of the ratio of the power of a 1004 Hz signal at a point to the power of the same signal at a reference point on the digital side of the codec. Therefore, an increase in the RTLP will result in a gain toward the analog side. The default is set to match the standard settings for an RPOTS card. RTLP is of type Rlp. The default value is "-2.0".
TTLP|Transmit Transmission Loss Plan. Transmission level point for transmitting toward the equipment. The transmission level point is the decibel value of the ratio of the power of a 1004 Hz signal at a point to the power of the same signal at a reference point on the digital side of the codec. Therefore, an increase in the TTLP will result in a gain toward the digital side. The default is set to match the standard settings for an RPOTS card. TTLP is of type Tlp. The default value is "-2.0".
Z|Impedance. This parameter indicates the expected impedance of the line in Ohms. Z is of type ImpedanceOhms.
EBSLVL|Electronic Business Service LeVeL This attribute is only applicable to Nortel's Electronic Business Service. It specifies the level of the secondary signaling channel. EBSLVL is of type EBSLvl.
EFTT|Enable Full-Time Transmission. This attribute is set to Y to enable transmission of the audio channel even when the subscriber is on-hook and the phone has not recently been rung. EFTT is of type BoolYN.
RATE|Data Rate. (DDS only) Note: Changing rates terminates the loopbacks on an OCUDP line unit due to the required reset on hardware. RATE is of type DdsRate.
EC|Error Correction. (DDS only) This parameter is valid if there are no cross connections. A value of EC=Y is invalid if one cross connection exists for 56 and 64 kbps rates and cross connect must be deleted first. EC=Y is also invalid if two cross connections exist for 2.4, 4.8, 9.6 and 19.2 kbps rates and cross connect must be deleted first. A value of EC=N is invalid if two cross connection exists at any data rates and cross connection must be deleted first. EC is of type BoolYN.
ZCS|Zero Code Supression. (DDS only) ZCS is of type BoolYN.
SC|Secondary Channel. (DDS only) This parmater is only valid for OCUDPx6 line unit. It can be entered for the DS0Dpx6 line unit, but it will be ignored. Note that SC=Y is invalid for 64 kbps rate. Also SC=N is always valid without any restrictions. SC is of type BoolYN.
TIMEOUT|Latching Loopback Timeout (in minutes). (DDS only) If TIMEOUT = 0, Latching loopback continues to operate, but it cancels the timer if active. If TIMEOUT > 0, the new timeout value is applied to the currently active latching loopback or subsequent loopback. If the new timeout value is greater than the previous value, the difference is applied to the currently outstanding timer. If the new timeout value is less than the previous value, the loopback terminates. If the new timeout value is the same as before, no further action is required. TIMEOUT is of type LatchLpbkTimeout.
LLBE|Latching LoopBack Enable. (DDS only) LLBE is of type BoolYN.
DDSTEST|DDS Test Mode (DDS only). The DDS card supports two modes of loop testing: Bipolar (analog) and Logic Near/Far (digital TTY). This parameter indicates which mode is to be used. DDSTEST is of type DdsTest.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. Note: For OOS, DDS service is disabled. For OCUDP, sealing current is revmoved. For IS, DDS service is enabled. For OCUDP, sealing current is applied. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service states which can be changed are redline and SB. The redline state indicates that the line cannot be deleted unless, redline is removed from the service state first. SB indicates that both Tx and Rx should be suspended. SST is of type SecondaryStateChg and is listable.

##### Syntax: ```ED-T1:[TID]:<Ds1Aid>:[CTAG]:::[[TYPE=<TYPE>,][T1MAP=<T1MAP>,][EQLZ=<EQLZ>,][ATTEN=<ATTEN>,][PWR=<PWR>,][FMT=<FMT>,][LINECDE=<LINECDE>,][GOS=<GOS>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][EXT=<EXT>,][PDOM=<PDOM>,][NDS0RESVD=<NDS0RESVD>,][TMGMODE=<TMGMODE>,][IBLBEN=<IBLBEN>,][CAS=<CAS>,][IBLBCODE=<IBLBCODE>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port being modified. Ds1Aid is the AID TwelvePortLuAid.
TYPE|TYPE of T1. This indicates whether the port is to be configured as a DS1 or a T1. TYPE is of type T1Type.
T1MAP|MAPping of the payload signal. When payload signal is a form that may be altered at the T1 port, this parameter specifies the mapping. Otherwise, its value should be NA. T1MAP is of type T1Map.
EQLZ|Equalization. Indicates equalization setting (aka Line Build Out). It applies only when TYPE=DS1. EQLZ is of type Equalization.
ATTEN|ATTENuation. Indicates the attenuation for T1 lines. It applies only when TYPE=T1. ATTEN is of type Attenuation.
PWR|Line PoWeRing. This parameter indicates whether the line is to supply power. PWR is of type T1Pwr.
FMT|DS1 Format. This parameter indicates DS1 signal format. FMT is of type FormatSignal.
LINECDE|Line Code. This is the provisioned DS1 line coding. LINECDE is of type LineCode.
GOS|Grade of Service Access Identifier. This is the T1 Grade of Service which is to be applied to the DS1. GOS is the AID GosAid.
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. It is only applicable when T1MAP is UNI or NNI. PYLDSCRM is of type BoolYN.
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. ATMMON is of type BoolYN.
EXT|External Interface. This indicates if the T1 is an internal or external path in the network. The value should be set to "Y" when the port is an external interface. It should be set to "N" when the port is connected to other shelves within a network of C7s. This parameter is valid only if T1MAP is NNI. Note that this parameter must be changed independently of others, ie. a separate ED-T1 command is required. EXT is of type BoolYN.
PDOM|Protection DOMain. This is an integer that is used to associate a transport facility into a protection domain that is used for A to Z connection provisioning. The PDOM for each domain must be a unique non-zero integer. The value of 0 is reserved to indicate that the facility is not to be used for A to Z connections. PDOM is of type Pdom.
NDS0RESVD|Number of Reserved DS0s. This parameter indicates the number of sequential DS0s that are to be reserved in a T1 facility that has a non-DS0 mapping for the remainder of its payload. The DS0s reserved are sequential decreasing from time slot 24. This parameter is only applicable when T1MAP is NNI or UNI. NDS0RESVD is a Integer.
TMGMODE|Timing Mode. This parameter selects the timing source for the T1 port transmit signal. TMGMODE defaults to LOOP for ATM interfaces (i.e. T1MAP of UNI or NNI). For non-ATM interfaces, TMGMODE will default to LOOP when FMT=UF, else TMGMODE will default to SOURCE. TMGMODE is of type T1TimingMode.
IBLBEN|Enable/Disable the ability of the hardware to activate or deactivate remotely controlled T1 loopbacks. IBLBEN is of type BoolYN.
CAS|The signaling bits are carried in the TDM data, as well as in the signaling substructure. CAS enabled/ disabled shall affect all PWs on the Port. CAS is of type BoolYN.
IBLBCODE|Inband Loopback code. If detected in the egress direction, terminal loopback will be performed automatically on this T1 port. "Inband Loopback Terminal" condition will be also raised. Loop down code detected in egress direction will remove this condition. If detected in the ingress direction, facility loopback will be performed automatically on this T1 port. "Inband Loopback Facility" condition will be also raised. Loop down code detected in ingress direction will remove this condition. In addition, the "Inband Loopback Facility/Terminal" condition can be overridden administratively. User can perform OPR-LPBK-T1 to override inband loopback condition to administrative loopback, then use RLS-LPBK-T1 to release the loopback. For ONT T1 port, it only can be set to "11000". IBLBCODE is a String.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-T3:[TID]:<Ds3Aid>:[CTAG]:::[[INTF=<INTF>,][AIS=<AIS>,][AIST=<AIST>,][IDLE=<IDLE>,][FMT=<FMT>,][LBO=<LBO>,][GOS=<GOS>,][EXT=<EXT>,][ATM=<ATM>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][PDOM=<PDOM>,][TMGMODE=<TMGMODE>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifer. The address of the T3 port being modified. Ds3Aid is the AID T3Aid.
INTF|Interface Type. The type of interface being provided by the DS3. When the equipment type is DS3-12s the interface type must be CCHAN. When the equipment type is DS3-12p, the interface type must be either NNI or UNI. INTF is of type T3Interface.
AIS|Alarm Indication Signal. Indicates whether AIS is transmitted from the DS3 being provisioned. AIS is of type BoolYN.
AIST|AIS Type. This parameter indicates the type of the AIS signal to be generated/transmitted, and the AIS signal mode expected on input should a failure condition occur. When the card type is a DS3-12p, then only a value of NAS will be accepted. AIST is of type AisType.
IDLE|Idle signal. This parameter indicates the transmission or non-transmission of the IDLE signal. For Ds3S(CCHAN) card IDLE can be transmitted only in the INGRESS direction and not the EGRESS direction. For Ds3 packet card IDLE can be transmitted only in the EGRESS direction. IDLE is of type Idle.
FMT|DS3 Format. This parameter indicates DS3 signal format. FMT is of type FormatT3.
LBO|Line Build Out. This parameter indicates the line build out setting. LBO is a Integer.
GOS|Grade of Service Access Identifier. This is the T3 Grade of Service which is to be applied to the DS3. GOS is the AID GosAid.
EXT|External Interface. This indicates if the T3 is an internal or external path in the network. The value should be set to "Y" when the port is an external interface. It should be set to "N" when the port is connected to other shelves within a network of C7s. For INTF=CCHAN, EXT must be Y. Note that this parameter must be changed independently of others, ie. a separate ED-T3 command is required. EXT is of type BoolYN.
ATM|ATM Mapping. This parameter indicates how the ATM payload is mapped into the DS3 Frame. If the INTF parameter is set to CCHAN this parameter is invalid. ATM is of type ATMPayload.
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. If the INTF parameter is set to CCHAN this parameter is invalid. PYLDSCRM is of type BoolYN.
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. ATMMON is of type BoolYN.
PDOM|Protection domain. This is an integer that is used to associate FFPs into a coordinated protection domain. The PDOM for each domain must be a unique integer. If the INTF parameter is set to CCHAN this parameter is invalid. PDOM is of type Pdom.
TMGMODE|Timing Mode. This parameter selects the timing source for the T3 port transmit signal. TMGMODE defaults to SOURCE. TMGMODE is of type DS3TimingMode.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-TDMGW:[TID]:<IgAid>:[CTAG]:::[[VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][ECENABLE=<ECENABLE>,][ECTAIL=<ECTAIL>,][SUBNET=<SUBNET>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgAid.
VLAN|The integer value of the VLAN. VLAN is the AID VlanIndexAid.
BRIDGE|LOCAL is not valid for this command. BRIDGE is the AID BridgeProvAid.
ECENABLE|ECENABLE is of type BoolYN.
ECTAIL|ECTAIL is a Integer.
SUBNET|SUBNET is the AID IpAid.
PST|PST is of type PrimaryStateChg.

##### Syntax: ```ED-TGRP:[TID]:<MsAid>:[CTAG]:::[[TBUS=<TBUS>,][GTAP=<GTAP>]]; ```

##### Parameters
Attribute | Description
|---
MsAid|Maintenance Slot Access Identifier. The address of the maintenance slot which controls the test bus. MsAid is the AID MsAid.
TBUS|Test Bus. This parameter indicates which shelfs are connected (via wiring) to the maintenance slot which controls the test bus. TBUS is the AID ShelfAid and is listable.
GTAP|GTAP Gold Test Access Port. This parameter specifies which slot hosts the GTAP. For VDSL2 port test, it is necessary to have a valid GTAP parameter. GTAP is the AID SlotLuAid.

##### Syntax: ```ED-TMG:[TID]:<ShelfAid>:[CTAG]:::[[SIMPLEX=<SIMPLEX>,][TMREF=<TMREF>,][EXT=<EXT>,][PRI=<PRI>,][SEC=<SEC>,][RVRTV=<RVRTV>,][DS1FMT=<DS1FMT>]]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the timing is to be modified. ShelfAid is the AID ShelfAid.
SIMPLEX|Simplex timing. Set this to TRUE if no redundant Composite Clock or External DS1 timing source is available. This will suppress the alarm that would otherwise be generated due to a secondary timing source failure. SIMPLEX is of type BoolYN. The default value is "N".
TMREF|Timing Reference. This parameter indicates the configuration of the timing system on the C7 shelf. TMREF is of type TimingReference.
EXT|External Timing. When the TMREF is EXTERNAL, this parameter indicates what type of external timing reference is to be used. When the TMREF is LINE, this parameter indicates what timing outputs should be generated. EXT is of type ExtTmg. The default value is "CC".
PRI|Primary Timing Source. When TMREF is LINE, this parameter indicates the AID of the working line of primary timing interface. The working line of this interface supplies the source for the derived DS1 generated by the CSA RAP. The protect line of this interface supplies the source for the derived DS1 generated by the CSB RAP. When TMREF is EXTERNAL, it indicates the source of the derived DS1 generated by the CSA RAP -- NONE indicates that no derived DS1 is to be generated. PRI is the AID PortNoneAid.
SEC|Secondary Timing Source. When TMREF is LINE, this parameter indicates the AID of the working line of the secondary timing interface. When both working and protect of the primary timing interface have failed, this interface is used as the system timing source. Also, when the primary timing interface has failed, the working line of the secondary interface supplies the source for the derived DS1 generated by the CSA RAP. The protect line of the secondary interface supplies the source for the derived DS1 generated by the CSB RAP. When TMREF is EXTERNAL, it indicates the source of the derived DS1 generated by the CSB RAP -- NONE indicates that no derived DS1 is to be generated. SEC is the AID PortNoneAid.
RVRTV|Revertive. This parameter is Y if timing should revert to the primary timing source when the primary timing source is restored after a failure. RVRTV is of type BoolYN. The default value is "N".
DS1FMT|DS1 Format. This parameter indicates the format for the transmitted and/or received timing DS1 signals. If both are used both formats must be the same. DS1FMT is of type TmgDS1Fmt. The default value is "EFSNS".

##### Syntax: ```ED-TMPLT-ADSL:[TID]:<DslProfAid>:[CTAG]::[<SRVTYPE>],[<CHNL0>],[<CHNL1>]:[[XDSR0=<XDSR0>,][MDSR0=<MDSR0>,][XUSR0=<XUSR0>,][MUSR0=<MUSR0>,][XDSR1=<XDSR1>,][MDSR1=<MDSR1>,][XUSR1=<XUSR1>,][MUSR1=<MUSR1>,][DSEXR=<DSEXR>,][USEXR=<USEXR>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][DSLAT=<DSLAT>,][USLAT=<USLAT>,][TC=<TC>,][RAMODEDS=<RAMODEDS>,][RAMODEUS=<RAMODEUS>,][RAUMDS=<RAUMDS>,][RADMDS=<RADMDS>,][RAUTDS=<RAUTDS>,][RADTDS=<RADTDS>,][RAUMUS=<RAUMUS>,][RADMUS=<RADMUS>,][RAUTUS=<RAUTUS>,][RADTUS=<RADTUS>,][PMMODE=<PMMODE>,][L0TIME=<L0TIME>,][L2TIME=<L2TIME>,][L2ATPR=<L2ATPR>,][L2MINR=<L2MINR>,][L2EXITR=<L2EXITR>,][L2ENTRYR=<L2ENTRYR>,][L2ENTRYT=<L2ENTRYT>,][DSST=<DSST>,][DSET=<DSET>,][USST=<USST>,][USET=<USET>,][ENABLENOTCH=<ENABLENOTCH>,][DPBOEPSDBP1TONE=<DPBOEPSDBP1TONE>,][DPBOEPSDBP1PSD=<DPBOEPSDBP1PSD>,][DPBOEPSDBP2TONE=<DPBOEPSDBP2TONE>,][DPBOEPSDBP2PSD=<DPBOEPSDBP2PSD>,][DPBOEPSDBP3TONE=<DPBOEPSDBP3TONE>,][DPBOEPSDBP3PSD=<DPBOEPSDBP3PSD>,][DPBOEPSDBP4TONE=<DPBOEPSDBP4TONE>,][DPBOEPSDBP4PSD=<DPBOEPSDBP4PSD>,][DPBOEPSDBP5TONE=<DPBOEPSDBP5TONE>,][DPBOEPSDBP5PSD=<DPBOEPSDBP5PSD>,][DPBOEPSDBP6TONE=<DPBOEPSDBP6TONE>,][DPBOEPSDBP6PSD=<DPBOEPSDBP6PSD>,][DPBOEPSDBP7TONE=<DPBOEPSDBP7TONE>,][DPBOEPSDBP7PSD=<DPBOEPSDBP7PSD>,][DPBOEPSDBP8TONE=<DPBOEPSDBP8TONE>,][DPBOEPSDBP8PSD=<DPBOEPSDBP8PSD>,][DPBOEPSDBP9TONE=<DPBOEPSDBP9TONE>,][DPBOEPSDBP9PSD=<DPBOEPSDBP9PSD>,][DPBOEPSDBP10TONE=<DPBOEPSDBP10TONE>,][DPBOEPSDBP10PSD=<DPBOEPSDBP10PSD>,][DPBOEPSDBP11TONE=<DPBOEPSDBP11TONE>,][DPBOEPSDBP11PSD=<DPBOEPSDBP11PSD>,][DPBOEPSDBP12TONE=<DPBOEPSDBP12TONE>,][DPBOEPSDBP12PSD=<DPBOEPSDBP12PSD>,][DPBOEPSDBP13TONE=<DPBOEPSDBP13TONE>,][DPBOEPSDBP13PSD=<DPBOEPSDBP13PSD>,][DPBOEPSDBP14TONE=<DPBOEPSDBP14TONE>,][DPBOEPSDBP14PSD=<DPBOEPSDBP14PSD>,][DPBOEPSDBP15TONE=<DPBOEPSDBP15TONE>,][DPBOEPSDBP15PSD=<DPBOEPSDBP15PSD>,][DPBOEPSDBP16TONE=<DPBOEPSDBP16TONE>,][DPBOEPSDBP16PSD=<DPBOEPSDBP16PSD>,][DPBOESEL=<DPBOESEL>,][DPBOESCMA=<DPBOESCMA>,][DPBOESCMB=<DPBOESCMB>,][DPBOESCMC=<DPBOESCMC>,][DPBOMUS=<DPBOMUS>,][DPBOFMIN=<DPBOFMIN>,][DPBOFMAX=<DPBOFMAX>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
DslProfAid|ADSL Profile Access Identifier. The address of the specific entry in ADSL Profile table. DslProfAid is the AID DslProfProvAid.
SRVTYPE|Service Type. This parameter specifies the ADSL operating modes which dictate the ADSL handshaking protocol, channel capacity, and other physical line characteristics. SRVTYPE is of type AdslType.
CHNL0|Channel 0 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (2 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL0 is of type ChnlSelect0.
CHNL1|Channel 1 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (2 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL1 is of type ChnlSelect1.
XDSR0|Maximum Downstream Rate - Channel 0. XDSR0 is of type DwnStreamRate.
MDSR0|Minimum Downstream Rate - Channel 0. MDSR0 is of type DwnStreamRate.
XUSR0|Maximum Upstream Rate - Channel 0. XUSR0 is of type UpStreamRate.
MUSR0|Minimum Upstream Rate - Channel 0. MUSR0 is of type UpStreamRate.
XDSR1|Maximum Downstream Rate - Channel 1. XDSR1 is of type DwnStreamRate.
MDSR1|Minimum Downstream Rate - Channel 1. MDSR1 is of type DwnStreamRate.
XUSR1|Maximum Upstream Rate - Channel 1. XUSR1 is of type UpStreamRate.
MUSR1|Minimum Upstream Rate - Channel 1. MUSR1 is of type UpStreamRate.
DSEXR|Downstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. DSEXR is of type ExcessRate.
USEXR|Upstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. USEXR is of type ExcessRate.
TMDS|Target Downstream SNR Margin. This parameter specifies the target signal to noise ratio which basically quantifies the quality of the physical line through which the DSL signal flows. TMDS is of type SnrTargetMargins.
XMDS|Maximum Downstream SNR Margin. This parameter specifies the maximum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. XMDS is of type SnrMaxMargins.
MMDS|Minimum Downstream SNR Margin. This parameter specifies the minimum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. MMDS is of type SnrMinMargins.
TMUS|Target Upstream SNR Margin. This parameter specifies the target signal to noise ratio which basically quantifies the quality of the physical line through which the DSL signal flows. TMUS is of type SnrTargetMargins.
XMUS|Maximum Upstream SNR Margin. This parameter specifies the maximum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. XMUS is of type SnrMaxMargins.
MMUS|Minimum Upstream SNR Margin. This parameter specifies the minimum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. MMUS is of type SnrMinMargins.
DSLAT|Downstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. DSLAT is of type Latency.
USLAT|Upstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. USLAT is of type Latency.
TC|Trellis Coding. Trellis Coding is an encoding scheme for piggybacking bits onto the electrical signal on the twisted pair. Turning on this parameter will improve the DSL system performance. TC is of type TrellisCoding.
RAMODEDS|Rate Adaptation MODE DownStream. RAMODEDS is of type RateAdaptationMode.
RAMODEUS|Rate Adaptation MODE UpStream. RAMODEUS is of type RateAdaptationMode.
RAUMDS|Rate Adaptation Upshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RAUMDS is of type SnrMaxMargins.
RADMDS|Rate Adaptation Downshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RADMDS is of type SnrMaxMargins.
RAUTDS|Rate Adaptation Upshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RAUTDS is of type RateAdaptationMarginSeconds.
RADTDS|Rate Adaptation Downshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RADTDS is of type RateAdaptationMarginSeconds.
RAUMUS|Rate Adaptation Upshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RAUMUS is of type SnrMaxMargins.
RADMUS|Rate Adaptation Downshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RADMUS is of type SnrMaxMargins.
RAUTUS|Rate Adaptation Upshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RAUTUS is of type RateAdaptationMarginSeconds.
RADTUS|Rate Adaptation Downshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RADTUS is of type RateAdaptationMarginSeconds.
PMMODE|Power Management MODE. PMMODE is of type AdslPowerMgmtStates.
L0TIME|Minimum L0 Time interval between L2 exit and next L2 entry. (0-255 seconds) L0TIME is a Integer.
L2TIME|Minimum L2 time interval between L2 entry and first L2 trim. (0-255 seconds) L2TIME is a Integer.
L2ATPR|Maximum Aggregate Transmit Power Reduction per L2 trim. (dB) L2ATPR is of type SnrMaxMargins.
L2MINR|Minimum Data Rate in Low Power Mode (L2). This parameter specifies the minimum net data rate (in Kbps) during the low power state. If the actual user data rate is lower than L2MINR, raw cells will be injected to maintain the provisioned value. The value can range from 256 to 1024 Kbps. L2MINR is a Integer.
L2EXITR|L2 Exit Rate Threshold. This parameter specifies the downstream datarate threshold (in Kbps), which triggers exit from low power state (L2). The value ranges between 1 and 1024 Kbps, and must be less than L2MINR. L2EXITR is a Integer.
L2ENTRYR|L2 Entry Rate Threshold. This parameter specifies the downstream data rate threshold (in Kbps), which triggers autonomous entry into low power state (L2). The value can range from 1 to 1024, and must be less or equal to L2EXITR. L2ENTRYR is a Integer.
L2ENTRYT|L2 Entry Time Threshold. This parameter specifies minimum interval of time (in seconds) that the net data rate should stay below L2ENTRYR before autonomous entry into low power state (L2). The value can range from 900 to 65535 seconds. L2ENTRYT is a Integer.
DSST|DownStream Start Tone index. DSST must be less than or equal to DSET. DSST is a Integer.
DSET|DownStream End Tone index. DSET must be greater than or equal to DSST. DSET is a Integer.
USST|UpStream Start Tone index. USST must be less than or equal to USET. USST is a Integer.
USET|UpStream End Tone index. USET must be greater than or equal to USST. USET is a Integer.
ENABLENOTCH|Enable notching for adsl. ENABLENOTCH is of type BoolYN.
DPBOEPSDBP1TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP1TONE is of type Tone.
DPBOEPSDBP1PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, PSD value. The valid range is from -127 to 0. DPBOEPSDBP1PSD is a Integer.
DPBOEPSDBP2TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP2TONE is of type Tone.
DPBOEPSDBP2PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, PSD value. The valid range is from -127 to 0. DPBOEPSDBP2PSD is a Integer.
DPBOEPSDBP3TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP3TONE is of type Tone.
DPBOEPSDBP3PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, PSD value. The valid range is from -127 to 0. DPBOEPSDBP3PSD is a Integer.
DPBOEPSDBP4TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP4TONE is of type Tone.
DPBOEPSDBP4PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, PSD value. The valid range is from -127 to 0. DPBOEPSDBP4PSD is a Integer.
DPBOEPSDBP5TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP5TONE is of type Tone.
DPBOEPSDBP5PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, PSD value. The valid range is from -127 to 0. DPBOEPSDBP5PSD is a Integer.
DPBOEPSDBP6TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP6TONE is of type Tone.
DPBOEPSDBP6PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, PSD value. The valid range is from -127 to 0. DPBOEPSDBP6PSD is a Integer.
DPBOEPSDBP7TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP7TONE is of type Tone.
DPBOEPSDBP7PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, PSD value. The valid range is from -127 to 0. DPBOEPSDBP7PSD is a Integer.
DPBOEPSDBP8TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP8TONE is of type Tone.
DPBOEPSDBP8PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, PSD value. The valid range is from -127 to 0. DPBOEPSDBP8PSD is a Integer.
DPBOEPSDBP9TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP9TONE is of type Tone.
DPBOEPSDBP9PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, PSD value. The valid range is from -127 to 0. DPBOEPSDBP9PSD is a Integer.
DPBOEPSDBP10TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP10TONE is of type Tone.
DPBOEPSDBP10PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, PSD value. The valid range is from -127 to 0. DPBOEPSDBP10PSD is a Integer.
DPBOEPSDBP11TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP11TONE is of type Tone.
DPBOEPSDBP11PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, PSD value. The valid range is from -127 to 0. DPBOEPSDBP11PSD is a Integer.
DPBOEPSDBP12TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP12TONE is of type Tone.
DPBOEPSDBP12PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, PSD value. The valid range is from -127 to 0. DPBOEPSDBP12PSD is a Integer.
DPBOEPSDBP13TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP13TONE is of type Tone.
DPBOEPSDBP13PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, PSD value. The valid range is from -127 to 0. DPBOEPSDBP13PSD is a Integer.
DPBOEPSDBP14TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP14TONE is of type Tone.
DPBOEPSDBP14PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, PSD value. The valid range is from -127 to 0. DPBOEPSDBP14PSD is a Integer.
DPBOEPSDBP15TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP15TONE is of type Tone.
DPBOEPSDBP15PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, PSD value. The valid range is from -127 to 0. DPBOEPSDBP15PSD is a Integer.
DPBOEPSDBP16TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, Tone Value. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP16TONE is of type Tone.
DPBOEPSDBP16PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, PSD value. The valid range is from -127 to 0. DPBOEPSDBP16PSD is a Integer.
DPBOESEL|Downstream Power Back Off, Exchange-side Electrical Length. The valid range is from 0 to 255. DPBOESEL is a Integer.
DPBOESCMA|Downstream Power Back Off, Exchange-side Cable Model Parameter A. DPBOESCMA is of type Escm.
DPBOESCMB|Downstream Power Back Off, Exchange-side Cable Model Parameter B. DPBOESCMB is of type Escm.
DPBOESCMC|Downstream Power Back Off, Exchange-side Cable Model Parameter C. DPBOESCMC is of type Escm.
DPBOMUS|Downstream Power Back Off, Minimum Usable PSD Mask. The valid range is from -127 to 0. DPBOMUS is a Integer.
DPBOFMIN|Downstream Power Back Off, Frequency Min. DPBOFMIN is of type Fmin.
DPBOFMAX|Downstream Power Back Off, Frequency Max. DPBOFMAX is of type Fmax.
DESC|DESCription. A user-settable description field, up to 11 characters. The description defaults to be the template address/index number. DESC is a String.

##### Syntax: ```ED-TMPLT-PW:[TID]:<PwTmpltAid>:[CTAG]:::[[RTPTS=<RTPTS>,][RTPTSMODE=<RTPTSMODE>,][FPP=<FPP>,][PYLDSIZE=<PYLDSIZE>,][JBUFDEPTH=<JBUFDEPTH>,][PYLDS=<PYLDS>,][PKTSINSYN=<PKTSINSYN>,][PKTSOUTSYN=<PKTSOUTSYN>,][HOLDOFF=<HOLDOFF>,][FILLP=<FILLP>,][FILL=<FILL>,][RTPPTTX=<RTPPTTX>,][RTPPTRX=<RTPPTRX>,][SSRCTX=<SSRCTX>,][SSRCRX=<SSRCRX>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
PwTmpltAid|PW template Aid pattern. PwTmpltAid is the AID AtmTrfProfProvAid.
RTPTS|Allows enabling RTP timestamp. RTPTS is of type BoolYN.
RTPTSMODE|Timestamp generation mode if RTPTS is enabled. RTPTSMODE is of type RtpTsMode.
FPP|Number of T1 frames per packet for structured service. Packet interval is computed in the range of 0.5ms to 7.5ms. FPP is of type T1FrmsPerPkt.
PYLDSIZE|This is the size of the PWE3 payload. For PWUNSTRUCT only. PYLDSIZE must be in multiples of 32 when the container T1 port is enabled with TMGMODE as either ADAPT or DIFF. PYLDSIZE is of type PayloadSize.
JBUFDEPTH|The size of the buffer to absorb the PDV. Jitter buffer latency is based on the FramesPerPacket. Its max value for ONT PW is limited to 250000. JBUFDEPTH is of type JitBufSize.
PYLDS|Selecting Yes means suppression is allowed. Payload MAY be omitted in order to conserve bandwidth. Otherwise, no suppression under any condition. PYLDS is of type BoolYN.
PKTSINSYN|The number of packets required to exit the LOPS state. PKTSINSYN is of type PktsInSyn.
PKTSOUTSYN|The number of consecutive packets missed required to enter LOPS state. PKTSOUTSYN is of type PktsOutSyn.
HOLDOFF|The number of consecutive packets missed required to enter LOPS state. HOLDOFF is of type NonNegativeInteger.
FILLP|Policy to be applied when the CE-bound Jitter buffer is overflow/ underflow for any reason. FILLP is of type TdmFillPolicy.
FILL|User Defined Fill Pattern to be used towards the T1 port. FILL is of type FillerRange.
RTPPTTX|RTP Payload type to be used to transmit and received PW packets. RTPPTTX is of type RtpPayloadType.
RTPPTRX|RTP Payload expected to be received from the far-end PW. For Ont PWE3, Calix ONT only accepts RTPPTRX=0. RTPPTRX is of type RtpPayloadType.
SSRCTX|SSRC value to be transmitted on towards PSN. It's not applicable for ONT PW. SSRCTX is of type NonNegativeInteger.
SSRCRX|SSRC value expected to be received at the near-end. It's not applicable for ONT PW. SSRCRX is of type NonNegativeInteger.
DESC|A user-settable description field, up to 31 characters. DESC is a String.

##### Syntax: ```ED-TMPLT-SECU:[TID]:<SecuTmpltAid>:[CTAG]:::[[PAGE=<PAGE>,][PCND=<PCND>,][TMOUT=<TMOUT>,][UAPMA=<UAPMA>,][UAPMT=<UAPMT>,][UAPSE=<UAPSE>,][UAPSY=<UAPSY>,][UAPTS=<UAPTS>,][NODEAID=<NODEAID>,][ENTADA=<ENTADA>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
SecuTmpltAid|This is the Access Identifier of the Security Template to be modified. SecuTmpltAid is the AID SecuTmpltAid.
PAGE|Password Aging Interval. The passward aging interval is expressed in days. It is an integer less than or equal to 999, typically 45 to 60. At the end of the interval the user is notified that the existing password needs to be changed each time they log in. A value of zero indicates the user's password will never expire. PAGE is of type UserInterval.
PCND|Password ChaNge Days. This parameter specifies the number of days the user has between the time they are first notified that they must change their password and the time their USERID is disabled. PCND is of type UserInterval.
TMOUT|TiMe OUT. This parameter specifies the number of minutes of inactivity that must pass before their session is automatically logged out. A value of zero indicates that the user's sessions are never to be logged out due to inactivity. TMOUT is of type TimeOut.
UAPMA|User Access Privilege for Memory Administration. This parameter specifies the abilities of a user for executing memory administration commands. UAPMA is of type AcsPrv.
UAPMT|User Access Privilege for MainTenance. This parameter specifies the abilities of a user for executing maintenance commands. UAPMT is of type AcsPrv.
UAPSE|User Access Privilege for Security. This parameter specifies the abilities of a user for executing security commands. UAPSE is of type AcsPrv.
UAPSY|User Access Privilege for SYstem. This parameter specifies the abilities of a user for executing system commands. UAPSY is of type AcsPrv.
UAPTS|User Access Privilege for TeSting. This parameter specifies the abilities of a user for executing testing commands. UAPTS is of type AcsPrv.
NODEAID|Use NODE Access IDentifier. This parameter is set to Y (Yes) if AIDs in responses to this user are to contain node identifiers. This is the normal setting. N (No) needs to be specified for Operations Systems (such as NMA) that cannot tolerate node identifiers. For these systems, AIDs for the same node as was identified in the TID of the command will have the Nx- deleted from the AID in responses and autonomous reports. For input, the node identifier may be omitted if the node is the same as is identified in the TID. NODEAID is of type BoolYN.
ENTADA|This boolean flag determines whether or not the user may perform an ENTer on an object that is in ADA state. ENTADA is of type BoolYN.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ED-TMPLT-VLANIF:[TID]:<VlanIfTmpltAid>:[CTAG]:::[[ARP=<ARP>,][DHCPDIR=<DHCPDIR>,][OPT82ACT=<OPT82ACT>,][IGMP=<IGMP>,][PPPOEAC=<PPPOEAC>,][PPPOESUB=<PPPOESUB>,][LSVID=<LSVID>,][PRIO=<PRIO>,][ENCAP=<ENCAP>,][DOS=<DOS>,][DFLTROUTE=<DFLTROUTE>,][STP=<STP>,][STPCOST=<STPCOST>,][STPPRIO=<STPPRIO>,][DIRN=<DIRN>,][STAGTYPE=<STAGTYPE>,][PORTTYPE=<PORTTYPE>,][TRFPROF=<TRFPROF>,][BCKPROF=<BCKPROF>,][PATH=<PATH>,][PC=<PC>,][RXETHBWPROF=<RXETHBWPROF>,][TXETHBWPROF=<TXETHBWPROF>,][MCASTPROF=<MCASTPROF>,][LEASELMT=<LEASELMT>,][MATCHLIST=<MATCHLIST>,][ACSPROF=<ACSPROF>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VlanIfTmpltAid|VlanIfTmpltAid is the AID VlanIfTmpltAid.
ARP|ARP is of type BoolYN.
DHCPDIR|DHCPDIR is of type DhcpDirection.
OPT82ACT|OPT82ACT is of type Option82Action.
IGMP|IGMP is of type IgmpType.
PPPOEAC|PPPOEAC is of type BoolYN.
PPPOESUB|PPPOESUB is of type BoolYN.
LSVID|LSVID is of type VlanTagOrNone.
PRIO|802.1q Priority Bits Policy. PRIO is of type PrioBits.
ENCAP|ENCAP is of type EncapType.
DOS|DOS is of type BoolYN.
DFLTROUTE|Indicates whether it is the "default" VLAN-IF and would be the owner of the default route. Only applicable for ONT RSG. The default value for DHCP VLAN-IF is N. The default value for PPPoE/STATIC VLAN-IF is Y. Only one RG VLAN-IF can set it to Y. DFLTROUTE is of type BoolYN. DFLTROUTE is of type BoolYN.
STP|STP is of type StpAddr.
STPCOST|STPCOST is a Integer.
STPPRIO|STPPRIO is a Integer.
DIRN|DIRN is of type VbPortDirection.
STAGTYPE|STAGTYPE is of type StagEthType.
PORTTYPE|PORTTYPE is of type VbPortType.
TRFPROF|TRFPROF is the AID TrfId.
BCKPROF|BCKPROF is the AID TrfId.
PATH|PATH is of type Path.
PC|PC is of type ProtClass.
RXETHBWPROF|RXETHBWPROF is the AID VlanifId.
TXETHBWPROF|TXETHBWPROF is the AID VlanifId.
MCASTPROF|MCASTPROF is the AID IfId4.
LEASELMT|LEASELMT is of type LeaseLimit.
MATCHLIST|MATCHLIST is the AID IfId6.
ACSPROF|The AID of a defined ACS Profileto be applied to this VLAN interface. No other VLAN-IFs on the same RG with this parameter presented. Only allowed for RG. ACSPROF is the AID IfId7.
DESC|DESC is a String.

##### Syntax: ```ED-TMPLT-XDSL:[TID]:<XdslTmpltAid>:[CTAG]::[<SRVTYPE>]:[[XDSLLINEPROF=<XDSLLINEPROF>,][PKTMODE=<PKTMODE>,][PTMOVER=<PTMOVER>,][FALLBACKVPI=<FALLBACKVPI>,][FALLBACKVCI=<FALLBACKVCI>,][CHNLLAT=<CHNLLAT>,][XRDS=<XRDS>,][MRDS=<MRDS>,][XRUS=<XRUS>,][MRUS=<MRUS>,][INTLVLATDS=<INTLVLATDS>,][INTLVLATUS=<INTLVLATUS>,][MININPDS=<MININPDS>,][MININPUS=<MININPUS>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][RAMODEDS=<RAMODEDS>,][RAMODEUS=<RAMODEUS>,][RAUMDS=<RAUMDS>,][RADMDS=<RADMDS>,][RAUTDS=<RAUTDS>,][RADTDS=<RADTDS>,][RAUMUS=<RAUMUS>,][RADMUS=<RADMUS>,][RAUTUS=<RAUTUS>,][RADTUS=<RADTUS>,][PMMODE=<PMMODE>,][L0TIME=<L0TIME>,][L2TIME=<L2TIME>,][L2ATPR=<L2ATPR>,][L2MINR=<L2MINR>,][L2ENTRYT=<L2ENTRYT>,][GOS=<GOS>,][AHC=<AHC>,][EINP=<EINP>,][REPTRMVRST=<REPTRMVRST>,][US0PSD=<US0PSD>,][VNSTART1=<VNSTART1>,][VNSTOP1=<VNSTOP1>,][VNSTART2=<VNSTART2>,][VNSTOP2=<VNSTOP2>,][VNSTART3=<VNSTART3>,][VNSTOP3=<VNSTOP3>,][VNSTART4=<VNSTART4>,][VNSTOP4=<VNSTOP4>,][VRSTART1=<VRSTART1>,][VRSTOP1=<VRSTOP1>,][VRSTART2=<VRSTART2>,][VRSTOP2=<VRSTOP2>,][VRSTART3=<VRSTART3>,][VRSTOP3=<VRSTOP3>,][VRSTART4=<VRSTART4>,][VRSTOP4=<VRSTOP4>,][VRSTART5=<VRSTART5>,][VRSTOP5=<VRSTOP5>,][VRSTART6=<VRSTART6>,][VRSTOP6=<VRSTOP6>,][VRSTART7=<VRSTART7>,][VRSTOP7=<VRSTOP7>,][VRSTART8=<VRSTART8>,][VRSTOP8=<VRSTOP8>,][VRSTART9=<VRSTART9>,][VRSTOP9=<VRSTOP9>,][VRSTART10=<VRSTART10>,][VRSTOP10=<VRSTOP10>,][VRSTART11=<VRSTART11>,][VRSTOP11=<VRSTOP11>,][VRSTART12=<VRSTART12>,][VRSTOP12=<VRSTOP12>,][VRSTART13=<VRSTART13>,][VRSTOP13=<VRSTOP13>,][VRSTART14=<VRSTART14>,][VRSTOP14=<VRSTOP14>,][VRSTART15=<VRSTART15>,][VRSTOP15=<VRSTOP15>,][VRSTART16=<VRSTART16>,][VRSTOP16=<VRSTOP16>,][UPBOUS1PSDA=<UPBOUS1PSDA>,][UPBOUS1PSDB=<UPBOUS1PSDB>,][UPBOUS2PSDA=<UPBOUS2PSDA>,][UPBOUS2PSDB=<UPBOUS2PSDB>,][UPBOUS3PSDA=<UPBOUS3PSDA>,][UPBOUS3PSDB=<UPBOUS3PSDB>,][UPBOUS4PSDA=<UPBOUS4PSDA>,][UPBOUS4PSDB=<UPBOUS4PSDB>,][UPBOELELEN=<UPBOELELEN>,][DPBOEPSDBP1TONE=<DPBOEPSDBP1TONE>,][DPBOEPSDBP1PSD=<DPBOEPSDBP1PSD>,][DPBOEPSDBP2TONE=<DPBOEPSDBP2TONE>,][DPBOEPSDBP2PSD=<DPBOEPSDBP2PSD>,][DPBOEPSDBP3TONE=<DPBOEPSDBP3TONE>,][DPBOEPSDBP3PSD=<DPBOEPSDBP3PSD>,][DPBOEPSDBP4TONE=<DPBOEPSDBP4TONE>,][DPBOEPSDBP4PSD=<DPBOEPSDBP4PSD>,][DPBOEPSDBP5TONE=<DPBOEPSDBP5TONE>,][DPBOEPSDBP5PSD=<DPBOEPSDBP5PSD>,][DPBOEPSDBP6TONE=<DPBOEPSDBP6TONE>,][DPBOEPSDBP6PSD=<DPBOEPSDBP6PSD>,][DPBOEPSDBP7TONE=<DPBOEPSDBP7TONE>,][DPBOEPSDBP7PSD=<DPBOEPSDBP7PSD>,][DPBOEPSDBP8TONE=<DPBOEPSDBP8TONE>,][DPBOEPSDBP8PSD=<DPBOEPSDBP8PSD>,][DPBOEPSDBP9TONE=<DPBOEPSDBP9TONE>,][DPBOEPSDBP9PSD=<DPBOEPSDBP9PSD>,][DPBOEPSDBP10TONE=<DPBOEPSDBP10TONE>,][DPBOEPSDBP10PSD=<DPBOEPSDBP10PSD>,][DPBOEPSDBP11TONE=<DPBOEPSDBP11TONE>,][DPBOEPSDBP11PSD=<DPBOEPSDBP11PSD>,][DPBOEPSDBP12TONE=<DPBOEPSDBP12TONE>,][DPBOEPSDBP12PSD=<DPBOEPSDBP12PSD>,][DPBOEPSDBP13TONE=<DPBOEPSDBP13TONE>,][DPBOEPSDBP13PSD=<DPBOEPSDBP13PSD>,][DPBOEPSDBP14TONE=<DPBOEPSDBP14TONE>,][DPBOEPSDBP14PSD=<DPBOEPSDBP14PSD>,][DPBOEPSDBP15TONE=<DPBOEPSDBP15TONE>,][DPBOEPSDBP15PSD=<DPBOEPSDBP15PSD>,][DPBOEPSDBP16TONE=<DPBOEPSDBP16TONE>,][DPBOEPSDBP16PSD=<DPBOEPSDBP16PSD>,][DPBOESEL=<DPBOESEL>,][DPBOESCMA=<DPBOESCMA>,][DPBOESCMB=<DPBOESCMB>,][DPBOESCMC=<DPBOESCMC>,][DPBOMUS=<DPBOMUS>,][DPBOFMIN=<DPBOFMIN>,][DPBOFMAX=<DPBOFMAX>,][PHYRUS=<PHYRUS>,][PHYRDS=<PHYRDS>]]; ```

##### Parameters
Attribute | Description
|---
XdslTmpltAid|DSL Configuration Template Number. XdslTmpltAid is the AID DslProfProvAid.
SRVTYPE|This parameter specifies the DSL operating profile that dictates the DSL handshaking protocol, channel capacity, and other physical line characteristics based on DSL specifications. SRVTYPE is of type AdslType.
XDSLLINEPROF|This parameters specifies which of the standard profiles to use. XDSLLINEPROF is of type VdslProfRange.
PKTMODE|Packet mode defines if this port is to operate in packet or ATM VC mode PKTMODE is of type XdslTmpltPktMode.
PTMOVER|This parameter overrides the default encapsulation selection and forces the line to use PTM encapsulation regardless of mode. PTMOVER is of type BoolYN.
FALLBACKVPI|The VPI value to use on the singular VC in packet mode. FALLBACKVPI is of type XdslVPRange.
FALLBACKVCI|The VCI value to use on the singular VC in packet mode. FALLBACKVCI is of type VCRange.
CHNLLAT|The setting for channel path latency. Choosing a latency path of FAST means minimum (4 ms) delay is expected while choosing a latency path of INTLV (interleaved) means more delay. CHNLLAT is of type ChnlSelect0.
XRDS|The maximum downstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRDS is of type DwnStreamRate.
MRDS|This is the minimum downstream rate for the default channel (kbps). MRDS is of type DwnStreamRate.
XRUS|This is the maximum upstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRUS is of type UpStreamRate.
MRUS|This is the minimum upstream rate for the default channel (kbps). MRUS is of type UpStreamRate.
INTLVLATDS|The Downstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATDS is of type Latency.
INTLVLATUS|The upstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATUS is of type Latency.
MININPDS|The Downstream Minimum Impulse Noise Protection Downstream MININPDS is of type SymbolProtection.
MININPUS|The Upstream Minimum Impulse Noise Protection MININPUS is of type SymbolProtection.
TMDS|This parameter specifies the desired downstream signal to noise ratio margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMDS is of type SnrTargetMargins.
XMDS|This parameter specifies the maximum downstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-C. XMDS is of type SnrMaxMargins.
MMDS|This parameter specifies the minimum downstream signal to noise ratio margin in dB. This margin specifies the minimum threshold allowed for modem operation. MMDS is of type SnrMinMargins.
TMUS|This parameter specifies the desired upstream signal to noise ratio (SNR) margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMUS is of type SnrTargetMargins.
XMUS|This parameter specifies the maximum upstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-R. XMUS is of type SnrMaxMargins.
MMUS|This parameter specifies the minimum upstream signal to noise ratio (SNR) margin in dB. This margin specifies the minimum threshold allowed for modem training. MMUS is of type SnrMinMargins.
RAMODEDS|The Rate Adaptation Mode for Downstream RAMODEDS is of type RateAdaptationMode.
RAMODEUS|The Rate Adaptation Mode for Upstream RAMODEUS is of type RateAdaptationMode.
RAUMDS|The Rate Adaptation Upshift Margin Downstream in dB. RAUMDS is of type SnrMaxMargins.
RADMDS|The Rate Adaptation Downshift Margin Downstream in dB. RADMDS is of type SnrMaxMargins.
RAUTDS|The Rate Adaptation Upshift Time Downstream in seconds. RAUTDS is of type RateAdaptationMarginSeconds.
RADTDS|The Rate Adaptation Downshift Time Downstream in seconds. RADTDS is of type RateAdaptationMarginSeconds.
RAUMUS|The Rate Adaptation Upshift Margin Upstream in dB. RAUMUS is of type SnrMaxMargins.
RADMUS|The Rate Adaptation Downshift Margin Upstream in dB. RADMUS is of type SnrMaxMargins.
RAUTUS|The Rate Adaptation Upshift Time Upstream in seconds. RAUTUS is of type RateAdaptationMarginSeconds.
RADTUS|The Rate Adaptation Downshift Time Upstream in seconds. RADTUS is of type RateAdaptationMarginSeconds.
PMMODE|Power Management Mode PMMODE is of type AdslPowerMgmtStates.
L0TIME|The Minimum L0 Time interval between L2 exit and next L2 entry. L0TIME is of type MinL0TimeInt.
L2TIME|The Minimum L2 time interval between L2 entry and first L2 trim. L2TIME is of type MinL2TimeInt.
L2ATPR|Maximum Aggregate Transmit Power Reduction per L2 trim in dB. L2ATPR is of type SnrMaxMargins.
L2MINR|The Minimum Data Rate in Low Power Mode specifies the minimum net data rate (in Kbps) during the low power state. L2MINR is of type MinDRInLPM.
L2ENTRYT|The ADSL2 L2 Entry Time Threshold specifies minimum interval of time that the net data rate should stay below L2ENTRYR before autonomous entry into low power state (L2). L2ENTRYT is of type AdslL2EntTimeThreshold.
GOS|The grade of service identifies the DSL grade of service for performance monitoring (PM) which will be applied to the port. GOS is the AID GosAid.
AHC|Compression of the ATM header results to improve throughput. AHC is of type BoolYN.
EINP|This allows the caller to enable enhanced impulse noise protection. Several technology specific mechanisms are supported. EINP is of type INPType.
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the port. REPTRMVRST is of type BoolYN.
US0PSD|Upstream Power Spectral Density Mask. US0PSD is of type US0PSD.
VNSTART1|The beginning frequency for the first band to skip. Value range for this parameter is [0-65535]kHz. VNSTART1 is of type RfiBand.
VNSTOP1|The ending frequency for the first band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP1 is of type RfiBand.
VNSTART2|The beginning frequency for the second band to skip. Value range for this parameter is [0-65535]kHz. VNSTART2 is of type RfiBand.
VNSTOP2|The ending frequency for the second band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP2 is of type RfiBand.
VNSTART3|The beginning frequency for the third band to skip. Value range for this parameter is [0-65535]kHz. VNSTART3 is of type RfiBand.
VNSTOP3|The ending frequency for the third band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP3 is of type RfiBand.
VNSTART4|The beginning frequency for the fourth band to skip. Value range for this parameter is [0-65535]kHz. VNSTART4 is of type RfiBand.
VNSTOP4|The ending frequency for the fourth band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP4 is of type RfiBand.
VRSTART1|The beginning frequency for the first low power band. Value range for this parameter is [0-65535]kHz. VRSTART1 is of type RfiBand.
VRSTOP1|The ending frequency for the first low power band. Value range for this parameter is [0-65535]kHz. VRSTOP1 is of type RfiBand.
VRSTART2|The beginning frequency for the second low power band. Value range for this parameter is [0-65535]kHz. VRSTART2 is of type RfiBand.
VRSTOP2|The ending frequency for the second low power band. Value range for this parameter is [0-65535]kHz. VRSTOP2 is of type RfiBand.
VRSTART3|The beginning frequency for the third low power band. Value range for this parameter is [0-65535]kHz. VRSTART3 is of type RfiBand.
VRSTOP3|The ending frequency for the third low power band. Value range for this parameter is [0-65535]kHz. VRSTOP3 is of type RfiBand.
VRSTART4|The beginning frequency for the fourth low power band. Value range for this parameter is [0-65535]kHz. VRSTART4 is of type RfiBand.
VRSTOP4|The ending frequency for the fourth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP4 is of type RfiBand.
VRSTART5|The beginning frequency for the fifth low power band. Value range for this parameter is [0-65535]kHz. VRSTART5 is of type RfiBand.
VRSTOP5|The ending frequency for the fifth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP5 is of type RfiBand.
VRSTART6|The beginning frequency for the sixth low power band. Value range for this parameter is [0-65535]kHz. VRSTART6 is of type RfiBand.
VRSTOP6|The ending frequency for the sixth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP6 is of type RfiBand.
VRSTART7|The beginning frequency for the seventh low power band. Value range for this parameter is [0-65535]kHz. VRSTART7 is of type RfiBand.
VRSTOP7|The ending frequency for the seventh low power band. Value range for this parameter is [0-65535]kHz. VRSTOP7 is of type RfiBand.
VRSTART8|The beginning frequency for the eighth low power band. Value range for this parameter is [0-65535]kHz. VRSTART8 is of type RfiBand.
VRSTOP8|The ending frequency for the eighth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP8 is of type RfiBand.
VRSTART9|The beginning frequency for the ninth low power band. Value range for this parameter is [0-65535]kHz. VRSTART9 is of type RfiBand.
VRSTOP9|The ending frequency for the ninth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP9 is of type RfiBand.
VRSTART10|The beginning frequency for the tenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART10 is of type RfiBand.
VRSTOP10|The ending frequency for the tenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP10 is of type RfiBand.
VRSTART11|The beginning frequency for the eleventh low power band. Value range for this parameter is [0-65535]kHz. VRSTART11 is of type RfiBand.
VRSTOP11|The ending frequency for the eleventh low power band. Value range for this parameter is [0-65535]kHz. VRSTOP11 is of type RfiBand.
VRSTART12|The beginning frequency for the twelfth low power band. Value range for this parameter is [0-65535]kHz. VRSTART12 is of type RfiBand.
VRSTOP12|The ending frequency for the twelfth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP12 is of type RfiBand.
VRSTART13|The beginning frequency for the thirteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART13 is of type RfiBand.
VRSTOP13|The ending frequency for the thirteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP13 is of type RfiBand.
VRSTART14|The beginning frequency for the fourteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART14 is of type RfiBand.
VRSTOP14|The ending frequency for the fourteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP14 is of type RfiBand.
VRSTART15|The beginning frequency for the fifteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART15 is of type RfiBand.
VRSTOP15|The ending frequency for the fifteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP15 is of type RfiBand.
VRSTART16|The beginning frequency for the sixteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART16 is of type RfiBand.
VRSTOP16|The ending frequency for the sixteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP16 is of type RfiBand.
UPBOUS1PSDA|Upstream power back off reference PSD parameter A for US1. UPBOUS1PSDA is of type PsdA.
UPBOUS1PSDB|Upstream power back off reference PSD parameter B for US1. UPBOUS1PSDB is of type PsdB.
UPBOUS2PSDA|Upstream power back off reference PSD parameter A for US2. UPBOUS2PSDA is of type PsdA.
UPBOUS2PSDB|Upstream power back off reference PSD parameter A for US2. UPBOUS2PSDB is of type PsdB.
UPBOUS3PSDA|Upstream power back off reference PSD parameter A for US2. UPBOUS3PSDA is of type PsdA.
UPBOUS3PSDB|Upstream power back off reference PSD parameter B for US1. UPBOUS3PSDB is of type PsdB.
UPBOUS4PSDA|Upstream power back off reference PSD parameter A for US2. UPBOUS4PSDA is of type PsdA.
UPBOUS4PSDB|Upstream power back off reference PSD parameter B for US1. UPBOUS4PSDB is of type PsdB.
UPBOELELEN|Upstream power back off electrical length. UPBOELELEN is the AID EleLenAid.
DPBOEPSDBP1TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, Tone Value. DPBOEPSDBP1TONE is of type Tone.
DPBOEPSDBP1PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, PSD value. The valid range is from -127 to 0. DPBOEPSDBP1PSD is a Integer.
DPBOEPSDBP2TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, Tone Value. DPBOEPSDBP2TONE is of type Tone.
DPBOEPSDBP2PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, PSD value. The valid range is from -127 to 0. DPBOEPSDBP2PSD is a Integer.
DPBOEPSDBP3TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, Tone Value. DPBOEPSDBP3TONE is of type Tone.
DPBOEPSDBP3PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, PSD value. The valid range is from -127 to 0. DPBOEPSDBP3PSD is a Integer.
DPBOEPSDBP4TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, Tone Value. DPBOEPSDBP4TONE is of type Tone.
DPBOEPSDBP4PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, PSD value. The valid range is from -127 to 0. DPBOEPSDBP4PSD is a Integer.
DPBOEPSDBP5TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, Tone Value. DPBOEPSDBP5TONE is of type Tone.
DPBOEPSDBP5PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, PSD value. The valid range is from -127 to 0. DPBOEPSDBP5PSD is a Integer.
DPBOEPSDBP6TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, Tone Value. DPBOEPSDBP6TONE is of type Tone.
DPBOEPSDBP6PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, PSD value. The valid range is from -127 to 0. DPBOEPSDBP6PSD is a Integer.
DPBOEPSDBP7TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, Tone Value. DPBOEPSDBP7TONE is of type Tone.
DPBOEPSDBP7PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, PSD value. The valid range is from -127 to 0. DPBOEPSDBP7PSD is a Integer.
DPBOEPSDBP8TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, Tone Value. DPBOEPSDBP8TONE is of type Tone.
DPBOEPSDBP8PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, PSD value. The valid range is from -127 to 0. DPBOEPSDBP8PSD is a Integer.
DPBOEPSDBP9TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, Tone Value. DPBOEPSDBP9TONE is of type Tone.
DPBOEPSDBP9PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, PSD value. The valid range is from -127 to 0. DPBOEPSDBP9PSD is a Integer.
DPBOEPSDBP10TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, Tone Value. DPBOEPSDBP10TONE is of type Tone.
DPBOEPSDBP10PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, PSD value. The valid range is from -127 to 0. DPBOEPSDBP10PSD is a Integer.
DPBOEPSDBP11TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, Tone Value. DPBOEPSDBP11TONE is of type Tone.
DPBOEPSDBP11PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, PSD value. The valid range is from -127 to 0. DPBOEPSDBP11PSD is a Integer.
DPBOEPSDBP12TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, Tone Value. DPBOEPSDBP12TONE is of type Tone.
DPBOEPSDBP12PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, PSD value. The valid range is from -127 to 0. DPBOEPSDBP12PSD is a Integer.
DPBOEPSDBP13TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, Tone Value. DPBOEPSDBP13TONE is of type Tone.
DPBOEPSDBP13PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, PSD value. The valid range is from -127 to 0. DPBOEPSDBP13PSD is a Integer.
DPBOEPSDBP14TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, Tone Value. DPBOEPSDBP14TONE is of type Tone.
DPBOEPSDBP14PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, PSD value. The valid range is from -127 to 0. DPBOEPSDBP14PSD is a Integer.
DPBOEPSDBP15TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, Tone Value. DPBOEPSDBP15TONE is of type Tone.
DPBOEPSDBP15PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, PSD value. The valid range is from -127 to 0. DPBOEPSDBP15PSD is a Integer.
DPBOEPSDBP16TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, Tone Value. DPBOEPSDBP16TONE is of type Tone.
DPBOEPSDBP16PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, PSD value. The valid range is from -127 to 0. DPBOEPSDBP16PSD is a Integer.
DPBOESEL|Downstream Power Back Off, Exchange-side Electrical Length. The valid range is from 0 to 255. DPBOESEL is a Integer.
DPBOESCMA|Downstream Power Back Off, Exchange-side Cable Model Parameter A. DPBOESCMA is of type Escm.
DPBOESCMB|Downstream Power Back Off, Exchange-side Cable Model Parameter B. DPBOESCMB is of type Escm.
DPBOESCMC|Downstream Power Back Off, Exchange-side Cable Model Parameter C. DPBOESCMC is of type Escm.
DPBOMUS|Downstream Power Back Off, Minimum Usable PSD Mask. The valid range is from -127 to 0. DPBOMUS is a Integer.
DPBOFMIN|Downstream Power Back Off, Frequency Min. DPBOFMIN is of type Fmin.
DPBOFMAX|Downstream Power Back Off, Frequency Max. DPBOFmax must be no less than (DPBOFmin+2). DPBOFMAX is of type Fmax.
PHYRUS|PhyR Upstream. PHYRUS is of type BoolYN.
PHYRDS|PhyR Downstream. PHYRDS is of type BoolYN.

##### Syntax: ```ED-USER-SECU:[TID]:<UID>:[CTAG]::[<NEWUID>],[<NEWPID>]:[[TMPLT=<TMPLT>,][PAGE=<PAGE>,][PCND=<PCND>,][TMOUT=<TMOUT>,][UAPMA=<UAPMA>,][UAPMT=<UAPMT>,][UAPSE=<UAPSE>,][UAPSY=<UAPSY>,][UAPTS=<UAPTS>,][NODEAID=<NODEAID>,][ENTADA=<ENTADA>]]; ```

##### Parameters
Attribute | Description
|---
UID|User Identifier. The user's identifier for session to be cancelled. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination of alphanumeric characters 4 to 10 characters long and is case-sensitive. UID is the AID UserAid.
NEWUID|New User Identifier. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination alphanumeric characters which is 4 to 10 characters and is case-sensitive. NEWUID is the AID UserAid.
NEWPID|New user's password. If specified, this parameter will change the user's password. The password must conform to the rules provisioned via ED-SYS-SECU. NEWPID is a String.
TMPLT|Security Template. This specifies the security template to be used to provide default values for this command. The values in the template will be over-riden by any parameter values specified in the command. TMPLT is the AID SecuTmpltAid. The default value is "DEFLT".
PAGE|Password Aging Interval. The passward aging interval is expressed in days. It is an integer less than or equal to 999, typically 45 to 60. At the end of the interval the user is notified that the existing password needs to be changed each time they log in. A value of zero indicates the user's password will never expire. This value over-rides the value in the template if a template was specified. PAGE is of type UserInterval.
PCND|Password ChaNge Days. This parameter specifies the number of days the user has between the time they are first notified that they must change their password and the time their USERID is disabled. When a password is set by the ED-USER-SECU command, users are notified that they must change their password. They have PCND days to do this. This value over-rides the value in the template if a template was specified. PCND is of type UserInterval.
TMOUT|TiMe OUT. This parameter specifies the number of minutes of inactivity that must pass before their session is automatically logged out. A value of zero indicates that the user's sessions are never to be logged out due to inactivity. This value over-rides the value in the template if a template was specified. TMOUT is of type TimeOut.
UAPMA|User Access Privilege for Memory Administration. This parameter specifies the abilities of a user for executing memory administration commands. This value over-rides the value in the template if a template was specified. UAPMA is of type AcsPrv.
UAPMT|User Access Privilege for MainTenance. This parameter specifies the abilities of a user for executing maintenance commands. This value over-rides the value in the template if a template was specified. UAPMT is of type AcsPrv.
UAPSE|User Access Privilege for Security. This parameter specifies the abilities of a user for executing security commands. This value over-rides the value in the template if a template was specified. UAPSE is of type AcsPrv.
UAPSY|User Access Privilege for SYstem. This parameter specifies the abilities of a user for executing system commands. This value over-rides the value in the template if a template was specified. UAPSY is of type AcsPrv.
UAPTS|User Access Privilege for TeSting. This parameter specifies the abilities of a user for executing testing commands. This value over-rides the value in the template if a template was specified. UAPTS is of type AcsPrv.
NODEAID|Node Access Identifier. This parameter indicates if the AID used in the commands or responses should include the node identifer. If the NODEAID = Y, then the AID values will contain the Node Id (example N6-4-3). If the NODEAID = N, then the AID values will not contain the Node Id (example 4-3). When the user connecting to the C7 is a NMA user, the NODEAID should be set to N (no). NODEAID is of type BoolYN.
ENTADA|This boolean flag determines whether or not the user may perform an ENTer on an object that is in ADA state. ENTADA is of type BoolYN.

##### Syntax: ```ED-VB:[TID]:<VbAid>:[CTAG]:::[[BW=<BW>,][AGETMR=<AGETMR>,][PPPOAIWF=<PPPOAIWF>,][OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VbAid|Virtual Bridge Access Identifier. VbAid is the AID VbAid.
BW|Bandwidth - Amount of guaranteed bandwidth allocated (in kbps), per slot, for slot-to-slot intra-bridge traffic BW is a Integer.
AGETMR|The range is 0,300-1000000. AGETMR is a Integer.
PPPOAIWF|Not supported in release 6.0. PPPOAIWF is of type BoolYN.
OPTION82|This parameter is deprecated after release 7.2. The Option-82 type used by the L2 DHCP relay. OPTION82 is of type Option82.
L2RLYMODE|This parameter is deprecated after release 7.2. DHCP L2 Relay Mode. L2RLYMODE is of type DhcpL2RelayMode.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.

##### Syntax: ```ED-VBPORT:[TID]:<VbPortAid>:[CTAG]:::[[ENCAP=<ENCAP>,][DOS=<DOS>,][STP=<STP>,][STPCOST=<STPCOST>,][STPPRIO=<STPPRIO>,][PVID=<PVID>,][DIRN=<DIRN>,][STAGTYPE=<STAGTYPE>,][PINNED=<PINNED>]]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|Virtual Bridge Port Aid - This identifies either physical port or VC endpoint associated with the Virtual Bridge. VbPortAid is the AID VirtualBridgePortId5.
ENCAP|Encapsulation Type. ENCAP is of type EncapType.
DOS|Denial of Service enabled. DOS is of type BoolYN.
STP|This is used to enable or disable STP on a particular VB Port. STP is of type StpAddr.
STPCOST|Cost of the port participating in STP. This is used to determine the root port. STPCOST is a Integer.
STPPRIO|STP Priority. STP Priority values are in the range 0-240 and in steps of 16. STPPRIO is a Integer.
PVID|Port Vlan ID. Not supported in release 6.1 PVID is of type VlanTagOrNone.
DIRN|The direction of forwarded traffic. DIRN is of type VbPortDirection.
STAGTYPE|S_TAG ETH Type. This is used to restamp Ethernet Type field for legacy devices on Network side ports. STAGTYPE is of type StagEthType.
PINNED|For logical VBPORTs (used in ENT-CRS-VC), this parameter governs whether the VBPORT endpoint will be automatically deleted upon DLT-CRS-VC. If absent, PINNED is interpreted as FALSE. PINNED is of type BoolYN.

##### Syntax: ```ED-VCG:[TID]:<IgAid>:[CTAG]:::[[CAPALMTHR=<CAPALMTHR>,][ECENABLE=<ECENABLE>,][EPCD=<EPCD>,][ECTAIL=<ECTAIL>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The address of the VCG. IgAid is the AID IgAid.
CAPALMTHR|Capacity Alarm Threshold. The percentage of active call capacity of the VCG at which a capacity alarm should be raised. CAPALMTHR is of type Percentage.
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN.
EPCD|Echo Path Change Detection. EPCD=Y is only effective when ECCONFIG=SPARSE on the supporting equipement (VGP/VIPR). Enabling EPCD improves the ability to track changes in the echo path, but reduces channel density. EPCD is of type BoolYN.
ECTAIL|Integer: 64ms to 128ms in steps of 8ms. The maximum echo delay that the echo canceller is able to eliminate. If ECCONFIG=DUAL, increasing ECTAIL may further reduce channel density. If ECCONFIG=SPARSE, increasing ECTAIL does not impact channel density. ECTAIL is a Integer.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "OOS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-VEP:[TID]:<VepAid>:[CTAG]:::[[USER=<USER>,][PID=<PID>,][AOR=<AOR>,][HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>,][CWAITEN=<CWAITEN>,][CIDEN=<CIDEN>,][3WCEN=<3WCEN>,][OPX=<OPX>,][ECENABLE=<ECENABLE>,][DESC=<DESC>,][CALLMODE=<CALLMODE>]],AUTONUM=<AUTONUM>,[[FQDN=<FQDN>,][DIALPLAN=<DIALPLAN>]]; ```

##### Parameters
Attribute | Description
|---
VepAid|Voice Endpoint AID of POTs port on ONT or C7 Line Unit VepAid is the AID VepAid.
USER|SIP subscriber User Name USER is a String.
PID|Password. Password for authorization of the subscriber. PID is a String.
AOR|SIP Address Of Record or TDMGW 303 CRV AID AOR is a String.
HOSTPROTO|Is IP address derived via DHCP or Statically Assigned HOSTPROTO is of type SipT0HostProto.
IP|Statically assigned IP address associated with the subscriber. IP is the AID IpAid.
IPMSK|IP Mask of Statically assigned IP address associated with the subscriber. IPMSK is the AID IpAid.
GADDR|Gateway address. GADDR is the AID IpAid.
CWAITEN|Enable or disable Call waiting feature on this endpoint. Only take effect with UAHOOKFLASHCTRL=Y and this feature must not be enabled on the switch. CWAITEN is of type BoolYN.
CIDEN|Enable or disable Caller ID presentation on this endpoint. Only take effect with UAHOOKFLASHCTRL=Y and this feature must not be enabled on the switch. CIDEN is of type BoolYN.
3WCEN|Enable or disable Three way calling on this endpoint. Only take effect with UAHOOKFLASHCTRL=Y and this feature must not be enabled on the switch. 3WCEN is of type BoolYN.
OPX|Identify this voice endpoint as an Off Premises Extension. OPX is of type BoolYN.
ECENABLE|Enable/Disable Echo Cancellation on subscriber lines. ECENABLE is of type BoolYN.
DESC|A user-settable description field, up to 31 characters. DESC is a String.
CALLMODE|Enable hotline or warnline mode of operation. CALLMODE is of type CallMode.
AUTONUM|Number to dial in hotline or warmline operation. It is 16 digits followed by option Tn, where n=1..16. AUTONUM is a String.
FQDN|FQDN. FQDN is a String.
DIALPLAN|The Dial Plan to be used for digit collection on this voice endpoint. DIALPLAN is the AID VepId2.

##### Syntax: ```ED-VID-CHAN:[TID]:<IP>:[CTAG]:::[[VP=<VP>,][VC=<VC>,][TRFPROF=<TRFPROF>,][VIDSRCLIST=<VIDSRCLIST>,][INHSRCLIST=<INHSRCLIST>,][IGMPJOINTYPE=<IGMPJOINTYPE>,][TYPE=<TYPE>,][BW=<BW>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP Address. IP is the AID IpAid.
VP|The VP number associated with the video transport VCs to deliver this channel to the different shelves. This is applicable for AVT Model channels only and only when ATM video source is present in the VIDSRCLIST. VP is of type VPRange.
VC|The VC number associated with the video transport VCs to deliver this channel to the different shelves. This is applicable for AVT Model channels only and only when ATM video source is present in the VIDSRCLIST. VC is of type VCRange.
TRFPROF|Traffic Profile. This parameter identifies which Traffic Profile which will be used by the channel. The Traffic Profile specifies the bandwidth parameters. The Traffic Profile must have its APP set to an Application Id of either VIDCHNL or DATACAROUSEL to be used as a channel. Note if the TRFPROF parameter is changed, existing cross-connects created for this channel will not be updated with the new profile. This is not applicable for AVT Model channels. TRFPROF is the AID AtmTrfProfProvAid.
VIDSRCLIST|Video Source List. This is the list of video sources (video source indexes separated by &)that should receive this channel. This is applicable for AVT mode channels only. VIDSRCLIST is the AID ChanId and is listable.
INHSRCLIST|Inhibit Video Source List. This is the list of video sources (video source indexes separated by &)on which to inhibit discovery of this video channel. This is applicable for AVT Model channels only. INHSRCLIST is the AID ChanId and is listable.
IGMPJOINTYPE|IGMP Join Type. This should be static if any of the video source is ATM. Must be static for EPG/AGGEPG channels. This is applicable for AVT Model channels only. IGMPJOINTYPE is of type IgmpJoinType.
TYPE|Video Channel Type. This is applicable for AVT mode channels only. TYPE is of type ChannelType.
BW|Video Channel Bandwidth (in Kbps) including ATM overhead. This is applicable for AVT Model channels only. BW is a Integer.
DESC|Channel description. The description can be up to 40 characters in length for VCVT Model channels and upto 31 characters in length for AVT Model Channels. DESC is a String.

##### Syntax: ```ED-VID-SOURCE:[TID]:<VidSrcAid>:[CTAG]:::[[BW=<BW>,][BWC1=<BWC1>,][BWC2=<BWC2>,][DISCOVERY=<DISCOVERY>,][DFLTCHNLBW=<DFLTCHNLBW>,][DISCOVERDFLT=<DISCOVERDFLT>,][MINBWTHRESH=<MINBWTHRESH>,][MAXBWTHRESH=<MAXBWTHRESH>,][DESC=<DESC>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source Index AID. VidSrcAid is the AID VidSrcAid.
BW|Source Bandwidth. Total aggregate bandwidth (in Kbps) reserved for video channels including ATM header. BW is a Integer.
BWC1|Bandwidth Constraint 1 associated with the video source. BWC1 is the AID BwcIdNone.
BWC2|Bandwidth Constraint 2 associated with the video source. BWC2 is the AID BwcIdNone.
DISCOVERY|Channel DISCOVERY Enable/Disable. Channel DISCOVERY Enable/Disable. Channel Discovery is enabled by default for Ethernet Video Source. This is not applicable for an ATM video source. DISCOVERY is of type BoolYN.
DFLTCHNLBW|DeFauLT CHaNneL BandWidth. This is the default channel bandwidth (in Kbps) for channel discovered on an Ethernet video source. This is not applicable for ATM video source. DFLTCHNLBW is a Integer.
DISCOVERDFLT|DISCOVER DeFauLT Action. This is the default discovery action for all unfiltered channels discovered on the Ethernet video source. This is not applicable for ATM video source. DISCOVERDFLT is of type ChannelDiscoveryMode.
MINBWTHRESH|MINimum BandWidth THRESHold.Lower Threshold value defined for notification of bandwidth usage (in %)approaching the provisioned BW value. A minor alarm is raised on reaching this BW usage and cleared when the current usage retreats 5% less than this BW usage. Applicable for video GE uplinks only. MINBWTHRESH is of type Percentage.
MAXBWTHRESH|MAXimum BandWidth THRESHold. Upper Threshold value defined for notification of bandwidth usage (in %) approaching the provisioned BW value. A major alarm is raised on reaching this BW usage and cleared when the current usage retreats 5% less than this BW usage. Applicable for video GE uplinks only. MAXBWTHRESH is of type Percentage.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
INCL|INCLusive Flag. This flag is needed when editing the video source bandwidth below the actively used bandwidth. INCL is of type BoolYN.

##### Syntax: ```ED-VID-SUB:[TID]:<VidSubAid>:[CTAG]:::RTRAID=<RTRAID>,[[CHANCNT=<CHANCNT>,][VIDBW=<VIDBW>,][VIDLOANBW=<VIDLOANBW>]]; ```

##### Parameters
Attribute | Description
|---
VidSubAid|Video Subscriber Access Identifier - The port or channel to which subscribers are connected. Usually an ADSL Channel or ONT (or vdsl in the future) port. VidSubAid is the AID SubId1.
RTRAID|RTRAID - Location of IRC to handle the command RTRAID is the AID SlotLuAid.
CHANCNT|Maximum Channel Count - Number of unique channels flowing to the port. Zero CHANCNT means that the VIDBW and VIDLOANBW values are still used but the subscriber's port will use the global IGMP channel limit when validating channel changes. Setting the CHANCNT to zero is, in effect, turning off the count for that specific port. The valid range is from 0 to 65535. CHANCNT is a Integer.
VIDBW|Video Bandwidth - In Kilobits per second. This value is the maximum Downstream (TX) BW reserved for video on the port. This can be any value but will be rejected if it exceeds the port's trained rate or provisioned rate. VIDBW is a Integer.
VIDLOANBW|Maximum Video Loan Bandwidth - in kbps. Maximum amount of bandwidth to lend back to UBR applications. This value cannot exceed the Max Video BW value. VIDLOANBW is a Integer.

##### Syntax: ```ED-VID-SVC:[TID]:<VidSvcAid>:[CTAG]:::[[VIDVLANTAG=<VIDVLANTAG>,][MAXVIDBW=<MAXVIDBW>,][DHCPLOCK=<DHCPLOCK>,][CLEARCNT=<CLEARCNT>]]; ```

##### Parameters
Attribute | Description
|---
VidSvcAid|Video Service Access Identifier. The AID of the Video Service that contains the channel. VidSvcAid is the AID VidSvcAid.
VIDVLANTAG|VIDVLANTAG is of type VlanTagOrNone.
MAXVIDBW|Maximum Video Bandwidth - in kbps. This defines the maximum aggregate video channel bandwidth the proxy will request at any given time. MAXVIDBW is a Integer.
DHCPLOCK|Enable or disable device mobility. When set to "Y", restrict mobility by allowing a DHCP host to obtain an IP address only once for a specific VLAN port. DHCPLOCK is of type BoolYN.
CLEARCNT|Clear Counters. When set to "Y", the igmp drop count will be reset to 0. CLEARCNT is of type BoolYN.

##### Syntax: ```ED-VIRT-IF:[TID]:<VirtIfAid>:[CTAG]:::[[ADDMEM=<ADDMEM>,][REMMEM=<REMMEM>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
VirtIfAid|Virtual Interface Access Identifier. VirtIfAid is the AID VirtIfAid.
ADDMEM|This is the AID of the member port to be added. ADDMEM is the AID VirtIfMemAid and is listable.
REMMEM|This is the AID of the member port to be removed. REMMEM is the AID VirtIfMemAid and is listable.
DESC|Description. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-VLAN:[TID]:<VlanAid>:[CTAG]:::[[OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>,][NUMPRIO=<NUMPRIO>,][IGMPMODE=<IGMPMODE>,][STBRLYARP=<STBRLYARP>,][DHCPLOCK=<DHCPLOCK>,][MFF=<MFF>,][RMTIDOPT=<RMTIDOPT>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VlanAid|VLAN Access Identifier. VlanAid is the AID VlanId.
OPTION82|The Option-82 type used by the L2 DHCP relay. OPTION82 is of type Option82.
L2RLYMODE|DHCP L2 Relay Mode. L2RLYMODE is of type DhcpL2RelayMode.
NUMPRIO|VLAN Number Priority. NUMPRIO is of type NumPrioRange.
IGMPMODE|Determines if IGMP snoop is enabled. This parameter only applies to release 7.2 and above. IGMPMODE is of type VlanIgmpMode.
STBRLYARP|STBRLYARP is of type BoolYN.
DHCPLOCK|DHCPLOCK is of type BoolYN.
MFF|MFF is of type BoolYN.
RMTIDOPT|RMTIDOPT is of type RmtIdOpt.
DESC|User Description, up to 31 characters. DESC is a String.

##### Syntax: ```ED-VLAN-IF:[TID]:<IfAid>:[CTAG]:::VLAN=<VLAN>,[[BRIDGE=<BRIDGE>,][ARP=<ARP>,][DHCPDIR=<DHCPDIR>,][OPT82ACT=<OPT82ACT>,][IGMP=<IGMP>,][PPPOEAC=<PPPOEAC>,][PPPOESUB=<PPPOESUB>,][ENCAP=<ENCAP>,][DOS=<DOS>,][STP=<STP>,][STPCOST=<STPCOST>,][STPPRIO=<STPPRIO>,][DIRN=<DIRN>,][STAGTYPE=<STAGTYPE>,][MCASTPROF=<MCASTPROF>,][CVID=<CVID>,][PRIO=<PRIO>,][RCVID=<RCVID>,][DELCVID=<DELCVID>,][TAGGING=<TAGGING>,][LEASELMT=<LEASELMT>,][MATCHLIST=<MATCHLIST>,][ACSPROF=<ACSPROF>,][PPPOEUN=<PPPOEUN>,][PPPOEPW=<PPPOEPW>,][IPADDR=<IPADDR>,][IPMASK=<IPMASK>,][IPGW=<IPGW>,][PRIDNS=<PRIDNS>,][SECDNS=<SECDNS>]]; ```

##### Parameters
Attribute | Description
|---
IfAid|Interface Access Identifier. IfAid is the AID IfId11.
VLAN|Packet VLAN Access Identifier. Only VLAN number AID is allowed since R7.0. VLAN is the AID IfId1.
BRIDGE|VB Access Identifier. BRIDGE is the AID IfId8.
ARP|Enable/Disable ARP. ARP is of type BoolYN.
DHCPDIR|DHCP Directionality. This defines if the Vlan VB Port faces a DHCP-Client, DHCP-Server or no DHCP hosts. DHCPDIR is of type DhcpDirection.
OPT82ACT|The action to take if a DHCP packet is received on a Client facing interface with Option82 sub-option 1 /2 content. OPT82ACT is of type Option82Action.
IGMP|IGMP TYPE: a) SINK b) NONE. IGMP is of type IgmpType.
PPPOEAC|Enable/Disable PPPOE Access Concentrator. PPPOEAC is of type BoolYN.
PPPOESUB|Enable/Disable PPPoE Subscriber. PPPOESUB is of type BoolYN.
ENCAP|Encapsulation Type. ENCAP is of type EncapType.
DOS|Enable/Disable Denial of Service. DOS is of type BoolYN.
STP|Enable/Disbale STP. STP is of type StpAddr.
STPCOST|Cost of the port participating in STP. STPCOST is a Integer.
STPPRIO|STP Priority. STP Priority values are in the range 0-240 and in steps of 16. STPPRIO is a Integer.
DIRN|The direction of forwarded traffic. DIRN is of type VbPortDirection.
STAGTYPE|S_TAG ETH Type.Used to restamp Ethernet Type field for legacy devices on Network-side ports. STAGTYPE is of type StagEthType.
MCASTPROF|MultiCast Vlan profile used by EXA video. This parameter only applies to release 7.2 and above. MCASTPROF is the AID IfId4.
CVID|CVID Registration Access Identifier. DFLT CVID Reg is not allowed for VlanPerService/VlanPerPort/Routed VLAN. CVID is of type CvidTag.
PRIO|802.1q Priority Bits Policy. PRIO is of type PrioBits.
RCVID|Relay C-VID. Used to translate the incoming local C-Tag for tagged frames arriving on this user-side port. DFLT CVID Reg is not allowed for VlanPerService/VlanPerPort/Routed VLAN. RCVID is of type RCVid.
DELCVID|This parameter is used to delete the CVIDREG entry specified by the CVID. DELCVID is of type BoolYN.
TAGGING|Tagging Properties of the VLAN Port TAGGING is of type Tagging.
LEASELMT|LEASELMT is of type LeaseLimit.
MATCHLIST|MATCHLIST is the AID IfId6.
ACSPROF|The AID of a defined ACS Profile to be applied to this VLAN interface. Only allowed for RG. No other VLAN-IFs on the same RG with this parameter presented. ACSPROF is the AID IfId7.
PPPOEUN|The username to be used for PPPoE authentication by the RG. Up to 31 characters. PPPOEUN is a String.
PPPOEPW|The password to be used for PPPoE authentication by the RG. Only allowed for RG. Up to 25 characters. PPPOEPW is a String.
IPADDR|The static IP address to be used by the host for this VLAN interface. Mutually exclusive with the PPPOEUN and PPPOEPW parameters. Only allowed for RG. IPADDR is the AID IpAid.
IPMASK|The static IP address mask to be used by this VLAN interface. Requires the presence of IPADDR parameter. Only allowed for RG. IPMASK is the AID IpAid.
IPGW|The default Gateway to be used by the static IP address. Requires the presence of IPADDR parameter. Only allowed for RG. IPGW is the AID IpAid.
PRIDNS|Primary DNS address if a static WAN interface is configured. Requires the presence of IPADDR parameter. Only allowed for RG. PRIDNS is the AID IpAid.
SECDNS|Secondary DNS address if a static WAN interface is configured. Requires the presence of IPADDR parameter. Only allowed for RG. SECDNS is the AID IpAid.

##### Syntax: ```ED-VLAN-PORT:[TID]:<VLanPortAid>:[CTAG]:::[TRFPROF=<TRFPROF>]; ```

##### Parameters
Attribute | Description
|---
VLanPortAid|VLAN port Access Identifier. VLanPortAid is the AID VLanPortAid.
TRFPROF|ethernet TRaFfic PROFile TRFPROF is the AID EthProfAid.

##### Syntax: ```ED-VLAN-VBPORT:[TID]:<VbPortAid>:[CTAG]:::VLAN=<VLAN>,[[ARP=<ARP>,][DHCP=<DHCP>,][DHCPDIR=<DHCPDIR>,][OPT82ACT=<OPT82ACT>,][IGMP=<IGMP>,][PPPOEAC=<PPPOEAC>,][PPPOESUB=<PPPOESUB>,][PRIO=<PRIO>,][TAGGING=<TAGGING>,][LEASELMT=<LEASELMT>]]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|VbPortAid is the AID VirtualBridgePortId2.
VLAN|VLAN Address - Address of the VLAN associated with the Port. VLAN is the AID PacketVlanAid.
ARP|Enable/Disable ARP ARP is of type BoolYN.
DHCP|Not supported in release 6.1 and above.Enable/Disable DHCP. DHCP is of type BoolYN.
DHCPDIR|DHCP Directionality. This defines if the Vlan VB Port faces a DHCP-Client, DHCP-Server or no DHCP hosts. DHCPDIR is of type DhcpDirection.
OPT82ACT|Not supported in release 6.0. The action to take if a DHCP packet is received on a Client facing interface with Option82 sub-option 1 /2 content. OPT82ACT is of type Option82Action.
IGMP|IGMP TYPE: a) SINK b) NONE IGMP is of type IgmpType.
PPPOEAC|Enable/Disable PPPOE Access Concentrator PPPOEAC is of type BoolYN.
PPPOESUB|Enable/Disable PPPoE Subscriber PPPOESUB is of type BoolYN.
PRIO|Deprecated in 6.1 and above. VLAN Port Priority. PRIO values are in the range 0-7. PRIO is a Integer.
TAGGING|TAGGING is of type Tagging.
LEASELMT|LEASELMT is of type LeaseLimit.

##### Syntax: ```ED-VODDSTLU:[TID]:<EqptAid>:[CTAG]:::IRCAID=<IRCAID>,[FLOWLMT=<FLOWLMT>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|VOD Destination LU Access Identifier. The address of the VOD Destination Line Unit. EqptAid is the AID EquipmentId3.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid.
FLOWLMT|Flow Limit. The upper bound on the number of VOD flows that can egress through this OLU. For each possible flow, a hidden "VOD Internal Flow VC" is created with source and destination on PP1 of this card. There must be sufficient bandwidth in the shelf to support the specified number of flows. FLOWLMT is a Integer.

##### Syntax: ```ED-VR:[TID]:<VrAid>:[CTAG]:::[DHCPLOCK=<DHCPLOCK>]; ```

##### Parameters
Attribute | Description
|---
VrAid|VrAid is the AID VrAid.
DHCPLOCK|Enable or disable device mobility. When set to "Y", restrict mobility by allowing a DHCP host to obtain an IP address only once for a specific VR. DHCPLOCK is of type BoolYN. The default value is "Y".

##### Syntax: ```ED-VRP:[TID]:<VrpAid>:[CTAG]:::[[MODE=<MODE>,][RATE=<RATE>,][FREQ=<FREQ>,][DQPSK=<DQPSK>,][RAND=<RAND>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
VrpAid|Video Return Path Access Identifier. VrpAid is the AID VrpAid.
MODE|MODE is of type RFReturnMode.
RATE|When MODE = SCTE 55-2, this parameter controls the upstream rate for the RF-Return signal in kbit/sec. RATE is of type VrpDataRate.
FREQ|When MODE = SCTE55-1, frequency is 8096 to 40160 in step sizes of 192 kHz. When MODE = SCTE55-2 and RATE =256 kbps, frequency is 8000 to 26500 in steps of 256 kHz. When MODE = SCTE55-2 and RATE =1544 kbps, frequency is 8000 to 26500 in steps of 1000 kHz. When MODE = SCTE55-2 and RATE =3088 kbps, frequency is 8000 to 26500 in steps of 2000 kHz FREQ is a Integer.
DQPSK|When MODE equals SCTE55-1 set the DQPSK mode to Default or Alternate Operation DQPSK is of type DQPSKMode.
RAND|SCTE55-1 Randomizer Pre-Load - When MODE equals SCTE55-1, set the eight bits of the Randomizer pre-Load. Value range is from 00 to FF in hex. Default value is FF. RAND is a String. RAND is a String.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State of the Video Return Path PST is of type PrimaryStateChg.
SST|Secondary Service State of the Video Return Path. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-VSP:[TID]:<VspAid>:[CTAG]:::[[IP=<IP>,][HOSTPROTO=<HOSTPROTO>,][UDPSTART=<UDPSTART>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
VspAid|The AID of the VSP port being modified. VspAid is the AID VspPortAid.
IP|IP Address for Bearer traffic handled by VSP. IP is the AID IpAid.
HOSTPROTO|Is IP address derived via DHCP or Statically Assigned. The parameter value should be DHCP or STATIC. HOSTPROTO is of type SipHostProto.
UDPSTART|Starting UDP port number for bearer traffic transport handled by VSP. For a VSP on a VIPR/VGP the valid range is 3000-65534. For a VSP on an EGW the valid values are 49408, 53504, 57600, and 61696. UDPSTART is a Integer.
PST|PST is of type PrimaryStateChg.

##### Syntax: ```ED-XDSL:[TID]:<XdslAid>:[CTAG]::[<SRVTYPE >]:[[PKTMODE=<PKTMODE>,][CHNLLAT=<CHNLLAT>,][XDSLTEMPLATE=<XDSLTEMPLATE>,][FALLBACKVPI=<FALLBACKVPI>,][FALLBACKVCI=<FALLBACKVCI>,][XDSLLINEPROF=<XDSLLINEPROF>,][XRDS=<XRDS>,][MRDS=<MRDS>,][XRUS=<XRUS>,][MRUS=<MRUS>,][GOS=<GOS>,][MININPDS=<MININPDS>,][MININPUS=<MININPUS>,][INTLVLATDS=<INTLVLATDS>,][INTLVLATUS=<INTLVLATUS>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][REPTRMVRST=<REPTRMVRST>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
XdslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. XdslAid is the AID TwentyFourPortAid.
SRVTYPE|This parameter specifies the DSL operating profile that dictates the DSL handshaking protocol, channel capacity, and other physical line characteristics based on DSL specifications. SRVTYPE is of type AdslType.
PKTMODE|Packet mode defines if this port is to operate in packet or ATM VC mode. PKTMODE is of type BoolYN.
CHNLLAT|The setting for channel path latency. Choosing a latency path of FAST means minimum (4 ms) delay is expected while choosing a latency path of INTLV (interleaved) means more delay. CHNLLAT is of type ChnlSelect0.
XDSLTEMPLATE|The template contains all the parameters for the DSL line including Advanced Parameters and SVCTYPE. XDSLTEMPLATE is the AID DslProfAid.
FALLBACKVPI|The VPI value to use on the singular VC in packet mode. FALLBACKVPI is of type XdslVPRange.
FALLBACKVCI|The VCI value to use on the singular VC in packet mode. FALLBACKVCI is of type VCRange.
XDSLLINEPROF|This parameters specifies which of the standard profiles to use. XDSLLINEPROF is of type VdslProfRange.
XRDS|The maximum downstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRDS is of type DwnStreamRate.
MRDS|This is the minimum downstream rate for the default channel (kbps). MRDS is of type DwnStreamRate.
XRUS|This is the maximum upstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRUS is of type UpStreamRate.
MRUS|This is the minimum upstream rate for the default channel (kbps). MRUS is of type UpStreamRate.
GOS|Identifies the DSL grade of service for performance monitoring (PM) which will be applied to the port. GOS is the AID GosAid.
MININPDS|The Downstream Minimum Impulse Noise Protection. MININPDS is of type SymbolProtection.
MININPUS|The Upstream Minimum Impulse Noise Protection. MININPUS is of type SymbolProtection.
INTLVLATDS|The Downstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATDS is of type Latency.
INTLVLATUS|The upstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATUS is of type Latency.
TMDS|This parameter specifies the desired downstream signal to noise ratio margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMDS is of type SnrTargetMargins.
XMDS|This parameter specifies the maximum downstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-C. XMDS is of type SnrMaxMargins.
MMDS|This parameter specifies the minimum downstream signal to noise ratio margin in dB. This margin specifies the minimum threshold allowed for modem operation. MMDS is of type SnrMinMargins.
TMUS|This parameter specifies the desired upstream signal to noise ratio (SNR) margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMUS is of type SnrTargetMargins.
XMUS|This parameter specifies the maximum upstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-R. XMUS is of type SnrMaxMargins.
MMUS|This parameter specifies the minimum upstream signal to noise ratio (SNR) margin in dB. This margin specifies the minimum threshold allowed for modem training. MMUS is of type SnrMinMargins.
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the port. REPTRMVRST is of type BoolYN.
DESC|A user-settable description field, up to 31 characters. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ED-XLAN:[TID]:<XLanAid>:[CTAG]:::[[XLANNAME=<XLANNAME>,][XLANBW=<XLANBW>,][TOPO=<TOPO>]]; ```

##### Parameters
Attribute | Description
|---
XLanAid|EXtended LAN Access Identifier. XLanAid is the AID XLanAid.
XLANNAME|EXtended LAN NAME. XLANNAME is a String.
XLANBW|EXtended LAN BandWidth. XLANBW is of type XlanBw.
TOPO|Indicates the topology of the Extended LAN. Note the system makes no effort to ensure the specified topology matches the actual XLAN configuration; ``` it is provided for user convenience only. TOPO is of type EthTopo.

##### Syntax: ```ENT-<OCN>:[TID]:<OcNAid>:[CTAG]:::[[TXS1=<TXS1>,][RXS1=<RXS1>,][LSREN=<LSREN>,][EXT=<EXT>,][FEPM=<FEPM>,][ALMPROF=<ALMPROF>,][SDBER=<SDBER>,][SFBER=<SFBER>,][GOS=<GOS>,][PDOM=<PDOM>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifier. The address of the OCn port being created. OcNAid is the AID FourPortLuAndRapAid.
TXS1|Transmit S1. This parameter is set to Y if the sync status nibble indicates the source of timing. It is set to N if the nibble is set to Do not Use for Synchronization (DUS). TXS1 is of type BoolYN. The default value is "Y".
RXS1|Receive S1. This parameter is set to Y if the received S1 sync status is to be acted uppon. It is set to N if it is to be ignored. RXS1 is of type BoolYN. The default value is "Y".
LSREN|LaSeR ENable. This parameter is set to Y to enable transmitting a signal over this facility. If the facility is to be used for receiving only, the value should be set to N. LSREN is of type BoolYN. The default value is "Y".
EXT|External Interface. This indicates if the OCn port is an internal or external path in the network. The value should be set to "Y" when the port is an external interface. It should be set to "N" when the port is connected to other shelves within a network of C7s. Note that EXT cannot be set to "N" on Sonet-only cards. Also note that this parameter must be changed independently of others, ie. a separate ED-OCn command is required. EXT is of type BoolYN. The default value is "N".
FEPM|Far End Performance Monitoring. When this parameter is set to "N", the Far End Performance Monitoring data is not collected. When retrieving Far End PM, the Monitored Values (MONVAL) field will contain '0' and the Validity (VLDTY) field will contain 'INVLD'. When this parameter is set to "Y", data collection for Far End Performance Monitoring is enabled. The default value is "N". FEPM is of type BoolYN. The default value is "N".
ALMPROF|Alarm Profile. The set of alarm Notification codes to be associated with this entity. ALMPROF is the AID AlmProfileAid. The default value is "AISNR".
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD. The default value is "5".
SFBER|Signal Failed Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Failed Signal. SFBER is of type BitErrorRateSF. The default value is "3".
GOS|Grade of service. This identifies the OCn grade of service for performance monitoring (PM) which will be applied to the OCn port. GOS is the AID GosAid. The default value is "DEFLT".
PDOM|Protection DOMain. This is an integer that is used to associate a transport facility into a protection domain that is used for A to Z connection provisioning. The PDOM for each domain must be a unique non-zero integer. The value of 0 is reserved to indicate that the facility is not to be used for A to Z connections. PDOM is of type Pdom. The default value is "0".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-<STSN>:[TID]:<StsAid>:[CTAG]:::STSMAP=<STSMAP>,[[TIMDET=<TIMDET>,][EXPTRC=<EXPTRC>,][TRC=<TRC>,][FEPM=<FEPM>,][ALMPROF=<ALMPROF>,][SDBER=<SDBER>,][SFBER=<SFBER>,][GOS=<GOS>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path being created. StsAid is the AID StsAid.
STSMAP|STS Mapping. This parameter indicates the type of mapping supported by the STS-p SPE. STSMAP is of type StsMap.
TIMDET|Trace Identifier Mismatch Detection. This parameter indicates whether to turn on or off the trace identifer mismatch detection for the expected trace. TIMDET is of type OnOff. The default value is "OFF".
EXPTRC|Expected Path Trace. This parameter is the expected Path Trace (J1) content. The maximum length of the string is 62 characters. The system will automatically add a carriage return (CR) and line feed (LF) to end of string to make it 64 characters. EXPTRC is a String. The default value is "NULL".
TRC|Transmit Path Trace. This parameter indicates the path trace to be transmitted. The maximum length of the string is 62 characters. The system will automatically add a carriage return (CR) and line feed (LF) to end of string to make it 64 characters. TRC is a String. The default value is "NULL".
FEPM|Far End Performance Monitoring. When this parameter is set to "N", the Far End Performance Monitoring data is not collected. When retrieving Far End PM, the Monitored Values (MONVAL) field will contain '0' and the Validity (VLDTY) field will contain 'INVLD'. When this parameter is set to "Y", data collection for Far End Performance Monitoring is enabled. The default value is "N". FEPM is of type BoolYN. The default value is "N".
ALMPROF|Alarm Profile. The set of alarm Notification codes to be associated with this entity. ALMPROF is the AID AlmProfileStsAid. The default value is "AISNR".
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Path's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD. The default value is "6".
SFBER|Signal Failed Bit Error Rate. The threshold value above which the Path's bit error rate constitutes a Failed Signal. SFBER is of type BitErrorRateSF. The default value is "4".
GOS|Grade of Service Access Identifier. This identifies the specific Grade of Service for Performance Monitoring (PM) which will be applied to the STSnC facility. GOS is the AID GosAid. The default value is "OFF".
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. PYLDSCRM is of type BoolYN. The default value is "Y".
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. The default value is Y for internal interfaces and N for external interfaces. ATMMON is of type BoolYN.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-ADSL:[TID]:<AdslAid>:[CTAG]::[<SRVTYPE>],[<CHNL0>],[<CHNL1>]:[[PROF=<PROF>,][XDSR0=<XDSR0>,][MDSR0=<MDSR0>,][XUSR0=<XUSR0>,][MUSR0=<MUSR0>,][XDSR1=<XDSR1>,][MDSR1=<MDSR1>,][XUSR1=<XUSR1>,][MUSR1=<MUSR1>,][DSEXR=<DSEXR>,][USEXR=<USEXR>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][DSLAT=<DSLAT>,][USLAT=<USLAT>,][TC=<TC>,][RAMODEDS=<RAMODEDS>,][RAMODEUS=<RAMODEUS>,][RAUMDS=<RAUMDS>,][RADMDS=<RADMDS>,][RAUTDS=<RAUTDS>,][RADTDS=<RADTDS>,][RAUMUS=<RAUMUS>,][RADMUS=<RADMUS>,][RAUTUS=<RAUTUS>,][RADTUS=<RADTUS>,][PMMODE=<PMMODE>,][L0TIME=<L0TIME>,][L2TIME=<L2TIME>,][L2ATPR=<L2ATPR>,][L2MINR=<L2MINR>,][L2EXITR=<L2EXITR>,][L2ENTRYR=<L2ENTRYR>,][L2ENTRYT=<L2ENTRYT>,][DSST=<DSST>,][DSET=<DSET>,][USST=<USST>,][USET=<USET>,][GOS=<GOS>,][MININPDS=<MININPDS>,][MININPUS=<MININPUS>,][REPTRMVRST=<REPTRMVRST>,][INCL=<INCL>,][ENABLENOTCH=<ENABLENOTCH>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
AdslAid|Asymmetical Digital Subscriber Line Access Identifier. The address of the ADSL port being provisioned. AdslAid is the AID TwentyFourPortLuAid.
SRVTYPE|Service Type. This parameter specifies the ADSL operating modes that dictate the ADSL handshaking protocol, channel capacity, and other physical line characteristics based on ADSL specifications. SRVTYPE is of type AdslType. The default value is "MM".
CHNL0|Channel 0 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (4 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL0 is of type ChnlSelect0. The default value is "INTLV".
CHNL1|Channel 1 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (2 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL1 is of type ChnlSelect1. The default value is "DISABLE".
PROF|ADSL Profile. This specifies the ADSL profile which is to set the initial values for the confirguration parameters for the ADSL line. These parameters may be over-ridden by the values specified in the other parameters of the ENT-ADSL command. PROF is the AID DslProfAid.
XDSR0|Maximum Downstream Rate - Channel 0 (kbps). XDSR0 is of type DwnStreamRate.
MDSR0|Minimum Downstream Rate - Channel 0 (kbps). MDSR0 is of type DwnStreamRate. The default value is "384".
XUSR0|Maximum Upstream Rate - Channel 0 (kbps). XUSR0 is of type UpStreamRate.
MUSR0|Minimum Upstream Rate - Channel 0 (kbps). MUSR0 is of type UpStreamRate. The default value is "128".
XDSR1|Maximum Downstream Rate - Channel 1 (kbps). XDSR1 is of type DwnStreamRate.
MDSR1|Minimum Downstream Rate - Channel 1 (kbps). MDSR1 is of type DwnStreamRate.
XUSR1|Maximum Upstream Rate - Channel 1 (kbps). XUSR1 is of type UpStreamRate.
MUSR1|Minimum Upstream Rate - Channel 1 (kbps). MUSR1 is of type UpStreamRate.
DSEXR|Downstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. (Values in kbps) DSEXR is of type ExcessRate. The default value is "100".
USEXR|Upstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. (Values in kbps) USEXR is of type ExcessRate. The default value is "100".
TMDS|Target Downstream SNR Margin. This parameter specifies the desired downstream signal to noise ratio margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. Actual connection margins may be greater than or less than the desired target margin based on the configured maximum and minimum downstream bit rates. Higher connect margins will result when maximum configured data rates are lower than the maximum achievable data rates. Lower connect margins will result when the minimum configured data rate is not achievable at the desired margin. TMDS is of type SnrTargetMargins. The default value is "8".
XMDS|Maximum Downstream SNR Margin. This parameter specifies the maximum downstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-C. It may not always be possible to reduce the actual connection margin for short loops and lower bit rate configuration. As a result, a connect margin greater than the specified maximum margin is possible. The maximum downstream SNR margin must be greater than the target downstream SNR margin. XMDS is of type SnrMaxMargins. The default value is "16".
MMDS|Minimum Downstream SNR Margin. This parameter specifies the minimum downstream signal to noise ratio margin in dB. This margin specifies the minimum threshold allowed for modem operation. The connection will fail if the operating downstream margin falls below the specified minimum for more than 20 seconds and a modem retrain will be attempted. The minimum downstream margin must be less than the target downstream margin. MMDS is of type SnrMinMargins. The default value is "0".
TMUS|Target Upstream SNR Margin. This parameter specifies the desired upstream signal to noise ratio (SNR) margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. Actual connection margins may be greater than or less than the desired target margin based on the configured maximum and minimum upstream bit rates. Higher connect margins will result when maximum configured data rates are lower than the maximum achievable data rates. Lower connect margins will result when the minimum configured data rate is not achievable at the desired margin. TMUS is of type SnrTargetMargins. The default value is "8".
XMUS|Maximum Upstream SNR Margin. This parameter specifies the maximum upstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-R. It may not always be possible to reduce the actual connection margin for short loops and lower bit rate configuration. As a result, a connect margin greater than the specified maximum margin is possible. The maximum upstream SNR margin must be greater than the target upstream SNR margin. XMUS is of type SnrMaxMargins. The default value is "16".
MMUS|Minimum Upstream SNR Margin. This parameter specifies the minimum upstream signal to noise ratio (SNR) margin in dB. This margin specifies the minimum threshold allowed for modem training. The connection will fail if the operating upstream margin falls below the specified minimum for more than 20 seconds. The minimum upstream margin must be less than the target upstream margin MMUS is of type SnrMinMargins. The default value is "0".
DSLAT|Downstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. If either DSLAT or USLAT is set to AUTO, both will be set to AUTO in h/w. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. DSLAT is of type Latency. The default value is "AUTO".
USLAT|Upstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. If either DSLAT or USLAT is set to AUTO, both will be set to AUTO in h/w. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. USLAT is of type Latency. The default value is "AUTO".
TC|Trellis Coding. Enables trellis coding to improve the DSL system performance. Trellis coding is an encoding scheme for piggybacking bits onto the electrical signal on the twisted pair. TC is of type TrellisCoding. The default value is "ENABLED".
RAMODEDS|Rate Adaptation MODE DownStream. RAMODEDS is of type RateAdaptationMode. The default value is "INIT".
RAMODEUS|Rate Adaptation MODE UpStream. RAMODEUS is of type RateAdaptationMode. The default value is "INIT".
RAUMDS|Rate Adaptation Upshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RAUMDS is of type SnrMaxMargins. The default value is "9".
RADMDS|Rate Adaptation Downshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RADMDS is of type SnrMaxMargins. The default value is "3".
RAUTDS|Rate Adaptation Upshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RAUTDS is of type RateAdaptationMarginSeconds. The default value is "60".
RADTDS|Rate Adaptation Downshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RADTDS is of type RateAdaptationMarginSeconds. The default value is "60".
RAUMUS|Rate Adaptation Upshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RAUMUS is of type SnrMaxMargins. The default value is "9".
RADMUS|Rate Adaptation Downshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RADMUS is of type SnrMaxMargins. The default value is "3".
RAUTUS|Rate Adaptation Upshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RAUTUS is of type RateAdaptationMarginSeconds. The default value is "60".
RADTUS|Rate Adaptation Downshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RADTUS is of type RateAdaptationMarginSeconds. The default value is "60".
PMMODE|Power Management MODE. PMMODE is of type AdslPowerMgmtStates. The default value is "L0".
L0TIME|Minimum L0 Time interval between L2 exit and next L2 entry. (0-255 seconds) L0TIME is a Integer. The default value is "255".
L2TIME|Minimum L2 time interval between L2 entry and first L2 trim. (0-255 seconds) L2TIME is a Integer. The default value is "255".
L2ATPR|Maximum Aggregate Transmit Power Reduction per L2 trim. (dB) L2ATPR is of type SnrMaxMargins. The default value is "3".
L2MINR|Minimum Data Rate in Low Power Mode (L2). This parameter specifies the minimum net data rate (in Kbps) during the low power state. If the actual user data rate is lower than L2MINR, raw cells will be injected to maintain the provisioned value. The value can range from 256 to 1024 Kbps. L2MINR is a Integer. The default value is "1024".
L2EXITR|L2 Exit Rate Threshold. This parameter specifies the downstream datarate threshold (in Kbps), which triggers exit from low power state (L2). The value ranges between 1 and 1024 Kbps, and must be less than L2MINR. L2EXITR is a Integer. The default value is "512".
L2ENTRYR|L2 Entry Rate Threshold. This parameter specifies the downstream data rate threshold (in Kbps), which triggers autonomous entry into low power state (L2). The value can range from 1 to 1024, and must be less or equal to L2EXITR. L2ENTRYR is a Integer. The default value is "1".
L2ENTRYT|L2 Entry Time Threshold. This parameter specifies minimum interval of time (in seconds) that the net data rate should stay below L2ENTRYR before autonomous entry into low power state (L2). The value can range from 900 to 65535 seconds. L2ENTRYT is a Integer. The default value is "180".
DSST|DownStream Start Tone index. DSST must be less than or equal to DSET. DSST is a Integer. The default value is "0".
DSET|DownStream End Tone index. DSET must be greater than or equal to DSST. DSET is a Integer. The default value is "0".
USST|UpStream Start Tone index. USST must be less than or equal to USET. USST is a Integer. The default value is "0".
USET|UpStream End Tone index. USET must be greater than or equal to USST. USET is a Integer. The default value is "0".
GOS|Grade of service. This identifies the ADSL grade of service for performance monitoring (PM) which will be applied to the ADSL port. GOS is the AID GosAid. The default value is "OFF".
MININPDS|The Downstream Minimum Impulse Noise Protection. MININPDS is of type SymbolProtection. The default value is "0.5".
MININPUS|The Upstream Minimum Impulse Noise Protection. MININPUS is of type SymbolProtection. The default value is "0.5".
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the port. Note that RMV/RST are reported upon every modem retrain and can clutter the event logs if enabled. REPTRMVRST is of type BoolYN. The default value is "N".
INCL|INCLusive INCL is of type BoolYN. The default value is "N".
ENABLENOTCH|Enable notching for adsl. ENABLENOTCH is of type BoolYN.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-AP:[TID]:<ApAid>:[CTAG]:::[[ATMMAP=<ATMMAP>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][PDOM=<PDOM>,][GOS=<GOS>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid.
ATMMAP|When payload signal is a form that may be altered at the ATM Resource port, this parameter specifies the mapping. ATMMAP is of type AtmMap. The default value is "IMA".
PYLDSCRM|This parameter is set to Y to enable the scrambling of ATM cells. It is only applicable when ATMMAP is UNI or NNI. PYLDSCRM is of type BoolYN. The default value is "N".
ATMMON|This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to NNI and UNI interfaces ATMMON is of type BoolYN. The default value is "N".
PDOM|Protection Domain. This is an integer that is used to associate a transport facility into a protection domain that is used for A to Z connection provisioning. The PDOM for each domain must be a unique non-zero integer. The value of 0 is reserved to indicate that the facility is not to be used for A to Z connections PDOM is of type Pdom. The default value is "0".
GOS|Grade of Service. This identifies the AP grade of service for performance monitoring (PM) which will be applied to the AP port. GOS is the AID GosAid. The default value is "OFF".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Grade of Service. This identifies the AP grade of service for performance monitoring (PM) which will be applied to the AP port. PST is of type PrimaryStateChg.
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-AP-T1:[TID]:<ApAid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid.
PLOCN|Physical Location. This is the AID of a T1 or HDSL port being associated with the AP port. PLOCN is the AID TwelvePortLuAid.

##### Syntax: ```ENT-AVO:[TID]:<OntPortAid>:[CTAG]:::[[OMI=<OMI>,][RFRTRN=<RFRTRN>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Analog Video Overlay Port Access Identifer. The address of the AVO port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortAid.
OMI|The per-channel Optical Modulation Index of the RF-Video content that is being carried in the Analog Video Overlay signal. This parameter is only applied to ONTs that return an OMI value during initialization.
The value is a percentage, and must be between 3.2 and 3.8 . OMI is a String. The default value is "3.8".

RFRTRN|This will directly control the operation of the RF-Return function of the ONT, instead of enabling RF-Return only when RF-Video services are enabled. RFRTRN is of type RfRtrnAdminState. The default value is "LOCKED".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String. The default value is """".
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-BWC:[TID]:<BwcAid>:[CTAG]:::[[IG=<IG>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
BwcAid|Bandwidth Constraint Access Identifier. Identifier of the Bandwidth Constraint to be operated upon. BwcAid is the AID BwcProvAid.
IG|Interface Group. This is the interface group that is associated with the bandwidth constraint. This is a restricted parameter and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. IG is the AID IgAid.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.

##### Syntax: ```ENT-BWCLINK:[TID]:<LinkBwcAid>:[CTAG]:::[[RXLMT=<RXLMT>,][RXNTFY=<RXNTFY>,][TXLMT=<TXLMT>,][TXNTFY=<TXNTFY>]]; ```

##### Parameters
Attribute | Description
|---
LinkBwcAid|Link Bandwidth Constraint Access Identifier. Identifies the Link Bandwidth Constraint to be operated upon. LinkBwcAid is the AID LinkBwcAid.
RXLMT|Receive Limit. Bandwidth reserved for the constraint in the ingress or receive direction on the link in kbps. RXLMT is a Integer. The default value is "0".
RXNTFY|Receive Notification Threshold. This parameter sets the percent threshold at which the RXBWNTFY condition is raised. This condition indicates that bandwidth usage for the constraint in the receive direction exceeds this value. If this is set to OFF, no condition is raised. RXNTFY is of type BwcNtfyThrRange. The default value is "95".
TXLMT|Transmit Limit. Bandwidth reserved for the constraint in the egress or transmit direction on the link in kbps. TXLMT is a Integer. The default value is "0".
TXNTFY|Transmit Notification Threshold. This parameter sets the percent threshold at which the TXBWNTFY condition is raised. This condition indicates that bandwidth usage for the constraint in the receive direction exceeds this value. If this is set to OFF, no condition is raised. TXNTFY is of type BwcNtfyThrRange. The default value is "95".

##### Syntax: ```ENT-CFG-ONT:[TID]:<CfgAid>:[CTAG]:::FNAME=<FNAME>,VEND=<VEND>,[[MODEL=<MODEL>,][PROD=<PROD>]],VER=<VER>,INST=<INST>; ```

##### Parameters
Attribute | Description
|---
CfgAid|Aid of ONT configuration file. CfgAid is the AID CfgAid.
FNAME|The file name of ONT CFG file. Character string up to 30 bytes. It is case sensitive. FNAME is a String.
VEND|Vendor ID. Character string up to 4 bytes. It is case sensitive. VEND is a String.
MODEL|Model Identifier. Character string up to 14 bytes. It is case sensitive. MODEL is a String.
PROD|Profuct Identifier. Character string up to 2 bytes. It is case sensitive. PROD is a String.
VER|Version. Character string up to 14 bytes. It is case sensitive. VER is a String.
INST|Instance. Character string up to 3 bytes.INST can be one of the following values: "RG1", "RG2", "RG3", "RG4", "RG5", "RG6", "RG7", "RG8". INST is of type CFGONTINST.

##### Syntax: ```ENT-CRS-<STSN>:[TID]:<SrcStsAid>,<DstStsAid>:[CTAG]::[<CCT>]:[[PROTN=<PROTN>,][HBH=<HBH>]],PATH=<PATH>; ```

##### Parameters
Attribute | Description
|---
SrcStsAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. SrcStsAid is the AID StsCrsAid.
DstStsAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. DstStsAid is the AID StsCrsAid.
CCT|Connection Type. This parameter is used for specifying whether the cross-connect is a one or two way connection. CCT is of type ConnectionType3. The default value is "2WAY".
PROTN|Cross-Connect Protection. When cross-connect are created the user has the option of making the cross-connect protected or not. This parameter indicates if the cross-connect should be protected with a protection path or not. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. PROTN is of type BoolYN. The default value is "N".
HBH|Hop-By-Hop. This parameter indicates whether the cross-connect is being entered Hop-By-Hop. If it is, it indicates whether this is part of the working or the protection path. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. HBH is of type HopByHop. The default value is "NOTHBH".
PATH|Path on which to create the cross-connect. Note: PROTN and HBH have been deprecated. Specifying PATH is now the preferred way to enter cross-connects. The presence of PATH will also override any values specified in PROTN or HBH. Note: For network-scoped creates (end-to-end), only UNPROT and BOTH apply. PATH is of type Path.

##### Syntax: ```ENT-CRS-DCC:[TID]:<CrsDccSrcAid>,<CrsDccDestAid>:[CTAG]:::[[PROTN=<PROTN>,][HBH=<HBH>]],PATH=<PATH>,[VIA=<VIA>]; ```

##### Parameters
Attribute | Description
|---
CrsDccSrcAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. SDCC denotes a section DCC. LDCC denotes a line DCC. LDCC(1-3) denotes one byte in the line DCC overhead. CrsDccSrcAid is the AID DccAid.
CrsDccDestAid|Destination (To) Access Identifier. The address of the destination (to) endpoint of the cross-connect being created. SDCC denotes a section DCC. LDCC denotes a line DCC. LDCC(1-3) denotes one byte in the line DCC overhead. CrsDccDestAid is the AID DccAid.
PROTN|Cross-Connect Protection. When cross-connect are created the user has the option of making the cross-connect protected or not. This parameter indicates if the cross-connect should be protected with a protection path or not. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. PROTN is of type BoolYN. The default value is "N".
HBH|Hop-By-Hop. This parameter indicates whether the cross-connect is being entered Hop-By-Hop. If it is, it indicates whether this is part of the working or the protection path. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. HBH is of type HopByHop. The default value is "WORK".
PATH|Path on which to create the cross-connect. Note: PROTN and HBH have been deprecated. Specifying PATH is now the preferred way to enter cross-connects. The presence of PATH will also override any values specified in PROTN or HBH. Note: For network-scoped creates (end-to-end), only UNPROT and BOTH apply. PATH is of type Path.
VIA|Channel VIA which cross-connect is set up. VIA must be specified for inter-shelf connections; ``` it must not be specified for intra-shelf connections. VIA is of type DataLink.

##### Syntax: ```ENT-CRS-T0:[TID]:<SrcDs0Aid>,<DstDs0Aid>:[CTAG]::[<CCT>]:[[NSG=<NSG>,][NDS0=<NDS0>,][NAILUP=<NAILUP>,][IDT=<IDT>,][ECMODE=<ECMODE>,][AUDIT=<AUDIT>]]; ```

##### Parameters
Attribute | Description
|---
SrcDs0Aid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. This endpoint can refer to either a Ds0 facility or a call reference value (circuit) within a GR-303 or GR-8 Interface Group. SrcDs0Aid is the AID T0Id1.
DstDs0Aid|Destination (To) Access Identifier. The address of the destination (to) endpoint of the cross-connect being created. DstDs0Aid is the AID T0Id.
CCT|Connection Type. This parameter is used for specifying whether the cross-connect is a one or two way connection. CCT is of type ConnectionType2. The default value is "2WAY".
NSG|Number of Signaling Bits. The NSG parameter specifies the number of signaling bits in the bit-oriented subscriber signaling channel. This parameter can usually be omitted so that it can be set to the value consistent with the network interface. However, when the network interface is a T1 trunk with ESF signaling that is not part of a GR-303 or GR-8 IG, values of 0 (clear channel), 2 (DS0 Yellow and AIS disabled), or 4 (full ESF codes enabled) could be . NSG=2 is appropriate if an SF (D4) T1 trunk is involved. NSG=3 is reserved for the GR-8 signaling scheme which encodes 9 states. NSG is of type Nsg. The default value is "Endpoint Dependent".
NDS0|Number of DS0s. THIS PARAMETER IS NOT TO BE USED AS A SHORTHAND FOR MUTIPLE ORDINARY CONNECTIONS. DOING SO WILL RESULT IN INEFFICIENT BANDWIDTH USAGE, CONFUSING RETRIEVAL RESULTS, AND THE INABILITY TO DELETE THE CONNECTIONS SEPARATELY. The NDS0 parameter specifies the number of DS0s that are to be created in the same VC. When a value greater than 1 is specified, consecutive DS0s are connected starting with the source and destination DS0s. This parameter is required to insure that the delay is the same within the set of DS0s. This is needed for services like ISDN transport where the service cannot tolerate differing frame delays among the DS0s from the same port. On retrieval, such a connection is displayed as a single connection but with an NDS0 parameter greater than 1. NDS0 is a Integer. The default value is "1".
NAILUP|NAILUP the connection. Specifying NAILUP=Y with this parameter can be used to specify that a connection is to be maintained, even when no call is being carried. If the connection is carried over a T1 Transport Group (T1TG), bandwidth will be permanently consumed by the connection. Bandwidth is only consumed during an active call when NAILUP=N.
It is by default "Y" when an endpoint of the connection cannot indicate the beginning or end of a call. This is the case with EBS, DDS, and TO endpoints. It is also currently the case with GR-8 Mode I endpoints. It is by default "N" for all other endpoints. A GR-8 Mode II Coin service must use NAILUP=Y.

NAILUP is of type BoolYN. The default value is "Endpoint / T1TG Dependent".
IDT|IDT is the AID IgAid and is listable.
ECMODE|Echo Cancellation Mode. This parameter is only applicable to VOIP lines. ECMODE is of type Ds0EcMode. The default value is "USEIG".
AUDIT|Enable line audit. AUDIT is of type BoolYN. The default value is "N".

##### Syntax: ```ENT-CRS-T1:[TID]:<SrcDs1Aid>,<DstDs1Aid>:[CTAG]::[<CCT>]:[[PROTN=<PROTN>,][HBH=<HBH>]],PATH=<PATH>,[BWC=<BWC>]; ```

##### Parameters
Attribute | Description
|---
SrcDs1Aid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. This can include a VC portion for hop-by-hop. SrcDs1Aid is the AID T1CrsAid.
DstDs1Aid|Destination (To) Access Identifier. The address of the destination (to) endpoint of the cross-connect being created. This can include a VC portion for hop-by-hop. DstDs1Aid is the AID T1CrsAid.
CCT|Connection Type. This parameter is used for specifying whether the cross-connect is a one or two way connection. For T1 cross-connections, "2WAY" is the only valid value. CCT is of type ConnectionType2. The default value is "2WAY".
PROTN|Cross-Connect Protection. When cross-connect are created the user has the option of making the cross-connect protected or not. This parameter indicates if the cross-connect should be protected with a protection path or not. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. PROTN is of type BoolYN. The default value is "N".
HBH|Hop-By-Hop. This parameter indicates whether the cross-connect is being entered Hop-By-Hop. If it is, it indicates whether this is part of the working or the protection path. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. HBH is of type HopByHop. The default value is "NOTHBH".
PATH|Path on which to create the cross-connect. Note: PROTN and HBH have been deprecated. Specifying PATH is now the preferred way to enter cross-connects. The presence of PATH will also override any values specified in PROTN or HBH. Note: For network-scoped creates (end-to-end), only UNPROT and BOTH apply. PATH is of type Path.
BWC|Bandwidth Constraint. The Bandwidth Constraint used when creating the cross-connect. BWC is the AID BwcProvAid.

##### Syntax: ```ENT-CRS-VC:[TID]:<SrcVcAid>,<DstVcAid>:[CTAG]::[<CCT>]:[[PROTN=<PROTN>,][HBH=<HBH>,][PC=<PC>]],TRFPROF=<TRFPROF>,[BCKPROF=<BCKPROF>],PATH=<PATH>,[[BWC=<BWC>,][SRCPPL=<SRCPPL>,][DSTPPL=<DSTPPL>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVcAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. SrcVcAid is the AID VcId19.
DstVcAid|Destination (To) Access Identifier. The address of the destination (to) endpoint of the cross-connect being created. DstVcAid is the AID VcId20.
CCT|Connection Type. This parameter is used for specifying whether the cross-connect is a one or two way connection. CCT is of type ConnectionType. The default value is "2WAY".
PROTN|Cross-Connect Protection. When cross-connect are created the user has the option of making the cross-connect protected or not. This parameter indicates if the cross-connect should be protected with a protection path or not. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. PROTN is of type BoolYN. The default value is "N".
HBH|Hop-By-Hop. This parameter indicates whether the cross-connect is being entered Hop-By-Hop. If it is, it indicates whether this is part of the working or the protection path. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. HBH is of type HopByHop. The default value is "NOTHBH".
PC|Protection Class - Indicates whether the cross connect is uses Bridged or UnBridged protection. PC is of type ProtClass.
TRFPROF|Traffic Profile. This parameter identifies which Traffic Profile which will be applied to the cross-connect. The Traffic Profile specifies the bandwidth parameters. TRFPROF is the AID TrfId. The default value is "UBR".
BCKPROF|Backward Traffic Profile. This parameter identifies which Traffic Profile which applies to the backward direction of the cross-connect. If no BCKPROF is specified, then the service on the cross-connect is symmetrical and the TRFPROF is applied to both directions. BCKPROF is the AID TrfId. The default value is "UBR".
PATH|Path on which to create the cross-connect. Note: PROTN and HBH have been deprecated. Specifying PATH is now the preferred way to enter cross-connects. The presence of PATH will also override any values specified in PROTN or HBH. Note: For network-scoped creates (end-to-end), only UNPROT and BOTH apply. PATH is of type Path.
BWC|Bandwidth Constraint. The Bandwidth Constraint used when creating the cross-connect. BWC is the AID BwcAid. The default value is "None".
SRCPPL|Source Path Protection Label. This parameter indicates the PPL association for the cross-connect source end-point, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. SRCPPL is the AID PplId1.
DSTPPL|Destination Path Protection Label. This parameter indicates the PPL association for the cross-connect destination end-point, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. DSTPPL is the AID PplId1.
INCL|INCLusive. This parameter provides a way for the user to override the check that prevents creating using ENT-CRS-VC to create a Video VC, which would normally be created using ENT-CRS-VIDVC. This should only be needed in the case of entering a new shelf in a Video VC that is normally created A to Z, such as the IP VC. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```ENT-CRS-VIDVC:[TID]:<SrcVcAid>,<DstVcAid>:[CTAG]:::IRCAID=<IrcAid>,TRFPROF=<TRFPROF>,[BCKPROF=<BCKPROF>],PATH=<PATH>,[[PC=<PC>,][BWC=<BWC>,][ARP=<ARP>,][PARP=<PARP>,][SRCPPL=<SRCPPL>,][DSTPPL=<DSTPPL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVcAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. SrcVcAid is the AID VidvcId3.
DstVcAid|Destination (To) Access Identifier. The address of the destination (to) endpoint of the cross-connect being created. DstVcAid is the AID VidvcId3.
IrcAid|The slot address of the IRC. IrcAid is the AID SlotLuAid.
TRFPROF|Traffic Profile. This parameter identifies which Traffic Profile which will be applied to the cross-connect. The Traffic Profile specifies the bandwidth parameters. The Traffic Profile must have its APPID set to one of the video application ids. TRFPROF is the AID TrfId.
BCKPROF|Backward Traffic Profile. This parameter identifies which Traffic Profile which applies to the backward direction of the cross-connect. If no BCKPROF is specified, then the service on the cross-connect is symmetrical and the TRFPROF is applied to both directions. The Backward Traffic Profile must have its APPID set to one of the video application ids. BCKPROF is the AID TrfId.
PATH|Path on which to create the cross-connect. Note: For A2Z, only UNPROT and BOTH apply. For HBH, UNPROT, WKG and PROT apply. PATH is of type Path.
PC|Protection Class - Indicates whether the cross connect is using Bridged or UnBridged protection. If PC value is not specified, "UNBR" is applied for all video applications that don't use class of service as CBR or UBR; ``` otherwise "BR" protection is applied. PC is of type ProtClassAny.
BWC|Bandwidth Constraint. The Bandwidth Constraint used when creating the cross-connect. BWC is the AID BwcAid. The default value is "None".
ARP|ARP Enabled. This option is only valid on VCs with a traffic profile containing the IP application ID. If set to Y, the IRC will answer ARP requests on this VC, thus creating dynamic ARP entries. ARP is of type BoolYN. The default value is "N".
PARP|Proxy ARP Enabled. This option is only valid on VCs with a traffic profile containing the IP application ID. PARP is of type BoolYN. The default value is "Y".
SRCPPL|Source Path Protection Label. This parameter indicates the PPL association for the cross-connect source end-point, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. SRCPPL is the AID PplId1.
DSTPPL|Destination Path Protection Label. This parameter indicates the PPL association for the cross-connect destination end-point, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. DSTPPL is the AID PplId1.

##### Syntax: ```ENT-CRS-VP:[TID]:<SrcVpAid>,<DstVpAid>:[CTAG]::[<CCT>]:[[PROTN=<PROTN>,][HBH=<HBH>,][PC=<PC>]],TRFPROF=<TRFPROF>,[BCKPROF=<BCKPROF>],PATH=<PATH>,[[BWC=<BWC>,][SRCPPL=<SRCPPL>,][DSTPPL=<DSTPPL>]]; ```

##### Parameters
Attribute | Description
|---
SrcVpAid|Source (From) Access Identifier. The address of the source (from) endpoint of the cross-connect being created. SrcVpAid is the AID VpAid.
DstVpAid|Destination (To) Access Identifier. The address of the destination (to) endpoint of the cross-connect being created. DstVpAid is the AID VpAid.
CCT|Connection Type, used for specifying one or two way connections; ``` a null value defaults to 2WAY. CCT is of type ConnectionType. The default value is "2WAY".
PROTN|Cross-Connect Protection. When cross-connect are created the user has the option of making the cross-connect protected or not. This parameter indicates if the cross-connect should be protected with a protection path or not. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. PROTN is of type BoolYN. The default value is "N".
HBH|Hop-By-Hop. This parameter indicates whether the cross-connect is being entered Hop-By-Hop. If it is, it indicates whether this is part of the working or the protection path. NOTE: the HBH and PROTN parameters have been deprecated; ``` the PATH parameter should be used instead. HBH is of type HopByHop. The default value is "NOTHBH".
PC|Protection Class - Indicates whether the cross connect is uses Bridged or UnBridged protection. PC is of type ProtClass.
TRFPROF|Traffic Profile. This parameter identifies which Traffic Profile which will be applied to the cross-connect. The Traffic Profile specifies the bandwidth parameters. TRFPROF is the AID TrfId. The default value is "UBR".
BCKPROF|Backward Traffic Profile. This parameter identifies which Traffic Profile which applies to the backward direction of the cross-connect. If no BCKPROF is specified, then the service on the cross-connect is symmetrical and the TRFPROF is applied to both directions. BCKPROF is the AID TrfId. The default value is "UBR".
PATH|Path on which to create the cross-connect. Note: PROTN and HBH have been deprecated. Specifying PATH is now the preferred way to enter cross-connects. The presence of PATH will also override any values specified in PROTN or HBH. Note: For network-scoped creates (end-to-end), only UNPROT and BOTH apply. PATH is of type Path.
BWC|Bandwidth Constraint. The Bandwidth Constraint used when creating the cross-connect. BWC is the AID BwcAid. The default value is "None".
SRCPPL|Source Path Protection Label. This parameter indicates the PPL association for the cross-connect source end-point, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. SRCPPL is the AID PplId1.
DSTPPL|Destination Path Protection Label. This parameter indicates the PPL association for the cross-connect destination end-point, if applicable. This parameter should only be used by expert users and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. DSTPPL is the AID PplId1.

##### Syntax: ```ENT-CVIDREG:[TID]:<CVidRegAid>:[CTAG]:::SVID=<SVID>,[PRIO=<PRIO>],RCVID=<RCVID>; ```

##### Parameters
Attribute | Description
|---
CVidRegAid|CVID Registration Access Identifier. CVidRegAid is the AID CVidRegAid.
SVID|S-Vlan ID. This represents the SVLAN to be associated with the C-tagged frame. SVID is a Integer.
PRIO|802.1q Priority Bits Policy. PRIO is of type PrioBits. The default value is "0".
RCVID|Relay C-VID. Used to translate the incoming local C-Tag for tagged frames arriving on this user-side port. RCVID is of type RCVid.

##### Syntax: ```ENT-DHCP-OUI:[TID]:<OUIAID>:[CTAG]:::RTRAID=<RTRAID>,[[GADDR=<GADDR>,][OUITYPE=<OUITYPE>]]; ```

##### Parameters
Attribute | Description
|---
OUIAID|Organizationally Unique Identifier. The OUI is first 3 octets of the MAC address and identifies the vendor OUIAID is the AID OuiAid.
RTRAID|Router AID - target slot address of the command (currently, the slot address is the IRC) RTRAID is the AID SlotLuAid.
GADDR|Gateway IP address. The discover message is relayed to this server. Note: This parameter is deprecated beginning with C7 release 5.0, but maintained for CMS TL1 only to support backward compatibility. GADDR is the AID IpAid.
OUITYPE|OUI Equipment type. The default value is "STB" except if the OUI is 00-00-00 in which case the default is "OTHER". OUITYPE is of type IpHostEqptType.

##### Syntax: ```ENT-DHCPSVR:[TID]:<IP>:[CTAG]:::[[RTRAID=<RTRAID>,][OPTION82=<OPTION82>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP Address of the DHCP server. IP is the AID IpAid.
RTRAID|RTRAID is the AID RouterAid.
OPTION82|DHCP Option 82 - This feature adds a unique identifier in the relay agent information option. OPTION82 is of type Option82.

##### Syntax: ```ENT-EC1:[TID]:<Ec1Aid>:[CTAG]:::[[FEPM=<FEPM>,][ALMPROF=<ALMPROF>,][SDBER=<SDBER>,][SFBER=<SFBER>,][GOS=<GOS>,][LBO=<LBO>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|Access Identifier. The address of the EC1 port being created. Ec1Aid is the AID TwelvePortLuAid.
FEPM|Far End Performance Monitoring. When this parameter is set to "N", the Far End Performance Monitoring data is not collected. When retrieving Far End PM, the Monitored Values (MONVAL) field will contain '0' and the Validity (VLDTY) field will contain 'INVLD'. When this parameter is set to "Y", data collection for Far End Performance Monitoring is enabled. The default value is "N". FEPM is of type BoolYN. The default value is "N".
ALMPROF|Alarm Profile. The set of alarm Notification codes to be associated with this entity. ALMPROF is the AID AlmProfileAid. The default value is "AISCR".
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD. The default value is "5".
SFBER|Signal Failed Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Failed Signal. Only values of 3 and 4 are valid for EC1. SFBER is of type BitErrorRateSF. The default value is "3".
GOS|Grade of service. This identifies the EC1 grade of service for performance monitoring (PM) which is applied to the EC1 port. GOS is the AID GosAid. The default value is "DEFLT".
LBO|Line Build Out. LBO is a Integer. The default value is "100".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-EOAM-FMP:[TID]:<FMPAID>:[CTAG]:::[[FRMSIZE=<FRMSIZE>,][DELAYRATE=<DELAYRATE>,][LOSSRATE=<LOSSRATE>,][LOSSMEASTYPE=<LOSSMEASTYPE>,][LOSSFRMTYPE=<LOSSFRMTYPE>,][MAXNELOSSALM=<MAXNELOSSALM>,][MAXNELOSSALMCLR=<MAXNELOSSALMCLR>,][AVENELOSSALM=<AVENELOSSALM>,][AVENELOSSALMCLR=<AVENELOSSALMCLR>,][MAXFELOSSALM=<MAXFELOSSALM>,][MAXFELOSSALMCLR=<MAXFELOSSALMCLR>,][AVEFELOSSALM=<AVEFELOSSALM>,][AVEFELOSSALMCLR=<AVEFELOSSALMCLR>,][MAXRTDLYALM=<MAXRTDLYALM>,][MAXRTDLYALMCLR=<MAXRTDLYALMCLR>,][AVERTDLYALM=<AVERTDLYALM>,][AVERTDLYALMCLR=<AVERTDLYALMCLR>,][MAXRTDLYVARALM=<MAXRTDLYVARALM>,][MAXRTDLYVARALMCLR=<MAXRTDLYVARALMCLR>,][AVERTDLYVARALM=<AVERTDLYVARALM>,][AVERTDLYVARALMCLR=<AVERTDLYVARALMCLR>,][MAXNEDLYALM=<MAXNEDLYALM>,][MAXNEDLYALMCLR=<MAXNEDLYALMCLR>,][AVENEDLYALM=<AVENEDLYALM>,][AVENEDLYALMCLR=<AVENEDLYALMCLR>,][MAXNEDLYVARALM=<MAXNEDLYVARALM>,][MAXNEDLYVARALMCLR=<MAXNEDLYVARALMCLR>,][AVENEDLYVARALM=<AVENEDLYVARALM>,][AVENEDLYVARALMCLR=<AVENEDLYVARALMCLR>,][MAXFEDLYALM=<MAXFEDLYALM>,][MAXFEDLYALMCLR=<MAXFEDLYALMCLR>,][AVEFEDLYALM=<AVEFEDLYALM>,][AVEFEDLYALMCLR=<AVEFEDLYALMCLR>,][MAXFEDLYVARALM=<MAXFEDLYVARALM>,][MAXFEDLYVARALMCLR=<MAXFEDLYVARALMCLR>,][AVEFEDLYVARALM=<AVEFEDLYVARALM>,][AVEFEDLYVARALMCLR=<AVEFEDLYVARALMCLR>]]; ```

##### Parameters
Attribute | Description
|---
FMPAID|FMPAID is the AID EthOamFmpAid.
FRMSIZE|FRMSIZE is a Integer.
DELAYRATE|DELAYRATE is of type EthOamFmpSamplePeriod.
LOSSRATE|LOSSRATE is of type EthOamFmpSamplePeriod.
LOSSMEASTYPE|LOSSMEASTYPE is of type EthOamLossMsType.
LOSSFRMTYPE|LOSSFRMTYPE is of type EthOamLossFrameType.
MAXNELOSSALM|MAXNELOSSALM is of type EthOamLossAlmThreshold.
MAXNELOSSALMCLR|MAXNELOSSALMCLR is of type EthOamLossAlmThreshold.
AVENELOSSALM|AVENELOSSALM is of type EthOamLossAlmThreshold.
AVENELOSSALMCLR|AVENELOSSALMCLR is of type EthOamLossAlmThreshold.
MAXFELOSSALM|MAXFELOSSALM is of type EthOamLossAlmThreshold.
MAXFELOSSALMCLR|MAXFELOSSALMCLR is of type EthOamLossAlmThreshold.
AVEFELOSSALM|AVEFELOSSALM is of type EthOamLossAlmThreshold.
AVEFELOSSALMCLR|AVEFELOSSALMCLR is of type EthOamLossAlmThreshold.
MAXRTDLYALM|MAXRTDLYALM is of type EthOamDelayAlmThreshold.
MAXRTDLYALMCLR|MAXRTDLYALMCLR is of type EthOamDelayAlmThreshold.
AVERTDLYALM|AVERTDLYALM is of type EthOamDelayAlmThreshold.
AVERTDLYALMCLR|AVERTDLYALMCLR is of type EthOamDelayAlmThreshold.
MAXRTDLYVARALM|MAXRTDLYVARALM is of type EthOamDelayAlmThreshold.
MAXRTDLYVARALMCLR|MAXRTDLYVARALMCLR is of type EthOamDelayAlmThreshold.
AVERTDLYVARALM|AVERTDLYVARALM is of type EthOamDelayAlmThreshold.
AVERTDLYVARALMCLR|AVERTDLYVARALMCLR is of type EthOamDelayAlmThreshold.
MAXNEDLYALM|MAXNEDLYALM is of type EthOamDelayAlmThreshold.
MAXNEDLYALMCLR|MAXNEDLYALMCLR is of type EthOamDelayAlmThreshold.
AVENEDLYALM|AVENEDLYALM is of type EthOamDelayAlmThreshold.
AVENEDLYALMCLR|AVENEDLYALMCLR is of type EthOamDelayAlmThreshold.
MAXNEDLYVARALM|MAXNEDLYVARALM is of type EthOamDelayAlmThreshold.
MAXNEDLYVARALMCLR|MAXNEDLYVARALMCLR is of type EthOamDelayAlmThreshold.
AVENEDLYVARALM|AVENEDLYVARALM is of type EthOamDelayAlmThreshold.
AVENEDLYVARALMCLR|AVENEDLYVARALMCLR is of type EthOamDelayAlmThreshold.
MAXFEDLYALM|MAXFEDLYALM is of type EthOamDelayAlmThreshold.
MAXFEDLYALMCLR|MAXFEDLYALMCLR is of type EthOamDelayAlmThreshold.
AVEFEDLYALM|AVEFEDLYALM is of type EthOamDelayAlmThreshold.
AVEFEDLYALMCLR|AVEFEDLYALMCLR is of type EthOamDelayAlmThreshold.
MAXFEDLYVARALM|MAXFEDLYVARALM is of type EthOamDelayAlmThreshold.
MAXFEDLYVARALMCLR|MAXFEDLYVARALMCLR is of type EthOamDelayAlmThreshold.
AVEFEDLYVARALM|AVEFEDLYVARALM is of type EthOamDelayAlmThreshold.
AVEFEDLYVARALMCLR|AVEFEDLYVARALMCLR is of type EthOamDelayAlmThreshold.

##### Syntax: ```ENT-EOAM-MEG:[TID]:<MEGAID>:[CTAG]:::[[MEGNAME=<MEGNAME>,][VLAN=<VLAN>,][LEVEL=<LEVEL>,][MEGIDFMT=<MEGIDFMT>,][RMEPIDLIST=<RMEPIDLIST>,][CCMINT=<CCMINT>,][AUTODISC=<AUTODISC>,][AUTODISCTMO=<AUTODISCTMO>,][MINCCDEFECT=<MINCCDEFECT>,][ALMTIME=<ALMTIME>,][ALMCLRTIME=<ALMCLRTIME>]]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid.
MEGNAME|MEGNAME is a String.
VLAN|VLAN is the AID VlanIndexAid.
LEVEL|LEVEL is of type ZeroTo7.
MEGIDFMT|MEGIDFMT is of type BoolYN.
RMEPIDLIST|RMEPIDLIST is of type OneTo8191 and is listable.
CCMINT|CCMINT is of type CcmInterval.
AUTODISC|AUTODISC is of type BoolYN.
AUTODISCTMO|AUTODISCTMO is of type ThrityFiveTo100.
MINCCDEFECT|MINCCDEFECT is of type MinCcDefect.
ALMTIME|ALMTIME is of type AlmTimeRng.
ALMCLRTIME|ALMCLRTIME is of type AlmClrTimeRng.

##### Syntax: ```ENT-EOAM-MEP:[TID]:<MEPAID>:[CTAG]:::[[IFAID=<IFAID>,][DIRN=<DIRN>,][CONTCHK=<CONTCHK>,][CCMLTMPRIO=<CCMLTMPRIO>,][FRMMEASPROF=<FRMMEASPROF>,][DLYLOSSMAC=<DLYLOSSMAC>,][DLYMEASUREMENT=<DLYMEASUREMENT>,][LOSSMEASUREMENT=<LOSSMEASUREMENT>,][CFGPST=<CFGPST>,][CFGSST=<CFGSST>]]; ```

##### Parameters
Attribute | Description
|---
MEPAID|MEPAID is the AID EthOamMepAid.
IFAID|IFAID is the AID MepId1.
DIRN|DIRN is of type MepDirn.
CONTCHK|CONTCHK is of type BoolYN. The default value is "Y".
CCMLTMPRIO|CCMLTMPRIO is of type CcmLtmPrio.
FRMMEASPROF|FRMMEASPROF is of type FrmMeasProf.
DLYLOSSMAC|DLYLOSSMAC is the AID MacAid.
DLYMEASUREMENT|DLYMEASUREMENT is of type BoolYN.
LOSSMEASUREMENT|LOSSMEASUREMENT is of type BoolYN.
CFGPST|CFGPST is of type PrimaryStateChg. The default value is "IS".
CFGSST|CFGSST is of type SecondaryState.

##### Syntax: ```ENT-EOAM-MIP:[TID]:<MIPAID>:[CTAG]:::[[MEGAID=<MEGAID>,][MIPENABLED=<MIPENABLED>]]; ```

##### Parameters
Attribute | Description
|---
MIPAID|MIPAID is the AID OntPortAid.
MEGAID|MEGAID is the AID MegAid.
MIPENABLED|MIPENABLED is of type BoolYN.

##### Syntax: ```ENT-EOAM-RMEP:[TID]:<RMEPAID>:[CTAG]:::[RMEPIDLIST=<RMEPIDLIST>]; ```

##### Parameters
Attribute | Description
|---
RMEPAID|RMEPAID is the AID EthOamMepAid.
RMEPIDLIST|RMEPIDLIST is of type OneTo8191 and is listable.

##### Syntax: ```ENT-EQPT:[TID]:<EqptAid>:[CTAG]::<TYPE>:[[PROTN=<PROTN>,][RVRTV=<RVRTV>,][RNPRTY=<RNPRTY>,][PWR=<PWR>,][LINERATE=<LINERATE>,][IMAIDLECELL=<IMAIDLECELL>,][UBRBWRES=<UBRBWRES>,][DBA=<DBA>,][ECCONFIG=<ECCONFIG>,][BANDPLAN=<BANDPLAN>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address (location) for the Equipment entity being provisioned. EqptAid is the AID EquipmentId.
TYPE|Equipment Type. This parameter identifies the type of equipment which can be plugged into the slot. The provisioned equipment type must be the exact equipment card type. Examples of card types are RPOTS-24, OC12-4-IR, etc. TYPE is of type EqptTypeProv.
PROTN|Protection Unit Access Identifier. This is the address of the equipment which is to provide protection for this card. If this equipment is to provide protection for other cards in the system, then this will be it's own address. The equipment providing protection must be provisioned before the equipments that use it as their protection. PROTN is the AID EquipmentId6. The default value is "NONE".
RVRTV|Revertive. This parameter indicates if the protection requested is to be revertive or non-revertive. The parameter value can be either Y = revertive or N = non-revertive. This parameter is only applicable in a 1:1 protection scheme. In a 1:n protection scheme, the equipment protection is always revertive. RAP cards are always non-revertive and cannot be provisioned to be revertive. This parameter is only applicable if this is the protection card unit. It is not provided when this is the protected card. RVRTV is of type BoolYN. The default value is "N".
RNPRTY|Redundancy Priority. This parameter only applies in a 1:n protection scheme. It gives the priority of this working equipment versus other working equipment protected by the same protection card. Equipment given a smaller RNPRTY number will pre-empt any protection already in effect for equipment given a larger RNPRTY number. When equipment fails with the same RNPRTY number as the already protected equipment, no protection switch will occur. RNPRTY is of type ProtnPriority. The default value is "5".
PWR|Power Category. The system shall minimize the power dissipation during power failure (battery backup). Following power failure the system needs to enter a power-save mode. Upon entering this mode, the C7 turns off the DSL cards. The period in which the system enters power-save mode after a power failure shall be a user provisionable interval. To accomplish this task three power categories are created: Category 1 that do not get shut down during battery back up (AC power failure). Category 2 cards that get shut down after 2 hours. Category 3 card that get shut down after the period of time specified by PWRCAT3 (up to a maximum of 30 minutes - see ED-SHELF). The system defaults are that POTS, DS1, DS3, and optics are category 1 and ADSL are category 3. Presently, no Category 2 cards are supported. PWR is of type PowerCategory.
LINERATE|Line Rate. This parameter only applies when provisioning RAP-OC cards. This is the configurable line speed of the equipment. When decreasing the linerate, there can be no STS provisioned outside the acceptable range of the new rate. As well, the current packet bandwidth used by the port must not exceed the new maximum bandwidth. NOTE: The card will reboot if this parameter is changed when it has provisioned services! LINERATE is of type LineRate. The default value is "OC48".
IMAIDLECELL|This indicates how IMA idle cells will be transmitted by all IMA groups on this card. IMAIDLECELL is of type ImaIdleCellType. The default value is "FILLERV1.0".
UBRBWRES|UBR BandWidth REServed. Amount of backplane bandwidth reserved for UBR bandwidth by user in kbps. This parameter takes value of zero and values greater than or equal to 128 kbps in increments of 128. This is a restricted parameter and requires the "allow restricted commands (ALW-CMD-RESTR)" option to be specified before it will be accepted by the system. UBRBWRES is a Integer. The default value is "0". UBRBWRES is a Integer. The default value is "0".
DBA|Enable/Disable Dynamic Bandwidth Allocation on all PONs on the OLTG card. Applicable to OLTG card only. DBA is of type BoolYN. The default value is "Y".
ECCONFIG|Indicates the type of echo cancellation filtering to be used on all VSPs or VSD1s on the equipment. This parameter is only applicable to VGP and VIPR line units. ECCONFIG is of type EqptEcConfig.
BANDPLAN|This parameter only applies when provisioning COMBO2-24V or VDSL2-24 cards. It selects which VDSL2 profiles are available for provisioning. When set to �3BAND�, 8a, 8b, 8c and 8d profiles are available for provisioning each of 24 ports. BANDPLAN set to �5BAND� extends the available profile selection to 8a, 8b, 8c, 8d, 12a, 12b and 17a but limits usable ports to 12. BANDPLAN is of type BandPlan. The default value is "3BAND".
PST|Primary Service State. This is the service state which the user wants the equipment to transition into after provisioning. If the user enters IS (in service) and equipment is not capable of going into service, then the service will become OOS-AU,AINS. The secondary service state of AINS indicates that the equipment will automatically transition to IS when it is capable doing so. PST is of type PrimaryStateChg. The default value is "IS".

##### Syntax: ```ENT-ERPS:[TID]:<ErpsAid>:[CTAG]:::PRIM=<PRIM>,SEC=<SEC>,CVLAN=<CVLAN>,[[HMF=<HMF>,][RMF=<RMF>,][ISMASTER=<ISMASTER>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsAid.
PRIM|The primary interface for this ERPS domain. If the domain is of role 'MASTER', then this is the primary interface. Otherwise, it is just one of the 2 interfaces. PRIM is the AID RapEthPortAid.
SEC|This is the secondary interface for this ERPS domain. If the domain is of role 'MASTER', then this is the secondary interface. Otherwise, it is just one of the 2 interfaces. SEC is the AID RapEthPortAid.
CVLAN|This is the VLAN on which the control messages will be sent. This VLAN will be reserved from the VLAN pool and unavailable for use. CVLAN is the AID ErpsVlanIndexAid.
HMF|The frequency (in seconds) at which health messages will be sent. The valid range is 1-10. HMF is a Integer.
RMF|The frequency (in seconds) at which recover messages are sent. The valid range is 1-10. RMF is a Integer.
ISMASTER|Indicate this is master or not. ISMASTER is of type BoolYN.
DESC|The name of the ERPS domain. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-ETH:[TID]:<EthPortAid>:[CTAG]:::[[SPD=<SPD>,][DPLX=<DPLX>,][TAGGED=<TAGGED>,][MTU=<MTU>,][POLICE=<POLICE>,][LSREN=<LSREN>,][VIDTXMODE=<VIDTXMODE>,][ENONBAT=<EONBAT>,][GOS=<GOS>,][AHDISCENABLE=<AHDISCENABLE>,][AHLPBKACCEPT=<AHLPBKACCEPT>,][PRIO=<PRIO>,][LACPTMOUT=<LACPTMOUT>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Access Identifier. EthPortAid is the AID EthId.
SPD|Speed. The default value is 1000 for GE-12S equipment, and AUTO for FE-12S equipment. SPD is of type Speed.
DPLX|Duplex. DPLX is of type Duplex. The default value is "AUTO".
TAGGED|Tagged. TAGGED is of type BoolYN. The default value is "N".
MTU|Max Transmission Unit. Varies by equipment type. GE-2P/EGW: must be 2048. RAP10 : must be within [1518,9022], default 2048. GE-4S and FE-12S: must be within [1518, 9022], default 1522. ONT: MTU is not settable. (For ONT ETH ports, MTU can be retrieved with RTRV-STAT-ETH) MTU is of type Mtu. The default value is "1522".
POLICE|Policing. POLICE is of type BoolYN. The default value is "N".
LSREN|LaSeR ENable - Laser On/Off. Applies to GE ports only. LSREN is of type BoolYN. The default value is "N".
VIDTXMODE|For ONT ports, allows conversion of multicast video streams to unicast streams to the specific Set Top Boxes that have joined the associated stream. VIDTXMODE is of type OntEthVidTxMode. The default value is "MCAST".
EONBAT|For ONT ports, this parameter specifies the behavior the port when the ONT is running on battery backup, and overrides the default (ONTETHONBAT) specified by ED-SYS. EONBAT is of type OntPortPwrOpt. The default value is "USEDEF".
GOS|GOS is the AID GosAid. The default value is "OFF".
AHDISCENABLE|AHDISCENABLE is of type BoolYN. The default value is "N".
AHLPBKACCEPT|AHLPBKACCEPT is of type BoolYN. The default value is "N".
PRIO|Lacp Priority. Only effective for cross-card LinkAgg. PRIO is of type One264K. The default value is "32768".
LACPTMOUT|Timeout for LACP when operating in Protection mode. LACPTMOUT is of type LacpTmout. The default value is "SHORT".
DESC|DESCription. A user-settable description field, up to 63 characters. DESC is a String. The default value is """".
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-ETH-ACL:[TID]:<EthPortAid>:[CTAG]:::[[MAC=<MAC>,][MMSK=<MMSK>]]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Port Access Identifier. EthPortAid is the AID TwelvePortLuAid.
MAC|MAC address. MAC is the AID MacAid.
MMSK|MAC address mask. MMSK is the AID MacAid.

##### Syntax: ```ENT-FFP-<OCN>:[TID]:<WrkOcNAid>,<ProtOcNAid>:[CTAG]:::BDCST=<BDCST>,[[PSDIRN=<PSDIRN>,][RVRTV=<RVRTV>]],MODE=<MODE>,[[PDIP=<PDIP>,][WTR=<WTR>,][ORP=<ORP>,][APSOP=<APSOP>]]; ```
##### Parameters
Attribute | Description
|---
WrkOcNAid|Working OCn Access Identifier. The address of the port which receives the traffic from the working fiber in the facility protection group. WrkOcNAid is the AID FourPortLuAndRapAid.
ProtOcNAid|Protection OCn Access Identifier. The address of the port which receives the traffic from the protect fiber in the facility protection group. ProtOcNAid is the AID FourPortLuAndRapAid.
BDCST|Broadcast. This parameter is set to Y if the signal is to be broadcast over the protected (main) and the protecting (protection) channels simultaneously for a 1+1 protection scheme. It is set to N if the signal is only to be sent over the active channel. BDCST is of type BoolYN.
PSDIRN|Protection Switch Direction. Specifies whether both directions of a bi-directional connection are to be switched together. The default will be set to UNI when BDCST = Y and BI when BDCST = N. PSDIRN is of type ProtnSwDirection.
RVRTV|Revertive. This parameter indicates the type of protection requested. The parameter value can be either Y = revertive or N = non-revertive. The default will be set to Y when BDCST = N or N when BDCST = Y. RVRTV is of type BoolYN.
MODE|Protection Mode. The mode parameter indicates whether the protection is applied to an OPEN (linear) protection scheme or a CLOSED (ring) protection scheme. MODE is of type Mode.
PDIP|Payload Defect Indication. This parameter indicates whether to switch on a PDI-P defect. This parameter is applicable only when MODE = CLOSED. PDIP is of type BoolYN. The default value is "N".
WTR|Wait to Restore. The amount of time in minutes to wait before restoring a revertive protection switch. Does not apply to non-revertive protection switch. WTR is of type WaitToRestore. The default value is "5".
ORP|Optical Restoration Protocol (ORP). This parameter indicates if the optical facility should provide ORP protection. A value of Y = ORP requested and a N = No ORP protection. This parameter is applicable only when MODE = CLOSED. ORP is of type BoolYN. The default value is "N".
APSOP|Automatic Protection Switch Operation. This parameter may be set to N to disable the execution of the Automatic Protection Switching (APS) protocol (processing of K-bytes). This option is useful for Ring Management when new Nodes are added/deleted in a BLSR which allows the ring maps to be updated for all the existing nodes in a ring. In the case of a Linear protection configuration, the addition/deletion of a new NE in an existing span will require that APS operation be temporarily turned off, while traffic re-configuration is in progress. NOTE: This parameter has been deprecated and will be ignored by the C7. APSOP is of type BoolYN.

##### Syntax: ```ENT-FTP:[TID]:<FTPAID>:[CTAG]:::FTPIP=<FTPIP>,FTPUID=<FTPUID>,FTPPID=<FTPPID>,LOCN=<LOCN>; ```
##### Parameters
Attribute | Description
|---
FTPAID|FTP server AID. FTPAID is the AID FtpAid.
FTPIP|IP address of the FTP server. FTPIP is the AID IpAid.
FTPUID|User ID of the FTP server. FTPUID is a String.
FTPPID|Password on the FTP server. FTPPID is a String.
LOCN|Location of the C7 Gateway from which FTP functions will be performed. LOCN is the AID FtpGatewayAid.

##### Syntax: ```ENT-GOS-<OCN>:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][UASL=<UASL>,][CVS=<CVS>,][ESS=<ESS>,][SESS=<SESS>,][SEFSS=<SEFSS>,][DESC=<DESC>]]; ```
##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the OCn facility Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be entered. Section PM registers are only kept in association with the near end. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVL is of type CVThreshRange.
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 12 and for 1-DAY is 200. ESL is of type SecondsThreshRange.
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 3 and for 1-DAY is 7. SESL is of type SecondsThreshRange.
UASL|Errored Seconds Threshold Section. The threshold value for the errored seconds for the section. The default threshold for 15-MIN is 10 and for 1-DAY is 10. UASL is of type SecondsThreshRange.
CVS|Coding Violations Threshold Section. The threshold value for the coding violations for the section. The default threshold for 15-MIN is 25 and for 1-DAY is 250. This parameter does not apply to far end provisioning. CVS is of type CVThreshRange.
ESS|Errored Seconds Threshold Section. The threshold value for the errored seconds for the section. The default threshold for 15-MIN is 12 and for 1-DAY is 200. This parameter does not apply to far end provisioning. ESS is of type SecondsThreshRange.
SESS|Severely Errored Seconds Threshold Section. The threshold value for the severely errored seconds for the section. The default threshold for 15-MIN is 3 and for 1-DAY is 7. This parameter does not apply to far end provisioning. SESS is of type SecondsThreshRange.
SEFSS|Severely Errored Framing Seconds Threshold Section. The threshold value for the severely errored framing seconds for the section. This parameter does not apply to far end provisioning. Default threshold for 15-MIN interval and 1-DAY interval is 10 SEFSS is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-<STSN>:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SESP=<SESP>,][UASP=<UASP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```
##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the STS1 facility Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|The location associated with a particular command. Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|The accumulation period for performance counters. Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. CVP is of type CVThreshRange.
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. ESP is of type SecondsThreshRange.
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. SESP is of type SecondsThreshRange.
UASP|Un-Available seconds path. This is the threshold value for the un-available seconds for the path. UASP is of type SecondsThreshRange.
PERUPE|Percent Utilization - Path, Egress. Default value is 85 percent. PERUPE is of type Percentage. The default value is "85".
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-ADSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVFL=<CVFL>,][CVIL=<CVIL>,][ECFL=<ECFL>,][ECIL=<ECIL>,][ECSL=<ECSL>,][ESL=<ESL>,][SESL=<SESL>,][UASL=<UASL>,][LOSSL=<LOSSL>,][PERU=<PERU>,][PERUE=<PERUE>,][LOSC=<LOSC>,][DESC=<DESC>]]; ```
##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the ADSL Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVFL|Coding violations fast - line. The threshold value for the coding violations fast for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVFL is of type CVAdslThreshRange.
CVIL|Coding violations interleaved - line. The threshold value for the coding violations interleaved for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVIL is of type CVAdslThreshRange.
ECFL|Forward error correction count fast - line. The threshold value for the forward error correction count fast for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. ECFL is of type ECThreshRange.
ECIL|Forward error correction count interleaved - line. The threshold value for the forward error correction count interleaved for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. ECIL is of type ECThreshRange.
ECSL|Forward error correction count second - line. The threshold value for the forward error correction count second for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. ECSL is of type SecondsThreshRange.
ESL|Errored seconds - line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESL is of type SecondsThreshRange.
SESL|Severely errored seconds - line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 65. UASL is of type SecondsThreshRange.
LOSSL|LOS Seconds Threshold Line. The threshold value for the LOS seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 10. LOSSL is of type SecondsThreshRange.
PERU|Percent Utilization, Ingress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERU is of type Percentage.
PERUE|Percent Utilization - Path, Egress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERUE is of type Percentage.
LOSC|Loss of Signal Count (Near End only). This indicates the number of times a LOS condition was set, and also represents the number of modem retrains in the time period. The default threshold for 15-MIN is 3 and for 1-DAY is 10. LOSC is a Integer.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-AP:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[PERUP=<PERUP>,][PERUPE=<PERUPE>,][IVIMA=<IVIMA>,][OIFIMA=<OIFIMA>,][SESIMA=<SESIMA>,][UASIMA=<UASIMA>,][TXUUSIMA=<TXUUSIMA>,][RXUUSIMA=<RXUUSIMA>,][TXFC=<TXFC>,][RXFC=<RXFC>,][TXSTUFFIMA=<TXSTUFFIMA>,][RXSTUFFIMA=<RXSTUFFIMA>,][DESC=<DESC>]]; ```
##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
PERUP|Percent Utilization - Path, Ingress (Near End only). Default value is 85 percent. PERUP is of type Percentage.
PERUPE|Percent Utilization - Path, Egress (Near End only). Default value is 85 percent. PERUPE is of type Percentage.
IVIMA|ICP Violations. Count of errored, invalid, or missing ICP cells, except during seconds where a SES-IMA or UAS-IMA condition is reported (Near End only). Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. IVIMA is of type SecondsThreshRange.
OIFIMA|Out of IMA Frame (Near End only). Count of OIF anomalies except during SES-IMA or UAS-IMA conditions. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. OIFIMA is of type SecondsThreshRange.
SESIMA|Severely Errored Seconds. Count of 1-second intervals containing >= 30% of the ICP cells counted as IV-IMAs, or one or more near-end link defects (facility, LIF, or LODS) during non-UAS-IMA intervals. The number of IV-IMA counts required to meet the 30% criteria will depend on the facility line rate and the IMA frame size (M). Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. SESIMA is of type SecondsThreshRange.
UASIMA|Unavailable seconds at NE. The NE unavailability begins at the onset of 10 contiguous SES-IMA including the first 10 seconds to enter the UAS-IMA condition, and ends at the onset of 10 contiguous second with no SES-IMA, excluding the last 10 seconds to exit the UAS-IMA condition. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. UASIMA is of type SecondsThreshRange.
TXUUSIMA|Transit Unusable Seconds (Near End only). Count of Tx Unusable seconds at the Tx NE Link State Machine (LSM). Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. TXUUSIMA is of type SecondsThreshRange.
RXUUSIMA|Receive Unusable Seconds (Near End only). Count of Rx Unusable seconds at the Rx NE LSM. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. RXUUSIMA is of type SecondsThreshRange.
TXFC|Transit Failure Count. Count of the number of NE Transmit Link failure alarm entrances. The possible NE Tx link failure alarm conditions are: Tx-Mis-Connected and Tx-Fault. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. TXFC is of type SecondsThreshRange.
RXFC|Receive Failure Count. Count of the number of NE Receive Link failure alarm entrances. The possible NE Rx link failure alarm conditions are: LIF, LODS, and Rx-Fault. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. RXFC is of type SecondsThreshRange.
TXSTUFFIMA|Transmit Stuff Events (Near End only). Count of stuff events inserted in the transmited direction. Default value is 0. TXSTUFFIMA is of type ImaLinkStuff.
RXSTUFFIMA|Receive Stuff Events (Near End only). Count of stuff events inserted in the receive direction, except during SES-IMA and UAS-IMA conditions. Default value is 0. RXSTUFFIMA is of type ImaLinkStuff.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-EC1:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][UASL=<UASL>,][CVS=<CVS>,][ESS=<ESS>,][SESS=<SESS>,][SEFSS=<SEFSS>,][DESC=<DESC>]]; ```
##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the EC1 facility Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line. CVL is of type CVThreshRange. The default value is "15".
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. ESL is of type SecondsThreshRange. The default value is "12".
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. SESL is of type SecondsThreshRange. The default value is "3".
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. UASL is of type SecondsThreshRange. The default value is "10".
CVS|Coding Violations Threshold Section. The threshold value for the coding violations for the section. This parameter does not apply to far end provisioning. CVS is of type CVThreshRange. The default value is "15".
ESS|Errored Seconds Threshold Section. The threshold value for the errored seconds for the section. This parameter does not apply to far end provisioning. ESS is of type SecondsThreshRange. The default value is "12".
SESS|Severely Errored Seconds Threshold Section. The threshold value for the severely errored seconds for the section. This parameter does not apply to far end provisioning. SESS is of type SecondsThreshRange. The default value is "3".
SEFSS|Severely Errored Framing Seconds Threshold Section. The threshold value for the severely errored framing seconds for the section. This parameter does not apply to far end provisioning. SEFSS is of type SecondsThreshRange. The default value is "10".
DESC|A string description of this object, up to 11 characters in length. DESC is a String. The default value is "the GosAid".

##### Syntax: ```ENT-GOS-ETH:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[FCSERROR=<FCSERROR>,][XSCOLL=<XSCOLL>,][LATECOLL=<LATECOLL>,][TOOLONG=<TOOLONG>,][INBUFOVFL=<INBUFOVFL>,][OUTBUFOVFL=<OUTBUFOVFL>,][SQETEST=<SQETEST>,][DEFERRED=<DEFERRED>,][ALIGNERR=<ALIGNERR>,][RXINTERR=<RXINTERR>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. Only NEND counters are supported. LOCN is of type Location and can be one of the following values: "NEND".
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
FCSERROR|FCS Error Counter. FCSERROR is a Integer.
XSCOLL|Excessive Collision Counter. XSCOLL is a Integer.
LATECOLL|Late Collision Counter. LATECOLL is a Integer.
TOOLONG|FrameTooLongs. TOOLONG is a Integer.
INBUFOVFL|Buffer Overflows on Receive. INBUFOVFL is a Integer.
OUTBUFOVFL|Buffer Overflows on Transmit. OUTBUFOVFL is a Integer.
SQETEST|SQE Counter. SQETEST is a Integer.
DEFERRED|Deferred Transmission Counter. DEFERRED is a Integer.
ALIGNERR|Alignment Error Counter. ALIGNERR is a Integer.
RXINTERR|Internal MAC Receive Error Counter. RXINTERR is a Integer.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-GRPXDSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[FC=<FC>,][MDSRFS=<MDSRFS>,][MUSRFS=<MUSRFS>,][PERU=<PERU>,][PERUE=<PERUE>,][UAS=<UAS>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the GRPXDSL Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
FC|Failure Count FC is a Integer.
MDSRFS|Min Downstream Failure Seconds MDSRFS is of type SecondsThreshRange.
MUSRFS|Min Uptream Failure Seconds MUSRFS is of type SecondsThreshRange.
PERU|Percent Utilization, Ingress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERU is of type Percentage.
PERUE|Percent Utilization - Path, Egress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERUE is of type Percentage.
UAS|Unavailable Seconds UAS is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-HDSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SESP=<SESP>,][CSSP=<CSSP>,][UASP=<UASP>,][CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][LOSWSL=<LOSWSL>,][UASL=<UASL>,][RTRN=<RTRN>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the HDSL port Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. The default threshold for 15-MIN is 13,296 and for 1-DAY is 132,960. CVP is of type CVThreshRange.
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESP is of type SecondsThreshRange.
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESP is of type SecondsThreshRange.
CSSP|Controlled Slip Seconds Path. The threshold value for the controlled slip seconds path. The default threshold for 15-MIN is 1 and for 1-DAY is 4. CSSP is of type SecondsThreshRange.
UASP|Unavailable Seconds Threshold Path. The threshold value for the unavailable seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 10. UASP is of type SecondsThreshRange.
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line (Near End only). The default threshold for 15-MIN is 13,340 and for 1-DAY is 133,400. CVL is of type CVThreshRange.
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line (Near End only). The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESL is of type SecondsThreshRange.
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line (Near End only). The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange.
LOSWSL|Loss of Sync Word Seconds Threshold Line (Near End). The default threshold for 15-MIN is 30 seconds and for 1-DAY is 120 seconds. LOSWSL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line (Near End only). The threshold value for the unavailable seconds for the line. The default threshold for 15-MIN is 60 seconds and for 1-DAY is 120 seconds. UASL is of type SecondsThreshRange.
RTRN|ReTRaiN count (Near End). The threshold value for number of retrains on either loop (individually). The default threshold for 15-MIN is 3 retrains and for 1-DAY is 10 retrains. RTRN is a Integer.
DESC|A string description of this object, up to 11 characters in length. DESC is a String. The default value is "the GosAid".

##### Syntax: ```ENT-GOS-IMA:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[GRFC=<GRFC>,][GRUASIMA=<GRUASIMA>,][PERUP=<PERUP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Group Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
GRFC|Group failure count. Default threshold for 15MIN interval is 30 seconds. Default threshold for 1 Day is 300 seconds. GRFC is of type SecondsThreshRange.
GRUASIMA|Count of seconds where IMA GTSM is down (Near End only). Default threshold for 15MIN interval is 30 seconds. Default threshold for 1 Day is 300 seconds. GRUASIMA is of type SecondsThreshRange.
PERUP|Percent Utilization - Path, Ingress (Near End only). Default value is 85 percent. PERUP is of type Percentage.
PERUPE|Percent Utilization - Path, Egress (Near End only). Default value is 85 percent. PERUPE is of type Percentage.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-IMALINK:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[IVIMA=<IVIMA>,][SESIMA=<SESIMA>,][UASIMA=<UASIMA>,][TXUUSIMA=<TXUUSIMA>,][RXUUSIMA=<RXUUSIMA>,][TXFC=<TXFC>,][RXFC=<RXFC>,][TXSTUFFIMA=<TXSTUFFIMA>,][RXSTUFFIMA=<RXSTUFFIMA>,][OIFIMA=<OIFIMA>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Group Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
IVIMA|ICP Violations. Count of errored, invalid, or missing ICP cells, except during seconds where a SES-IMA or UAS-IMA condition is reported (Near End only). Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. IVIMA is of type SecondsThreshRange.
SESIMA|Severely Errored Seconds. Count of 1-second intervals containing >= 30% of the ICP cells counted as IV-IMAs, or one or more near-end link defects (facility, LIF, or LODS) during non-UAS-IMA intervals. The number of IV-IMA counts required to meet the 30% criteria will depend on the facility line rate and the IMA frame size (M). Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. SESIMA is of type SecondsThreshRange.
UASIMA|Unavailable seconds at NE. The NE unavailability begins at the onset of 10 contiguous SES-IMA including the first 10 seconds to enter the UAS-IMA condition, and ends at the onset of 10 contiguous second with no SES-IMA, excluding the last 10 seconds to exit the UAS-IMA condition. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. UASIMA is of type SecondsThreshRange.
TXUUSIMA|Transit Unusable Seconds (Near End only). Count of Tx Unusable seconds at the Tx NE Link State Machine (LSM). Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. TXUUSIMA is of type SecondsThreshRange.
RXUUSIMA|Receive Unusable Seconds (Near End only). Count of Rx Unusable seconds at the Rx NE LSM. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. RXUUSIMA is of type SecondsThreshRange.
TXFC|Transit Failure Count. Count of the number of NE Transmit Link failure alarm entrances. The possible NE Tx link failure alarm conditions are: Tx-Mis-Connected and Tx-Fault. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. TXFC is of type SecondsThreshRange.
RXFC|Receive Failure Count. Count of the number of NE Receive Link failure alarm entrances. The possible NE Rx link failure alarm conditions are: LIF, LODS, and Rx-Fault. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. RXFC is of type SecondsThreshRange.
TXSTUFFIMA|Transmit Stuff Events (Near End only). Count of stuff events inserted in the transmited direction. Default value is 0. TXSTUFFIMA is of type ImaLinkStuff.
RXSTUFFIMA|Receive Stuff Events (Near End only). Count of stuff events inserted in the receive direction, except during SES-IMA and UAS-IMA conditions. Default value is 0. RXSTUFFIMA is of type ImaLinkStuff.
OIFIMA|Out of IMA Frame (Near End only). Count of OIF anomalies except during SES-IMA or UAS-IMA conditions. Default threshold for 15MIN interval is 15 seconds. Default threshold for 1 DAY interval is 150 seconds. OIFIMA is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-ONT:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[BIP8=<BIP8>,][BES=<BES>,][SES=<SES>,][UAS=<UAS>,][MISSING=<MISSING>,][MES=<MES>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
BIP8|BIP8 errors detected on PON transport. NE is OLT detected, FE is ONT detected BIP8 is a Integer.
BES|Number of seconds during the period when a BIP8 error was detected. For the FE case, the granularity is 5 seconds rather than 1 second. BES is a Integer.
SES|For NEND this is the count of seconds where either the BIP8 count has exceeded a threshold or where the number of missing bursts equals the number of possible bursts for the ONT.
For FEND this is the count of seconds where the BIP8 count has exceeded a threshold. For the FE case the granularity is 5 seconds rather than 1 second. SES is a Integer.

UAS|This is defined a N consecutive SES. Once unavailable, N consecutive seconds must pass without SES before coming available again. In the FEND case this is a 5 second granularity rather than 1 second. UAS is a Integer.
MISSING|Count of missed bursts (no received traffic from ONT in allocated timeslot). NEND Only. MISSING is a Integer.
MES|Number of seconds during the period when a missing error was detected. NEND only. MES is a Integer.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.

##### Syntax: ```ENT-GOS-PW:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[MISSPKTS=<MISSPKTS>,][JBUFUR=<JBUFUR>,][MFPKT=<MFPKT>,][PKTLOSRT=<PKTLOSRT>,][ES=<ES>,][SES=<SES>,][UAS=<UAS>,][FC=<FC>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|GOS Provisioning Access Identifier. GosAid is the AID GosProvAid.
LOCN|This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
MISSPKTS|Threshold of Missing Packet. Default value is 30 for 15-min interval and 300 for 1-day interval. MISSPKTS is a Integer.
JBUFUR|Number of times a packet need to be played out and the jitter buffer was empty. Default value is 10 for 15-min interval and 100 for 1-day interval. JBUFUR is a Integer.
MFPKT|Any packet which contains improper format that is unexpected size or bad header. Default value is 5 for 15-min interval and 50 for 1-day interval. MFPKT is a Integer.
PKTLOSRT|Packet Loss Rate Threshold. PKTLOSRT is of type Percentage. The default value is "10".
ES|The number of seconds during which at least one discarded, LOPS, malformed and like. Default value is 5 for 15-min interval and 50 for 1-day interval. ES is a Integer.
SES|Counter associated with the number of severely errored seconds. Default value is 15 for 15 min interval 150 for 1 day interval. SES is a Integer.
UAS|Counter associated with the number of UAS encountered. Any consecutive 10 seconds of SES are counted as one Unavailable Seconds (UAS).
Once a sequence of 10 consecutive SES, these counter increments each second until 10 consecutive seconds without SES.

Default value is 15 for 15 min interval and 150 for 1 day interval. UAS is a Integer.

FC|The number of failure events. A failure event begins when the LOPS failure is detected and it ends when the failure is detected. Default value is 30 for 15 min interval and 300 for 1 day interval. FC is a Integer.
DESC|Description. DESC is a String.

##### Syntax: ```ENT-GOS-T1:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SESP=<SESP>,][SASP=<SASP>,][CSSP=<CSSP>,][UASP=<UASP>,][CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][PERUP=<PERUP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the T1 port Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. The default threshold for 15-MIN is 13,296 and for 1-DAY is 132,960. CVP is of type CVThreshRange. The default value is "13296".
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESP is of type SecondsThreshRange. The default value is "65".
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESP is of type SecondsThreshRange. The default value is "10".
SASP|Severely Errored Framing/Alarm Indication Signal Second Count. The threshold value for the severely errored framing/alarm indication signal second count. The default threshold for 15-MIN is 2 and for 1-DAY is 17. SASP is of type SecondsThreshRange. The default value is "2".
CSSP|Controlled Slip Seconds Path. The threshold value for the controlled slip seconds path. The default threshold for 15-MIN is 1 and for 1-DAY is 4. CSSP is of type SecondsThreshRange. The default value is "1".
UASP|Unavailable Seconds Threshold Path. The threshold value for the unavailable seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 4. UASP is of type SecondsThreshRange. The default value is "10".
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line. The default threshold for 15-MIN is 13,340 and for 1-DAY is 133,400. CVL is of type CVThreshRange. The default value is "13340".
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESL is of type SecondsThreshRange. The default value is "65".
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange. The default value is "10".
PERUP|Percent Utilization - Path, Ingress (Near End only). PERUP is of type Percentage. The default value is "85".
PERUPE|Percent Utilization - Path, Egress (Near End only). PERUPE is of type Percentage. The default value is "85".
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-T3:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVP=<CVP>,][ESP=<ESP>,][SASP=<SASP>,][SESP=<SESP>,][UASP=<UASP>,][CVL=<CVL>,][ESL=<ESL>,][SESL=<SESL>,][PERUP=<PERUP>,][PERUPE=<PERUPE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the T3 port Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVP|Coding Violations Threshold Path. The threshold value for the coding violations for the path. The default threshold for 15-MIN is 13,296 and for 1-DAY is 132,960. For C-bit parity applications, this parameter sets the threshold for both CVP-P and CVCP-P. CVP is of type CVThreshRange. The default value is "382".
ESP|Errored Seconds Threshold Path. The threshold value for the errored seconds for the path. The default threshold for 15-MIN is 65 and for 1-DAY is 648. For C-bit parity applications, this parameter sets the threshold for both ESP-P and ESCP-P. ESP is of type SecondsThreshRange. The default value is "25".
SASP|Severely Errored Framing/Alarm Indication Signal Second Count. The threshold value for the severely errored framing/alarm indication signal second count. The default threshold for 15-MIN is 2 and for 1-DAY is 17. For C-bit parity applications, this parameter sets the threshold for both SASP-P and SASCP-P. SASP is of type SecondsThreshRange. The default value is "4".
SESP|Severely Errored Seconds Threshold Path. The threshold value for the severely errored seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 100. For C-bit parity applications, this parameter sets the threshold for both SESP-P and SESCP-P. SESP is of type SecondsThreshRange. The default value is "2".
UASP|Unavailable Seconds Threshold Path. The threshold value for the unavailable seconds for the path. The default threshold for 15-MIN is 10 and for 1-DAY is 10. For C-bit parity applications, this parameter sets the threshold for both UASP-P and UASCP-P. UASP is of type SecondsThreshRange. The default value is "10".
CVL|Coding Violations Threshold Line. The threshold value for the coding violations for the line. The default threshold for 15-MIN is 13,340 and for 1-DAY is 133,400. This parameter does not apply to far end provisioning. CVL is of type CVThreshRange. The default value is "387".
ESL|Errored Seconds Threshold Line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 648. This parameter does not apply to far end provisioning. ESL is of type SecondsThreshRange. The default value is "25".
SESL|Severely Errored Seconds Threshold Line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. This parameter does not apply to far end provisioning. SESL is of type SecondsThreshRange. The default value is "4".
PERUP|Percent Utilization - Path, Ingress (Near End only). PERUP is of type Percentage. The default value is "85".
PERUPE|Percent Utilization - Path, Egress (Near End only). PERUPE is of type Percentage. The default value is "85".
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GOS-XDSL:[TID]:<GosAid>:[CTAG]::<LOCN>,<TMPER>:[[CVL=<CVL>,][ECL=<ECL>,][ECSL=<ECSL>,][ESL=<ESL>,][LOSC=<LOSC>,][LOSSL=<LOSSL>,][PERU=<PERU>,][PERUE=<PERUE>,][SESL=<SESL>,][UASL=<UASL>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the XDSL Grade of Service table entry. GosAid is the AID GosProvAid.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location.
TMPER|Time Period. This parameter specifies the accumulation time period for the PM information. TMPER is of type PMPeriod.
CVL|Coding violations - line. The threshold value for the coding violations for the line. The default threshold for 15-MIN is 25 and for 1-DAY is 250. CVL is of type CVAdslThreshRange.
ECL|Forward error correction count - line. The threshold value for the forward error correction count for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. ECL is of type ECThreshRange.
ECSL|Forward error correction count second - line. The threshold value for the forward error correction count second for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. ECSL is of type SecondsThreshRange.
ESL|Errored seconds - line. The threshold value for the errored seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 648. ESL is of type SecondsThreshRange.
LOSC|Loss of Signal Count (Near End only). This indicates the number of times a LOS condition was set, and also represents the number of modem retrains in the time period. LOSC is a Integer.
LOSSL|LOS Seconds Threshold Line. The threshold value for the LOS seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 10. LOSSL is of type SecondsThreshRange.
PERU|Percent Utilization, Ingress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERU is of type Percentage.
PERUE|Percent Utilization - Path, Egress (Near End only). The default threshold for 15-MIN is 85 and for 1-DAY is 85. PERUE is of type Percentage.
SESL|Severely errored seconds - line. The threshold value for the severely errored seconds for the line. The default threshold for 15-MIN is 10 and for 1-DAY is 100. SESL is of type SecondsThreshRange.
UASL|Unavailable Seconds Threshold Line. The threshold value for the unavailable seconds for the line. The default threshold for 15-MIN is 65 and for 1-DAY is 65. UASL is of type SecondsThreshRange.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-GR303:[TID]:<IgAid>:[CTAG]:::PRIOP=<PRIOP>,[SECOP=<SECOP>],SWTYPE=<SWTYPE>,[[T308=<T308>,][T303=<T303>,][T396=<T396>,][T397=<T397>,][EOCALARM=<EOCALARM>,][EOCUPSST=<EOCUPSST>,][FLOWTHROUGH=<FLOWTHROUGH>]]; ```

##### Parameters
Attribute | Description
|---
IgAid|GR-303 Interface Group Access Identifier. This is the address of the GR-303 Interface Group which is being created. IgAid is the AID IgAid.
PRIOP|Primary Operations Processor. This parameter identifies the primary Operations Processor which will terminate the EOC channel. This must be a Maintenance/Administration Slot (MS). PRIOP is the AID MsNoneAid.
SECOP|Secondary Operations Processor. This parameter identifies the Secondary Operations Processor which will terminate the EOC channel. This must be a Maintenance/Administration Slot (MS). SECOP is the AID MsNoneAid. The default value is "NONE".
SWTYPE|Switch Type. The parameter indicate the type of switch which the GR-303 interface group will be connected to. SWTYPE is of type SwitchType.
T308|Timer 308. This parameter specifies the maximum length of time in seconds the RDT will wait for a reply to a RELEASE message. T308 is of type T308. The default value is "4".
T303|T303 Timer. The parameter identifies the timer used at Layer 3 for the TMC and defines the maximum length of time in milliseconds that the RDT will wait for a reply to a SETUP message. T303 is of type T303. The default value is "700".
T396|T396 Timer. This parameter specifies the length of time in milliseconds that the RDT will wait for a reply to a SETUP message following the initial expiration of time T303. T396 is of type T396. The default value is "14700".
T397|T397 Timer. This parameter specifies the maximum length of time in seconds the RDT will wait for the IDT to acknowledge an INFORMATION message that indicated that a customer who had been generating a permanent signal has returned on-hook. T397 is of type T397. The default value is "120".
EOCALARM|EOC Alarms. This parameter indicates which alarms are to be reported through the EOC interface. The EOC can report alarms for either the shelf IG, the entire network, or no alarms at all. EOCALARM is of type EOCAlarmReport. The default value is "NETWORK".
EOCUPSST|EOC Up Send Service States. Although service state changes are always sent to the switch when the IG is in normal operation, they are not reported to the switch when the EOC link is down. Some switches, such as the DMS100, do not audit the CRVs when the EOC link comes up, so the switch continues to have the incorrect service state. This can result in the switch thinking that a CRV is down so no traffic is able to be carried. When set to "Y", this parameter will send service state notifications for all provisioned CRVs when the EOC link comes up. For SWTYPE DMS100, EOCUPSST defaults to "Y". EOCUPSST is of type BoolYN. The default value is "N".
FLOWTHROUGH|Flow through provisioning (also referred to as 'RDT provisioning'). This is a provisionable option that exists in a Class-5 switch which when enabled causes the switch to send provisioning messages over the EOC of a given GR303 interface group for the purposes of managing analogLineTerminations in the RDT. The switch will Create, Delete, Remove from Service, and audit each CRV in the RDT when this option is enabled. The RDT needs to be aware of how this option is set in the switch for the purposes of issuing service state notifications. If an analogLineTermination is not 'switch created' and flow through provisioning is enabled, then the RDT should not issue any service state notifications to the switch for that line. If flow through provisioning is disabled, then the RDT should always issue service state notifications for all lines. FLOWTHROUGH is of type BoolYN. The default value is "N".

##### Syntax: ```ENT-GR8:[TID]:<SlotIgAid>:[CTAG]:::IGMODE=<IGMODE>,[[SWTYPE=<SWTYPE>,][ALMBITS=<ALMBITS>]]; ```

##### Parameters
Attribute | Description
|---
SlotIgAid|GR-8 Interface Group Access Identifier. This is the address of the GR-8 Interface Group which is being created. SlotIgAid is the AID SlotIgAid.
IGMODE|Interface Group MODE (concentrated or non-concentrated). IGMODE is of type IgMode.
SWTYPE|Switch Type. The parameter indicate the type of switch which the GR-8 interface group will be connected to. SWTYPE is of type SwitchType.
ALMBITS|Number of ALarM BITS. ALMBITS is of type Gr8AlmBits. The default value is "16".

##### Syntax: ```ENT-GRPXDSL:[TID]:<GroupAid>:[CTAG]:::[[MEM=<MEM>,][PKTMODE=<PKTMODE>,][FALLBACKVPI=<FALLBACKVPI>,][FALLBACKVCI=<FALLBACKVCI>,][MRDS=<MRDS>,][XRDS=<XRDS>,][MRUS=<MRUS>,][XRUS=<XRUS>,][DIFDS=<DIFDS>,][DIFUS=<DIFUS>,][GOS=<GOS>,][REPTRMVRST=<REPTRMVRST>,][PROMOTEALARMS=<PROMOTEALARMS>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
GroupAid|Access Identifier of the Group. GroupAid is the AID DslGrpAid.
MEM|This parameter identifies the AID of member port(s) belonging to the group. The number of members should be 0, 1, 2, 4, 8, 12. MEM is the AID DslPortAid and is listable. The default value is "NONE".
PKTMODE|Packet mode defines if this port is to operate in packet or ATM VC mode. It could not be set to N when the service type of any group memeber is VDSL2 or VDSL2MM or when PTMOVER attribute of any group memeber is Y. PKTMODE is of type BoolYN. The default value is "Y".
FALLBACKVPI|The VPI value to use on the singular VC in packet mode. FALLBACKVPI is of type VPRange. The default value is "0".
FALLBACKVCI|The VCI value to use on the singular VC in packet mode. FALLBACKVCI is of type VCBndGrpRange. The default value is "35".
MRDS|Minimum aggregate downstream rate. MRDS is of type DwnStreamRateGrp. The default value is "32".
XRDS|Maximum aggregate downstream rate. XRDS is of type DwnStreamRateGrp. The default value is "65472".
MRUS|Minimum aggregate upstream rate. MRUS is of type UpStreamRateGrp. The default value is "32".
XRUS|Maximum aggregate upstream rate. XRUS is of type UpStreamRateGrp. The default value is "6144".
DIFDS|The differential delay for the downstream direction in milliseconds. DIFDS is a Integer. The default value is "16".
DIFUS|The differential delay for the upstream direction in milliseconds. DIFUS is a Integer. The default value is "16".
GOS|This is the related Grade of Service for GRPXDSL that is to be applied to the group. GOS is the AID GosAid. The default value is "OFF".
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the Group. Note that RMV/RST are reported upon every modem retrain and can clutter the event logs if enabled. REPTRMVRST is of type BoolYN. The default value is "N".
PROMOTEALARMS|It depends on this toggle to raise alarms or events for the following CondType. If N, raise as event. If Y, raise as alarm _CondTypeMinRateFailUs_ = 547, // Aggregate US train rate below mininum _CondTypeMinRateFailDs_ = 548, // Aggregate DS train rate below mininum _CondTypeDiffDlyFailUs_ = 551, // Diff. delay US between members exceeded _CondTypeDiffDlyFailDs_ = 552, // Diff. delay DS between members exceeded _CondTypeLinkRateFailUs_ = 553, // Ratio between low/high rates US exceeded _CondTypeLinkRateFailDs_ = 554, // Ratio between low/high rates DS exceeded _CondTypeLinkTcModeMismatch_= 605, // VDSL PTM Bonding: Mismatch of the TC mode between group members _CondTypeMemDown_ = 546, // Group Member Down PROMOTEALARMS is of type BoolYN. The default value is "N".
DESC|Description. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-GW-VOIP:[TID]:<VOIPGWAID>:[CTAG]:::IGAID=<IGAID>,[[FQDN=<FQDN>,][HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
VOIPGWAID|AID of the VoIP Gateway. VOIPGWAID is the AID VoIPGWONTAid.
IGAID|Interface Group identifying the type and parameters of the VoIP Gateway. IGAID is the AID IgAid.
FQDN|Fully Qualified Domain Name for the VoIP Gateway. FQDN is a String.
HOSTPROTO|Determines whether static or Dynamic (DHCP) IP addressing will be performed for the VoIP Gateway IP Address HOSTPROTO is of type GwHostProto. The default value is "STATIC".
IP|Statically Provisioned IP Address of VoIP Gateway. IP is the AID IpAid. The default value is "0.0.0.0".
IPMSK|Network Address Mask of Gateway IP Address. IPMSK is the AID IpAid. The default value is "0.0.0.0".
GADDR|IP Address of Network Gateway. GADDR is the AID IpAid. The default value is "0.0.0.0".
PST|Operational Service State of the VoIP Gateway. PST is of type PrimaryStateChg.

##### Syntax: ```ENT-H248:[TID]:<IgAid>:[CTAG]:::SWTYPE=<SWTYPE>,[[MGIP=<MGIP>,][MG2IP=<MG2IP>,][MGUDP=<MGUDP>,][MGC1IP=<MGC1IP>,][MGC1UDP=<MGC1UDP>,][MGC2IP=<MGC2IP>,][MGC2UDP=<MGC2UDP>,][MGC2SWTYPE=<MGC2SWTYPE>,][MGC2ESA=<MGC2ESA>,][TERMPREFIX=<TERMPREFIX>,][EPHEMTERMID=<EPHEMTERMID>,][TMAX=<TMAX>,][MWD=<MWD>,][EPHEMAUDITDELAY=<EPHEMAUDITDELAY>,][FIRSTDIGWAIT=<FIRSTDIGWAIT>,][LONGDIGWAIT=<LONGDIGWAIT>,][SHORTDIGWAIT=<SHORTDIGWAIT>,][LONGDIGDUR=<LONGDIGDUR>,][MINFLASH=<MINFLASH>,][MAXFLASH=<MAXFLASH>,][MAXACTCALLS=<MAXACTCALLS>,][RFC2833ENABLE=<RFC2833ENABLE>,][ECENABLE=<ECENABLE>,][EPCD=<EPCD>,][ECTAIL=<ECTAIL>,][MGC1FQDN=<MGC1FQDN>,][MGC2FQDN=<MGC2FQDN>,][RTPUDP=<RTPUDP>,][APPMODE=<APPMODE>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|IG number within a shelf. IgAid is the AID IgAid.
SWTYPE|SWitch TYPE The parameter indicate the type of switch which the H.248 interface group will be connected to. The only switches supported for primary switch type are: CS2K, META9020, SONUS. SWTYPE is of type H248SwitchType.
MGIP|Media Gateway's IP address for control message transport. MGIP is the AID IpAid. The default value is "0.0.0.0".
MG2IP|Secondary MGC IP address for control message transport. MG2IP is the AID IpAid. The default value is "0.0.0.0".
MGUDP|MGUDP is a Integer. The default value is "2944".
MGC1IP|Primary Media Gateway Controller's IP address. MGC1IP is the AID IpAid. The default value is "0.0.0.0".
MGC1UDP|MGC1UDP is a Integer. The default value is "2944".
MGC2IP|Secondary Media Gateway Controller's IP address. A value of 0.0.0.0 indicates there is none. MGC2IP is the AID IpAid. The default value is "0.0.0.0".
MGC2UDP|MGC2UDP is a Integer. The default value is "2944".
MGC2SWTYPE|Secondary MGC Switch Type. When MGC2ESA is set to N(by default), the only switches supported for secondary switch type are: CS2K, META9020, SONUS, NONE; ``` When MGC2ESA is set to Y, the only switches supported for secondary switch type are: GBANDG2, GBANDG6, NONE. MGC2SWTYPE is of type H248SwitchType. The default value is "NONE".
MGC2ESA|This parameter indicates whether the secondary MGC is ESA MGC2ESA is of type BoolYN. The default value is "N".
TERMPREFIX|Prefix on Termination Ids. This is a string of up to 11 characters. TERMPREFIX is a String. The default value is "TP".
EPHEMTERMID|H248 Ephemeral Termination ID. Used to allow the media gateway to properly interpret the string sent by the media gateway controller. Default value is NONE, max length is 30. EPHEMTERMID is a String.
TMAX|Maximum delay in seconds between first transmission and final retransmission of a message before declaring a communication failure with the MGC.
A value of 0 for TMAX disables the declaring of a MGC communication failure due to a message timeout, including a timeout waiting for a heartbeat message. TMAX is a Integer. The default value is "30".

MWD|Maximum delay in seconds [0,60] before announcing MG presence to MGC. MWD is a Integer. The default value is "30".
EPHEMAUDITDELAY|The number of seconds between repetitions of reporting of a stranded "ephemeral termination" (Network trunk). The value should be in the range 0-3600. The value 0 indicates that the audit is not to be performed. EPHEMAUDITDELAY is a Integer. The default value is "0".
FIRSTDIGWAIT|Default number of seconds to wait for the start of dialing. The valid range is 0-60 (0 disables the timer). FIRSTDIGWAIT is a Integer. The default value is "16".
LONGDIGWAIT|Default value in seconds of the long inter-digit timer. The valid range is 1-60. LONGDIGWAIT is a Integer. The default value is "16".
SHORTDIGWAIT|Default value in seconds of the short inter-digit timer. The valid range is 1-60. SHORTDIGWAIT is a Integer. The default value is "5".
LONGDIGDUR|Default minimum duration, in seconds, of a long digit event. The valid range is 1-60. LONGDIGDUR is a Integer. The default value is "20".
MINFLASH|Default minimum on-hook duration in milliseconds for a flash. The value range is 100-4900. MINFLASH is a Integer. The default value is "500".
MAXFLASH|Default maximum on-hook duration in milliseconds for a flash. The value range is 100-4900. MAXFLASH is a Integer. The default value is "1500".
MAXACTCALLS|Maximum number of concurrent calls (up to 384) for this IG. MAXACTCALLS is a Integer.
RFC2833ENABLE|RFC2833ENABLE is of type BoolYN. The default value is "N".
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN. The default value is "Y".
EPCD|Echo Path Change Detection. EPCD=Y is only effective when ECCONFIG=SPARSE on the supporting equipement (VGP/VIPR). Enabling EPCD improves the ability to track changes in the echo path, but reduces channel density. EPCD is of type BoolYN. The default value is "N".
ECTAIL|Integer: 64ms to 128ms in steps of 8ms. The maximum echo delay that the echo canceller is able to eliminate. If ECCONFIG=DUAL, increasing ECTAIL may further reduce channel density. If ECCONFIG=SPARSE, increasing ECTAIL does not impact channel density. ECTAIL is a Integer. The default value is "64".
MGC1FQDN|None is a special value to unset its previous value. MGC1FQDN is a String.
MGC2FQDN|None is a special value to unset its previous value. MGC2FQDN is a String.
RTPUDP|RTPUDP is a Integer. The default value is "49152".
APPMODE|Application Mode. APPMODE is of type H248AppMode. The default value is "OFF".
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "OOS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-HDSL:[TID]:<HdslAid>:[CTAG]:::[[LINETYPE=<LINETYPE>,][T1MAP=<T1MAP>,][FMT=<FMT>,][TERM=<TERM>,][SNRTHR=<SNRTHR>,][ATTHR=<ATTHR>,][PWR=<PWR>,][GOS=<GOS>,][TMGMODE=<TMGMODE>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port being entered. HdslAid is the AID SixPortLuAid.
LINETYPE|HDSL Line Type: 2- or 4-wire mode. In 4-wire mode, two consecutive port addresses are required for one HDSL port. LINETYPE is of type HdslLineType. The default value is "2WIRE".
T1MAP|MAPping of the T1 payload signal. When payload signal is a form that may be altered at the port, this parameter specifies the mapping. Otherwise, its value should be NA. T1MAP is of type T1MapHdsl. The default value is "NA".
FMT|DS1 Format. This parameter indicates DS1 signal format. FMT is of type FormatSignal. The default value is "UF".
TERM|TERMinal Unit Type TERM is of type HdslTermType. The default value is "COT".
SNRTHR|Signal-to-Noise Margin Threshold (near-end), in dB. (0 == OFF) SNRTHR is of type SnrTargetMargins. The default value is "6".
ATTHR|Loop Attenuation Threshold (near-end), in dB. (0 == OFF) ATTHR is of type HdslLoopAttenThresh. The default value is "20".
PWR|Line PoWeRing. This parameter indicates whether the line is to supply power. PWR is of type T1Pwr. The default value is "SINK".
GOS|Grade of Service Access Identifier. This is the HDSL Grade of Service which is to be applied to the port. GOS is the AID GosAid. The default value is "OFF".
TMGMODE|Timing Mode. This parameter selects the timing source for the T1 port transmit signal. For T1MAP other than UNI or NNI, C7 will default TMGMODE to LOOP when FMT=UF, SOURCE otherwise. TMGMODE is of type T1TimingMode. The default value is "LOOP".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-IG-CRV:[TID]:<CrvAid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
CrvAid|Call Reference Value Access Identifier. This is the address of the call reference value of a subscriber line in a GR-303 interface group. CrvAid is the AID CrvAid.
PLOCN|Physical Location. The physical location of the subscriber line to be cross connected to the Call Reference Value within the C7 network. This input parameter is provided for compatibility with the release that did not support T1 transport. The ENT-CRS-T0 command should be used to establish this association. PLOCN is the AID T0CrvAid.

##### Syntax: ```ENT-IG-CSHELF:[TID]:<IgAid>:[CTAG]::<SHELF>:NVDS1=<NVDS1>,[CAPALMTHR=<CAPALMTHR>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The Interface Group AID. IgAid is the AID IgAid.
SHELF|The associated subscriber shelf. SHELF is the AID ShelfAid.
NVDS1|The number of Virtual DS1s allocated for this association. This determines the call capacity for the IG to the associated shelf. NVDS1 is a Integer.
CAPALMTHR|Call Capacity Alarm Threshold. If the number of active calls reaches or exceeds this percentage of total, an alarm is raised. CAPALMTHR is of type Percentage. The default value is "85".

##### Syntax: ```ENT-IG-DS1:[TID]:<IgDs1Aid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
IgDs1Aid|Interface Group DS1 Access Identifier. The address of the DS1 Line Termination in an interface group. IgDs1Aid is the AID IgDs1Aid.
PLOCN|Physical Location. The physical location of the DS1 Line Termination within the C7 network. PLOCN is the AID TwelvePortLuAid.

##### Syntax: ```ENT-IG-VDS1:[TID]:<IgDs1Aid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
IgDs1Aid|Interface Group DS1 Access Identifier. The address of the DS1 Line Termination in a VCG interface group. IgDs1Aid is the AID IgDs1Aid.
PLOCN|The "physical location" of the virtual DS1 port associated with the IG. PLOCN is the AID Vds1Aid.

##### Syntax: ```ENT-IG-VSP:[TID]:<IgVspAid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
IgVspAid|The address of the VSP Termination in a H.248 interface group. IgVspAid is the AID IgVspAid.
PLOCN|The "physical location" of the VSP port associated with the IG. PLOCN is the AID VspPortAid.

##### Syntax: ```ENT-IGMP-JOIN:[TID]:<IP>:[CTAG]:::IRCAID=<IRCAID>,L2IFAID=<L2IFAID>; ```

##### Parameters
Attribute | Description
|---
IP|IP address of the EPG channel or Multicast IP address for video. IP is the AID IpAid.
IRCAID|IrcAid - IRC slot IRCAID is the AID SlotLuAid.
L2IFAID|L2IFAID is the AID VbPortAid.

##### Syntax: ```ENT-IMA:[TID]:<ImaAid>:[CTAG]:::[[IMAMAP=<IMAMAP>,][MLINKS=<MLINKS>,][XDIFDLY=<XDIFDLY>,][INH=<INH>,][FRMLEN=<FRMLEN>,][ALTV1_0=<ALTV1_0>,][GOS=<GOS>,][LINKGOS=<LINKGOS>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][TMGMODE=<TMGMODE>,][TXIMAGRPID=<TXIMAGRPID>,][TXIMAGRPVER=<TXIMAGRPVER>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. This is the address of the IMA Group that is being created. ImaAid is the AID ImaGrpAid.
IMAMAP|IMA Mapping. This parameter indicates how the internal fixed length packets are to be mapped at the IMA interface. IMAMAP is of type ImaMap. The default value is "NNI".
MLINKS|Minimum links. Minimum number of links required to be Active for the IMA group to be in the Up state. MLINKS is of type ImaLinks. The default value is "1".
XDIFDLY|Maximum Differential Delay. The maximum number of milliseconds of differential delay among the links that will be tolerated. XDIFDLY is of type ImaDiffDelay. The default value is "25".
INH|Inhibited. Configures whether the group is allowed to become operational and carry ATM data. INH is of type BoolYN. The default value is "N".
FRMLEN|Frame Length. The IMA frame length to be used by the IMA group. FRMLEN is of type ImaFrm. The default value is "128".
ALTV1_0|Alternative V1.0. The C7 IMA interface uses the IMA version 1.1 specification as default to interoperate with other IMA interfaces, this is normally backward compatible with older v1.0 interfaces. However, there are recognized interoperability issues with some older IMA interfaces. This parameter enables/disables the IMA group to use the alternative v1.0 IMA specification that should avoid these interoperability problems. For example, the parameter should be set in a group that is interoperating with an older Cisco IMA interface. Please see Atm Forum: Inverse Multiplexing for ATM Specification Version 1.1(AF-PHY-0086.001) - Abstract for further details. ALTV1_0 is of type BoolYN. The default value is "N".
GOS|Grade of Service Access Identifier. This is the Grade of Service that is to be applied to the IMA group. GOS is the AID GosAid. The default value is "OFF".
LINKGOS|Link Grade of Service Access Identifier. This is the Grade of Service that is to be applied to the IMA links. LINKGOS is the AID GosAid. The default value is "OFF".
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. PYLDSCRM is of type BoolYN. The default value is "N".
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. The default value is Y for internal interfaces and N for external interfaces. ATMMON is of type BoolYN. The default value is "N".
TMGMODE|Timing Mode. This parameter selects the timing source. TMGMODE is of type T1TimingMode. The default value is "SOURCE".
TXIMAGRPID|Specifies the transmit IMA Group ID, a value between 1 and 255. TXIMAGRPID is a Integer.
TXIMAGRPVER|Specifies the transmitted IMA version. TXIMAGRPVER is of type ImaVersion. The default value is "1.1".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-IMA-PORT:[TID]:<ImaAid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA AID. This is the address of the IMA Interface Group that is being created. The slot number of this AID must be that of the T1 lines which are to be included in the group. ImaAid is the AID ImaGrpAid.
PLOCN|Physical LOCatioN of the port. This specifies the location of the T1 port. It must specify the same slot as that of the IMA group. PLOCN is the AID PortId.

##### Syntax: ```ENT-IP-HOST:[TID]:<IP>:[CTAG]:::[[RTRAID=<RTRAID>,][MAC=<MAC>,][L2IFAID=<L2IFAID>,][VLAN=<VLAN>,][BRIDGE=<BRIDGE>]],HOSTTYPE=<HOSTTYPE>,[[MFFGW=<MFFGW>,][INCL=<INCL>]]; ```

##### Parameters
Attribute | Description
|---
IP|The static IP address of the Host IP is the AID IpAid.
RTRAID|RTRAID is the AID RouterAid.
MAC|The Mac address of the Host. MAC is the AID MacAid.
L2IFAID|Layer 2 Interface Access Identifier - This is the port address or the VC AID on which the host can be found. The system will use an IP VC if it is the only IP VC on the specified PORT. If the IP VC hasn't been provisioned yet, the system will use the first one upon its creation. IP HOST creation to a PON port is not allowed. IP HOST creation between an IRC PP1 and GE-2p VB port is not allowed. Hosts may be identified by enabling ARP between the IRC and Ge2p. L2IFAID is the AID HostId.
VLAN|VLAN is the AID IfId1.
BRIDGE|BRIDGE is the AID BridgeProvAid.
HOSTTYPE|Identifies the equiptment associated with an IP host. This parameter will indicate whether the system will allow channel-change requests from this host. HOSTTYPE is of type IpHostEqptType.
MFFGW|MFFGW is the AID IpAid.
INCL|INCLusive Flag. This inclusive flag allows an user to forcefully add an IP host entry when the provided MAC address is already bound to another IP host. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```ENT-IP-HOSTID:[TID]:<IPHostIdAid>:[CTAG]:::[[IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>]]; ```

##### Parameters
Attribute | Description
|---
IPHostIdAid|IP HostId AID on 8/12-port line-unit. Only one instance per ONT. IPHostIdAid is the AID IPHostIdAid.
IP|IP Address of HOST. IP is the AID IpAid. The default value is "NONE".
IPMSK|IP Mask. IPMSK is the AID IpAid. The default value is "0.0.0.0".
GADDR|Gateway Address. GADDR is the AID IpAid.

##### Syntax: ```ENT-IP-IF:[TID]:<IP>:[CTAG]:::IPMSK=<IPMSK>,[[L2IFAID=<L2IFAID>,][RTRAID=<RTRAID>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP address. The IP address may not be all zeros. The IP address anded with the IPMSK may not equal zero. The IP address anded with the compliment of the IPMSK may not be zero IP is the AID IpAid.
IPMSK|IP address mask. The most significant bit of the IP address must be set (1). The IP mask must be made up of consecutive set bits. This means a bit pattern like ...101... is disallowed because the set bits are not consecutive. IPMSK is the AID IpAid.
L2IFAID|Layer 2 Interface Access Identifier. Required for IRC. L2IFAID is the AID IpIfAid.
RTRAID|Router AID. Required for GE-2P. RTRAID is the AID RouterAid.

##### Syntax: ```ENT-IP-ROUTE:[TID]:<IPMASK>:[CTAG]:::RTRAID=<RTRAID>,GADDR=<GADDR>,[METRIC=<METRIC>]; ```

##### Parameters
Attribute | Description
|---
IPMASK|IP/MASK - The destination subnet IP address and destination subnet IP Address Mask. For routes from the Management slot, this address must be on the same subnet as one of the E1, E2, or E3 interfaces. IPMASK is the AID IpMask.
RTRAID|Access IDentifier of an AMP, IRC or Virtual Router. RTRAID is the AID RouteId1.
GADDR|Gateway, or "next hop" IP host address. GADDR is the AID IpAid.
METRIC|The routing metric of the interface. If no value is specified, the default is 1. The routing metric is used by the routing protocol. Higher metrics have the effect of making a route less favorable; ``` metrics are counted as addition hops to the destination network or host. For routes provisioned on IRC, the metric must be 1. METRIC is a Integer. The default value is "1".

##### Syntax: ```ENT-IPIF-PORT:[TID]:<IP>:[CTAG]:::INTERFACE=<INTERFACE>,RTRAID=<RTRAID>,[DHCPIPIF=<DHCPIPIF>]; ```

##### Parameters
Attribute | Description
|---
IP|IP is the AID IpAid.
INTERFACE|INTERFACE is the AID IpIfPortAid.
RTRAID|RTRAID is the AID VrAid.
DHCPIPIF|Indicates that this IPIF-PORT's interface is used for relaying DHCP requests. For DHCP requests to be relayed, exactly one IP interface for a given layer-2 interface must have DHCPIPIF=Y.
For SIPVCG DHCP to work, DHCPIPIF must be set to Y.

A given virtual bridge may have at most one IPIF-PORT, attached at the VB level, with the DHCPIPIF set to Y. Each VLAN, independent of the virtual bridge attachments, may also have at most one attached IP-Interface with DHCPIPIF set to Y. DHCPIPIF is of type BoolYN. The default value is "N".


##### Syntax: ```ENT-LAG:[TID]:<LinkAggAid>:[CTAG]:::MEM=<MEM>,[[LACPMODE=<LACPMODE>,][MTU=<MTU>,][RVRTV=<RVRTV>,][SYSPRIO=<SYSPRIO>,][PARTNERACTSTBY=<PARTNERACTSTBY>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 12 groups are supported on a single slot, and up to 4 on a single VB. LinkAggAid is the AID LinkAggAid.
MEM|This is the AID of a member port. MEM is the AID LagId2 and is listable.
LACPMODE|Only effective for Rap. LACPMODE is of type LacpMode. The default value is "SRCDSTMAC".
MTU|Max Transmission Unit.The default value for GE card is 2048. MTU is of type Mtu. The default value is "9000".
RVRTV|Revertive. This parameter indicates if the protection requested is to be revertive or non-revertive. This parameter is only applicable for RAP10G Active/Standby mode. Non-revertive prevents the link from switching back to the active members when a link is restored. The default value for RAP10G is Y. The default value for the other cards is N. RVRTV is of type BoolYN.
SYSPRIO|Used between two systems connected by the LAG to dertermine which should be controlling the LAG. The lower value takes priority. Typically, the upstream side of the LAG is configured for the LAG master (lower value). SYSPRIO is of type Zero264k. The default value is "32768".
PARTNERACTSTBY|Y - Suppress alarms consistent with Active/Standby operation. N - Do not supress alarms. PARTNERACTSTBY is of type BoolYN. The default value is "N".
DESC|The name of the LinkAgg. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-LSWITCH:[TID]:<LSwitchAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LSwitchAid|Logical Switch Access Identifier. LSwitchAid is the AID LSwitchAid.

##### Syntax: ```ENT-LSWITCH-PORT:[TID]:<LSwitchPortAid>:[CTAG]::<PLOCN>; ```

##### Parameters
Attribute | Description
|---
LSwitchPortAid|Logical Switch Port Access Identifier. LSwitchPortAid is the AID LSwitchPortAid.
PLOCN|Physical LOCatioN of the port. This specifies the location of the Logical Bridge port. PLOCN is the AID EthVtiAggPortAid.

##### Syntax: ```ENT-MACHOST:[TID]:<MACAID>:[CTAG]:::VLAN=<VLAN>,[BRIDGE=<BRIDGE>],L2IFAID=<L2IFAID>; ```

##### Parameters
Attribute | Description
|---
MACAID|MAC Address, unique within a VLAN. MACAID is the AID MacAid.
VLAN|VLAN is the AID IfId1.
BRIDGE|BRIDGE is the AID VbAid.
L2IFAID|Layer 2 Access Identifier. This is the port address or the VC Aid on which the host can be found. L2IFAID is the AID MachostId1.

##### Syntax: ```ENT-NODE:[TID]:<NodeAid>:[CTAG]::<SID>:[[NODEAMP=<NODEAMP>,][ALMCONT=<ALMCONT>,][MOUNT=<MOUNT>,][LAT=<LAT>,][LONG=<LONG>]]; ```

##### Parameters
Attribute | Description
|---
NodeAid|Node Access Identifier. The node number of the node which is to be defined. NodeAid is the AID NodeAid.
SID|System identification code (SID). This is the SID to be assigned to the the node. It is the SID which will be used to identify the node in the TID field of any subsequent TL1 commands issued by TL1 users who do not specify a Node Number in their AIDs. The value of SID may be any valid simple or compound TL1 identifier or text string. It is limited to 24 characters. The recommended value for this parameter is the node's CLLI. SID is a String.
NODEAMP|Node AMP. This is the AID of the AMP or ATP which is to report alarms for all shelves within the node. It must be in a shelf within the node. NODEAMP is the AID MsNoneAid.
ALMCONT|ALarM CONTact. This parameter determines whether alarm contacts can be scoped to reflect just the node or can be scoped report for the network. ALMCONT is of type AlarmContact.
MOUNT|Mount Type. This describes how the Node of C7's is mounted, such as a Rack or Outdoor Cabinet. MOUNT is of type MountType.
LAT|Latitude. This is the Latitude in real world coordinates. LAT is a Integer.
LONG|Longitude. This is the Longitude in real world coordinates. LONG is a Integer.

##### Syntax: ```ENT-ONT:[TID]:<OntAid>:[CTAG]:::[[ONTNUM=<ONTNUM>,][REGID=<REGID>]],ONTPROF=<ONTPROF>,[[VCG=<VCG>,][BATPROV=<BATPROV>,][ONTPID=<ONTPID>,][SDBER=<SDBER>,][GOS=<GOS>,][ADRMODE=<ADRMODE>,][RGALWRMT=<RGALWRMT>,][RGCFGINST=<RGCFGINST>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OntAid|The ONT Port Access Identifier. OntAid is the AID OntAid.
ONTNUM|The ONT Number for the ONT. This can be physical serial number of the unit or an assigned number programmed into the ONT. The ONT Number is entered as a string of at most 8 hexidecimal digits, optionally preceeded by "0x". The ONT Number always takes precedence over the registration id if present. ONTNUM is a String.
REGID|Registration Id. This is a string of up to 10 printable ASCII characters (Space is disallowed), that can be used instead of ONTNUM for remote ONT registration. When an ONT has been ranged and associated with a matching REGID in the database, the ONTNUM will be automatically recorded in the C7 database and service to the ONT enabled. REGID is a String.
ONTPROF|The ONT Profile that describes the capabilities of the ONT. If not specified, the system default (see ED-SYS) is used. ONTPROF is the AID OntId2.
VCG|The Voice Concentration Group used to support T0 cross-connects from this ONT. VCG is the AID OntId. The default value is "NONE".
BATPROV|This parameter indicates the expected Battery Backup capability. BATPROV is of type BoolYN. The default value is "Y".
ONTPID|The ONT Password is a string of up to 10 characters that can be used to verify the authenticity of an arriving ONT. A password cannot be provided when using a Calix defined ONT Profile. ONTPID is a String. The default value is """".
SDBER|The threshold value above which the PON Interface bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD. The default value is "5".
GOS|GOS is the AID GosAid. The default value is "OFF".
ADRMODE|ADRMODE is of type AdrMode. The default value is "GRP".
RGALWRMT|This parameter specifies a timeout which enables the RG remote management. This would only be allowed for ONTs with a NUMRG=1 profile. RGALWRMT is of type RgAlwRmtTimeOut.
RGCFGINST|RGCFGINST is of type ONTCFGINST. The default value is "NONE".
DESC|DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-ONT-QUAR:[TID]:<QuarOntAid>:[CTAG]:::[[ONTAID=<ONTAID>,][ONTNUM=<ONTNUM>,][VENDOR=<VENDOR>]]; ```

##### Parameters
Attribute | Description
|---
QuarOntAid|QuarOntAid is the AID QuarOntAid.
ONTAID|ONTAID is the AID OntAid.
ONTNUM|Vendor specific portion of the FSAN serial number.This is up to 8 hexidecimal characters. ONTNUM is a String.
VENDOR|Vendor identification.Four ascii characters in the range "A".."Z". VENDOR is a String. VENDOR is a String. The default value is "CXNX".

##### Syntax: ```ENT-PON:[TID]:<PonAid>:[CTAG]:::[[SDBER=<SDBER>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
PonAid|The PON Port Access Identifier. PonAid is the AID FourPortLuAid.
SDBER|Signal Degraded Bit Error Rate. The threshold value above which the Line's bit error rate constitutes a Degraded Signal. SDBER is of type BitErrorRateSD. The default value is "5".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String. The default value is """".
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-PP:[TID]:<PpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpAid|The PseudoPort AID PpAid is the AID PpAid.

##### Syntax: ```ENT-PPL:[TID]:<PplAid>:[CTAG]:::[[WKGRTELST=<WKGRTELST>,][PROTRTELST=<PROTRTELST>]]; ```

##### Parameters
Attribute | Description
|---
PplAid|PplAid is the AID PplUnbrAid.
WKGRTELST|List of route elements in the form of source and drop shelves on the working path. WKGRTELST is the AID StsAid and is listable.
PROTRTELST|List of route elements in the form of source and drop shelves on the protect path. PROTRTELST is the AID StsAid and is listable.

##### Syntax: ```ENT-PROF-ACS:[TID]:<ACSPROFAID>:[CTAG]:::ACSURL=<ACSURL>,USER=<USER>,[[PID=<PID>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
ACSPROFAID|The ACSProf AID. ACSPROFAID is the AID AcsProfAid.
ACSURL|The ACSURL is a string of up to 63 characters. It must begin with "http://". ACSURL is a String.
USER|The ACS user is a string of up to 31 characters. USER is a String.
PID|The ACS password is a string of up to 25 characters. PID is a String.
DESC|DESC is a String.

##### Syntax: ```ENT-PROF-ETH:[TID]:<EthProfAid>:[CTAG]:::BW=<BW>; ```

##### Parameters
Attribute | Description
|---
EthProfAid|Ethernet Profile Number. EthProfAid is the AID EthProfAid.
BW|BandWidth. BW is of type EthProfBw. The default value is "10".

##### Syntax: ```ENT-PROF-ETHBW:[TID]:<ProfileId>:[CTAG]:::[[CIR=<CIR>,][EIR=<EIR>,][EIRMODE=<EIRMODE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
ProfileId|This identifies which profile is being operated on. ProfileId is the AID BwpProfAid.
CIR|This is the rate (in Kbits/sec) which is guaranteed by this profile and the range is 0-10G in 128K increments. CIR and EIR can not be zero/non-zero at the same time. CIR is a Integer. The default value is "0".
EIR|This is the rate (in Kbits/sec) above the CIR which may be available for passing frames and the range is 0-10G in 128K increments. CIR and EIR can not be zero/non-zero at the same time. EIR is a Integer. The default value is "0".
EIRMODE|The EIR value represents excess bandwidth that is available to all priority levels within the VLAN interface. This is the current operating mode for Ethernet Bandwidth profiles. EIRMODE is of type EirMode.
DESC|A string describing the profile or its use. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ENT-PROF-MATCHLIST:[TID]:<MatchListAid>:[CTAG]:::[[MATCHRULE=<MATCHRULE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
MatchListAid|A unique network wide ID. MatchListAid is the AID MatchListAid.
MATCHRULE|The ID of a match rule to be included in this match list. MATCHRULE is the AID MatchRuleId and is listable.
DESC|An 11 character string description of the MatchList. DESC is a String.

##### Syntax: ```ENT-PROF-MATCHRULE:[TID]:<RuleAid>:[CTAG]:::SRCMAC=<SRCMAC>,[[SRCMACMASK=<SRCMACMASK>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
RuleAid|A C7 Network unique number identifying the rule. RuleAid is the AID MatchRuleId.
SRCMAC|The Source MAC Address. SRCMAC is the AID MacAid.
SRCMACMASK|The Number of Bits to use in the Src MAC address. SRCMACMASK is a Integer. The default value is "24".
DESC|An 11 character string description of the rule. DESC is a String.

##### Syntax: ```ENT-PROF-MCAST:[TID]:<McastProfId>:[CTAG]:::MVRPROF=<MVRPROF>,[[MAXSTREAMS=<MAXSTREAMS>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
McastProfId|McastProfId is the AID McastProfAid.
MVRPROF|This identifies an existing Multicast Vlan Registration profile entry. MVRPROF is the AID MvrProfAid.
MAXSTREAMS|Maximum number of video streams that can be joined. MAXSTREAMS is of type McastProfMaxStreams. The default value is "32".
DESC|User string. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ENT-PROF-MCASTRANGE:[TID]:<McastRangeProfAid>:[CTAG]:::RANGE=<RANGE>,[DESC=<DESC>]; ```

##### Parameters
Attribute | Description
|---
McastRangeProfAid|Mcast Range Profile AID. McastRangeProfAid is the AID McastRangeProfAid.
RANGE|This is a multicast address range to be allowed in a profile. Both the start and end address must be provided. Upto 4 non-overlapping address ranges are allowed per profile. RANGE is the AID IpAid and is listable and rangeable.
DESC|User String. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ENT-PROF-MVR:[TID]:<MvrProfAid>:[CTAG]:::VLAN=<VLAN>,RANGEPROF=<RANGEPROF>,[DESC=<DESC>]; ```

##### Parameters
Attribute | Description
|---
MvrProfAid|MvrProfAid is the AID MvrProfAid.
VLAN|Up to 4 VLANs may be associated with one profile. At least one VLAN must be specified. VLAN is the AID VlanIndexAid and is listable.
RANGEPROF|The Multicast Range profile ID added to a VLAN. The number of Range profile specified must match the number of VLAN specified. RANGEPROF is the AID MvrId1 and is listable.
DESC|User String. The maximum length of the string is 11 characters. DESC is a String.

##### Syntax: ```ENT-PROF-ONT:[TID]:<OntProfAid>:[CTAG]:::VENDOR=<VENDOR>,[[NUMPOTS=<NUMPOTS>,][NUMDS1=<NUMDS1>,][NUMGETH=<NUMGETH>,][NUMETH=<NUMETH>,][NUMHPNA=<NUMHPNA>,][NUMRFVID=<NUMRFVID>,][GEMONLY=<GEMONLY>,][AUXPWR=<AUXPWR>,][PWE3=<PWE3>,][NUMRG=<NUMRG>,][NUMBR=<NUMBR>,][DFLTRG=<DFLTRG>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
OntProfAid|ONT profile number. OntProfAid is the AID OntProfAid.
VENDOR|The Vendor ID for ONTs using this profile. This is a string up to 4 characters long. VENDOR is a String.
NUMPOTS|The number of POTS ports supported on the ONT; ``` the supported values are 0,2,4 and 8. NUMPOTS is a Integer. The default value is "0".
NUMDS1|The number of DS1 ports supported on the ONT. {0-12} NUMDS1 is a Integer. The default value is "0".
NUMGETH|The number of Gigabit Ethernet ports supported on the ONT. {0-8} NUMGETH is a Integer. The default value is "0".
NUMETH|The number of Ethernet ports supported on the ONT. {0-8} NUMETH is a Integer. The default value is "0".
NUMHPNA|The number of HPNA Ethernet ports supported on the ONT. {0-2} NUMHPNA is a Integer. The default value is "0".
NUMRFVID|The number of RF Video (COAX) output ports supported on the ONT. {0-12} NUMRFVID is a Integer. The default value is "0".
GEMONLY|This ONT has GEM /IP only capability. GEMONLY is of type BoolYN. The default value is "N".
AUXPWR|This ONT Auxiliary Power capability. AUXPWR is of type BoolYN. The default value is "N".
PWE3|PWE3 Capability. PWE3 is of type BoolYN.
NUMRG|Indicated the number of RG Ports supported by ONT; ``` the supported values are 0 and 1. NUMRG is a Integer. The default value is "0".
NUMBR|Indicated the number of Full Bridge ports supports by ONT; ``` the supported values are 0 and 1. NUMBR is a Integer. The default value is "0".
DFLTRG|Indicated the default mode of the ONT. DFLTRG is of type BoolYN. The default value is "N".
DESC|A user-settable description field for this profile, of up to 31 characters. DESC defaults to be the template address/index number. DESC is a String.

##### Syntax: ```ENT-PROF-SIPDIAL:[TID]:<SipDialAid>:[CTAG]:::[[ADDRULE=<ADDRULE>,][DELRULE=<DELRULE>,][SHDIGTIM=<SHDIGTIM>,][LNDIGTIM=<LNDIGTIM>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
SipDialAid|System scoped Dial Plan for SIP Gateways. SipDialAid is the AID DialPlanAid.
ADDRULE|A string specifying a rule to add to the dial plan. ADDRULE is a String.
DELRULE|A string specifying a rule to delete from the dial plan. DELRULE is a String.
SHDIGTIM|The timeout, in seconds, for digit collection when no match exists. SHDIGTIM is of type STimeOut. The default value is "4".
LNDIGTIM|The timeout, in seconds, for digit collection when no match exists. LNDIGTIM is of type LTimeOut. The default value is "16".
DESC|A string describing this Profile. DESC is a String.

##### Syntax: ```ENT-PROF-SIPSVC:[TID]:<SipSvcAid>:[CTAG]:::[[PRIPROXYADR=<PRIPROXYADR>,][SECPROXYADR=<SECPROXYADR>,][PROXYNAME=<PROXYNAME>,][PROXYPORT=<PROXYPORT>,][CODEC=<CODEC>,][PKTRATE=<PKTRATE>,][RTPPORT=<RTPPORT>,][RTPPRIO=<RTPPRIO>,][RTPDSCP=<RTPDSCP>,][TIMER_T1=<TIMER_T1>,][TIMER_T2=<TIMER_T2>,][SIPREGPER=<SIPREGPER>,][DTMFMODE=<DTMFMODE>,][CWSTRING=<CWSTRING>,][DISTRINGPREFIX=<DISTRINGPREFIX>,][UAHOOKFLASHCTRL=<UAHOOKFLASHCTRL>,][DNSSRV=<DNSSRV>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
SipSvcAid|System scoped SIP Profile. SipSvcAid is the AID SipSvcAid.
PRIPROXYADR|Primary SIP proxy server. PRIPROXYADR is the AID IpAid. The default value is "0.0.0.0".
SECPROXYADR|Secondary SIP proxy server. SECPROXYADR is the AID IpAid. The default value is "0.0.0.0".
PROXYNAME|FQDN of next hop Proxy Server for forwarding SIP messages. It should be 5 to 63 characters. PROXYNAME is a String.
PROXYPORT|UDP Port to use for SIP Proxy messaging. PROXYPORT is of type PortRange. The default value is "5060".
CODEC|Codec to use for digitization. CODEC is of type Codec. The default value is "G711_MU".
PKTRATE|Sample period to use for digitization. PKTRATE is of type PacketRate. The default value is "10MS".
RTPPORT|Base UDP port to be used for RTP streams. RTPPORT is of type RTPPORT. The default value is "49408".
RTPPRIO|802.1p priority value to be used for RTP frames. RTPPRIO is of type EthPrio. The default value is "6".
RTPDSCP|IP DSCP Value to be used for RTP PDUs. RTPDSCP is the AID DscpAid. The default value is "EF".
TIMER_T1|SIP RTT estimate. TIMER_T1 is of type TimerRange. The default value is "500".
TIMER_T2|SIP max retransmit interval TIMER_T2 is of type TimerRange. The default value is "4000".
SIPREGPER|Default lifetime of SIP registrations. SIPREGPER is of type TimerRange. The default value is "3600".
DTMFMODE|Enable out of band encoding of DTMF signals. DTMFMODE is of type DtmfMode. The default value is "INBAND".
CWSTRING|String used to identify Call Waiting tone in SIP messages CWSTRING is a String. The default value is ""CallWaitingTone"".
DISTRINGPREFIX|text string used to identify distinctive ring in SIP messages N/A. It is up to 20 characters. DISTRINGPREFIX is a String. The default value is ""Bellcore-dr"".
UAHOOKFLASHCTRL|Handle Hook Flash events at the SIP UA (true) or send Hook Flash notification to switch (false). UAHOOKFLASHCTRL is of type BoolYN. The default value is "Y".
DNSSRV|DNS SRV control flag. DNSSRV is of type BoolYN. The default value is "N".
DESC|A string description of the profile. DESC is a String.

##### Syntax: ```ENT-PROF-TRF:[TID]:<TrfProfAid>:[CTAG]:::COS=<COS>,[[CDVT=<CDVT>,][PCR01=<PCR01>,][SCR0=<SCR0>,][SCR01=<SCR01>,][MCR=<MCR>,][APP=<APP>,][MBS=<MBS>,][MFS=<MFS>,][CELLTAG=<CELLTAG>,][POLICE=<POLICE>,][ACTIVE=<ACTIVE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
TrfProfAid|Traffic Profile Access Identifier. The address of a specific entry in Traffic Profile table to be retrieved. TrfProfAid is the AID AtmTrfProfProvAid.
COS|Class of Service. This parameter indicates the general charactistics of the service desired. COS is of type ClassOfService.
CDVT|Cell Delay Variation Tolerance. This parameter indicates the maximum variance in cell delay that is acceptable. The units are microseconds. The parameter is applicable for CBR, GFR, and real-time VBR. Minimum CDVT must be at least (1/PCR01)*1000000 microsecs. Typical values would be around 5/PCR for ATM transport and 32/PCR for Video or IP. CDVT is a Integer.
PCR01|Peak Cell Rate. This parameter identifies the fastest rate at which back to back cells of a given ATM connection arrive. The rate is specified in cells per second. This parameter is applicable for all the supported COSs. PCR01 is a Integer.
SCR0|Sustainable Cell Rate for cell loss priority 0. This parameter indicates the maximum average rate of the connection over its lifetime for cells that do not have their CLP bit set. The rate is specified in cells per second. The parameter is reported only for VBR COSs. SCR0 is a Integer.
SCR01|Sustainable Cell Rate for cell loss priority 0 and 1. This parameter indicates the maximum average rate of the connection over its lifetime for cells regardless of their CLP bit setting. The rate is specified in cells per second. The parameter is applicable only to VBR COSs. SCR01 is a Integer.
MCR|Minimum Cell Rate. This parameter specifies a guaranteed minimimum cell rate that the connection will support. The rate is specified in cells per second. This parameter is applicable only to the GFR COS. MCR is a Integer.
APP|Applicationg ID. For Video applications. APP is of type ApplicationId.
MBS|Maximum Burst Size. This parameter specifies maximum number of consecutive cells that the source may send before the cells are tagged or discarded. This parameter is only applicable to the VBR and GFR COSs. MBS is a Integer.
MFS|Maximum Frame Size. The maximum number of cells in a frame. This parameter is applicable only to the GFR COS. MFS is a Integer.
CELLTAG|CELL TAGging. This parameter specifies whether the cells that exceed the specification should be tagged with CLP=1. The parameter is applicable to the VBRRT and VBRNRT COSs. CELLTAG is of type BoolYN. The default value is "N".
POLICE|Policing. Indicates whether rate policing is turned on. Note: the extra processing required to support policing will result in a total available bandwidth reduction of approximately 20%. POLICE is of type BoolYN. The default value is "Y".
ACTIVE|This parameter indicates that the profile may be used for new cross-connect provisioning. Setting ACTIVE=N will prevent the VOD Flow Manager from selecting a traffic profile for flow VC creation when the operator is attempting to "age out" a profile and later delete it. ACTIVE is of type BoolYN. The default value is "Y".
DESC|Description. A string description of this object, up to 11 characters in length. The string is intended to help users track profiles they create. DESC is a String.

##### Syntax: ```ENT-PW:[TID]:<PwAid>:[CTAG]:::[[TMPLT=<TMPLT>,][STARTDS0=<STARTDS0>,][NDS0=<NDS0>]],IPHOSTID=<IPHOSTID>,DSTIP=<DSTIP>,SRCUDP=<SRCUDP>,[[DSTUDP=<DSTUDP>,][RTPTS=<RTPTS>,][RTPTSMODE=<RTPTSMODE>,][FPP=<FPP>,][PYLDSIZE=<PYLDSIZE>,][JBUFDEPTH=<JBUFDEPTH>,][GOS=<GOS>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
PwAid|PW Aid pattern. Only PW1 is valid for ONT PWE3. For ONT PWUNSTRUCT, the index of PW Aid is limited to PW1. For ONT PWSTRUCT(currently this is not implemented), the index of PW Aid will be in a range. PwAid is the AID PwAid.
TMPLT|Includes all the following attributes after UDP. TMPLT is the AID PwTmpltAid.
STARTDS0|First DS0 timeslot in the range of consecutive DS0 timeslots associated with the PWUSTRUCT PW. STARTDS0 is of type PwDs0TimeSlot. The default value is "1".
NDS0|Number of consecutive DS0 timeslots associated with the PWUSTRUCT PW starting at STARTDS0. NDS0 is of type PwDs0TimeSlot. The default value is "24".
IPHOSTID|IP Host of the PW bundle at the near-end. Slot scope IP Host identifier. IPHOSTID is the AID IPHostIdAid.
DSTIP|Destination IP address of the PW. DSTIP is the AID IpAid.
SRCUDP|Source UDP Port# identifying this PW at the given IP address. SRCUDP is of type PwUdpPort.
DSTUDP|Destination UDP Port# identifying this PW at the given IP address. DSTUDP is of type PwUdpPort.
RTPTS|Allows enabling RTP timestamp. RTPTS can only be Y when TMGMODE is set to DIFF. RTPTS is of type BoolYN. The default value is "Y".
RTPTSMODE|Timestamp generation mode -ignored if RTPTS=N. When RTPTS is enabled, if TMGMODE is set to ADAPT/LOOP/SOURCE, RTPTSMODE must be ABS; ``` and if TMGMODE is set to DIFF, RTPTSMODE must be DIFF. RTPTSMODE is of type RtpTsMode. The default value is "DIFF".
FPP|Number of T1 frames per packet for structured service. Packet interval is computed in the range of 0.5ms to 7.5ms. FPP is of type T1FrmsPerPkt. The default value is "8".
PYLDSIZE|This is the size of the PWE3 payload. For PWUNSTRUCT only. PYLDSIZE must be in multiples of 32 when the container T1 port is enabled with TMGMODE as either ADAPT or DIFF. PYLDSIZE is of type PayloadSize. The default value is "192".
JBUFDEPTH|The size of the buffer to absorb the PDV. Jitter buffer latency is based on the FramesPerPacket. Its max value for ONT PW is limited to 250000. JBUFDEPTH is of type JitBufSize. The default value is "3000".
GOS|This identifies the grade of service for performance monitoring (PM) which will be applied to the PW. GOS is the AID GosAid.
DESC|A user-settable description field, up to 31 characters. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisonable is SB. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-RFVID:[TID]:<OntPortAid>:[CTAG]:::[[ENONBAT=<EONBAT>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Rf-Video Port Access Identifer. The address of the RFVID port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortAid.
EONBAT|For ONT ports, this parameter specifies the behavior the port when the ONT is running on battery backup, and overrides the default (ONTRFVIDONBAT) specified by ED-SYS. EONBAT is of type OntPortPwrOpt. The default value is "USEDEF".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String. The default value is """".
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-RMTDEV:[TID]:<RmtDevAid>:[CTAG]:::[[SERIAL=<SERIAL>,][DEVNAME=<DEVNAME>,][DEVTYPE=<DEVTYPE>,][MGMTIP=<MGMTIP>,][PLOCN=<PLOCN>,][SAMENODE=<SAMENODE>,][SIPVCG=<SIPVCG>]]; ```

##### Parameters
Attribute | Description
|---
RmtDevAid|Remote Device Access Identifier. RmtDevAid is the AID RmtDevAid.
SERIAL|The remote device serial number. This may correspond to a backplane identifier, or some other means of identifying the physical piece of equipment. SERIAL is a String.
DEVNAME|The name of the remote device. This could be the CLLI code of a network element, or an arbitrary name assigned to the device DEVNAME is a String.
DEVTYPE|The type of the Remote Device. DEVTYPE is of type RmtDeviceType.
MGMTIP|The IP address(es) of the device to which an operator or the CMS can connect. MGMTIP is the AID IpAid.
PLOCN|The identifier(s) of the physical port(s) to which the remote device is connected. This can include in-band ports such as a GE or OCn port, or a port on the AMP. PLOCN is the AID RmtdevId.
SAMENODE|This indicates if the device is considered part of the same node for management purposes. In a general sense, a node refers to co-located equipment of performing a collective function. SAMENODE is of type BoolYN.
SIPVCG|The SIP VCG created for managing SIP-based subscribers. The SIP VCG is required if this device will use a PSTN gateway capabilities of the C7 SIPVCG is the AID IgAid.

##### Syntax: ```ENT-SHELF:[TID]:<ShelfAid>:[CTAG]::<BackplaneNo>:[[PWRCAT3=<PWRCAT3>,][DCIN=<DCIN>,][EXPRESSLINKS=<EXPRESSLINKS>,][ROGDTCT=<ROGDTCT>,][AUTOQUAR=<AUTOQUAR>,][DEFAULTVB=<DEFAULTVB>]]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|This is the AID to be set for the backplane identified in the BackplaneNo field. ShelfAid is the AID ShelfAid.
BackplaneNo|This is the serial number of the backplane that is to be given the Shelf AID specified in the ShelfAid field. Note that to input a HEX-value, the leading 2 characters should be 0x (zero x). Otherwise, the value will be processed as Decimal-value. BackplaneNo is a String.
PWRCAT3|Power Category 3 Shutdown time. This is the time equipment assigned to power category 3 is allowed to remain powered up after the system switches to emergency backup power. PWRCAT3 is of type PowerCat3Time. The default value is "10 minutes".
DCIN|DC Inputs. This parameter indicates the type of DC power being supplied to the shelf. DCIN is of type DCIN. The default value is "BOTH".
EXPRESSLINKS|Express Links. When set to Y, this will cause the system will attempt to save bandwidth on cross-connects the following criteria: 1) Connection is of type T0, T1, VP or VC. 2) Connection is on an intermediate transport shelf that is ATM-capable. 3) Source and destination are on slots 9-12, CSA and CSB. 4) Connection is bi-directional, or a unicast VOD connection. 5) Connection is unprotected or is going to an unprotected destination. Note that INCL=Y must also be specified when changing this parameter, as the shelf will reboot as a result! EXPRESSLINKS is of type BoolYN. The default value is "N".
ROGDTCT|System will enable rogue detection on PONs by default. ROGDTCT is of type BoolYN. The default value is "Y".
AUTOQUAR|System will auto quarantine Rogue ONTs. AUTOQUAR is of type BoolYN. The default value is "Y".
DEFAULTVB|Default VB number for this shelf. DEFAULTVB is of type VbNum. The default value is "1".

##### Syntax: ```ENT-SIP:[TID]:<IgAid>:[CTAG]:::[[PRICFGURL=<PRICFGURL>,][SECCFGURL=<SECCFGURL>,][HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>,][MAXACTCALLS=<MAXACTCALLS>,][OPTION82=<OPTION82>,][DNSSVR=<DNSSVR>,][SECDNSSVR=<SECDNSSVR>,][ETHPRIO=<ETHPRIO>,][ECENABLE=<ECENABLE>,][DSCP=<DSCP>,][VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][ECTAIL=<ECTAIL>,][SIPSVCPROF=<SIPSVCPROF>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|Access Identifier for the SIP Group. IgAid is the AID IgAid.
PRICFGURL|PRImary ConFiGuration Uniform Resource Locator. URL of the configuration needed to access the SIP network. Currently TFTP access and direct registration with the SIP registrar are supported. The value can take following 1 of 2 formats: "TFTP: //IP address of TFTP server/Path to Config File" or "REGISTER SIP: IP address of SIP registrar" PRICFGURL is a String.
SECCFGURL|SECondary ConFiGuration Uniform Resource Locator. URL of backup network access configuration. The value takes the same format as PRICFGURL. SECCFGURL is a String.
HOSTPROTO|Protocol to be used to obtain the IP address for the host for SIP lines in the group. HOSTPROTO is of type SipHostProto. The default value is "STATIC".
IP|IP address. Statically assigned IP address associated with the group. IP is the AID IpAid. The default value is "0.0.0.0".
IPMSK|Subnet IP MASK. IPMSK is the AID IpAid. The default value is "0.0.0.0".
GADDR|Subnet IP GATEWAY Address. Statically assigned IP address associated with the group's gateway. GADDR is the AID IpAid. The default value is "0.0.0.0".
MAXACTCALLS|Maximum number of concurrent calls (up to 384) for this IG. MAXACTCALLS is a Integer. The default value is "360".
OPTION82|Indicates whether DHCP Relay Option 82 is enabled. This field is only used for C7 SIP service. It has been deprecated since C7 9.0. OPTION82 is of type Option82.
DNSSVR|IP Address of Primary DNS Server. DNSSVR is the AID IpAid. The default value is "0.0.0.0".
SECDNSSVR|IP Address of Secondary DNS Server. SECDNSSVR is the AID IpAid. The default value is "0.0.0.0".
ETHPRIO|802.1p priority value to be used for SIP messages. ETHPRIO is of type EthPrio. The default value is "6".
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN. The default value is "Y".
DSCP|IP DSCP Value to be used for SIP messages. DSCP is the AID DscpAid. The default value is "EF".
VLAN|The integer value of the VLAN. VLAN is the AID VlanIndexAid.
BRIDGE|The virtual bridge providing Ethernet services. BRIDGE is the AID BridgeProvAid.
ECTAIL|ECTAIL. ECTAIL is of type Ectail. The default value is "32".
SIPSVCPROF|Sip service profile index. SIPSVCPROF is the AID SipSvcAid.
PST|Primary services state. PST is of type PrimaryStateChg.

##### Syntax: ```ENT-SIPT0:[TID]:<T0Aid>:[CTAG]:::SIPIG=<SIPIG>,USER=<USER>,[[AOR=<AOR>,][PID=<PID>,][HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>]]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0Aid is the AID SipT0PortAid.
SIPIG|SIP Group AID. Identifies the SIP group to which the line belongs. SIPIG is the AID IgAid.
USER|User Name. User name for the subscriber. This string is used to form the UserId field toe the left of the @ in the SIP URL. It is also used as the username for authentication protocols. The value is a character string up to 20 bytes. It must either be a telephone number or the AID of a legacy telephony interface provided by a C7. USER is a String.
AOR|Address Of Record. This is an alphanumeric string that describes the phone number used to reference a user in the network. The value is a character string up to 32 bytes. AOR is a String. The default value is "0".
PID|Password. Password for authorization of the subscriber. The value is a character string up to 20 bytes. PID is a String.
HOSTPROTO|HOSTPROTO is of type SipT0HostProto. The default value is "GROUP".
IP|IP is the AID IpAid. The default value is "0.0.0.0".
IPMSK|IPMSK is the AID IpAid. The default value is "0.0.0.0".
GADDR|GADDR is the AID IpAid. The default value is "0.0.0.0".

##### Syntax: ```ENT-SIPVCG:[TID]:<IgAid>:[CTAG]:::[[CTLIP=<CTLIP>,][MAXACTCALLS=<MAXACTCALLS>,][ECENABLE=<ECENABLE>,][EPCD=<EPCD>,][ECTAIL=<ECTAIL>,][VSPIP=<VSPIP>,][VSPUDP=<VSPUDP>,][HOSTPROTO=<HOSTPROTO>,][SUBNET=<SUBNET>,][RTRAID=<RTRAID>,][VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][PKTRATE=<PKTRATE>,][RETRYTMR=<RETRYTMR>,][UDPSTART=<UDPSTART>,][LEASETIME=<LEASETIME>,][FORCERENEW=<FORCERENEW>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|Ig Number within a shelf. IgAid is the AID IgAid.
CTLIP|Control IP Address. IP address for control message transport. This IP address is used to contact both the SIP registrar and the SIP user agents associated with the IG. CTLIP is the AID IpAid.
MAXACTCALLS|MAXACTCALLS is a Integer. The default value is "48".
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN. The default value is "N".
EPCD|Echo Path Change Detection. EPCD=Y is only effective when ECCONFIG=SPARSE on the supporting equipement (VGP/VIPR). Enabling EPCD improves the ability to track changes in the echo path, but reduces channel density. EPCD is of type BoolYN. The default value is "N".
ECTAIL|ECTAIL is a Integer. The default value is "64".
VSPIP|This parameter is only applicable when the associated VSP resource resides on an EGW. VSPIP is the AID IpAid.
VSPUDP|This parameter is only applicable when the associated VSP resource resides on an EGW. Allowable values are 49408, 53504, 57600, and 61696. VSPUDP is a Integer.
HOSTPROTO|HOSTPROTO is of type SipHostProto. The default value is "STATIC".
SUBNET|SUBNET is the AID IpAid. The default value is "0.0.0.0".
RTRAID|RTRAID is the AID VrAid.
VLAN|The integer value of the VLAN. VLAN is the AID VlanIndexAid.
BRIDGE|LOCAL is not valid for this command. BRIDGE is the AID BridgeProvAid.
PKTRATE|PKTRATE is a Integer. The default value is "10".
RETRYTMR|RETRYTMR is a Integer. The default value is "60".
UDPSTART|UDPSTART is restricted to the values 49408, 53504, 57600, and 61696 UDPSTART is a Integer. The default value is "49408".
LEASETIME|LEASETIME is a Integer.
FORCERENEW|FORCERENEW is of type BoolYN.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "OOS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-SNMP-ACL:[TID]::[CTAG]:::IP=<IP>,IPMSK=<IPMSK>; ```

##### Parameters
Attribute | Description
|---
IP|IP Address. The IP address of the SNMP manager that is allowed to make requests to the C7 network. IP is the AID IpAid.
IPMSK|IP Address Mask. The mask to apply to the IP address, allowing for a range of IP addresses to be considered. IPMSK is the AID IpAid.

##### Syntax: ```ENT-SUBIF-BINDING:[TID]:<PHYSLOC>:[CTAG]:::IP=<IP>,RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
PHYSLOC|Physical Location Access Identifier - specifies the subscriber location scope. This AID can be ALL, Node, Shelf, Slot or Port. Scope must be disjoint for different IP adddresses or proper subsets of each other.
IP|Layer 3 interface address. This is assigned to a physical location and used instead of the GADDR field in all relayed DHCP client messages. IP is the AID IpAid.
RTRAID|This is the IRC slot location. RTRAID is the AID SlotLuAid.

##### Syntax: ```ENT-T0:[TID]:<T0Aid>:[CTAG]:::[[GSFN=<GSFN>,][RTLP=<RTLP>,][TTLP=<TTLP>,][Z=<Z>,][EBSLVL=<EBSLVL>,][EFTT=<EFTT>,][RATE=<RATE>,][EC=<EC>,][ZCS=<ZCS>,][SC=<SC>,][TIMEOUT=<TIMEOUT>,][LLBE=<LLBE>,][DDSTEST=<DDSTEST>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Port Access Identifier. The address of the T0 port which is being created. T0Aid is the AID TwentyFourPortLuAid.
GSFN|General Signaling Function. This indicates the signaling used by the T0 port, such as loop start, ground start, etc. Note: 4DU is valid for the OCUDPx6 line unit. 4D0 is valid for the DS0DPx6 line unit. GSFN is of type GenSigFunction. The default value is "2LS".
RTLP|Receive Transmission Loss Plan. Transmission level point for receiving from the equipment. The transmission level point is the decibel value of the ratio of the power of a 1004 Hz signal at a point to the power of the same signal at a reference point on the digital side of the codec. Therefore, an increase in the RTLP will result in a gain toward the analog side. The default is set to match the standard settings for an RPOTS card. RTLP is of type Rlp. The default value is "-2.0".
TTLP|Transmit Transmission Loss Plan. Transmission level point for transmitting toward the equipment. The transmission level point is the decibel value of the ratio of the power of a 1004 Hz signal at a point to the power of the same signal at a reference point on the digital side of the codec. Therefore, an increase in the TTLP will result in a gain toward the digital side. The default is set to match the standard settings for an RPOTS card. TTLP is of type Tlp. The default value is "-2.0".
Z|Impedance. This parameter indicates the expected impedance of the line in Ohms. Z is of type ImpedanceOhms. The default value is "900".
EBSLVL|Electronic Business Service LeVeL This attribute is only applicable to Nortel's Electronic Business Service. It specifies the level of the secondary signaling channel. EBSLVL is of type EBSLvl. The default value is "AUTO".
EFTT|Enable Full-Time Transmission. This attribute is set to Y to enable transmission of the audio channel even when the subscriber is on-hook and the phone has not recently been rung. This parameter may be used to force a "nailed up" connection even when the DS0 is associated with a T1 transport group CRV. EFTT is of type BoolYN. The default value is "N".
RATE|Data Rate. (DDS only) Note: Changing rates terminates the loopbacks on an OCUDP line unit due to the required reset on hardware. RATE is of type DdsRate. The default value is "56".
EC|Error Correction. (DDS only) This parameter is valid if there are no cross connections. A value of EC=Y is invalid if one cross connection exists for 56 and 64 kbps rates and cross connect must be deleted first. EC=Y is also invalid if two cross connections exist for 2.4, 4.8, 9.6 and 19.2 kbps rates and cross connect must be deleted first. A value of EC=N is invalid if two cross connection exists at any data rates and cross connection must be deleted first. EC is of type BoolYN. The default value is "N".
ZCS|Zero Code Supression. (DDS only) ZCS is of type BoolYN. The default value is "Y".
SC|Secondary Channel. (DDS only) This parmater is only valid for OCUDPx6 line unit. It can be entered for the DS0Dpx6 line unit, but it will be ignored. Note that SC=Y is invalid for 64 kbps rate. Also SC=N is always valid without any restrictions. SC is of type BoolYN. The default value is "N".
TIMEOUT|Latching Loopback Timeout (in minutes). (DDS only) If TIMEOUT = 0, Latching loopback continues to operate, but it cancels the timer if active. If TIMEOUT > 0, the new timeout value is applied to the currently active latching loopback or subsequent loopback. If the new timeout value is greater than the previous value, the difference is applied to the currently outstanding timer. If the new timeout value is less than the previous value, the loopback terminates. If the new timeout value is the same as before, no further action is required. TIMEOUT is of type LatchLpbkTimeout. The default value is "0".
LLBE|Latching LoopBack Enable. (DDS only) LLBE is of type BoolYN. The default value is "Y".
DDSTEST|DDS Test Mode (DDS only). The DDS card supports two modes of loop testing: Bipolar (analog) and Logic Near/Far (digital TTY). This parameter indicates which mode is to be used. DDSTEST is of type DdsTest. The default value is "LOGIC".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. Note: For OOS, DDS service is disabled. For OCUDP, sealing current is removed. For IS, DDS service is enabled. For OCUDP, sealing current is applied. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service states which can be changed are redline and SB. The redline state indicates that the line cannot be deleted unless, redline is removed from the service state first. SB indicates that both Tx and Rx should be suspended. It only applies when the PST is OOS. SST is of type SecondaryStateChg and is listable.

##### Syntax: ```ENT-T1:[TID]:<Ds1Aid>:[CTAG]:::[[TYPE=<TYPE>,][T1MAP=<T1MAP>,][EQLZ=<EQLZ>,][ATTEN=<ATTEN>,][PWR=<PWR>,][FMT=<FMT>,][LINECDE=<LINECDE>,][GOS=<GOS>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][EXT=<EXT>,][PDOM=<PDOM>,][NDS0RESVD=<NDS0RESVD>,][TMGMODE=<TMGMODE>,][IBLBEN=<IBLBEN>,][CAS=<CAS>,][IBLBCODE=<IBLBCODE>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port being modified. Ds1Aid is the AID TwelvePortLuAid.
TYPE|TYPE of T1. This indicates whether the port is to be configured as a DS1 or a T1. TYPE is of type T1Type. The default value is "DS1".
T1MAP|MAPping of the payload signal. When payload signal is a form that may be altered at the T1 port, this parameter specifies the mapping. Otherwise, its value should be NA. Default values for T1MAP will be NA for DS1A-12 cards and SEQ for both T1-6 and T1-6A+T cards. T1MAP is of type T1Map.
EQLZ|Equalization. Indicates equalization setting (aka Line Build Out). It applies only when TYPE=DS1. EQLZ is of type Equalization. The default value is "300".
ATTEN|ATTENuation. Indicates the attenuation for T1 lines. It applies only when TYPE=T1. ATTEN is of type Attenuation. The default value is "0.0".
PWR|Line PoWeRing. This parameter indicates whether the line is to supply power. PWR is of type T1Pwr. The default value is "SINK".
FMT|DS1 Format. This parameter indicates DS1 signal format. Default values for FMT will be UF for DS1A-12 cards and ESF for both T1-6 and T1-6A+T cards. FMT is of type FormatSignal.
LINECDE|Line Code. This is the provisioned DS1 line coding. LINECDE is of type LineCode. The default value is "B8ZS".
GOS|Grade of Service Access Identifier. This is the T1 Grade of Service which is to be applied to the DS1. GOS is the AID GosAid. The default value is "OFF".
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. It is only applicable when T1MAP is UNI or NNI. PYLDSCRM is of type BoolYN. The default value is "N".
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. The default value is Y for internal interfaces and N for external interfaces. ATMMON is of type BoolYN.
EXT|External Interface. This indicates if the T1 is an internal or external path in the network. The value should be set to "Y" when the port is an external interface. It should be set to "N" when the port is connected to other shelves within a network of C7s. This parameter is valid only if T1MAP is NNI. Note that this parameter must be changed independently of others, ie. a separate ED-T1 command is required. EXT is of type BoolYN. The default value is "Y".
PDOM|Protection DOMain. This is an integer that is used to associate a transport facility into a protection domain that is used for A to Z connection provisioning. The PDOM for each domain must be a unique non-zero integer. The value of 0 is reserved to indicate that the facility is not to be used for A to Z connections. PDOM is of type Pdom. The default value is "0".
NDS0RESVD|Number of Reserved DS0s. This parameter indicates the number of sequential DS0s that are to be reserved in a T1 facility that has a non-DS0 mapping for the remainder of its payload. The DS0s reserved are sequential decreasing from time slot 24. This parameter is only applicable when T1MAP is NNI or UNI. NDS0RESVD is a Integer. The default value is "0".
TMGMODE|Timing Mode. This parameter selects the timing source for the T1 port transmit signal. TMGMODE defaults to LOOP for ATM interfaces (i.e. T1MAP of UNI or NNI). For non-ATM interfaces, TMGMODE will default to LOOP when FMT=UF, else TMGMODE will default to SOURCE. TMGMODE is of type T1TimingMode. The default value is "SOURCE".
IBLBEN|Enable/Disable the ability of the hardware to activate or deactivate remotely controlled T1 loopbacks. IBLBEN is of type BoolYN. The default value is "N".
CAS|The signaling bits are carried in the TDM data, as well as in the signaling substructure. CAS enabled/ disabled shall affect all PWs on the Port. CAS is of type BoolYN. The default value is "Y".
IBLBCODE|Inband Loopback code. If detected in the egress direction, terminal loopback will be performed automatically on this T1 port. "Inband Loopback Terminal" condition will be also raised. Loop down code detected in egress direction will remove this condition. If detected in the ingress direction, facility loopback will be performed automatically on this T1 port. "Inband Loopback Facility" condition will be also raised. Loop down code detected in ingress direction will remove this condition. In addition, the "Inband Loopback Facility/Terminal" condition can be overridden administratively. User can perform OPR-LPBK-T1 to override inband loopback condition to administrative loopback, then use RLS-LPBK-T1 to release the loopback. For ONT T1 port, the default value is "11000" and it only can be set to "11000". For the other types of T1 port, the defalut value is "00001". IBLBCODE is a String. The default value is "00001".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-T1TG:[TID]:<IdtIgAid>,<RdtIgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IdtIgAid|IdtIgAid is an IDT T1 tranport interface group. T1 transport interface groups form IDT/RDT pairs. The IDT is the T1 connection endpoint closer to the network side of the interface and is therefore the subscriber-facing interface group. IdtIgAid is the AID IgAid.
RdtIgAid|RdtIgAid is an RDT T1 tranport interface group. T1 transport interface groups groups form IDT/RDT pairs. The RDT is the T1 connection endpoint closer to the subscriber side of the interface and is therefore the network-facing interface group. RdtIgAid is the AID IgAid.

##### Syntax: ```ENT-T3:[TID]:<Ds3Aid>:[CTAG]:::[[INTF=<INTF>,][AIS=<AIS>,][AIST=<AIST>,][IDLE=<IDLE>,][FMT=<FMT>,][LBO=<LBO>,][GOS=<GOS>,][EXT=<EXT>,][ATM=<ATM>,][PYLDSCRM=<PYLDSCRM>,][ATMMON=<ATMMON>,][PDOM=<PDOM>,][TMGMODE=<TMGMODE>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port being modified. Ds3Aid is the AID T3Aid.
INTF|Interface Type. The type of interface being provided by the DS3. When the equipment type is DS3-12s the interface type must be CCHAN. When the equipment type is DS3-12p, the interface type must be either NNI or UNI. INTF is of type T3Interface.
AIS|Alarm Indication Signal. Indicates whether AIS is transmitted from the DS3 being provisioned. AIS is of type BoolYN. The default value is "N".
AIST|AIS Type. This parameter indicates the type of the AIS signal to be generated/transmitted, and the AIS signal mode expected on input should a failure condition occur. When the card type is a DS3-12p, then only a value of NAS will be accepted. AIST is of type AisType. The default value is "NAS".
IDLE|Idle signal. This parameter indicates the transmission or non-transmission of the IDLE signal. For Ds3S(CCHAN) card IDLE can be transmitted only in the INGRESS direction and not the EGRESS direction. For Ds3 packet card IDLE can be transmitted only in the EGRESS direction. IDLE is of type Idle. The default value is "OFF".
FMT|DS3 Format. This parameter indicates DS3 signal format. When the INTF is UNI or NNI, then the format must be CBIT. When the INTF is CCHAN, then either CBIT or M23 is valid. FMT is of type FormatT3. The default value is "CBIT".
LBO|Line Build Out. This parameter indicates the line build out setting. LBO is a Integer. The default value is "100".
GOS|Grade of Service Access Identifier. This is the T3 Grade of Service which is to be applied to the DS3. GOS is the AID GosAid. The default value is "OFF".
EXT|External Interface. This indicates if the T3 is an internal or external path in the network. The value should be set to "Y" when the port is an external interface. It should be set to "N" when the port is connected to other shelves within a network of C7s. For INTF=CCHAN, EXT must be Y. Note that this parameter must be changed independently of others, ie. a separate ED-T3 command is required. EXT is of type BoolYN. The default value is "Y".
ATM|ATM Mapping. This parameter indicates how the ATM payload is mapped into the DS3 Frame. If the INTF parameter is set to CCHAN this parameter is invalid. ATM is of type ATMPayload. The default value is "DIRECT".
PYLDSCRM|Payload Scrambling. This parameter is set to Y to enable the scrambling of ATM cells. If the INTF parameter is set to CCHAN this parameter is invalid. PYLDSCRM is of type BoolYN. The default value is "Y".
ATMMON|ATM Diagnostic Monitoring. This parameter is set to Y to enable ATM diagnostic monitoring on the STS path. If enabled, an ATM OAM loopback ping is injected on VP0-VC3 to verify point-to-point connectivity with the next line unit. It applies only to ATMNNI and ATMUNI interfaces. The default value is Y for internal interfaces and N for external interfaces. ATMMON is of type BoolYN.
PDOM|Protection domain. This is an integer that is used to associate FFPs into a coordinated protection domain. The PDOM for each domain must be a unique integer. If the INTF parameter is set to CCHAN this parameter is invalid. PDOM is of type Pdom. The default value is "0".
TMGMODE|Timing Mode. This parameter selects the timing source for the T3 port transmit signal. TMGMODE is only relevant to DS3E cards. Timing Mode defaults to SOURCE. TMGMODE is of type DS3TimingMode.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "IS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-TDMGW:[TID]:<IgAid>:[CTAG]:::[[VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][ECENABLE=<ECENABLE>,][ECTAIL=<ECTAIL>,][SUBNET=<SUBNET>]]:[<PST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgAid.
VLAN|The integer value of the VLAN. VLAN is the AID VlanIndexAid.
BRIDGE|LOCAL is not valid for this command. BRIDGE is the AID BridgeProvAid.
ECENABLE|ECENABLE is of type BoolYN. The default value is "Y".
ECTAIL|ECTAIL is a Integer.
SUBNET|SUBNET is the AID IpAid. The default value is "0.0.0.0".
PST|PST is of type PrimaryStateChg. The default value is "OOS".

##### Syntax: ```ENT-TGRP:[TID]:<MsAid>:[CTAG]:::[[TBUS=<TBUS>,][GTAP=<GTAP>]]; ```

##### Parameters
Attribute | Description
|---
MsAid|Maintenance Slot Access Identifier. The address of the maintenance slot which controls the test bus. MsAid is the AID MsAid.
TBUS|Test Bus. This parameter indicates which shelfs are connected (via wiring) to the maintenance slot which controls the test bus. TBUS is the AID ShelfAid and is listable.
GTAP|GTAP Gold Test Access Port. This parameter specifies which slot hosts the GTAP. For VDSL2 port test, it is necessary to have a valid GTAP parameter. GTAP is the AID SlotLuAid.

##### Syntax: ```ENT-TMPLT-ADSL:[TID]:<DslProfAid>:[CTAG]::[<SRVTYPE>],[<CHNL0>],[<CHNL1>]:[[XDSR0=<XDSR0>,][MDSR0=<MDSR0>,][XUSR0=<XUSR0>,][MUSR0=<MUSR0>,][XDSR1=<XDSR1>,][MDSR1=<MDSR1>,][XUSR1=<XUSR1>,][MUSR1=<MUSR1>,][DSEXR=<DSEXR>,][USEXR=<USEXR>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][DSLAT=<DSLAT>,][USLAT=<USLAT>,][TC=<TC>,][RAMODEDS=<RAMODEDS>,][RAMODEUS=<RAMODEUS>,][RAUMDS=<RAUMDS>,][RADMDS=<RADMDS>,][RAUTDS=<RAUTDS>,][RADTDS=<RADTDS>,][RAUMUS=<RAUMUS>,][RADMUS=<RADMUS>,][RAUTUS=<RAUTUS>,][RADTUS=<RADTUS>,][PMMODE=<PMMODE>,][L0TIME=<L0TIME>,][L2TIME=<L2TIME>,][L2ATPR=<L2ATPR>,][L2MINR=<L2MINR>,][L2EXITR=<L2EXITR>,][L2ENTRYR=<L2ENTRYR>,][L2ENTRYT=<L2ENTRYT>,][DSST=<DSST>,][DSET=<DSET>,][USST=<USST>,][USET=<USET>,][ENABLENOTCH=<ENABLENOTCH>,][DPBOEPSDBP1TONE=<DPBOEPSDBP1TONE>,][DPBOEPSDBP1PSD=<DPBOEPSDBP1PSD>,][DPBOEPSDBP2TONE=<DPBOEPSDBP2TONE>,][DPBOEPSDBP2PSD=<DPBOEPSDBP2PSD>,][DPBOEPSDBP3TONE=<DPBOEPSDBP3TONE>,][DPBOEPSDBP3PSD=<DPBOEPSDBP3PSD>,][DPBOEPSDBP4TONE=<DPBOEPSDBP4TONE>,][DPBOEPSDBP4PSD=<DPBOEPSDBP4PSD>,][DPBOEPSDBP5TONE=<DPBOEPSDBP5TONE>,][DPBOEPSDBP5PSD=<DPBOEPSDBP5PSD>,][DPBOEPSDBP6TONE=<DPBOEPSDBP6TONE>,][DPBOEPSDBP6PSD=<DPBOEPSDBP6PSD>,][DPBOEPSDBP7TONE=<DPBOEPSDBP7TONE>,][DPBOEPSDBP7PSD=<DPBOEPSDBP7PSD>,][DPBOEPSDBP8TONE=<DPBOEPSDBP8TONE>,][DPBOEPSDBP8PSD=<DPBOEPSDBP8PSD>,][DPBOEPSDBP9TONE=<DPBOEPSDBP9TONE>,][DPBOEPSDBP9PSD=<DPBOEPSDBP9PSD>,][DPBOEPSDBP10TONE=<DPBOEPSDBP10TONE>,][DPBOEPSDBP10PSD=<DPBOEPSDBP10PSD>,][DPBOEPSDBP11TONE=<DPBOEPSDBP11TONE>,][DPBOEPSDBP11PSD=<DPBOEPSDBP11PSD>,][DPBOEPSDBP12TONE=<DPBOEPSDBP12TONE>,][DPBOEPSDBP12PSD=<DPBOEPSDBP12PSD>,][DPBOEPSDBP13TONE=<DPBOEPSDBP13TONE>,][DPBOEPSDBP13PSD=<DPBOEPSDBP13PSD>,][DPBOEPSDBP14TONE=<DPBOEPSDBP14TONE>,][DPBOEPSDBP14PSD=<DPBOEPSDBP14PSD>,][DPBOEPSDBP15TONE=<DPBOEPSDBP15TONE>,][DPBOEPSDBP15PSD=<DPBOEPSDBP15PSD>,][DPBOEPSDBP16TONE=<DPBOEPSDBP16TONE>,][DPBOEPSDBP16PSD=<DPBOEPSDBP16PSD>,][DPBOESEL=<DPBOESEL>,][DPBOESCMA=<DPBOESCMA>,][DPBOESCMB=<DPBOESCMB>,][DPBOESCMC=<DPBOESCMC>,][DPBOMUS=<DPBOMUS>,][DPBOFMIN=<DPBOFMIN>,][DPBOFMAX=<DPBOFMAX>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
DslProfAid|ADSL Profile Access Identifier. The address of the specific entry in ADSL Profile table. DslProfAid is the AID DslProfProvAid.
SRVTYPE|Service Type. This parameter specifies the ADSL operating modes which dictate the ADSL handshaking protocol, channel capacity, and other physical line characteristics. SRVTYPE is of type AdslType. The default value is "MM".
CHNL0|Channel 0 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (2 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL0 is of type ChnlSelect0. The default value is "INTLV".
CHNL1|Channel 1 Selection/Allocation. Settings for channel path latency. Choosing a latency path of Fast means minimum (2 ms) delay is expected while choosing a latency path of Interleaved means more delay. CHNL1 is of type ChnlSelect1. The default value is "DISABLE".
XDSR0|Maximum Downstream Rate - Channel 0. XDSR0 is of type DwnStreamRate.
MDSR0|Minimum Downstream Rate - Channel 0. MDSR0 is of type DwnStreamRate. The default value is "384".
XUSR0|Maximum Upstream Rate - Channel 0. XUSR0 is of type UpStreamRate.
MUSR0|Minimum Upstream Rate - Channel 0. MUSR0 is of type UpStreamRate. The default value is "128".
XDSR1|Maximum Downstream Rate - Channel 1. XDSR1 is of type DwnStreamRate.
MDSR1|Minimum Downstream Rate - Channel 1. MDSR1 is of type DwnStreamRate.
XUSR1|Maximum Upstream Rate - Channel 1. XUSR1 is of type UpStreamRate.
MUSR1|Minimum Upstream Rate - Channel 1. MUSR1 is of type UpStreamRate.
DSEXR|Downstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. DSEXR is of type ExcessRate. The default value is "100".
USEXR|Upstream Excess Rate Ratio. The ratio configuration values, 1 for downstream and 1 for upstream, specify the ratio (expressed in %) of excess bit rate that is to be applied to the primary bearer channel before applying bit rate to the secondary bearer channel. The primary channel will always be channel 0. The excess bit rate is the rate considered for rate adaptation amongst the primary and secondary channels (Channel 0 and Channel 1). The rate that can be considered excess is the rate in excess of the minimum bit rate parameter for each DS and US channel. USEXR is of type ExcessRate. The default value is "100".
TMDS|Target Downstream SNR Margin. This parameter specifies the target signal to noise ratio which basically quantifies the quality of the physical line through which the DSL signal flows. TMDS is of type SnrTargetMargins. The default value is "8".
XMDS|Maximum Downstream SNR Margin. This parameter specifies the maximum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. XMDS is of type SnrMaxMargins. The default value is "16".
MMDS|Minimum Downstream SNR Margin. This parameter specifies the minimum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. MMDS is of type SnrMinMargins. The default value is "0".
TMUS|Target Upstream SNR Margin. This parameter specifies the target signal to noise ratio which basically quantifies the quality of the physical line through which the DSL signal flows. TMUS is of type SnrTargetMargins. The default value is "8".
XMUS|Maximum Upstream SNR Margin. This parameter specifies the maximum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. XMUS is of type SnrMaxMargins. The default value is "16".
MMUS|Minimum Upstream SNR Margin. This parameter specifies the minimum signal to noise ratio (SNR) which basically quantifies the quality of the physical line through which the DSL signal flows. The SNR margin setting specifies the "padding" beyond the minimum required SNR in order for the DSL link to stay up at a certain data rate. For example, if the SNR margin is set to a positive value, it guarantees that if the SNR of the line suddenly drops below the minimum requirement but not below the "padded" value (i.e. min. required SNR + SNR margin) that the link will stay connected. MMUS is of type SnrMinMargins. The default value is "0".
DSLAT|Downstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. DSLAT is of type Latency. The default value is "AUTO".
USLAT|Upstream Latency. Latency is the delay in data transmission through the DSL link. Latency parameter is configured in milliseconds. The AUTO setting allows the ADSL card to pick the most appropriate interleave latency. NOTE: If both DSLAT and USLAT are set to the value "AUTO", neither parameter can be changed individually. Both of these parameters must be set to a numeric value at the same time in order to change them. The "AUTO" value must be set for both DSLAT and USLAT if you want to use "AUTO" for either direction. USLAT is of type Latency. The default value is "AUTO".
TC|Trellis Coding. Trellis Coding is an encoding scheme for piggybacking bits onto the electrical signal on the twisted pair. Turning on this parameter will improve the DSL system performance. TC is of type TrellisCoding. The default value is "ENABLED".
RAMODEDS|Rate Adaptation MODE DownStream. RAMODEDS is of type RateAdaptationMode. The default value is "INIT".
RAMODEUS|Rate Adaptation MODE UpStream. RAMODEUS is of type RateAdaptationMode. The default value is "INIT".
RAUMDS|Rate Adaptation Upshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RAUMDS is of type SnrMaxMargins. The default value is "9".
RADMDS|Rate Adaptation Downshift Margin DownStream (dB). This applies when RAMODE is DYNAMIC. RAUMDS must be greater than RADMDS. RADMDS is of type SnrMaxMargins. The default value is "3".
RAUTDS|Rate Adaptation Upshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RAUTDS is of type RateAdaptationMarginSeconds. The default value is "60".
RADTDS|Rate Adaptation Downshift Time Downstream (seconds). This applies when RAMODE is DYNAMIC. RADTDS is of type RateAdaptationMarginSeconds. The default value is "60".
RAUMUS|Rate Adaptation Upshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RAUMUS is of type SnrMaxMargins. The default value is "9".
RADMUS|Rate Adaptation Downshift Margin UpStream (dB). This applies when RAMODE is DYNAMIC. RAUMUS must be greater than RADMUS. RADMUS is of type SnrMaxMargins. The default value is "3".
RAUTUS|Rate Adaptation Upshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RAUTUS is of type RateAdaptationMarginSeconds. The default value is "60".
RADTUS|Rate Adaptation Downshift Time UpStream (seconds). This applies when RAMODE is DYNAMIC. RADTUS is of type RateAdaptationMarginSeconds. The default value is "60".
PMMODE|Power Management MODE. PMMODE is of type AdslPowerMgmtStates. The default value is "L0".
L0TIME|Minimum L0 Time interval between L2 exit and next L2 entry. (0-255 seconds) L0TIME is a Integer. The default value is "255".
L2TIME|Minimum L2 time interval between L2 entry and first L2 trim. (0-255 seconds) L2TIME is a Integer. The default value is "25".
L2ATPR|Maximum Aggregate Transmit Power Reduction per L2 trim. (dB) L2ATPR is of type SnrMaxMargins. The default value is "3".
L2MINR|Minimum Data Rate in Low Power Mode (L2). This parameter specifies the minimum net data rate (in Kbps) during the low power state. If the actual user data rate is lower than L2MINR, raw cells will be injected to maintain the provisioned value. The value can range from 256 to 1024 Kbps. L2MINR is a Integer. The default value is "1024".
L2EXITR|L2 Exit Rate Threshold. This parameter specifies the downstream datarate threshold (in Kbps), which triggers exit from low power state (L2). The value ranges between 1 and 1024 Kbps, and must be less than L2MINR. L2EXITR is a Integer. The default value is "512".
L2ENTRYR|L2 Entry Rate Threshold. This parameter specifies the downstream data rate threshold (in Kbps), which triggers autonomous entry into low power state (L2). The value can range from 1 to 1024, and must be less or equal to L2EXITR. L2ENTRYR is a Integer. The default value is "1".
L2ENTRYT|L2 Entry Time Threshold. This parameter specifies minimum interval of time (in seconds) that the net data rate should stay below L2ENTRYR before autonomous entry into low power state (L2). The value can range from 900 to 65535 seconds. L2ENTRYT is a Integer. The default value is "1800".
DSST|DownStream Start Tone index. DSST must be less than or equal to DSET. DSST is a Integer. The default value is "0".
DSET|DownStream End Tone index. DSET must be greater than or equal to DSST. DSET is a Integer. The default value is "0".
USST|UpStream Start Tone index. USST must be less than or equal to USET. USST is a Integer. The default value is "0".
USET|UpStream End Tone index. USET must be greater than or equal to USST. USET is a Integer. The default value is "0".
ENABLENOTCH|Enable notching for adsl. ENABLENOTCH is of type BoolYN. The default value is "N".
DPBOEPSDBP1TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP1TONE is of type Tone. The default value is "32".
DPBOEPSDBP1PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, PSD value. The valid range is from -127 to 0. DPBOEPSDBP1PSD is a Integer.
DPBOEPSDBP2TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP2TONE is of type Tone. The default value is "33".
DPBOEPSDBP2PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, PSD value. The valid range is from -127 to 0. DPBOEPSDBP2PSD is a Integer.
DPBOEPSDBP3TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP3TONE is of type Tone. The default value is "255".
DPBOEPSDBP3PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, PSD value. The valid range is from -127 to 0. DPBOEPSDBP3PSD is a Integer.
DPBOEPSDBP4TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP4TONE is of type Tone. The default value is "376".
DPBOEPSDBP4PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, PSD value. The valid range is from -127 to 0. DPBOEPSDBP4PSD is a Integer.
DPBOEPSDBP5TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP5TONE is of type Tone. The default value is "511".
DPBOEPSDBP5PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, PSD value. The valid range is from -127 to 0. DPBOEPSDBP5PSD is a Integer.
DPBOEPSDBP6TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP6TONE is of type Tone. The default value is "512".
DPBOEPSDBP6PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, PSD value. The valid range is from -127 to 0. DPBOEPSDBP6PSD is a Integer.
DPBOEPSDBP7TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP7TONE is of type Tone. The default value is "0".
DPBOEPSDBP7PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, PSD value. The valid range is from -127 to 0. DPBOEPSDBP7PSD is a Integer.
DPBOEPSDBP8TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP8TONE is of type Tone. The default value is "0".
DPBOEPSDBP8PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, PSD value. The valid range is from -127 to 0. DPBOEPSDBP8PSD is a Integer.
DPBOEPSDBP9TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP9TONE is of type Tone. The default value is "0".
DPBOEPSDBP9PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, PSD value. The valid range is from -127 to 0. DPBOEPSDBP9PSD is a Integer.
DPBOEPSDBP10TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP10TONE is of type Tone. The default value is "0".
DPBOEPSDBP10PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, PSD value. The valid range is from -127 to 0. DPBOEPSDBP10PSD is a Integer.
DPBOEPSDBP11TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP11TONE is of type Tone. The default value is "0".
DPBOEPSDBP11PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, PSD value. The valid range is from -127 to 0. DPBOEPSDBP11PSD is a Integer.
DPBOEPSDBP12TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP12TONE is of type Tone. The default value is "0".
DPBOEPSDBP12PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, PSD value. The valid range is from -127 to 0. DPBOEPSDBP12PSD is a Integer.
DPBOEPSDBP13TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP13TONE is of type Tone. The default value is "0".
DPBOEPSDBP13PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, PSD value. The valid range is from -127 to 0. DPBOEPSDBP13PSD is a Integer.
DPBOEPSDBP14TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP14TONE is of type Tone. The default value is "0".
DPBOEPSDBP14PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, PSD value. The valid range is from -127 to 0. DPBOEPSDBP14PSD is a Integer.
DPBOEPSDBP15TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP15TONE is of type Tone. The default value is "0".
DPBOEPSDBP15PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, PSD value. The valid range is from -127 to 0. DPBOEPSDBP15PSD is a Integer.
DPBOEPSDBP16TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, Tone Index. The max tone for adsl2-24a/combo2-24a card is 512. DPBOEPSDBP16TONE is the AID AcsId.
DPBOEPSDBP16PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, PSD value. The valid range is from -127 to 0. DPBOEPSDBP16PSD is a Integer.
DPBOESEL|Downstream Power Back Off, Exchange-side Electrical Length. The valid range is from 0 to 255. DPBOESEL is a Integer. The default value is "0".
DPBOESCMA|Downstream Power Back Off, Exchange-side Cable Model Parameter A. DPBOESCMA is of type Escm. The default value is "263".
DPBOESCMB|Downstream Power Back Off, Exchange-side Cable Model Parameter B. DPBOESCMB is of type Escm. The default value is "509".
DPBOESCMC|Downstream Power Back Off, Exchange-side Cable Model Parameter C. DPBOESCMC is of type Escm. The default value is "261".
DPBOMUS|Downstream Power Back Off, Minimum Usable PSD Mask. The valid range is from -127 to 0. DPBOMUS is a Integer.
DPBOFMIN|Downstream Power Back Off, Frequency Min. DPBOFMIN is of type Fmin. The default value is "32".
DPBOFMAX|Downstream Power Back Off, Frequency Max. DPBOFMAX is of type Fmax. The default value is "511".
DESC|DESCription. A user-settable description field, up to 11 characters. The description defaults to be the template address/index number. DESC is a String.

##### Syntax: ```ENT-TMPLT-PW:[TID]:<PwTmpltAid>:[CTAG]:::[[RTPTS=<RTPTS>,][RTPTSMODE=<RTPTSMODE>,][FPP=<FPP>,][PYLDSIZE=<PYLDSIZE>,][JBUFDEPTH=<JBUFDEPTH>,][PYLDS=<PYLDS>,][PKTSINSYN=<PKTSINSYN>,][PKTSOUTSYN=<PKTSOUTSYN>,][HOLDOFF=<HOLDOFF>,][FILLP=<FILLP>,][FILL=<FILL>,][RTPPTTX=<RTPPTTX>,][RTPPTRX=<RTPPTRX>,][SSRCTX=<SSRCTX>,][SSRCRX=<SSRCRX>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
PwTmpltAid|PW template Aid pattern. PwTmpltAid is the AID PwTmpltAid.
RTPTS|Allows enabling RTP timestamp. RTPTS is of type BoolYN. The default value is "Y".
RTPTSMODE|Timestamp generation mode if RTPTS is enabled. RTPTSMODE is of type RtpTsMode. The default value is "DIFF".
FPP|Number of T1 frames per packet for structured service. Packet interval is computed in the range of 0.5ms to 7.5ms. FPP is of type T1FrmsPerPkt. The default value is "8".
PYLDSIZE|This is the size of the PWE3 payload. For PWUNSTRUCT only. PYLDSIZE must be in multiples of 32 when the container T1 port is enabled with TMGMODE as either ADAPT or DIFF. PYLDSIZE is of type PayloadSize.
JBUFDEPTH|The size of the buffer to absorb the PDV. Jitter buffer latency is based on the FramesPerPacket. Its max value for ONT PW is limited to 250000. JBUFDEPTH is of type JitBufSize. The default value is "3000".
PYLDS|Selecting Yes means suppression is allowed. Payload MAY be omitted in order to conserve bandwidth. Otherwise, no suppression under any condition. PYLDS is of type BoolYN. The default value is "N".
PKTSINSYN|The number of packets required to exit the LOPS state. PKTSINSYN is of type PktsInSyn. The default value is "2".
PKTSOUTSYN|The number of consecutive packets missed required to enter LOPS state. PKTSOUTSYN is of type PktsOutSyn. The default value is "10".
HOLDOFF|Hold-off timer to declare PW down when a PW is setup (refer RFC5604). HOLDOFF is of type NonNegativeInteger. The default value is "5000".
FILLP|Policy to be applied when the CE-bound Jitter buffer is overflow/ underflow for any reason. FILLP is of type TdmFillPolicy. The default value is "AIS".
FILL|User Defined Fill Pattern to be used towards the T1 port. FILL is of type FillerRange. The default value is "255".
RTPPTTX|RTP Payload type to be used to transmit and received PW packets. RTPPTTX is of type RtpPayloadType. The default value is "96".
RTPPTRX|RTP Payload expected to be received from the far-end PW.For Ont PWE3, Calix ONT only accepts RTPPTRX=0. RTPPTRX is of type RtpPayloadType. The default value is "96".
SSRCTX|SSRC value to be transmitted on towards PSN. It's not applicable for ONT PW. SSRCTX is of type NonNegativeInteger. The default value is "0".
SSRCRX|SSRC value expected to be received at the near-end. It's not applicable for ONT PW. SSRCRX is of type NonNegativeInteger. The default value is "0".
DESC|A user-settable description field, up to 31 characters. DESC is a String.

##### Syntax: ```ENT-TMPLT-SECU:[TID]:<SecuTmpltAid>:[CTAG]:::[[PAGE=<PAGE>,][PCND=<PCND>,][TMOUT=<TMOUT>,][UAPMA=<UAPMA>,][UAPMT=<UAPMT>,][UAPSE=<UAPSE>,][UAPSY=<UAPSY>,][UAPTS=<UAPTS>,][NODEAID=<NODEAID>,][ENTADA=<ENTADA>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
SecuTmpltAid|This is the Access Identifier of the Security Template to be created. SecuTmpltAid is the AID SecuTmpltProvAid.
PAGE|Password Aging Interval. The passward aging interval is expressed in days. An integer less than or equal to 999, typically 45 to 60. At the end of the interval the user is notified that the existing password needs to be changed each time they log in. A value of zero indicates the user's password will never expire. PAGE is of type UserInterval. The default value is "45".
PCND|Password ChaNge Days. This parameter specifies the number of days the user has between the time they are first notified that they must change their password and the time their USERID is disabled. PCND is of type UserInterval. The default value is "7".
TMOUT|TiMe OUT. This parameter specifies the number of minutes of inactivity that must pass before their session is automatically logged out. A value of zero indicates that the user's sessions are never to be logged out due to inactivity. TMOUT is of type TimeOut. The default value is "10".
UAPMA|User Access Privilege for Memory Administration. This parameter specifies the abilities of a user for executing memory administration commands. UAPMA is of type AcsPrv. The default value is "NONE".
UAPMT|User Access Privilege for MainTenance. This parameter specifies the abilities of a user for executing maintenance commands. UAPMT is of type AcsPrv. The default value is "NONE".
UAPSE|User Access Privilege for SEcurity. This parameter specifies the abilities of a user for executing security commands. UAPSE is of type AcsPrv. The default value is "MIN".
UAPSY|User Access Privilege for SYstem. This parameter specifies the abilities of a user for executing system commands. UAPSY is of type AcsPrv. The default value is "NONE".
UAPTS|User Access Privilege for TeSting. This parameter specifies the abilities of a user for executing testing commands. UAPTS is of type AcsPrv. The default value is "NONE".
NODEAID|Use NODE Access IDentifier. This parameter is set to Y (Yes) if AIDs in responses to this user are to contain node identifiers. This is the normal setting. N (No) needs to be specified for Operations Systems (such as NMA) that cannot tolerate node identifiers. For these systems, AIDs for the same node as was identified in the TID of the command will have the Nx- deleted from the AID in responses and autonomous reports. For input, the node identifier may be omitted if the node is the same as is identified in the TID. NODEAID is of type BoolYN. The default value is "Y".
ENTADA|This boolean flag determines whether or not the user may perform an ENTer on an object that is in ADA state. ENTADA is of type BoolYN.
DESC|A string description of this object, up to 11 characters in length. DESC is a String.

##### Syntax: ```ENT-TMPLT-VLANIF:[TID]:<VlanIfTmpltAid>:[CTAG]:::[[ARP=<ARP>,][DHCPDIR=<DHCPDIR>,][OPT82ACT=<OPT82ACT>,][IGMP=<IGMP>,][PPPOEAC=<PPPOEAC>,][PPPOESUB=<PPPOESUB>,][LSVID=<LSVID>,][PRIO=<PRIO>,][ENCAP=<ENCAP>,][DOS=<DOS>,][DFLTROUTE=<DFLTROUTE>,][STP=<STP>,][STPCOST=<STPCOST>,][STPPRIO=<STPPRIO>,][DIRN=<DIRN>,][STAGTYPE=<STAGTYPE>,][PORTTYPE=<PORTTYPE>,][TRFPROF=<TRFPROF>,][BCKPROF=<BCKPROF>,][PATH=<PATH>,][PC=<PC>,][RXETHBWPROF=<RXETHBWPROF>,][TXETHBWPROF=<TXETHBWPROF>,][MCASTPROF=<MCASTPROF>,][LEASELMT=<LEASELMT>,][MATCHLIST=<MATCHLIST>,][ACSPROF=<ACSPROF>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VlanIfTmpltAid|VlanIfTmpltAid is the AID VlanIfTmpltAid.
ARP|ARP is of type BoolYN.
DHCPDIR|DHCPDIR is of type DhcpDirection.
OPT82ACT|OPT82ACT is of type Option82Action.
IGMP|IGMP is of type IgmpType.
PPPOEAC|PPPOEAC is of type BoolYN.
PPPOESUB|PPPOESUB is of type BoolYN.
LSVID|LSVID is of type VlanTagOrNone.
PRIO|802.1q Priority Bits Policy. PRIO is of type PrioBits.
ENCAP|ENCAP is of type EncapType.
DOS|DOS is of type BoolYN.
DFLTROUTE|Indicates whether it is the "default" VLAN-IF and would be the owner of the default route. Only applicable for ONT RSG. The default value for DHCP VLAN-IF is N. The default value for PPPoE/STATIC VLAN-IF is Y. Only one RG VLAN-IF can set it to Y. DFLTROUTE is of type BoolYN. DFLTROUTE is of type BoolYN.
STP|STP is of type StpAddr.
STPCOST|STPCOST is a Integer.
STPPRIO|STPPRIO is a Integer.
DIRN|DIRN is of type VbPortDirection.
STAGTYPE|STAGTYPE is of type StagEthType.
PORTTYPE|PORTTYPE is of type VbPortType.
TRFPROF|TRFPROF is the AID TrfId.
BCKPROF|BCKPROF is the AID TrfId.
PATH|PATH is of type Path.
PC|PC is of type ProtClass.
RXETHBWPROF|RXETHBWPROF is the AID VlanifId.
TXETHBWPROF|TXETHBWPROF is the AID VlanifId.
MCASTPROF|MCASTPROF is the AID McastProfAid.
LEASELMT|LEASELMT is of type LeaseLimit.
MATCHLIST|MATCHLIST is the AID IfId6.
ACSPROF|The AID of a defined ACS Profileto be applied to this VLAN interface. No other VLAN-IFs on the same RG with this parameter presented. Only allowed for RG. ACSPROF is the AID IfId7.
DESC|DESC is a String.

##### Syntax: ```ENT-TMPLT-XDSL:[TID]:<XdslTmpltAid>:[CTAG]::<SRVTYPE>:[[XDSLLINEPROF=<XDSLLINEPROF>,][PKTMODE=<PKTMODE>,][PTMOVER=<PTMOVER>,][FALLBACKVPI=<FALLBACKVPI>,][FALLBACKVCI=<FALLBACKVCI>,][CHNLLAT=<CHNLLAT>,][XRDS=<XRDS>,][MRDS=<MRDS>,][XRUS=<XRUS>,][MRUS=<MRUS>,][INTLVLATDS=<INTLVLATDS>,][INTLVLATUS=<INTLVLATUS>,][MININPDS=<MININPDS>,][MININPUS=<MININPUS>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][RAMODEDS=<RAMODEDS>,][RAMODEUS=<RAMODEUS>,][RAUMDS=<RAUMDS>,][RADMDS=<RADMDS>,][RAUTDS=<RAUTDS>,][RADTDS=<RADTDS>,][RAUMUS=<RAUMUS>,][RADMUS=<RADMUS>,][RAUTUS=<RAUTUS>,][RADTUS=<RADTUS>,][PMMODE=<PMMODE>,][L0TIME=<L0TIME>,][L2TIME=<L2TIME>,][L2ATPR=<L2ATPR>,][L2MINR=<L2MINR>,][L2EXITR=<L2EXITR>,][L2ENTRYR=<L2ENTRYR>,][L2ENTRYT=<L2ENTRYT>,][GOS=<GOS>,][AHC=<AHC>,][EINP=<EINP>,][REPTRMVRST=<REPTRMVRST>,][US0PSD=<US0PSD>,][VNSTART1=<VNSTART1>,][VNSTOP1=<VNSTOP1>,][VNSTART2=<VNSTART2>,][VNSTOP2=<VNSTOP2>,][VNSTART3=<VNSTART3>,][VNSTOP3=<VNSTOP3>,][VNSTART4=<VNSTART4>,][VNSTOP4=<VNSTOP4>,][VRSTART1=<VRSTART1>,][VRSTOP1=<VRSTOP1>,][VRSTART2=<VRSTART2>,][VRSTOP2=<VRSTOP2>,][VRSTART3=<VRSTART3>,][VRSTOP3=<VRSTOP3>,][VRSTART4=<VRSTART4>,][VRSTOP4=<VRSTOP4>,][VRSTART5=<VRSTART5>,][VRSTOP5=<VRSTOP5>,][VRSTART6=<VRSTART6>,][VRSTOP6=<VRSTOP6>,][VRSTART7=<VRSTART7>,][VRSTOP7=<VRSTOP7>,][VRSTART8=<VRSTART8>,][VRSTOP8=<VRSTOP8>,][VRSTART9=<VRSTART9>,][VRSTOP9=<VRSTOP9>,][VRSTART10=<VRSTART10>,][VRSTOP10=<VRSTOP10>,][VRSTART11=<VRSTART11>,][VRSTOP11=<VRSTOP11>,][VRSTART12=<VRSTART12>,][VRSTOP12=<VRSTOP12>,][VRSTART13=<VRSTART13>,][VRSTOP13=<VRSTOP13>,][VRSTART14=<VRSTART14>,][VRSTOP14=<VRSTOP14>,][VRSTART15=<VRSTART15>,][VRSTOP15=<VRSTOP15>,][VRSTART16=<VRSTART16>,][VRSTOP16=<VRSTOP16>,][UPBOUS1PSDA=<UPBOUS1PSDA>,][UPBOUS1PSDB=<UPBOUS1PSDB>,][UPBOUS2PSDA=<UPBOUS2PSDA>,][UPBOUS2PSDB=<UPBOUS2PSDB>,][UPBOUS3PSDA=<UPBOUS3PSDA>,][UPBOUS3PSDB=<UPBOUS3PSDB>,][UPBOUS4PSDA=<UPBOUS4PSDA>,][UPBOUS4PSDB=<UPBOUS4PSDB>,][UPBOELELEN=<UPBOELELEN>,][DPBOEPSDBP1TONE=<DPBOEPSDBP1TONE>,][DPBOEPSDBP1PSD=<DPBOEPSDBP1PSD>,][DPBOEPSDBP2TONE=<DPBOEPSDBP2TONE>,][DPBOEPSDBP2PSD=<DPBOEPSDBP2PSD>,][DPBOEPSDBP3TONE=<DPBOEPSDBP3TONE>,][DPBOEPSDBP3PSD=<DPBOEPSDBP3PSD>,][DPBOEPSDBP4TONE=<DPBOEPSDBP4TONE>,][DPBOEPSDBP4PSD=<DPBOEPSDBP4PSD>,][DPBOEPSDBP5TONE=<DPBOEPSDBP5TONE>,][DPBOEPSDBP5PSD=<DPBOEPSDBP5PSD>,][DPBOEPSDBP6TONE=<DPBOEPSDBP6TONE>,][DPBOEPSDBP6PSD=<DPBOEPSDBP6PSD>,][DPBOEPSDBP7TONE=<DPBOEPSDBP7TONE>,][DPBOEPSDBP7PSD=<DPBOEPSDBP7PSD>,][DPBOEPSDBP8TONE=<DPBOEPSDBP8TONE>,][DPBOEPSDBP8PSD=<DPBOEPSDBP8PSD>,][DPBOEPSDBP9TONE=<DPBOEPSDBP9TONE>,][DPBOEPSDBP9PSD=<DPBOEPSDBP9PSD>,][DPBOEPSDBP10TONE=<DPBOEPSDBP10TONE>,][DPBOEPSDBP10PSD=<DPBOEPSDBP10PSD>,][DPBOEPSDBP11TONE=<DPBOEPSDBP11TONE>,][DPBOEPSDBP11PSD=<DPBOEPSDBP11PSD>,][DPBOEPSDBP12TONE=<DPBOEPSDBP12TONE>,][DPBOEPSDBP12PSD=<DPBOEPSDBP12PSD>,][DPBOEPSDBP13TONE=<DPBOEPSDBP13TONE>,][DPBOEPSDBP13PSD=<DPBOEPSDBP13PSD>,][DPBOEPSDBP14TONE=<DPBOEPSDBP14TONE>,][DPBOEPSDBP14PSD=<DPBOEPSDBP14PSD>,][DPBOEPSDBP15TONE=<DPBOEPSDBP15TONE>,][DPBOEPSDBP15PSD=<DPBOEPSDBP15PSD>,][DPBOEPSDBP16TONE=<DPBOEPSDBP16TONE>,][DPBOEPSDBP16PSD=<DPBOEPSDBP16PSD>,][DPBOESEL=<DPBOESEL>,][DPBOESCMA=<DPBOESCMA>,][DPBOESCMB=<DPBOESCMB>,][DPBOESCMC=<DPBOESCMC>,][DPBOMUS=<DPBOMUS>,][DPBOFMIN=<DPBOFMIN>,][DPBOFMAX=<DPBOFMAX>,][PHYRUS=<PHYRUS>,][PHYRDS=<PHYRDS>]]; ```

##### Parameters
Attribute | Description
|---
XdslTmpltAid|DSL Configuration Template Number XdslTmpltAid is the AID DslProfProvAid.
SRVTYPE|This parameter specifies the DSL operating profile that dictates the DSL handshaking protocol, channel capacity, and other physical line characteristics based on DSL specifications. SRVTYPE is of type AdslType.
XDSLLINEPROF|This parameters specifies which of the standard profiles to use. XDSLLINEPROF is of type VdslProfRange.
PKTMODE|Packet mode defines if this port is to operate in packet or ATM VC mode PKTMODE is of type XdslTmpltPktMode.
PTMOVER|This parameter overrides the default encapsulation selection and forces the line to use PTM encapsulation regardless of mode. PTMOVER is of type BoolYN.
FALLBACKVPI|The VPI value to use on the singular VC in packet mode. FALLBACKVPI is of type XdslVPRange.
FALLBACKVCI|The VCI value to use on the singular VC in packet mode. FALLBACKVCI is of type VCRange.
CHNLLAT|The setting for channel path latency. Choosing a latency path of FAST means minimum (4 ms) delay is expected while choosing a latency path of INTLV (interleaved) means more delay. CHNLLAT is of type ChnlSelect0.
XRDS|The maximum downstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRDS is of type DwnStreamRate.
MRDS|This is the minimum downstream rate for the default channel (kbps). MRDS is of type DwnStreamRate.
XRUS|This is the maximum upstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRUS is of type UpStreamRate.
MRUS|This is the minimum upstream rate for the default channel (kbps). MRUS is of type UpStreamRate.
INTLVLATDS|The Downstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATDS is of type Latency.
INTLVLATUS|The upstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATUS is of type Latency.
MININPDS|The Downstream Minimum Impulse Noise Protection Downstream MININPDS is a Integer.
MININPUS|The Upstream Minimum Impulse Noise Protection MININPUS is a Integer.
TMDS|This parameter specifies the desired downstream signal to noise ratio margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMDS is of type SnrTargetMargins.
XMDS|This parameter specifies the maximum downstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-C. XMDS is of type SnrMaxMargins.
MMDS|This parameter specifies the minimum downstream signal to noise ratio margin in dB. This margin specifies the minimum threshold allowed for modem operation. MMDS is of type SnrMinMargins.
TMUS|This parameter specifies the desired upstream signal to noise ratio (SNR) margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMUS is of type SnrTargetMargins.
XMUS|This parameter specifies the maximum upstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-R. XMUS is of type SnrMaxMargins.
MMUS|This parameter specifies the minimum upstream signal to noise ratio (SNR) margin in dB. This margin specifies the minimum threshold allowed for modem training. MMUS is of type SnrMinMargins.
RAMODEDS|The Rate Adaptation Mode for Downstream RAMODEDS is of type RateAdaptationMode.
RAMODEUS|The Rate Adaptation Mode for Upstream RAMODEUS is of type RateAdaptationMode.
RAUMDS|The Rate Adaptation Upshift Margin Downstream in dB. RAUMDS is of type SnrMaxMargins.
RADMDS|The Rate Adaptation Downshift Margin Downstream in dB. RADMDS is of type SnrMaxMargins.
RAUTDS|The Rate Adaptation Upshift Time Downstream in seconds. RAUTDS is of type RateAdaptationMarginSeconds.
RADTDS|The Rate Adaptation Downshift Time Downstream in seconds. RADTDS is of type RateAdaptationMarginSeconds.
RAUMUS|The Rate Adaptation Upshift Margin Upstream in dB. RAUMUS is of type SnrMaxMargins.
RADMUS|The Rate Adaptation Downshift Margin Upstream in dB. RADMUS is of type SnrMaxMargins.
RAUTUS|The Rate Adaptation Upshift Time Upstream in seconds. RAUTUS is of type RateAdaptationMarginSeconds.
RADTUS|The Rate Adaptation Downshift Time Upstream in seconds. RADTUS is of type RateAdaptationMarginSeconds.
PMMODE|Power Management Mode PMMODE is of type AdslPowerMgmtStates.
L0TIME|The Minimum L0 Time interval between L2 exit and next L2 entry. L0TIME is of type MinL0TimeInt.
L2TIME|The Minimum L2 time interval between L2 entry and first L2 trim. L2TIME is of type MinL2TimeInt.
L2ATPR|Maximum Aggregate Transmit Power Reduction per L2 trim in dB. L2ATPR is of type SnrMaxMargins.
L2MINR|The Minimum Data Rate in Low Power Mode specifies the minimum net data rate (in Kbps) during the low power state. L2MINR is of type MinDRInLPM.
L2EXITR|The ADSL2 L2 Exit Rate Threshold specifies the downstream data rate threshold which triggers exit from low power state (L2). L2EXITR is of type AdslL2RateThreshold.
L2ENTRYR|The ADSL2 L2 Entry Rate Threshold specifies the downstream data rate threshold which triggers autonomous entry into low power state (L2). L2ENTRYR is of type AdslL2RateThreshold.
L2ENTRYT|The ADSL2 L2 Entry Time Threshold specifies minimum interval of time that the net data rate should stay below L2ENTRYR before autonomous entry into low power state (L2). L2ENTRYT is of type AdslL2EntTimeThreshold.
GOS|The grade of service identifies the DSL grade of service for performance monitoring (PM) which will be applied to the port. GOS is the AID GosAid.
AHC|Compression of the ATM header results to improve throughput. AHC is of type BoolYN.
EINP|This allows the caller to enable enhanced impulse noise protection. Several technology specific mechanisms are supported. EINP is of type INPType.
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the port. REPTRMVRST is of type BoolYN.
US0PSD|Upstream Power Spectral Density Mask. US0PSD is of type US0PSD.
VNSTART1|The beginning frequency for the first band to skip. Value range for this parameter is [0-65535]kHz. VNSTART1 is of type RfiBand.
VNSTOP1|The ending frequency for the first band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP1 is of type RfiBand.
VNSTART2|The beginning frequency for the second band to skip. Value range for this parameter is [0-65535]kHz. VNSTART2 is of type RfiBand.
VNSTOP2|The ending frequency for the second band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP2 is of type RfiBand.
VNSTART3|The beginning frequency for the third band to skip. Value range for this parameter is [0-65535]kHz. VNSTART3 is of type RfiBand.
VNSTOP3|The ending frequency for the third band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP3 is of type RfiBand.
VNSTART4|The beginning frequency for the fourth band to skip. Value range for this parameter is [0-65535]kHz. VNSTART4 is of type RfiBand.
VNSTOP4|The ending frequency for the fourth band to skip. Value range for this parameter is [0-65535]kHz. VNSTOP4 is of type RfiBand.
VRSTART1|The beginning frequency for the first low power band. Value range for this parameter is [0-65535]kHz. VRSTART1 is of type RfiBand.
VRSTOP1|The ending frequency for the first low power band. Value range for this parameter is [0-65535]kHz. VRSTOP1 is of type RfiBand.
VRSTART2|The beginning frequency for the second low power band. Value range for this parameter is [0-65535]kHz. VRSTART2 is of type RfiBand.
VRSTOP2|The ending frequency for the second low power band. Value range for this parameter is [0-65535]kHz. VRSTOP2 is of type RfiBand.
VRSTART3|The beginning frequency for the third low power band. Value range for this parameter is [0-65535]kHz. VRSTART3 is of type RfiBand.
VRSTOP3|The ending frequency for the third low power band. Value range for this parameter is [0-65535]kHz. VRSTOP3 is of type RfiBand.
VRSTART4|The beginning frequency for the fourth low power band. Value range for this parameter is [0-65535]kHz. VRSTART4 is of type RfiBand.
VRSTOP4|The ending frequency for the fourth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP4 is of type RfiBand.
VRSTART5|The beginning frequency for the fifth low power band. Value range for this parameter is [0-65535]kHz. VRSTART5 is of type RfiBand.
VRSTOP5|The ending frequency for the fifth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP5 is of type RfiBand.
VRSTART6|The beginning frequency for the sixth low power band. Value range for this parameter is [0-65535]kHz. VRSTART6 is of type RfiBand.
VRSTOP6|The ending frequency for the sixth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP6 is of type RfiBand.
VRSTART7|The beginning frequency for the senventh low power band. Value range for this parameter is [0-65535]kHz. VRSTART7 is of type RfiBand.
VRSTOP7|The ending frequency for the senventh low power band. Value range for this parameter is [0-65535]kHz. VRSTOP7 is of type RfiBand.
VRSTART8|The beginning frequency for the eighth low power band. Value range for this parameter is [0-65535]kHz. VRSTART8 is of type RfiBand.
VRSTOP8|The ending frequency for the eighth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP8 is of type RfiBand.
VRSTART9|The beginning frequency for the ninth low power band. Value range for this parameter is [0-65535]kHz. VRSTART9 is of type RfiBand.
VRSTOP9|The ending frequency for the ninth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP9 is of type RfiBand.
VRSTART10|The beginning frequency for the tenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART10 is of type RfiBand.
VRSTOP10|The ending frequency for the tenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP10 is of type RfiBand.
VRSTART11|The beginning frequency for the eleventh low power band. Value range for this parameter is [0-65535]kHz. VRSTART11 is of type RfiBand.
VRSTOP11|The ending frequency for the eleventh low power band. Value range for this parameter is [0-65535]kHz. VRSTOP11 is of type RfiBand.
VRSTART12|The beginning frequency for the twlfth low power band. Value range for this parameter is [0-65535]kHz. VRSTART12 is of type RfiBand.
VRSTOP12|The ending frequency for the twlfth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP12 is of type RfiBand.
VRSTART13|The beginning frequency for the thirdth low power band. Value range for this parameter is [0-65535]kHz. VRSTART13 is of type RfiBand.
VRSTOP13|The ending frequency for the thirdth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP13 is of type RfiBand.
VRSTART14|The beginning frequency for the fourteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART14 is of type RfiBand.
VRSTOP14|The ending frequency for the fourteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP14 is of type RfiBand.
VRSTART15|The beginning frequency for the fifteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART15 is of type RfiBand.
VRSTOP15|The ending frequency for the fifteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP15 is of type RfiBand.
VRSTART16|The beginning frequency for the sixteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTART16 is of type RfiBand.
VRSTOP16|The ending frequency for the sixteenth low power band. Value range for this parameter is [0-65535]kHz. VRSTOP16 is of type RfiBand.
UPBOUS1PSDA|Upstream power back off reference PSD parameter A for US1. UPBOUS1PSDA is of type PsdA. The default value is "4000".
UPBOUS1PSDB|Upstream power back off reference PSD parameter B for US1. UPBOUS1PSDB is of type PsdB. The default value is "0".
UPBOUS2PSDA|Upstream power back off reference PSD parameter A for US2. UPBOUS2PSDA is of type PsdA. The default value is "4000".
UPBOUS2PSDB|Upstream power back off reference PSD parameter B for US2. UPBOUS2PSDB is of type PsdB. The default value is "0".
UPBOUS3PSDA|Upstream power back off reference PSD parameter A for US3. UPBOUS3PSDA is of type PsdA. The default value is "4000".
UPBOUS3PSDB|Upstream power back off reference PSD parameter B for US3. UPBOUS3PSDB is of type PsdB. The default value is "0".
UPBOUS4PSDA|Upstream power back off reference PSD parameter A for US4. UPBOUS4PSDA is of type PsdA. The default value is "4000".
UPBOUS4PSDB|Upstream power back off reference PSD parameter B for US4. UPBOUS4PSDB is of type PsdB. The default value is "0".
UPBOELELEN|Upstream power back off electrical length. UPBOELELEN is the AID EleLenAid. The default value is "NOTFORCED".
DPBOEPSDBP1TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, Tone Value. DPBOEPSDBP1TONE is of type Tone. The default value is "32".
DPBOEPSDBP1PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 1, PSD value. The valid range is from -127 to 0. DPBOEPSDBP1PSD is a Integer.
DPBOEPSDBP2TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, Tone Value. DPBOEPSDBP2TONE is of type Tone. The default value is "33".
DPBOEPSDBP2PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 2, PSD value. The valid range is from -127 to 0. DPBOEPSDBP2PSD is a Integer.
DPBOEPSDBP3TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, Tone Value. DPBOEPSDBP3TONE is of type Tone. The default value is "255".
DPBOEPSDBP3PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 3, PSD value. The valid range is from -127 to 0. DPBOEPSDBP3PSD is a Integer.
DPBOEPSDBP4TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, Tone Value. DPBOEPSDBP4TONE is of type Tone. The default value is "376".
DPBOEPSDBP4PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 4, PSD value. The valid range is from -127 to 0. DPBOEPSDBP4PSD is a Integer.
DPBOEPSDBP5TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, Tone Value. DPBOEPSDBP5TONE is of type Tone. The default value is "511".
DPBOEPSDBP5PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 5, PSD value. The valid range is from -127 to 0. DPBOEPSDBP5PSD is a Integer.
DPBOEPSDBP6TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, Tone Value. DPBOEPSDBP6TONE is of type Tone. The default value is "512".
DPBOEPSDBP6PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 6, PSD value. The valid range is from -127 to 0. DPBOEPSDBP6PSD is a Integer.
DPBOEPSDBP7TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, Tone Value. DPBOEPSDBP7TONE is of type Tone. The default value is "0".
DPBOEPSDBP7PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 7, PSD value. The valid range is from -127 to 0. DPBOEPSDBP7PSD is a Integer.
DPBOEPSDBP8TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, Tone Value. DPBOEPSDBP8TONE is of type Tone. The default value is "0".
DPBOEPSDBP8PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 8, PSD value. The valid range is from -127 to 0. DPBOEPSDBP8PSD is a Integer.
DPBOEPSDBP9TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, Tone Value. DPBOEPSDBP9TONE is of type Tone. The default value is "0".
DPBOEPSDBP9PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 9, PSD value. The valid range is from -127 to 0. DPBOEPSDBP9PSD is a Integer.
DPBOEPSDBP10TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, Tone Value. DPBOEPSDBP10TONE is of type Tone. The default value is "0".
DPBOEPSDBP10PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 10, PSD value. The valid range is from -127 to 0. DPBOEPSDBP10PSD is a Integer.
DPBOEPSDBP11TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, Tone Value. DPBOEPSDBP11TONE is of type Tone. The default value is "0".
DPBOEPSDBP11PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 11, PSD value. The valid range is from -127 to 0. DPBOEPSDBP11PSD is a Integer.
DPBOEPSDBP12TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, Tone Value. DPBOEPSDBP12TONE is of type Tone. The default value is "0".
DPBOEPSDBP12PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 12, PSD value. The valid range is from -127 to 0. DPBOEPSDBP12PSD is a Integer.
DPBOEPSDBP13TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, Tone Value. DPBOEPSDBP13TONE is of type Tone. The default value is "0".
DPBOEPSDBP13PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 13, PSD value. The valid range is from -127 to 0. DPBOEPSDBP13PSD is a Integer.
DPBOEPSDBP14TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, Tone Value. DPBOEPSDBP14TONE is of type Tone. The default value is "0".
DPBOEPSDBP14PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 14, PSD value. The valid range is from -127 to 0. DPBOEPSDBP14PSD is a Integer.
DPBOEPSDBP15TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, Tone Value. DPBOEPSDBP15TONE is of type Tone. The default value is "0".
DPBOEPSDBP15PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 15, PSD value. The valid range is from -127 to 0. DPBOEPSDBP15PSD is a Integer.
DPBOEPSDBP16TONE|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, Tone Value. DPBOEPSDBP16TONE is the AID AcsId.
DPBOEPSDBP16PSD|Downstream Power Back Off, Exchange PSD, BreakPoint Number 16, PSD value. The valid range is from -127 to 0. DPBOEPSDBP16PSD is a Integer.
DPBOESEL|Downstream Power Back Off, Exchange-side Electrical Length. The valid range is from 0 to 255. DPBOESEL is a Integer. The default value is "0".
DPBOESCMA|Downstream Power Back Off, Exchange-side Cable Model Parameter A. DPBOESCMA is of type Escm. The default value is "256".
DPBOESCMB|Downstream Power Back Off, Exchange-side Cable Model Parameter B. DPBOESCMB is of type Escm. The default value is "512".
DPBOESCMC|Downstream Power Back Off, Exchange-side Cable Model Parameter C. DPBOESCMC is of type Escm. The default value is "256".
DPBOMUS|Downstream Power Back Off, Minimum Usable PSD Mask. The valid range is from -127 to 0. DPBOMUS is a Integer.
DPBOFMIN|Downstream Power Back Off, Frequency Min. DPBOFMIN is of type Fmin. The default value is "0".
DPBOFMAX|Downstream Power Back Off, Frequency Max. DPBOFmax must be no less than (DPBOFmin+2). DPBOFMAX is of type Fmax. The default value is "511".
PHYRUS|PhyR Upstream. PHYRUS is of type BoolYN. The default value is "N".
PHYRDS|PhyR Downstream. PHYRDS is of type BoolYN. The default value is "N".

##### Syntax: ```ENT-USER-ACL:[TID]::[CTAG]:::IP=<IP>,IPMSK=<IPMSK>; ```

##### Parameters
Attribute | Description
|---
IP|IP Address. The IP address of the Tl1 or iMS client that is allowed to connect to the C7 network. IP is the AID IpAid.
IPMSK|IP Address Mask. The mask to apply to the IP address, allowing for a range of IP addresses to be considered. IPMSK is the AID IpAid.

##### Syntax: ```ENT-USER-SECU:[TID]:<UID>:[CTAG]::<PID>:[[TMPLT=<TMPLT>,][PAGE=<PAGE>,][PCND=<PCND>,][TMOUT=<TMOUT>,][UAPMA=<UAPMA>,][UAPMT=<UAPMT>,][UAPSE=<UAPSE>,][UAPSY=<UAPSY>,][UAPTS=<UAPTS>,][NODEAID=<NODEAID>,][ENTADA=<ENTADA>]]; ```

##### Parameters
Attribute | Description
|---
UID|User Identifier. The user's identifier for session to be cancelled. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination of alphanumeric characters 4 to 10 characters long and is case-sensitive. UID is the AID UserAid.
PID|Initial user's password. The password must conform to the rules provisioned via ED-SYS-SECU. PID is a String.
TMPLT|Security Template. This specifies the security template to be used to provide default values for this command. The values in the template will be over-riden by any parameter values specified in the command. TMPLT is the AID SecuTmpltAid. The default value is "DEFLT".
PAGE|Password Aging Interval. The passward aging interval is expressed in days. An integer less than or equal to 999, typically 45 to 60. At the end of the interval the user is notified that the existing password needs to be changed each time they log in. A value of zero indicates the user's password will never expire. PAGE is of type UserInterval.
PCND|Password ChaNge Days. This parameter specifies the number of days the user has between the time they are first notified that they must change their password and the time their USERID is disabled. When a password is set by the ENT-USER-SECU command, users are notified that they must change their password. They have PCND days to do this. PCND is of type UserInterval.
TMOUT|TiMe OUT. This parameter specifies the number of minutes of inactivity that must pass before their session is automatically logged out. A value of zero indicates that the user's sessions are never to be logged out due to inactivity. TMOUT is of type TimeOut.
UAPMA|User Access Privilege for Memory Administration. This parameter specifies the abilities of a user for executing memory administration commands. UAPMA is of type AcsPrv.
UAPMT|User Access Privilege for MainTenance. This parameter specifies the abilities of a user for executing maintenance commands. UAPMT is of type AcsPrv.
UAPSE|User Access Privilege for SEcurity. This parameter specifies the abilities of a user for executing security commands. UAPSE is of type AcsPrv.
UAPSY|User Access Privilege for SYstem. This parameter specifies the abilities of a user for executing system commands. UAPSY is of type AcsPrv.
UAPTS|User Access Privilege for TeSting. This parameter specifies the abilities of a user for executing testing commands. UAPTS is of type AcsPrv.
NODEAID|Node Access Identifier. This parameter indicates if the AID used in the commands or responses should include the node identifer. If the NODEAID = Y, then the AID values will contain the Node Id (example N6-4-3). If the NODEAID = N, then the AID values will not contain the Node Id (example 4-3). When the user connecting to the C7 is a NMA user, the NODEAID should be set to N (no). NODEAID is of type BoolYN.
ENTADA|This boolean flag determines whether or not the user may perform an ENTer on an object that is in ADA state. ENTADA is of type BoolYN.

##### Syntax: ```ENT-VB:[TID]:<VbAid>:[CTAG]:::[[FWDMODE=<FWDMODE>,][BW=<BW>,][AGETMR=<AGETMR>,][PPPOAIWF=<PPPOAIWF>,][OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VbAid|Virtual Bridge Access Identifier. VbAid is the AID VbAid.
FWDMODE|Deprecated in 6.1 and above. ForWarD MODE. Selects VB switching mode as either Layer 2 Switched Mode or Layer 3 RBE Routed Mode. FWDMODE is of type FwdMode.
BW|Bandwidth - Amount of guaranteed bandwidth allocated (in kbps), per slot, for slot-to-slot intra-bridge traffic BW is a Integer.
AGETMR|The range is 0,300-1000000. AGETMR is a Integer. The default value is "300".
PPPOAIWF|Not supported in release 6.0. PPPOAIWF is of type BoolYN. The default value is "Y".
OPTION82|This parameter is deprecated after release 7.2. The Option-82 type used by the L2 DHCP relay. OPTION82 is of type Option82. The default value is "NONE".
L2RLYMODE|This parameter is deprecated after release 7.2. DHCP L2 Relay Mode. L2RLYMODE is of type DhcpL2RelayMode. The default value is "NONE".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String. The default value is """".

##### Syntax: ```ENT-VBPORT:[TID]:<VbPortAid>:[CTAG]:::[[ENCAP=<ENCAP>,][DOS=<DOS>,][STP=<STP>,][STPCOST=<STPCOST>,][STPPRIO=<STPPRIO>,][PVID=<PVID>,][DIRN=<DIRN>,][STAGTYPE=<STAGTYPE>,][PORTTYPE=<PORTTYPE>,][PINNED=<PINNED>]]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|Virtual Bridge Port Aid - This identifies either physical port or VC endpoint associated with the Virtual Bridge. VbPortAid is the AID VirtualBridgePortId6.
ENCAP|Encapsulation Type. ENCAP is of type EncapType.
DOS|Denial of Service enabled. DOS is of type BoolYN.
STP|Enable/Disable STP on a particular VB Port. STP is of type StpAddr. The default value is "OFF".
STPCOST|Cost of the port participating in STP. This is used to determine the root port. STPCOST is a Integer.
STPPRIO|STP Priority. STP Priority values are in the range 0-240 and in steps of 16. STPPRIO is a Integer. The default value is "128".
PVID|Port Vlan ID. Not supported in release 5.1 PVID is of type VlanTagOrNone.
DIRN|The direction of forwarded traffic. DIRN is of type VbPortDirection.
STAGTYPE|S_TAG ETH Type. This is used to restamp Ethernet Type field for legacy devices on Network side ports. STAGTYPE is of type StagEthType. The default value is "CTAG_8100".
PORTTYPE|Provider Port Type. This is a required parameter. PORTTYPE is of type VbPortType.
PINNED|For logical VBPORTs (used in ENT-CRS-VC), this parameter governs whether the VBPORT endpoint will be automatically deleted upon DLT-CRS-VC. PINNED is of type BoolYN. The default value is "N".

##### Syntax: ```ENT-VCG:[TID]:<IgAid>:[CTAG]:::BWC=<BWC>,[[CAPALMTHR=<CAPALMTHR>,][ECENABLE=<ECENABLE>,][EPCD=<EPCD>,][ECTAIL=<ECTAIL>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The address of the Voice Concentration Group. Note that the VCG is created from the same pool of 15 AIDs as other interface groups (e.g. GR-303). IgAid is the AID IgAid.
BWC|Bandwidth Constraint used to manage AAL2 services in the network. The BWC specified cannot previously exist. The BWC specified here will be created with association to this IG. BWC is the AID BwcAid. BWC is the AID BwcAid.
CAPALMTHR|Capacity Alarm Threshold. The percentage of active call capacity of the VCG at which a capacity alarm should be raised. CAPALMTHR is of type Percentage.
ECENABLE|Echo cancellation enable/disable. A value of "N" will turn off echo cancellation filtering for this interface group regardless of the setting on the equipment and independent of any other IGs that may be using this same equipment. ECENABLE is of type BoolYN. The default value is "N".
EPCD|Echo Path Change Detection. EPCD=Y is only effective when ECCONFIG=SPARSE on the supporting equipement (VGP/VIPR). Enabling EPCD improves the ability to track changes in the echo path, but reduces channel density. EPCD is of type BoolYN. The default value is "N".
ECTAIL|Integer: 64ms to 128ms in steps of 8ms. The maximum echo delay that the echo canceller is able to eliminate. If ECCONFIG=DUAL, increasing ECTAIL may further reduce channel density. If ECCONFIG=SPARSE, increasing ECTAIL does not impact channel density. ECTAIL is a Integer. The default value is "64".
PST|Primary Service State. This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg. The default value is "OOS".
SST|Secondary Service State. The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-VCGLINK:[TID]:<IgAid>:[CTAG]::<LINK>; ```

##### Parameters
Attribute | Description
|---
IgAid|The address of the Voice Concentration Group. IgAid is the AID IgAid.
LINK|LINK is the AID VcglinkId2.

##### Syntax: ```ENT-VEP:[TID]:<VepAid>:[CTAG]:::IGAID=<IGAID>,[[USER=<USER>,][PID=<PID>]],AOR=<AOR>,[[HOSTPROTO=<HOSTPROTO>,][IP=<IP>,][IPMSK=<IPMSK>,][GADDR=<GADDR>,][CWAITEN=<CWAITEN>,][CIDEN=<CIDEN>,][3WCEN=<3WCEN>,][OPX=<OPX>,][ECENABLE=<ECENABLE>,][CALLMODE=<CALLMODE>]],AUTONUM=<AUTONUM>,[[DIALPLAN=<DIALPLAN>,][FQDN=<FQDN>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VepAid|Voice Endpoint AID of POTs port on ONT or C7 Line Unit VepAid is the AID VepAid.
IGAID|Identifies the client IG associated to this subscriber IGAID is the AID IgAid.
USER|SIP subscriber User Name USER is a String.
PID|Password. Password for authorization of the subscriber. PID is a String.
AOR|SIP Address Of Record or TDMGW 303 CRV AID AOR is a String.
HOSTPROTO|Is IP address derived via DHCP or Statically Assigned HOSTPROTO is of type SipT0HostProto. The default value is "GROUP".
IP|Statically assigned IP address associated with the subscriber. IP is the AID IpAid. The default value is "0.0.0.0".
IPMSK|IP Mask of Statically assigned IP address associated with the subscriber. IPMSK is the AID IpAid. The default value is "0.0.0.0".
GADDR|Gateway address. GADDR is the AID IpAid.
CWAITEN|Enable or disable Call waiting feature on this endpoint. Only take effect with UAHOOKFLASHCTRL=Y and this feature must not be enabled on the switch. CWAITEN is of type BoolYN. The default value is "Y".
CIDEN|Enable or disable Caller ID presentation on this endpoint. Only take effect with UAHOOKFLASHCTRL=Y and this feature must not be enabled on the switch. CIDEN is of type BoolYN. The default value is "Y".
3WCEN|Enable or disable Three way calling on this endpoint. Only take effect with UAHOOKFLASHCTRL=Y and this feature must not be enabled on the switch. 3WCEN is of type BoolYN. The default value is "Y".
OPX|Identify this voice endpoint as an Off Premises Extension. OPX is of type BoolYN.
ECENABLE|Enable/Disable Echo Cancellation on subscriber lines. ECENABLE is of type BoolYN. The default value is "Y".
CALLMODE|Enable hotline or warmlinemode of operation. CALLMODE is of type CallMode. The default value is "NORMAL".
AUTONUM|Number to dial in hotline or warmline operation. It is 16 digits followed by option Tn, where n=1..16. AUTONUM is a String.
DIALPLAN|The Dial Plan to be used for digit collection on this voice endpoint. DIALPLAN is the AID DialPlanAid.
FQDN|FQDN. FQDN is a String.
DESC|Desciption. Maximum length is 31 characters. DESC is a String.

##### Syntax: ```ENT-VID-CHAN:[TID]:<IP>:[CTAG]:::[[VP=<VP>,][VC=<VC>,][TRFPROF=<TRFPROF>,][VIDSRCLIST=<VIDSRCLIST>,][INHSRCLIST=<INHSRCLIST>,][IGMPJOINTYPE=<IGMPJOINTYPE>,][TYPE=<TYPE>,][BW=<BW>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP is the AID IpAid.
VP|The VP number associated with the video transport VCs to deliver this channel to the different shelves. This is applicable for AVT Model channels only if ATM video source is present in the VIDSRCLIST. VP is of type VPRange.
VC|The VC number associated with the video transport VCs to deliver this channel to the different shelves. This is applicable for AVT Model channels only if ATM video source is present in the VIDSRCLIST. VC is of type VCRange.
TRFPROF|Traffic Profile. This parameter identifies which Traffic Profile which will be used by the channel. The Traffic Profile specifies the bandwidth parameters. The Traffic Profile must have its APP set to an Application Id of either VIDCHNL or DATACAROUSEL to be used as a channel. This is not applicable for AVT model channels. TRFPROF is the AID AtmTrfProfProvAid.
VIDSRCLIST|Video Source List. This is the list of video sources (video source indexes separated by &)that should receive this channel. This is applicable for AVT Model channels only. VIDSRCLIST is the AID ChanId and is listable. The default value is "NONE".
INHSRCLIST|Inhibit Video Source List. This is the list of video sources (video source indexes separated by &)on which to inhibit discovery of this video channel. This is applicable for AVT Model channels only. INHSRCLIST is the AID ChanId and is listable. The default value is "NONE".
IGMPJOINTYPE|IGMP Join Type. This should be static if any of the video source is ATM. Must be static for EPG/AGGEPG channels. This is applicable for AVT Model channels only. IGMPJOINTYPE is of type IgmpJoinType. The default value is "PROXY".
TYPE|Video Channel Type. This is applicable for AVT Model channels only. TYPE is of type ChannelType. The default value is "VIDCHNL".
BW|Video Channel Bandwidth (in Kbps) including ATM overhead. This is applicable for AVT Model channels only. BW is a Integer. The default value is "4000".
DESC|Channel description. The description can be up to 40 characters in length for VCVT Model channels and upto 31 characters in length for AVT Model Channels. DESC is a String.

##### Syntax: ```ENT-VID-FILTER:[TID]:<VidSrcAid>:[CTAG]:::IP=<IP>,IPMSK=<IPMSK>,[PASS=<PASS>]; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source Index AID. VidSrcAid is the AID VidSrcAid.
IP|IP Address. This is the Multicast IP address of the channel. IP is the AID IpAid.
IPMSK|IP MASK. This is used to indicate whether a range of IP addresses should be included or excluded from Channel auto-detection on the specified video source. IPMSK is the AID IpAid.
PASS|PASS Enable/Disable. This indicates whether a set of IP addresses should be included or excluded from Channel auto-detection on the specified video source. PASS is of type BoolYN. The default value is "Y".

##### Syntax: ```ENT-VID-IRCLOC:[TID]:<VidServAid>:[CTAG]:::IRCAID=<IrcAid>; ```

##### Parameters
Attribute | Description
|---
VidServAid|Video Service Access Identifier. The AID of the Video Service that contains the IRC. VidServAid is the AID VidServAid.
IrcAid|Slot address of the IRC. IrcAid is the AID SlotLuAid.

##### Syntax: ```ENT-VID-SOURCE:[TID]:<VidSrcAid>:[CTAG]:::BW=<BW>,LOC=<LOC>,[[BWC1=<BWC1>,][BWC2=<BWC2>,][DISCOVERY=<DISCOVERY>,][DFLTCHNLBW=<DFLTCHNLBW>,][DISCOVERDFLT=<DISCOVERDFLT>,][MINBWTHRESH=<MINBWTHRESH>,][MAXBWTHRESH=<MAXBWTHRESH>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source Index AID. Upto 20 Video Sources are allowed in a network. VidSrcAid is the AID VidSrcAid.
BW|Total aggregate bandwidth (in Kbps) reserved for video channels including ATM header. BW is a Integer.
LOC|Video Source Location AID. This is either an ATM or Ethernet video source AID, identifying the Video Ingress. LOC is the AID SourceId.
BWC1|Bandwidth Constraint 1 associated with the video source. BWC1 is the AID BwcIdNone. The default value is "NONE".
BWC2|Bandwidth Constraint 2 associated with the video source. BWC2 is the AID BwcIdNone. The default value is "NONE".
DISCOVERY|Channel DISCOVERY Enable/Disable. Channel Discovery is enabled by default for Ethernet Video Source. This is not applicable for an ATM video source. DISCOVERY is of type BoolYN. The default value is "Y".
DFLTCHNLBW|DeFauLT CHaNneL BandWidth. This is the default channel bandwidth (in Kbps) for channel discovered on an Ethernet video source. This is not applicable for ATM video source. DFLTCHNLBW is a Integer. The default value is "4000".
DISCOVERDFLT|DISCOVER DeFauLT Action. This is the default discovery action for all unfiltered channels discovered on the Ethernet video source. This is not applicable for ATM video source. DISCOVERDFLT is of type ChannelDiscoveryMode. The default value is "PASS".
MINBWTHRESH|MINimum BandWidth THRESHold.Lower Threshold value defined for notification of bandwidth usage (in %) approaching the provisioned BW value. A minor alarm is raised on reaching this BW usage and cleared when the current usage retreats 5% less than this BW usage. Applicable for video GE uplinks only. MINBWTHRESH is of type Percentage. The default value is "85".
MAXBWTHRESH|MAXimum BandWidth THRESHold. Upper Threshold value defined for notification of bandwidth usage (in %) approaching the provisioned BW value. A major alarm is raised on reaching this BW usage and cleared when the current usage retreats 5% less than this BW usage. Applicable for video GE uplinks only. MAXBWTHRESH is of type Percentage. The default value is "95".
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String.

##### Syntax: ```ENT-VID-SUB:[TID]:<VidSubAid>:[CTAG]:::RTRAID=<RTRAID>,[CHANCNT=<CHANCNT>],VIDBW=<VIDBW>,VIDLOANBW=<VIDLOANBW>; ```

##### Parameters
Attribute | Description
|---
VidSubAid|Video Subscriber Access Identifier - The port or channel to which subscribers are connected. Usually an ADSL Channel or ONT (or vdsl in the future) port. VidSubAid is the AID SubId1.
RTRAID|RTRAID - Location of IRC to handle the command RTRAID is the AID SlotLuAid.
CHANCNT|Maximum Channel Count - Number of unique channels flowing to the port. Zero CHANCNT means that the VIDBW and VIDLOANBW values are still used but the subscriber's port will use the global IGMP channel limit when validating channel changes. Setting the CHANCNT to zero is, in effect, turning off the count for that specific port. The valid range is from 0 to 65535. CHANCNT is a Integer.
VIDBW|Video Bandwidth - In Kilobits per second. This value is the maximum Downstream (TX) BW reserved for video on the port. This can be any value but will be rejected if it exceeds the port's trained rate or provisioned rate. VIDBW is a Integer.
VIDLOANBW|Maximum Video Loan Bandwidth - in kbps. Maximum amount of bandwidth to lend back to UBR applications. This value cannot exceed the Max Video BW value. VIDLOANBW is a Integer.

##### Syntax: ```ENT-VID-SVC:[TID]:<VidSvcAid>:[CTAG]:::[[VIDVLANTAG=<VIDVLANTAG>,][MAXVIDBW=<MAXVIDBW>,][DHCPLOCK=<DHCPLOCK>]]; ```

##### Parameters
Attribute | Description
|---
VidSvcAid|Video Service Access Identifier. VidSvcAid is the AID VidSvcAid.
VIDVLANTAG|VIDVLANTAG is of type VlanTagOrNone. The default value is "NONE".
MAXVIDBW|Maximum Video Bandwidth - in kbps. This defines the maximum aggregate video channel bandwidth the proxy will request at any given time. MAXVIDBW is a Integer. The default value is "0".
DHCPLOCK|Enable or disable device mobility. When set to "Y", restrict mobility by allowing a DHCP host to obtain an IP address only once for a specific VLAN port. DHCPLOCK is of type BoolYN. The default value is "N".

##### Syntax: ```ENT-VLAN:[TID]:<VlanAid>:[CTAG]:::[[APPMODE=<APPMODE>,][OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>,][NUMPRIO=<NUMPRIO>,][IGMPMODE=<IGMPMODE>,][STBRLYARP=<STBRLYARP>,][DHCPLOCK=<DHCPLOCK>,][MFF=<MFF>,][RMTIDOPT=<RMTIDOPT>,][DESC=<DESC>]]; ```

##### Parameters
Attribute | Description
|---
VlanAid|VLAN Access Identifier. VlanAid is the AID VlanId.
APPMODE|APPMODE is of type AppMode.
OPTION82|The Option-82 type used by the L2 DHCP relay. OPTION82 is of type Option82. The default value is "NONE".
L2RLYMODE|DHCP L2 Relay Mode. L2RLYMODE is of type DhcpL2RelayMode. The default value is "NONE".
NUMPRIO|VLAN Number Priority. NUMPRIO is of type NumPrioRange. The default value is "1".
IGMPMODE|Determines if IGMP snoop is enabled. This parameter only applies to release 7.2 and above. IGMPMODE is of type VlanIgmpMode. The default value is "NONE".
STBRLYARP|STBRLYARP is of type BoolYN. The default value is "N".
DHCPLOCK|DHCPLOCK is of type BoolYN. The default value is "Y".
MFF|MFF is of type BoolYN. The default value is "N".
RMTIDOPT|RMTIDOPT is of type RmtIdOpt. The default value is "DESC".
DESC|User Description, up to 31 characters. DESC is a String. The default value is """".

##### Syntax: ```ENT-VLAN-IF:[TID]:<IfAid>:[CTAG]:::VLAN=<VLAN>,[[BRIDGE=<BRIDGE>,][TMPLT=<TMPLT>,][RXETHBWPROF=<RXETHBWPROF>,][TXETHBWPROF=<TXETHBWPROF>,][ARP=<ARP>,][DHCPDIR=<DHCPDIR>,][OPT82ACT=<OPT82ACT>,][IGMP=<IGMP>,][PPPOEAC=<PPPOEAC>,][PPPOESUB=<PPPOESUB>,][LSVID=<LSVID>,][ENCAP=<ENCAP>,][DOS=<DOS>,][DFLTROUTE=<DFLTROUTE>,][STP=<STP>,][STPCOST=<STPCOST>,][STPPRIO=<STPPRIO>,][DIRN=<DIRN>,][STAGTYPE=<STAGTYPE>,][PORTTYPE=<PORTTYPE>,][PC=<PC>,][TRFPROF=<TRFPROF>,][BCKPROF=<BCKPROF>,][PATH=<PATH>,][BWC=<BWC>,][MCASTPROF=<MCASTPROF>,][CVID=<CVID>,][PRIO=<PRIO>,][RCVID=<RCVID>,][TAGGING=<TAGGING>,][LEASELMT=<LEASELMT>,][MATCHLIST=<MATCHLIST>,][ACSPROF=<ACSPROF>,][PPPOEUN=<PPPOEUN>,][PPPOEPW=<PPPOEPW>,][IPADDR=<IPADDR>,][IPMASK=<IPMASK>,][IPGW=<IPGW>,][PRIDNS=<PRIDNS>,][SECDNS=<SECDNS>]]; ```

##### Parameters
Attribute | Description
|---
IfAid|Interface Access Identifier. IfAid is the AID IfId11.
VLAN|Packet VLAN Access Identifier. Only VLAN number AID is allowed since R7.0. VLAN is the AID IfId1.
BRIDGE|VB Access Identifier. BRIDGE is the AID IfId8.
TMPLT|VLANIF Template. Any parameters specified in the command would override those specified in TMPLT. TMPLT is the AID VlanIfTmpltAid.
RXETHBWPROF|Receive Ethernet Bandwidth Profile. This parameter indicates the bandwidth profile that will be used for recieved traffic on the EtherPoint.If no RXETHBWPROF is specified, then the service on the EtherPoint is symmetrical and the specified TXETHBWPROF is applied to both directions. RXETHBWPROF is the AID IfId.
TXETHBWPROF|Transmit Ethernet Bandwidth Profile. This parameter indicates the bandwidth profile that will be used for transmit traffic on the EtherPoint.If no TXETHBWPROF is specified, then the service on the EtherPoint is symmetrical and the specified RXETHBWPROF is applied to both directions. TXETHBWPROF is the AID IfId.
ARP|Enable/Disable ARP. ARP is of type BoolYN.
DHCPDIR|DHCP Directionality. This defines if the Vlan VB Port faces a DHCP-Client, DHCP-Server or no DHCP hosts. DHCPDIR is of type DhcpDirection.
OPT82ACT|The action to take if a DHCP packet is received on a Client facing interface with Option82 sub-option 1 /2 content. OPT82ACT is of type Option82Action.
IGMP|IGMP TYPE: a) SINK b) NONE. IGMP is of type IgmpType.
PPPOEAC|Enable/Disable PPPOE Access Concentrator. PPPOEAC is of type BoolYN.
PPPOESUB|Enable/Disable PPPoE Subscriber. PPPOESUB is of type BoolYN.
LSVID|Translated S-VID as seen on wire. Only valid for Provider-side ports. LSVID is of type VlanTag.
ENCAP|Encapsulation Type. ENCAP is of type EncapType.
DOS|Enable/Disable Denial of Service. DOS is of type BoolYN.
DFLTROUTE|Indicates whether it is the "default" VLAN-IF and would be the owner of the default route. Only applicable for ONT RSG. The default value for DHCP VLAN-IF is N. The default value for PPPoE/STATIC VLAN-IF is Y. Only one RG VLAN-IF can set it to Y. The value cannot be changed from Y->N or N->Y via EDIT operation, operator needs to delete the VLAN-IF and recreate it. DFLTROUTE is of type BoolYN.
STP|Enable/Disbale STP. STP is of type StpAddr. The default value is "OFF".
STPCOST|Cost of the port participating in STP. STPCOST is a Integer.
STPPRIO|STP Priority. STP Priority values are in the range 0-240 and in steps of 16. STPPRIO is a Integer.
DIRN|The direction of forwarded traffic. DIRN is of type VbPortDirection.
STAGTYPE|S_TAG ETH Type.Used to restamp Ethernet Type field for legacy devices on Network-side ports. STAGTYPE is of type StagEthType.
PORTTYPE|Provider Port Type. PORTTYPE is of type VbPortType.
PC|Protection Class - Indicates whether the cross connect is uses Bridged or UnBridged protection. PC is of type ProtClass.
TRFPROF|Traffic Profile. This parameter identifies which Traffic Profile which will be applied to the cross-connect. The Traffic Profile specifies the bandwidth parameters. TRFPROF is the AID TrfId.
BCKPROF|Backward Traffic Profile. This parameter identifies which Traffic Profile applies to the backward direction of the cross-connect. If no BCKPROF is specified, then the service on the cross-connect is symmetrical and the TRFPROF is applied to both directions. BCKPROF is the AID TrfId.
PATH|Path on which to create the cross-connect. PATH is of type Path.
BWC|Bandwidth Constraint. The Bandwidth Constraint used when creating the cross-connect. BWC is the AID BwcAid.
MCASTPROF|MultiCast Vlan profile used by EXA video. This parameter only applies to release 7.2 and above. MCASTPROF is the AID IfId5.
CVID|CVID Registration Access Identifier.DFLT CVID Reg is not allowed for VlanPerService/VlanPerPort/Routed VLAN. CVID is of type CvidTag.
PRIO|802.1q Priority Bits Policy. PRIO is of type PrioBits.
RCVID|Relay C-VID. Used to translate the incoming local C-Tag for tagged frames arriving on this user-side port. DFLT CVID Reg is not allowed for VlanPerService/VlanPerPort/Routed VLAN. RCVID is of type RCVid.
TAGGING|Tagging Properties of the VLAN Port TAGGING is of type Tagging.
LEASELMT|LEASELMT is of type LeaseLimit.
MATCHLIST|MATCHLIST is the AID IfId6.
ACSPROF|The AID of a defined ACS Profile to be applied to this VLAN interface. Only allowed for RG. No other VLAN-IFs on the same RG with this parameter presented. ACSPROF is the AID IfId7.
PPPOEUN|The username to be used for PPPoE authentication by the RG. Up to 31 characters. PPPOEUN is a String.
PPPOEPW|The password to be used for PPPoE authentication by the RG. Only allowed for RG. Up to 25 characters. PPPOEPW is a String.
IPADDR|The static IP address to be used by the host for this VLAN interface. Mutually exclusive with the PPPOEUN and PPPOEPW parameters. Only allowed for RG. IPADDR is the AID IpAid.
IPMASK|The static IP address mask to be used by this VLAN interface. Requires the presence of IPADDR parameter. Only allowed for RG. IPMASK is the AID IpAid.
IPGW|The default Gateway to be used by the static IP address. IPGW is the AID IpAid.
PRIDNS|Primary DNS address if a static WAN interface is configured. Requires the presence of IPADDR parameter. Only allowed for RG. PRIDNS is the AID IpAid.
SECDNS|Secondary DNS address if a static WAN interface is configured. Requires the presence of IPADDR parameter. Only allowed for RG. SECDNS is the AID IpAid.

##### Syntax: ```ENT-VLAN-PORT:[TID]:<VLanPortAid>:[CTAG]:::TRFPROF=<TRFPROF>; ```

##### Parameters
Attribute | Description
|---
VLanPortAid|Virtual LAN Port Access IDentifier. VLanPortAid is the AID VLanPortAid.
TRFPROF|ethernet TRaFfic PROFile TRFPROF is the AID EthProfAid.

##### Syntax: ```ENT-VLAN-VBPORT:[TID]:<VbPortAid>:[CTAG]:::VLAN=<VLAN>,[[ARP=<ARP>,][DHCP=<DHCP>,][DHCPDIR=<DHCPDIR>,][OPT82ACT=<OPT82ACT>,][IGMP=<IGMP>,][PPPOEAC=<PPPOEAC>,][PPPOESUB=<PPPOESUB>,][LSVID=<LSVID>,][PRIO=<PRIO>,][TAGGING=<TAGGING>,][LEASELMT=<LEASELMT>]]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|VbPortAid is the AID VirtualBridgePortId2.
VLAN|VLAN Access Identifier - The number of the VLAN this port is being added to. VLAN is the AID PacketVlanAid.
ARP|Enable/Disable ARP. This parameter will default to "Y" for physical ports (i.e. when VbPortAid=N{1-255}-{1-5}-VB{1-20}-{1-20}-{1-6}) and will default to "N" for cross-connect endpoints (i.e. when VbPortAid=N{1-255}-{1-5}-VB{1-20}-{1-7960}). ARP is of type BoolYN.
DHCP|Not supported in release 6.1 and above.Enable/Disable DHCP DHCP is of type BoolYN. The default value is "Y".
DHCPDIR|DHCP Directionality. This defines if the Vlan VB Port faces a DHCP-Client, DHCP-Server or no DHCP hosts. DHCPDIR is of type DhcpDirection. The default value is "CLIENT".
OPT82ACT|Not supported in release 6.0. The action to take if a DHCP packet is received on a Client facing interface with Option82 sub-option 1 /2 content. OPT82ACT is of type Option82Action. The default value is "NONE".
IGMP|IGMP TYPE: NONE SINK IGMP is of type IgmpType.
PPPOEAC|Enable/Disable PPPoE Access Concentrator. PPPOEAC is of type BoolYN. The default value is "N".
PPPOESUB|Enable/Disable PPPoE Subscriber. PPPOESUB is of type BoolYN. The default value is "N".
LSVID|Translated S-VID as seen on wire. Only valid for Provider-side ports. Will be assigned to the VID of provided VLAN AID if omitted. LSVID is of type VlanTag.
PRIO|Deprecated in 6.1 and above. VLAN Port Priority. PRIO values are in the range 0-7. PRIO is a Integer. The default value is "0".
TAGGING|TAGGING is of type Tagging.
LEASELMT|LEASELMT is of type LeaseLimit.

##### Syntax: ```ENT-VODDSTLU:[TID]:<EqptAid>:[CTAG]:::IRCAID=<IRCAID>,FLOWLMT=<FLOWLMT>,TRFPROF=<TRFPROF>; ```

##### Parameters
Attribute | Description
|---
EqptAid|VOD Destination LU Access Identifier. The address of the VOD Destination Line Unit. EqptAid is the AID EquipmentId3.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid.
FLOWLMT|Flow Limit. The upper bound on the number of VOD flows that can egress through this OLU. For each possible flow, a hidden "VOD Internal Flow VC" is created with source and destination on PP1 of this card. There must be sufficient bandwidth in the shelf to support the specified number of flows. FLOWLMT is a Integer.
TRFPROF|Traffic Profile. The traffic profile used to create hidden "VOD Internal Flow VCs". The Application Id of the specified traffic profile must be VIDSUBCHNL. TRFPROF is the AID AtmTrfProfProvAid.

##### Syntax: ```ENT-VR:[TID]:<VrAid>:[CTAG]:::[DHCPLOCK=<DHCPLOCK>]; ```

##### Parameters
Attribute | Description
|---
VrAid|Virtual Router Aid VrAid is the AID VrAid.
DHCPLOCK|Enable or disable device mobility. When set to "Y", restrict mobility by allowing a DHCP host to obtain an IP address only once for a specific VR. DHCPLOCK is of type BoolYN. The default value is "Y".

##### Syntax: ```ENT-VRP:[TID]:<VrpAid>:[CTAG]:::MODE=<MODE>,[[RATE=<RATE>,][FREQ=<FREQ>,][DQPSK=<DQPSK>,][RAND=<RAND>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
VrpAid|Video Return Path Access Identifier. VrpAid is the AID VrpAid.
MODE|RF Return Path Mode - Control the Mode of the RF-Return being utilized by the ONT. MODE is of type RFReturnMode.
RATE|SCTE 55-2 Data Rate - When MODE equals SCTE 55-2, this parameter controls the upstream rate for the RF-Return signal in kbit/sec. RATE is of type VrpDataRate.
FREQ|When MODE = SCTE55-1, frequency is 8096 to 40160 in step sizes of 192 kHz. When MODE = SCTE55-2 and RATE =256 kbps, frequency is 8000 to 26500 in steps of 256 kHz. When MODE = SCTE55-2 and RATE =1544 kbps, frequency is 8000 to 26500 in steps of 1000 kHz. When MODE = SCTE55-2 and RATE =3088 kbps, frequency is 8000 to 26500 in steps of 2000 kHz FREQ is a Integer.
DQPSK|SCTE55-1 DQSK Mode - When MODE equals CTE55-1, set the DQPSK mode to Default or Alternate Operation. Default value is DFLT. DQPSK is of type DQPSKMode.
RAND|SCTE55-1 Randomizer Pre-Load - When MODE equals SCTE55-1, set the eight bits of the Randomizer pre-Load. Value range is from 00 to FF in hex. Default value is FF. RAND is a String. RAND is a String.
DESC|DESCription. A user-settable description field, up to 31 characters. DESC is a String. The default value is """".
PST|Primary Service State of the VRP - Default value is IS. PST is of type PrimaryStateChg.
SST|Secondary Service State of the VRP. SB is the only allowed provisioned secondary state and only allowed when PST is set to OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-VRPORT:[TID]:<VrPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrPortAid|Virtual Router Port Access Identifier - Port that should be associated with the Virtual Router. VrPortAid is the AID VrEpIdxAid.

##### Syntax: ```ENT-VSP:[TID]:<VspAid>:[CTAG]:::[IP=<IP>],HOSTPROTO=<HOSTPROTO>,UDPSTART=<UDPSTART>:[<PST>]; ```

##### Parameters
Attribute | Description
|---
VspAid|Access Identifier of the VSP. VspAid is the AID VspPortAid.
IP|IP Address for Bearer traffic handled by VSP. IP is the AID IpAid.
HOSTPROTO|Is IP address derived via DHCP or Statically Assigned. The parameter value should be DHCP or STATIC. HOSTPROTO is of type SipHostProto.
UDPSTART|Starting UDP port number for bearer traffic transport handled by VSP. For a VSP on a VIPR/VGP the valid range is 3000-65534. For a VSP on an EGW the valid values are 49408, 53504, 57600, and 61696. UDPSTART is a Integer.
PST|Primary service state - controls whether the VSP is operational PST is of type PrimaryStateChg. The default value is "IS".

##### Syntax: ```ENT-XDSL:[TID]:<XdslAid>:[CTAG]::[<SRVTYPE>]:[[PKTMODE=<PKTMODE>,][CHNLLAT=<CHNLLAT>,][XDSLTEMPLATE=<XDSLTEMPLATE>,][FALLBACKVPI=<FALLBACKVPI>,][FALLBACKVCI=<FALLBACKVCI>,][XDSLLINEPROF=<XDSLLINEPROF>,][XRDS=<XRDS>,][MRDS=<MRDS>,][XRUS=<XRUS>,][MRUS=<MRUS>,][GOS=<GOS>,][MININPDS=<MININPDS>,][MININPUS=<MININPUS>,][INTLVLATDS=<INTLVLATDS>,][INTLVLATUS=<INTLVLATUS>,][TMDS=<TMDS>,][XMDS=<XMDS>,][MMDS=<MMDS>,][TMUS=<TMUS>,][XMUS=<XMUS>,][MMUS=<MMUS>,][REPTRMVRST=<REPTRMVRST>,][DESC=<DESC>]]:[<PST>],[<SST>]; ```

##### Parameters
Attribute | Description
|---
XdslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. XdslAid is the AID TwentyFourPortAid.
SRVTYPE|This parameter specifies the DSL operating profile that dictates the DSL handshaking protocol, channel capacity, and other physical line characteristics based on DSL specifications. SRVTYPE is of type AdslType. The default value is "MM2+/VDSL2MM".
PKTMODE|Packet mode defines if this port is to operate in packet or ATM VC mode. PKTMODE is of type BoolYN. The default value is "Y".
CHNLLAT|The setting for channel path latency. Choosing a latency path of FAST means minimum (4 ms) delay is expected while choosing a latency path of INTLV (interleaved) means more delay. CHNLLAT is of type ChnlSelect0. The default value is "INTLV".
XDSLTEMPLATE|The template contains all the parameters for the DSL line including Advanced Parameters and SVCTYPE. XDSLTEMPLATE is the AID DslProfAid.
FALLBACKVPI|The VPI value to use on the singular VC in packet mode. FALLBACKVPI is of type XdslVPRange. The default value is "0".
FALLBACKVCI|The VCI value to use on the singular VC in packet mode. FALLBACKVCI is of type VCRange. The default value is "35".
XDSLLINEPROF|This parameters specifies which of the standard profiles to use. XDSLLINEPROF is of type VdslProfRange. The default value is "8d".
XRDS|The maximum downstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRDS is of type DwnStreamRate. The default value is "512000".
MRDS|This is the minimum downstream rate for the default channel (kbps). MRDS is of type DwnStreamRate. The default value is "64".
XRUS|This is the maximum upstream rate for the default channel (kbps). The minimum value for Vdsl port is 64Kbps. XRUS is of type UpStreamRate. The default value is "512000".
MRUS|This is the minimum upstream rate for the default channel (kbps). MRUS is of type UpStreamRate. The default value is "64".
GOS|Identifies the DSL grade of service for performance monitoring (PM) which will be applied to the port. GOS is the AID GosAid. The default value is "OFF".
MININPDS|The Downstream Minimum Impulse Noise Protection. MININPDS is of type SymbolProtection. The default value is "0.5".
MININPUS|The Upstream Minimum Impulse Noise Protection. MININPUS is of type SymbolProtection. The default value is "0.5".
INTLVLATDS|The Downstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATDS is of type Latency. The default value is "AUTO".
INTLVLATUS|The upstream delay in data transmission through the XDSL link in milliseconds. The AUTO setting allows the card to pick the most appropriate interleave latency. INTLVLATUS is of type Latency. The default value is "AUTO".
TMDS|This parameter specifies the desired downstream signal to noise ratio margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMDS is of type SnrTargetMargins. The default value is "6".
XMDS|This parameter specifies the maximum downstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-C. XMDS is of type SnrMaxMargins. The default value is "16".
MMDS|This parameter specifies the minimum downstream signal to noise ratio margin in dB. This margin specifies the minimum threshold allowed for modem operation. MMDS is of type SnrMinMargins. The default value is "0".
TMUS|This parameter specifies the desired upstream signal to noise ratio (SNR) margin in dB. This margin specifies how much noise can increase while still achieving a BER of at least 10-7. TMUS is of type SnrTargetMargins. The default value is "6".
XMUS|This parameter specifies the maximum upstream signal to noise ratio (SNR) margin in dB. This margin is a threshold for reducing the transmit power of the ATU-R. XMUS is of type SnrMaxMargins. The default value is "16".
MMUS|This parameter specifies the minimum upstream signal to noise ratio (SNR) margin in dB. This margin specifies the minimum threshold allowed for modem training. MMUS is of type SnrMinMargins. The default value is "0".
REPTRMVRST|This parameter inhibits or enables the reporting of RMV/RST events for the port. REPTRMVRST is of type BoolYN.
DESC|A user-settable description field, up to 31 characters. DESC is a String.
PST|This is the service state which the user wants the entity to transition into. PST is of type PrimaryStateChg.
SST|The only secondary service state which is provisionable is SB. It only applies when the PST is OOS. SST is of type SecondaryStateChgSB.

##### Syntax: ```ENT-XLAN:[TID]:<XLanAid>:[CTAG]:::[[XLANNAME=<XLANNAME>,][XLANBW=<XLANBW>,][TOPO=<TOPO>]]; ```

##### Parameters
Attribute | Description
|---
XLanAid|EXtended LAN Access Identifier. XLanAid is the AID XLanAid.
XLANNAME|EXtended LAN NAME. This field is limited to 31 characters. XLANNAME is a String.
XLANBW|EXtended LAN BandWidth in STS-1. XLANBW is of type XlanBw.
TOPO|Indicates the topology of the Extended LAN. Note the system makes no effort to ensure the specified topology matches the actual XLAN configuration; ``` it is provided for user convenience only. TOPO is of type EthTopo. The default value is "LINEAR".

##### Syntax: ```INH-CMD-RESTR:[TID]::[CTAG]; ```


##### Syntax: ```INH-MSG-ALL:[TID]::[CTAG]::[<NTFCNCDE>]; ```

##### Parameters
Attribute | Description
|---
NTFCNCDE|Notification Code. This parameter identifies the notification code of the alarms which the user wants to inhibit. Alarms of a less severe notification code are also inhibited. NTFCNCDE is of type NotificationInh. The default value is "ALL".

##### Syntax: ```INH-MSG-SECU:[TID]::[CTAG]; ```


##### Syntax: ```INH-STBY-UPGRD:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the automatic upgrade of the standby RAP is to be inhibited. ShelfAid is the AID ShelfAid.

##### Syntax: ```INH-SWDX-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the equipment which is to be inhibited from duplex switching. EqptAid is the AID SlotCsAid.

##### Syntax: ```INH-SWDX-GR303:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|Data Link Access Identifier. The address of the data link which is now allowed to provide protection and which now cannot be switched into. DataLinkSwAid is the AID IgLinkSwAid.

##### Syntax: ```INH-SWDX-T1TG:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|Data Link Access Identifier. The address of the data link which is now allowed to provide protection and which now cannot be switched into. DataLinkSwAid is the AID IgLinkSwAid.

##### Syntax: ```INH-SWTOPROTN-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Protection Access Identifier. The address of the protection equipment unit which is to be inhibited from carrying the load. EqptAid is the AID SlotLuAid.

##### Syntax: ```INH-SWTOWKG-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Working Access Identifier. The address of the working equipment unit which is to be inhibited from carrying the load. EqptAid is the AID SlotLuAid.

##### Syntax: ```INH-USER-SECU:[TID]::[CTAG]::<UIDLIST>; ```

##### Parameters
Attribute | Description
|---
UIDLIST|User Identifier. A list of one or more non-confidential identifier that uniquely identifies the user which will have the session privileges inhibited (separated by &s). UIDLIST is a String.

##### Syntax: ```INIT-ADSL:[TID]:<AdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AdslAid|Asymmetical Digital Subscriber Line Access Identifier. The address of the ADSL port being intialized/retrained. AdslAid is the AID TwentyFourPortLuRngAid and is listable and rangeable.

##### Syntax: ```INIT-CSTAT-SIPT0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0Aid is the AID SipT0PortAid.

##### Syntax: ```INIT-CSTAT-VC:[TID]:<VcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VcAid|Virtual Circuit (VC) Access Identifier. The address of the virtual circuit being intialized/retrained. VcAid is the AID VcId13.

##### Syntax: ```INIT-CSTAT-VEP:[TID]:<VepAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VepAid|VepAid is the AID VepOntAid.

##### Syntax: ```INIT-CSTAT-VP:[TID]:<VpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VpAid|Virtual Path (VP) Access Identifier. The address of the virtual path being intialized/retrained. VpAid is the AID VpAid.

##### Syntax: ```INIT-GW-VOIP:[TID]:<VOIPGWAID>:[CTAG]:::[IGAID=<IGAID>]; ```

##### Parameters
Attribute | Description
|---
VOIPGWAID|AID of the VoIP Gateway. VOIPGWAID is the AID VoIPGWONTAid.
IGAID|Interface Group identifying the type and parameters of the VoIP Gateway. IGAID is the AID IgAid.

##### Syntax: ```INIT-HDSL:[TID]:<HdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port being initialized. HdslAid is the AID SixPortLuRngAid and is listable and rangeable.

##### Syntax: ```INIT-HOST-IP:[TID]:<Aid>:[CTAG]:::[IG=<IG>]; ```

##### Parameters
Attribute | Description
|---
Aid|Aid is the AID IpId and is listable.
IG|IG is the AID IgAid.

##### Syntax: ```INIT-LOG:[TID]:<ShelfAid>:[CTAG]::<LOGNM>; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the log is to be initialized. ShelfAid is the AID ShelfAid.
LOGNM|The name of the log to be initialized. Note that the security log cannot be initialized, per GR-815. LOGNM is of type LogName.

##### Syntax: ```INIT-LSWITCH:[TID]:<LSwitchAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LSwitchAid|Logical Switch Access Identifier. LSwitchAid is the AID LSwitchRngAid and is listable and rangeable.

##### Syntax: ```INIT-ONT-UA:[TID]:<PonRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PonRngAid|The PON Port Access Identifier. PonRngAid is the AID FourPortLuRngAid and is listable and rangeable.

##### Syntax: ```INIT-PWR-ADSL:[TID]:<AdslAid>:[CTAG]::<PMSF>; ```

##### Parameters
Attribute | Description
|---
AdslAid|Asymmetical Digital Subscriber Line Access Identifier. The address of the ADSL port being affected. AdslAid is the AID TwelvePortLuRngAid and is listable and rangeable.
PMSF|Power Mangement State Forced. A value of either L2 or L3 can be provided. PMSF is of type AdslPwrMgmtStatesFrcd.

##### Syntax: ```INIT-PWR-XDSL:[TID]:<DslAid>:[CTAG]::<PMSF>; ```

##### Parameters
Attribute | Description
|---
DslAid|XDSL Access Identifier. The address of the XDSL port being affected. DslAid is the AID DslPortAid and is listable and rangeable.
PMSF|Power Mangement State Forced. PMSF is of type AdslPwrMgmtStatesFrcd.

##### Syntax: ```INIT-REG-<OCN>:[TID]:<OcNAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifier. The address of the OCn Port which is to have the PM registers intialized. OcNAid is the AID FourPortLuAndRapAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-<STSN>:[TID]:<StsAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path which is to have the PM registers intialized. StsAid is the AID StsAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-ADSL:[TID]:<ApAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ADSL Port Access Identifier. The address of the ADSL port which is to have the PM registers intialized. ApAid is the AID TwentyFourPortLuAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-AP:[TID]:<ApAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ATM Resource Port Access Identifier. The address of the ATM Resource port which is to have the PM registers intialized. ApAid is the AID AtmRscPortAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-EC1:[TID]:<Ec1Aid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|Access Identifier. The address of the EC1 Port which is to have the PM registers intialized. Ec1Aid is the AID TwelvePortLuAid.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location.
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-ERPS:[TID]:<ErpsAid>:[CTAG]::,,,,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|Address of the ERPS domain. ErpsAid is the AID ErpsAid.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod. The default value is "ALL".

##### Syntax: ```INIT-REG-ETH:[TID]:<ApAid>:[CTAG]::,,[<LOCN >],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ADSL Port Access Identifier. The address of the ADSL port which is to have the PM registers intialized. ApAid is the AID EthId2.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-GRPXDSL:[TID]:<GroupAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GRPADSL Port Access Identifier. The address of the GRPADSL port which is to have the PM registers intialized. GroupAid is the AID DslGrpAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-HDSL:[TID]:<HdslAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port which is to have the PM registers intialized. HdslAid is the AID SixPortLuAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-IMA:[TID]:<ImaAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. The address of the IMA Group which is to have the PM registers intialized. ImaAid is the AID ImaGrpAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-IMALINK:[TID]:<ImaLinkAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
ImaLinkAid|IMA Link Access Identifier. The address of the IMA Link having the monitored parameter values retrieved. ImaLinkAid is the AID SixPortLuAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-ONT:[TID]:<OntAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
OntAid|ONT Access Identifier. The address of the GPON ONT for which the monitored parameter values are requested. OntAid is the AID OntAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-ONTPORTS:[TID]:<OntAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
OntAid|The AID of the target ONT. OntAid is the AID OntAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-PW:[TID]:<PwAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
PwAid|The AID of the target PW. PwAid is the AID PwAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-T1:[TID]:<Ds1Aid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port which is to have the PM registers intialized. Ds1Aid is the AID TwelvePortLuAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-T3:[TID]:<Ds3Aid>:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port which is to have the PM registers intialized. Ds3Aid is the AID T3Aid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-REG-VIDCHAN:[TID]:<IpAid>:[CTAG]::,,[<LOCN>],,[<TMPER>]:RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
IpAid|IpAid is the AID VidchanId.
LOCN|LOCN is of type Location. The default value is "ALL".
TMPER|TMPER is of type PMPeriod. The default value is "ALL".
RTRAID|RTRAID is the AID SlotLuAid.

##### Syntax: ```INIT-REG-XDSL:[TID]:<XpAid >:[CTAG]::,,[<LOCN>],,[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
XpAid|XDSL Port Access Identifier. The address of the XDSL port which is to have the PM registers intialized. XpAid is the AID TwentyFourPortAid.
LOCN|Location. This parameter indicates whether the near end or far end PM registers should be reset. If parameter is not entered, then the registers for both locations will be initialized. LOCN is of type Location.
TMPER|Time Period. This parameter indicates which of the threshold periods should be reset. If parameter is not entered, then all periods will be initialized. TMPER is of type PMPeriod.

##### Syntax: ```INIT-SIP:[TID]:<Aid>:[CTAG]:::[IG=<IG>]; ```

##### Parameters
Attribute | Description
|---
Aid|Aid is the AID SipId and is listable.
IG|IG is the AID IgAid.

##### Syntax: ```INIT-STAT-CHAN:[TID]:<IP>:[CTAG]:::LOC=<LOC>; ```

##### Parameters
Attribute | Description
|---
IP|Multicast video channel IP address. IP is the AID IpAid.
LOC|Location of the Multicast Channel statistics. LOC is the AID SourceId.

##### Syntax: ```INIT-STAT-DHCPL2RELAY:[TID]:<VlanId>:[CTAG]:::BRIDGE=<BRIDGE>,[L2IFAID=<L2IFAID>]; ```

##### Parameters
Attribute | Description
|---
VlanId|VlanId is the AID PacketVlanRngAid and is listable and rangeable.
BRIDGE|BRIDGE must be LOCAL if L2IFAID is specified. BRIDGE is the AID BridgeProvAid.
L2IFAID|L2IFAID is required if Bridge=Local. This must be the address of an EXA Slot. L2IFAID is the AID SlotLuAid.

##### Syntax: ```INIT-STAT-ERPS:[TID]:<ErpsAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsAid.

##### Syntax: ```INIT-STAT-ETH:[TID]:<EthAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
EthAid|Ethernet or Pseudoport interface identifier. EthAid is the AID EthId10.
INCL|Force flag. This must be supplied if the port is a member of a Link Aggregation Group. INCL is of type BoolYN.

##### Syntax: ```INIT-STAT-IP:[TID]:<PpRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpRngAid|Pseudoport Access Identifier on an IRC or Ge-2p. PpRngAid is the AID Pp1RngAid and is listable and rangeable.

##### Syntax: ```INIT-STAT-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|LinkAggAid is the AID LinkAggAid and is listable.

##### Syntax: ```INIT-STAT-MEP:[TID]:<MEGAID>:[CTAG]:::[MEP=<MEP>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid.
MEP|MEP is the AID LtraceId3.

##### Syntax: ```INIT-STAT-MEPFRAMEDELAY:[TID]:<MEGAID>:[CTAG]:::[MEP=<MEP>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid.
MEP|MEP is the AID LtraceId3.

##### Syntax: ```INIT-STAT-MEPFRAMELOSS:[TID]:<MEPGAID>:[CTAG]:::[MEP=<MEP>]; ```

##### Parameters
Attribute | Description
|---
MEPGAID|MEPGAID is the AID MegAid.
MEP|MEP is the AID LtraceId3.

##### Syntax: ```INIT-STAT-MIP:[TID]:<MEGAID>:[CTAG]:::[MIP=<MIP>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid.
MIP|MIP is the AID OntPortAid.

##### Syntax: ```INIT-STAT-NDP:[TID]:<VlanId>:[CTAG]:::BRIDGE=<BRIDGE>,[L2IFAID=<L2IFAID>]; ```

##### Parameters
Attribute | Description
|---
VlanId|VlanId is the AID PacketVlanRngAid and is listable and rangeable.
BRIDGE|BRIDGE must be LOCAL if L2IFAID is specified. BRIDGE is the AID BridgeProvAid.
L2IFAID|L2IFAID is required if Bridge=Local. This must be the address of an EXA Slot. L2IFAID is the AID SlotLuAid.

##### Syntax: ```INIT-STAT-PPPOA:[TID]:<Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Aid|The target AID may be a Virtual Bridge or VDSL slot. Aid is the AID PppoaId1 and is listable.

##### Syntax: ```INIT-STAT-PPPOE:[TID]:<Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Aid|The target AID may be a Virtual Bridge or VDSL slot. Aid is the AID PppoaId1 and is listable.

##### Syntax: ```INIT-STAT-PPPOEAC:[TID]:<MACAID>:[CTAG]:::SCOPE=<SCOPE>; ```

##### Parameters
Attribute | Description
|---
MACAID|This is the Ethernet Address of the AC as learned from the PPPoE Discovery packet. MACAID is the AID MacRngAid and is listable.
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1.

##### Syntax: ```INIT-STAT-PW:[TID]:<PwAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
PwAid|PW identifier. PwAid is the AID PwAid.

##### Syntax: ```INIT-STAT-SIPT0:[TID]:<T0Aid>:[CTAG]:::[IG=<IG>]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0Aid is the AID Sipt0Id.
IG|Identifies the client IG associated to this subscriber. IG is the AID IgAid.

##### Syntax: ```INIT-STAT-UDP:[TID]:<PpRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpRngAid|Pseudoport Access Identifier on an IRC or Ge-2p. PpRngAid is the AID Pp1RngAid and is listable and rangeable.

##### Syntax: ```INIT-STAT-VEP:[TID]:<VepAid>:[CTAG]:::[IG=<IG>]; ```

##### Parameters
Attribute | Description
|---
VepAid|VepAid is the AID VepId1.
IG|Identifies the client IG associated to this subscriber. IG is the AID IgAid.

##### Syntax: ```INIT-SYS:[TID]:<EqptAid>:[CTAG]::<PH>:[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the Equipment entity being initialized. If a list of AIDs is sepecified, the command will be executed on the equipment in the order that they are listed. Listing the active RAP or the AMP that is executing the command before other equipment will abort the command before the other equipment is initialized. EqptAid is the AID SystemId and is listable.
PH|PH is of type Phase.
INCL|INCLusive. This parameter provides a way for the user to request a forced initialization of each plug in on a shelf. This parameter is required when the command is applied to a card that is in NBK state. INCL is of type BoolYN.

##### Syntax: ```INIT-VEP:[TID]:<Aid>:[CTAG]:::[IG=<IG>]; ```

##### Parameters
Attribute | Description
|---
Aid|Aid is the AID VepId and is listable.
IG|This parameter is deprecated and ignored. IG is the AID IgAid.

##### Syntax: ```INIT-XDSL:[TID]:<DslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DslAid is the AID TwentyFourPortAid.

##### Syntax: ```INJ-LPBK-VC:[TID]:<VcAid>:[CTAG]::<LPBKTYPE>,[<CPID>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
VcAid|Virtual Circuit (VC) Access Identifier. The address of the virtual circuit having a loopback ping inserted. VcAid is the AID VcId4. VcAid must not be null.
LPBKTYPE|Loopback Type. This parameter indicates the type of loopback being requested. LPBKTYPE is of type LpbkVpVc. LPBKTYPE must not be null.
CPID|CPID is the AID ShelfAid. A null value is equivalent to "ALL".
DIRN|DIRN is of type Direction. A null value defaults to "TRMT".

##### Syntax: ```INJ-LPBK-VP:[TID]:<VpAid>:[CTAG]::<LPBKTYPE>,[<CPID>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
VpAid|Virtual Path (VP) Access Identifier. The address of the virtual path having a loopback ping inserted. VpAid is the AID VpAid. VpAid must not be null.
LPBKTYPE|Loopback Type. This parameter indicates the type of loopback being requested. LPBKTYPE is of type LpbkVpVc. LPBKTYPE must not be null.
CPID|CPID is the AID ShelfAid. A null value is equivalent to "ALL".
DIRN|DIRN is of type Direction. A null value defaults to "TRMT".

##### Syntax: ```MV-CRS-VC:[TID]:<SrcVcAid>,<DstVcAid>:[CTAG]:::FROM=<FROM>,TO=<TO>; ```

##### Parameters
Attribute | Description
|---
SrcVcAid|Source VC Access Identifier. This is the source endpoint of an existing cross-connect. SrcVcAid is the AID VcId10.
DstVcAid|Destination VC Access Identifier.Source VC Access Identifier. This is the destination endpoint of an existing cross-connect. DstVcAid is the AID VcId15.
FROM|The endpoint being modified. This must match either the source or destination endpoint. FROM is the AID VcId9.
TO|The new AID for the "FROM" endpoint. Only the VC value is allowed to change. TO is the AID VcId9.

##### Syntax: ```MV-CRS-VP:[TID]:<SrcVpAid>,<DstVpAid>:[CTAG]:::FROM=<FROM>,TO=<TO>; ```

##### Parameters
Attribute | Description
|---
SrcVpAid|Source VC Access Identifier. This is the source endpoint of an existing cross-connect. SrcVpAid is the AID VpAid.
DstVpAid|Destination VP Access Identifier. This is the destination endpoint of an existing cross-connect. DstVpAid is the AID VpAid.
FROM|The endpoint being modified. This must match either the source or destination endpoint. FROM is the AID VpAid.
TO|The new AID for the "FROM" endpoint. Only the VP value is allowed to change. TO is the AID VpAid.

##### Syntax: ```OPR-ACO:[TID]:<NodeAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
NodeAid|Alarm Cutoff Access Identifier. The address of the alarm cutoff being operated. NodeAid is the AID NodeAid.

##### Syntax: ```OPR-BAR:[TID]:<BarAid>:[CTAG]::<BARACT>:[[BARSESS=<BARSESS>,][FTPIP=<FTPIP>,][FTPUID=<FTPUID>,][FTPPID=<FTPPID>,][FTPFILE=<FTPFILE>]]; ```

##### Parameters
Attribute | Description
|---
BarAid|Access ID of the shelf or slot upon which the BAR operation is to be performed. BarAid is the AID ShelfOrSlotAid. BarAid must not be null.
BARACT|BAR Activity Type. BARACT is of type BaRActivity. BARACT must not be null.
BARSESS|BAR Session ID. This parameter is only used when BARACT is CANCEL and it indicates the BAR session to be cancelled. BARSESS is of type BarSession. A null value defaults to "no session".
FTPIP|IP address of the FTP server to which the backup is to be sent/received. FTPIP is the AID IpAid. A null value defaults to "required for Extract/Load".
FTPUID|User Name for login to the FTP server. This field is limited to 31 characters. FTPUID is a String. A null value defaults to "required for Extract/Load".
FTPPID|Password for login to the FTP server. This field is limited to 31 characters. FTPPID is a String. A null value defaults to "required for Extract/Load".
FTPFILE|Filename to use on the FTP server, possibly including a directory structure prefix. This field is limited to 79 characters. FTPFILE is a String. A null value defaults to "required for Extract/Load".

##### Syntax: ```OPR-BERT-T1:[TID]:<Ds1aid>:[CTAG]:::TYPE=<TYPE>,PTRN=<PTRN>; ```

##### Parameters
Attribute | Description
|---
Ds1aid|DS1 Port AID where to start the test. Only DS1 AIDs on DS1-12 PWE and T1-8 PWE are supported. Ds1aid is the AID TwentyFourPortAid.
TYPE|Selects whether the BERT is run on the TERMINAL or FACILITY side. TYPE is of type BertLoopBackType.
PTRN|Patterns to be used. PTRN is of type BertPattern.

##### Syntax: ```OPR-CC-VC:[TID]:<VcAid>:[CTAG]::<CCTYPE>,<CCMODE>; ```

##### Parameters
Attribute | Description
|---
VcAid|Virtual Circuit Access Identifier. The address of the VC for which the continuity will be operated. VcAid is the AID VcId.
CCTYPE|Continuity Check Type This parameter specifies whether the continuity check circuit looks on the INTernal SEGment toward the linecard from the port, on the EXTernalSEGment from the port toward the facility, or END-TO-END. CCTYPE is of type CcType.
CCMODE|Continuity Check Mode. This parameter indicates whether the continuity check circuit is to transmit cells, monitor for cells, or both. CCMODE is of type CcMode and can be one of the following values: "TXRX".

##### Syntax: ```OPR-CC-VP:[TID]:<VpAid>:[CTAG]::<CCTYPE>,<CCMODE>; ```

##### Parameters
Attribute | Description
|---
VpAid|Virtual Path Access Identifier. The address of the VP for which the continuity will be performed. VpAid is the AID VpAid.
CCTYPE|Continuity Check Type This parameter specifies whether the continuity check circuit looks on the INTernal SEGment toward the linecard from the port, on the EXTernalSEGment from the port toward the facility, or END-TO-END. An INVALID parameter releases any continuity check that exists on the VP. CCTYPE is of type CcType.
CCMODE|Continuity Check Mode. This parameter indicates whether the continuity check circuit is to transmit cells, monitor for cells, or both. CCMODE is of type CcMode.

##### Syntax: ```OPR-DEBUG:[TID]:<EqptAid>:[CTAG]:::[[CPU=<CPU>,][TIMEOUT=<TIMEOUT>,][BUFFER=<BUFFER>]],CMD=<CMD>; ```

##### Parameters
Attribute | Description
|---
EqptAid|The Slot number is used for the AID. EqptAid is the AID DebugSlotAid. EqptAid must not be null.
CPU|CPU to which the debug command is targeted. CPU is of type CpuType. A null value defaults to "PPC".
TIMEOUT|subsystem timeout in seconds. TIMEOUT is a Integer. A null value defaults to "60".
BUFFER|By default, TL1 responses are buffered until either the final message is received or until the buffer exceeds 4K. This parameter may be used to force a flush as each response is received. BUFFER is of type BoolYN. A null value defaults to "Y".
CMD|The command to run. CMD is a String. CMD must not be null.

##### Syntax: ```OPR-EXT-CONT:[TID]:<ExtContAid>:[CTAG]::[<DUR>]; ```

##### Parameters
Attribute | Description
|---
ExtContAid|External Control Access Identifier. The address of the external control within the node. ExtContAid is the AID ExtControlAid.
DUR|Duration. This parameter indicate the duration that the external control should be operated. DUR is of type Duration. The default value is "MNTRY".

##### Syntax: ```OPR-LPBK-<OCN>:[TID]:<OcNAid>:[CTAG]::,,,<LPBKTYPE>; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Access Identifier. The address of the OCn line which the loop back will be applied. OcNAid is the AID FourPortLuAndRapAid.
LPBKTYPE|Loop Back Type. This parameter specifies the type of loop back. LPBKTYPE is of type LpbkFacOrTerm.

##### Syntax: ```OPR-LPBK-EC1:[TID]:<Ec1Aid>:[CTAG]::,,,<LPBKTYPE>; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|Access Identifier. The address of the EC1 line which the loop back will be applied. Ec1Aid is the AID TwelvePortLuAid.
LPBKTYPE|Loop Back Type. This parameter specifies the type of loop back. LPBKTYPE is of type LpbkFacTermOrPayload.

##### Syntax: ```OPR-LPBK-EOAM:[TID]:<LPBAID>:[CTAG]:::[[LPBTYPE=<LPBTYPE>,][VLAN=<VLAN>]]; ```

##### Parameters
Attribute | Description
|---
LPBAID|LPBAID is the AID MepId1.
LPBTYPE|LPBTYPE is of type EthOamLpbkType.
VLAN|VLAN is the AID VlanIndexAid.

##### Syntax: ```OPR-LPBK-HDSL:[TID]:<HdslAid>:[CTAG]::[<LOCN>],,,<LPBKTYPE >; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port which the loop back will be applied. HdslAid is the AID SixPortLuAid.
LOCN|Location. This indicates the location at which the loopback is to be applied. LOCN is of type LocationAll. The default value is "NEND".
LPBKTYPE|Loop Back Type. This parameter specifies the type of loop back. LPBKTYPE is of type LpbkFacTermOrPayload.

##### Syntax: ```OPR-LPBK-T1:[TID]:<Ds1Aid>:[CTAG]::,,,<LPBKTYPE>; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port which the loop back will be applied. Ds1Aid is the AID T1Id1.
LPBKTYPE|LPBKTYPE is of type LpbkFacTermOrPayload.

##### Syntax: ```OPR-LPBK-T3:[TID]:<Ds3Aid>:[CTAG]::,,,<LPBKTYPE>; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port which the loop back will be applied. Ds3Aid is the AID T3Aid.
LPBKTYPE|Loop Back Type. This parameter specifies the type of loop back. LPBKTYPE is of type LpbkFacTermOrPayload.

##### Syntax: ```OPR-PROTNSW-<OCN>:[TID]:<OcNAid>:[CTAG]::<SC>; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifier. The address of either the working or the protecting OCn port in a facility protection group which is to be operated. OcNAid is the AID FourPortLuAndRapAid.
SC|Switch Command Priority. Priority of the switch command to be initiated on the entity. SC is of type SwtchCmd.

##### Syntax: ```OPR-PROTNSW-<STSN>:[TID]:<StsAid>:[CTAG]::<SC>; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of either the working or the protecting STS path in a facility protection group which is to be operated. StsAid is the AID StsAid.
SC|Switch Command Priority. Priority of the switch command to be initiated on the entity. SC is of type SwtchCmd.

##### Syntax: ```OPR-PROTNSW-PPL:[TID]:<PplAid>:[CTAG]::<SC>; ```

##### Parameters
Attribute | Description
|---
PplAid|Packet Protection Label Access Identifier. The address of either the working or the protecting PPL which is to be operated. PplAid is the AID PplBrAid.
SC|Switch Command Priority. Priority of the switch command to be initiated on the entity. SC is of type SwtchCmd.

##### Syntax: ```OPR-ROGDTCT:[TID]:<PonAid>:[CTAG]:::[ROGDTCTST=<ROGDTCTST>]; ```

##### Parameters
Attribute | Description
|---
PonAid|PonAid. PonAid is the AID FourPortLuAid.
ROGDTCTST|Enable or disable rogue detection on the associated PON. ROGDTCTST is of type RogDtctState.

##### Syntax: ```OPR-SYNCNSW:[TID]:<TimingAid>:[CTAG]::<SWITCHTO>,<SYNCCMD>; ```

##### Parameters
Attribute | Description
|---
TimingAid|AID of the timing system to be switched. This identifies the shelf and whether the system timing or the DS1 derived timing source is to be changed. TimingAid is the AID TimingAid.
SWITCHTO|Switch To. This parameter identifies the new synchronization reference that will be used. SWITCHTO is of type SwitchTo.
SYNCCMD|Sych Command Priority. Priority of the switch command to be initiated on the entity. SYNCCMD is of type SyncCmd.

##### Syntax: ```PING-IP-HOST:[TID]:<RtrAid>:[CTAG]:::IP=<IP>,[[NPING=<NPING>,][PSIZE=<PSIZE>,][INTERVAL=<INTERVAL>,][TIMEOUT=<TIMEOUT>]]; ```

##### Parameters
Attribute | Description
|---
RtrAid|Access IDentifier of an AMP, IRC, Virtual Router, H.248 IG, or VSP port. RtrAid is the AID HostId2. RtrAid must not be null.
IP|The host IP address. IP is the AID IpAid. IP must not be null.
NPING|The number of ping requests to send. NPING must be between 1 and 100. NPING is a Integer. A null value defaults to "5".
PSIZE|The ICMP data size for each ping packet. This size excludes the size of the ICMP header. PSIZE must be between 0 and 1472 bytes. PSIZE is a Integer. A null value defaults to "64".
INTERVAL|Interval between pings, in milliseconds. INTERVAL must be between 50 and 2000. INTERVAL is a Integer. A null value defaults to "50".
TIMEOUT|The number of milliseconds to wait for a reply. TIMEOUT must be between 500 and 3000. TIMEOUT is a Integer. A null value defaults to "500".

##### Syntax: ```REPT-STAT:[TID]::[CTAG]; ```


##### Syntax: ```RLS-BERT-T1:[TID]:<Ds1Aid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|DS1 Port AID where to start the test. Only DS1 AIDs on DS1-12 PWE and T1-8 PWE are supported. Ds1Aid is the AID TwentyFourPortAid.

##### Syntax: ```RLS-CC-VC:[TID]:<VcAid>:[CTAG]::<CCTYPE>; ```

##### Parameters
Attribute | Description
|---
VcAid|Virtual Circuit Access Identifier. The address of the VC for which the continuity check will be released. VcAid is the AID VcId.
CCTYPE|Continuity Check Type This parameter specifies whether the continuity check to be deleted looks on the INTernal SEGment toward the linecard from the port, on the EXTernalSEGment from the port toward the facility, or END-TO-END. CCTYPE is of type CcType.

##### Syntax: ```RLS-CC-VP:[TID]:<VpAid>:[CTAG]::<CCTYPE>; ```

##### Parameters
Attribute | Description
|---
VpAid|Virtual Path Access Identifier. The address of the VP for which the continuity check will be released. VpAid is the AID VpAid.
CCTYPE|Continuity Check Type This parameter specifies whether the continuity check to be deleted looks on the INTernal SEGment toward the linecard from the port, on the EXTernalSEGment from the port toward the facility, or END-TO-END. An INVALID parameter releases any continuity check that exists on the VP. CCTYPE is of type CcType.

##### Syntax: ```RLS-EXT-CONT:[TID]:<ExtContAid>:[CTAG]::[<DUR>]; ```

##### Parameters
Attribute | Description
|---
ExtContAid|External Control Access Identifier. The address of the external control which is being released. ExtContAid is the AID ExtControlAid.
DUR|Duration. This parameter indicate the duration that the external control should be operated. DUR is of type Duration. The default value is "CONTS".

##### Syntax: ```RLS-LPBK-<OCN>:[TID]:<OcNAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifer. The address of the port to have its loopback released. OcNAid is the AID FourPortLuAndRapAid.

##### Syntax: ```RLS-LPBK-EC1:[TID]:<Ec1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|Access Identifer. The address of the port to have its loopback released. Ec1Aid is the AID TwelvePortLuAid.

##### Syntax: ```RLS-LPBK-EOAM:[TID]:<LPBAID>:[CTAG]:::[LPBTYPE=<LPBTYPE>]; ```

##### Parameters
Attribute | Description
|---
LPBAID|LPBAID is the AID MepId1.
LPBTYPE|LPBTYPE is of type EthOamLpbkType.

##### Syntax: ```RLS-LPBK-HDSL:[TID]:<HdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port for which the loop back will be released. HdslAid is the AID SixPortLuAid.

##### Syntax: ```RLS-LPBK-T1:[TID]:<Ds1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port for which the loop back will be released. Ds1Aid is the AID T1Id1.

##### Syntax: ```RLS-LPBK-T3:[TID]:<Ds3Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port for which the loop back will be released. Ds3Aid is the AID T3Aid.

##### Syntax: ```RLS-PROTNSW-<OCN>:[TID]:<OcNAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Access Identifier. The address of the either the working or the protecting OCn in a facility protection group which is to be released. OcNAid is the AID FourPortLuAndRapAid.

##### Syntax: ```RLS-PROTNSW-<STSN>:[TID]:<StsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the either the working or the protecting STS path in a facility protection group which is to be released. StsAid is the AID StsAid.

##### Syntax: ```RLS-PROTNSW-PPL:[TID]:<PplAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PplAid|Packet Protection Label Access Identifier. The address of the either the working or the protecting PPL in a facility protection group which is to be released. PplAid is the AID PplId1.

##### Syntax: ```RLS-SYNCNSW:[TID]:<TimingAId>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TimingAId|TimingAId is the AID TimingAid.

##### Syntax: ```RMV-<OCN>:[TID]:<OcNAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifer. The address of the OCn port being removed from service. OcNAid is the AID FourPortLuAndRapAid.

##### Syntax: ```RMV-<STSN>:[TID]:<StsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifer. The address of the STS path being removed from service. StsAid is the AID StsAid.

##### Syntax: ```RMV-ADSL:[TID]:<AdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AdslAid|ADSL Port Access Identifer. The address of the ADSL port being removed from service. AdslAid is the AID TwentyFourPortLuAid.

##### Syntax: ```RMV-AP:[TID]:<ApAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid.

##### Syntax: ```RMV-AVO:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Analog Video Overlay Port Access Identifer. The address of the AVO port being removed from service. The port number must be equal to 1. OntPortAid is the AID OntPortAid.

##### Syntax: ```RMV-EC1:[TID]:<Ec1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|EC1 Port Access Identifer. The address of the EC1 port being removed from service. Ec1Aid is the AID TwelvePortLuAid.

##### Syntax: ```RMV-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|ADSL Access Identifer. The address of the equipment being removed from service. EqptAid is the AID EquipmentId.

##### Syntax: ```RMV-ERPS:[TID]:<ErpsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsAid.

##### Syntax: ```RMV-ETH:[TID]:<EthPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Access Identifier. EthPortAid is the AID TwelvePortLuAid.

##### Syntax: ```RMV-GRPXDSL:[TID]:<GroupAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GroupAid is the AID DslGrpAid.

##### Syntax: ```RMV-HDSL:[TID]:<HdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port being removed from service. HdslAid is the AID SixPortLuAid.

##### Syntax: ```RMV-IMA:[TID]:<ImaAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. The address of the IMA Group which is to be removed from service. ImaAid is the AID ImaGrpAid.

##### Syntax: ```RMV-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 12 groups are supported on a single slot, and up to 4 on a single VB. LinkAggAid is the AID LinkAggAid.

##### Syntax: ```RMV-ONT:[TID]:<OntAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntAid|Optical Network Termination Access Identifier. The address of the ONT which is to be removed from service. OntAid is the AID OntAid.

##### Syntax: ```RMV-PON:[TID]:<PonAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PonAid|Passive Optical Network Access Identifier. The address of the ONT which is to be removed from service. PonAid is the AID FourPortLuAid.

##### Syntax: ```RMV-PP:[TID]:<PpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpAid|Pseudo Port Identifier. PpAid is the AID PpAid.

##### Syntax: ```RMV-RFVID:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Rf-Video Port Access Identifer. The address of the RFVID port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortAid.

##### Syntax: ```RMV-T0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Port Access Identifer. The address of the T0 port being removed from service. T0Aid is the AID TwentyFourPortLuAid.

##### Syntax: ```RMV-T1:[TID]:<Ds1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifer. The address of the T1 port being removed from service. Ds1Aid is the AID TwelvePortLuAid.

##### Syntax: ```RMV-T3:[TID]:<Ds3Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifer. The address of the T3 port being removed from service. Ds3Aid is the AID T3Aid.

##### Syntax: ```RMV-XDSL:[TID]:<DslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DslAid is the AID TwentyFourPortAid.

##### Syntax: ```RST-<OCN>:[TID]:<OcNAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifier. The address of the OCn port being restored to service. OcNAid is the AID FourPortLuAndRapAid.

##### Syntax: ```RST-<STSN>:[TID]:<StsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path being restored to service. StsAid is the AID StsAid.

##### Syntax: ```RST-ADSL:[TID]:<AdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AdslAid|ADSL Port Access Identifier. The address of the ADSL port being restored to service. AdslAid is the AID TwentyFourPortLuAid.

##### Syntax: ```RST-AP:[TID]:<ApAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid.

##### Syntax: ```RST-AVO:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Analog Video Overlay Port Access Identifer. The address of the AVO port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortAid.

##### Syntax: ```RST-EC1:[TID]:<Ec1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|EC1 Port Access Identifier. The address of the EC1 port being restored to service. Ec1Aid is the AID TwelvePortLuAid.

##### Syntax: ```RST-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the equipment being restored to service. EqptAid is the AID EquipmentId.

##### Syntax: ```RST-ERPS:[TID]:<ErpsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsAid.

##### Syntax: ```RST-ETH:[TID]:<EthPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Access Identifier. EthPortAid is the AID TwelvePortLuAid.

##### Syntax: ```RST-GRPXDSL:[TID]:<GroupAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GroupAid is the AID DslGrpAid.

##### Syntax: ```RST-HDSL:[TID]:<HdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port being restored to service. HdslAid is the AID SixPortLuAid.

##### Syntax: ```RST-IMA:[TID]:<ImaAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. The address of the IMA Group which is to be restored into service. ImaAid is the AID ImaGrpAid.

##### Syntax: ```RST-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 12 groups are supported on a single slot, and up to 4 on a single VB. LinkAggAid is the AID LinkAggAid.

##### Syntax: ```RST-ONT:[TID]:<OntAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntAid|Optical Network Termination Access Identifier. The address of the ONT which is to be restored to service. OntAid is the AID OntAid.

##### Syntax: ```RST-PON:[TID]:<PonAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PonAid|Passive Optical Network Access Identifier. The address of the PON which is to be restored to service. PonAid is the AID FourPortLuAid.

##### Syntax: ```RST-PP:[TID]:<PpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpAid|Pseudo Port Identifier. PpAid is the AID PpAid.

##### Syntax: ```RST-RFVID:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Rf-Video Port Access Identifer. The address of the RFVID port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortAid.

##### Syntax: ```RST-T0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Port Access Identifier. The address of the T0 port being restored to service. T0Aid is the AID TwentyFourPortLuAid.

##### Syntax: ```RST-T1:[TID]:<Ds1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port being restored to service. Ds1Aid is the AID TwelvePortLuAid.

##### Syntax: ```RST-T3:[TID]:<Ds3Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port being restored to service. Ds3Aid is the AID T3Aid.

##### Syntax: ```RST-XDSL:[TID]:<DslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DslAid is the AID TwentyFourPortAid.

##### Syntax: ```RTRV-<OCN>:[TID]:<OcNAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifier. The address of the OCn port being retrieved. OcNAid is the AID FourPortLuAndRapNtwkRngAid and is listable and rangeable. OcNAid must not be null.

##### Syntax: ```RTRV-<STSN>:[TID]:<StsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path which is being retrieved. StsAid is the AID StsNtwkRngAid and is listable and rangeable. StsAid must not be null.

##### Syntax: ```RTRV-ACO:[TID]:<NodeAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
NodeAid|Alarm Cutoff Access Identifier. The address of the alarm cutoff being retrieved. NodeAid is the AID NodeId and is listable and rangeable. NodeAid must not be null.

##### Syntax: ```RTRV-ADSL:[TID]:<AdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AdslAid|ADSL Port Access Identifier. The address of the ADSL port being retrieved. AdslAid is the AID TwentyFourPortLuNtwkRngAid and is listable and rangeable. AdslAid must not be null.

##### Syntax: ```RTRV-ALM-<OCN>:[TID]:<OcNAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifier. The address of the OCn port which may have an outstanding alarm. OcNAid is the AID FourPortLuAndRapRngAid and is listable and rangeable. OcNAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeOcN. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-<STSN>:[TID]:<StsAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path which may have an outstanding alarm. StsAid is the AID StsRngAid and is listable and rangeable. StsAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeStsAlm. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-ADSL:[TID]:<AdslAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
AdslAid|ADSL Port Access Identifier. The address of the ADSL port which may have an outstanding alarm. AdslAid is the AID TwentyFourPortLuRngAid and is listable and rangeable. AdslAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the condition type of the alarm. Where a condition type is a trouble conditions, irregularity or error conditions respectively. CONDTYPE is of type CondTypeDsl. A null value is equivalent to "ALL".
SRVEFF|SeRVice EFFect. This parameter identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|LOCatioN. This parameter identifies the location associated with a particular alarm. This parameter is currently ignored. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-ALL:[TID]:<AllAlarmAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],; ```

##### Parameters
Attribute | Description
|---
AllAlarmAid|All Access Identifier. The address of any entity within the system which may have an outstanding alarm. AllAlarmAid is the AID AllAlarmAid and is listable and rangeable. AllAlarmAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeAll. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type LocationAll. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-AP:[TID]:<ApAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID ApId and is listable and rangeable. ApAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypeAp. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-AVO:[TID]:<OntPortAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|AVO Port Access Identifier. The address of the AVO port which may have an outstanding alarm. OntPortAid is the AID OntPortRngAid and is listable and rangeable. OntPortAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the condition type of the alarm. Where a condition type is a trouble conditions, irregularity or error conditions respectively. CONDTYPE is of type CondTypeAvo. A null value is equivalent to "ALL".
SRVEFF|SeRVice EFFect. This parameter identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-BWCLINK:[TID]:<LinkBwcAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
LinkBwcAid|Access Identifier. The address of the Link Bandwidth Constraint which may have an outstanding alarm. LinkBwcAid is the AID LinkBwcRngAid and is listable and rangeable. LinkBwcAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeBwcLink. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-EC1:[TID]:<Ec1Aid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|Access Identifier. The address of the EC1 port which may have an outstanding alarm. Ec1Aid is the AID TwelvePortLuRngAid and is listable and rangeable. Ec1Aid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeOcN. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-ENV:[TID]:<EnvAid>:[CTAG]::[<NTFCNCDE>],[<ALMTYPE>]; ```

##### Parameters
Attribute | Description
|---
EnvAid|Environmental Access Identifier. The address of the environmental input contact within the system which may have an outstanding alarm. EnvAid is the AID EnvRngAid and is listable and rangeable. EnvAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
ALMTYPE|Alarm Type. This parameter is used to filter the response based on the alarm type. ALMTYPE is of type CondTypeEnvAlm. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-EQPT:[TID]:<EqptAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],,; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the equipment which may have an outstanding alarm. EqptAid is the AID EquipmentId1 and is listable and rangeable. EqptAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeEqpt. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-ERPS:[TID]:<ErpsAid >:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsId. ErpsAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeErpsDomain. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-ETH:[TID]:<EthAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
EthAid|Ethernet Access Identifier. EthAid is the AID TwelvePortLuRngAid and is listable and rangeable. EthAid must not be null.
NTFCNCDE|Notification Code. This parameter identifies the notification code of the event that caused the condition to be reported. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeEth. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-GR303:[TID]:<DataLinkSwAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|GR303 Data Link Access Identifier. The address of the GR303 EOC/TMC data links which may have an outstanding alarm. DataLinkSwAid is the AID IgLinkSwRngAid and is listable and rangeable. DataLinkSwAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeIg. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the effect on service associated with the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-GRPXDSL:[TID]:<GroupAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GroupAid is the AID GrpdslId and is listable and rangeable. GroupAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypeDsl. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-H248:[TID]:<IgAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The target H248 IG(s). IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeH248. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-HDSL:[TID]:<HdslAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port which may have an outstanding alarm. HdslAid is the AID SixPortLuRngAid and is listable and rangeable. HdslAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeHdsl. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|LOCatioN. This parameter identifies the location associated with a particular alarm. This parameter is currently ignored. LOCN is of type LocationAll. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-IMA:[TID]:<ImaAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. The address of the IMA group which may have an outstanding alarm. ImaAid is the AID ImaRngAid and is listable and rangeable. ImaAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeIma. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-IMALINK:[TID]:<ImaLinkAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
ImaLinkAid|IMA Link Access Identifier. The address of the IMA link which may have an outstanding alarm. ImaLinkAid is the AID SixPortLuRngAid and is listable and rangeable. ImaLinkAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeImaLink. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-LAG:[TID]:<LinkAggAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 12 groups are supported on a single slot, and up to 4 on a single VB. LinkAggAid is the AID LagId and is listable and rangeable. LinkAggAid must not be null.
NTFCNCDE|This is a filter defining the notification code of interest. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|This is a filter defining the condition type of interest. CONDTYPE is of type CondTypeLag. A null value is equivalent to "ALL".
SRVEFF|This is a filter defining the service effect of interest. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-LSWPORT:[TID]:<LSwitchPortAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
LSwitchPortAid|LSwitch Access Identifier. The address of the LSwitch which may have an outstanding alarm. LSwitchPortAid is the AID LSwitchPortRngAid. LSwitchPortAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeLSwitch. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-ONT:[TID]:<OntAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
OntAid|ONT Access Identifier. OntAid is the AID OntRngAid and is listable and rangeable. OntAid must not be null.
NTFCNCDE|Notification Code. This parameter indicates the notification code associated with the alarm condition. NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter indicates the type of alarm condition. CONDTYPE is of type CondTypeOnt. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the effect on service associated with the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-PON:[TID]:<PonAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
PonAid|The Access Identifier of a PON port. PonAid is the AID FourPortLuRngAid and is listable and rangeable. PonAid must not be null.
NTFCNCDE|Notification Code. This parameter indicates the notification code associated with the alarm condition. NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter indicates the type of alarm condition. CONDTYPE is of type CondTypePon. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the effect on service associated with the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-PP:[TID]:<PpAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
PpAid|Pseudo-Port Access Identifier. The address of the pseudo-port which may have an outstanding alarm. PpAid is the AID PpRngAid and is listable and rangeable. PpAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypePp. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-PPL:[TID]:<PplAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
PplAid|Path Protection LayerIdentifier. The address of the STS1 path for which conditions are being retrieved. PplAid is the AID PplId1 and is listable and rangeable. PplAid must not be null.
NTFCNCDE|Notification Code. This parameter indicates the notification code associated with the condition. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypePpl. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-PPPOEHOSTS:[TID]:<RTRAID>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
RTRAID|RTRAID is the AID SlotLuAid and is listable and rangeable. RTRAID must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypePPPoE. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-PW:[TID]:<PwAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
PwAid|PwAid is the AID PwRangeAid and is listable and rangeable. PwAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypePw. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-RFVID:[TID]:<OntPortAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|The Access Identifier of a RFVID port on an ONT. OntPortAid is the AID OntPortRngAid and is listable and rangeable. OntPortAid must not be null.
NTFCNCDE|Notification Code. This parameter indicates the notification code associated with the alarm condition. NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter indicates the type of alarm condition. CONDTYPE is of type CondTypeRfVid. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the effect on service associated with the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-SECU:[TID]:<SecuAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
SecuAid|Security Access Identifier. This will be either a management slot AID or "SYS", representing system-level alarms. SecuAid is the AID SecurityId and is listable. SecuAid must not be null.
NTFCNCDE|Notification Code. This parameter indicates the notification code associated with the condition. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeSecu. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-SHELF:[TID]:<ShelfAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. ShelfAid is the AID ShelfId1. ShelfAid must not be null.
NTFCNCDE|Notification Code. This parameter indicates the notification code associated with the condition. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeShelf. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-SIP:[TID]:<IgAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgAid. IgAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypeSipIg. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-SIPVCG:[TID]:<IgAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgAid. IgAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypeSipVcg. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-T0:[TID]:<Ds0Aid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
Ds0Aid|T0 Port Access Identifier. The address of the T0 port which may have an outstanding alarm. Ds0Aid is the AID TwentyFourPortLuRngAid and is listable and rangeable. Ds0Aid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeT0Alm. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-T1:[TID]:<Ds1Aid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port which may have an outstanding alarm. Ds1Aid is the AID TwelvePortLuRngAid and is listable and rangeable. Ds1Aid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeT1. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-T1TG:[TID]:<DataLinkSwAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|T1TG Data Link Access Identifier. The address of the T1 Transport Group EOC/TMC data links which may have an outstanding alarm. DataLinkSwAid is the AID IgLinkSwRngAid and is listable and rangeable. DataLinkSwAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeIg. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-T3:[TID]:<Ds3Aid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>],[<LOCN>],[<DIRN>]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port which may have an outstanding alarm. Ds3Aid is the AID T3RngAid and is listable and rangeable. Ds3Aid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeT3. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".
LOCN|Location. This parameter is used to filter the response based on the Location of the alarm. Thus, "near end" refers to alarm conditions occurring at the identified entity, and "far end" refers to alarm conditions occurring at a distant entity that is connected to the identified entity. Likewise, LINE[-x] refers to an intermediate point. LOCN is of type Location. A null value is equivalent to "ALL".
DIRN|DIRectioN. This is the direction of the alarm condition and is relative to the entity identified by the AID. This parameter is currently ignored. DIRN is of type Direction. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-TDMGW:[TID]:<IgAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgAid. IgAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypeTdmGw. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-TMG:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the timing is location which may have an outstanding alarm. ShelfAid is the AID ShelfAid. ShelfAid must not be null.

##### Syntax: ```RTRV-ALM-VB:[TID]:<VbAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
VbAid|VbAid is the AID VirtualBridgeId1 and is listable and rangeable. VbAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypeVb. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-VCG:[TID]:<IgAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The AID of the target VCG(s). IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeVcg. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-VIDSOURCE:[TID]:<VidSrcAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source AID. VidSrcAid is the AID SourceId1 and is listable. VidSrcAid must not be null.
NTFCNCDE|Notification Code. This parameter is used to filter the response based on the notification code associated with the alarm conditions. NTFCNCDE is of type NotificationRtrv. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeVidSrc. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-VR:[TID]:<VrAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
VrAid|VrAid is the AID VirtualRouterId and is listable and rangeable. VrAid must not be null.
NTFCNCDE|NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|CONDTYPE is of type CondTypeVr. A null value is equivalent to "ALL".
SRVEFF|SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-VRP:[TID]:<VrpAid>:[CTAG]::[<NTFCNCDE>],[<CONDTYPE>],[<SRVEFF>]; ```

##### Parameters
Attribute | Description
|---
VrpAid|Video Return Path Access Identifier VrpAid is the AID VrpNtwkRngAid and is listable and rangeable. VrpAid must not be null.
NTFCNCDE|Notification Code. This parameter indicates the notification code associated with the alarm condition. NTFCNCDE is of type NotificationAlm. A null value is equivalent to "ALL".
CONDTYPE|Condition Type. This parameter is used to filter the response based on the Condition Type of the alarm, where a Condition Type is the type of alarm condition. CONDTYPE is of type CondTypeVrp. A null value is equivalent to "ALL".
SRVEFF|Service Effect. This parameter is used to filter the response based on the Service Effect of the alarm, where Service Effect identifies the effect on service caused by the alarm condition. SRVEFF is of type ServiceEffect. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ALM-XDSL:[TID]:<DSLAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DSLAID|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DSLAID is the AID TwentyFourPortRngAid. DSLAID must not be null.

##### Syntax: ```RTRV-AP:[TID]:<ApRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ApRngAid|ApRngAid is the AID T1Id and is listable and rangeable. ApRngAid must not be null.

##### Syntax: ```RTRV-ARP:[TID]:<RTRAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
RTRAID|RTRAID is the AID RouterAid. RTRAID must not be null.

##### Syntax: ```RTRV-ATTR-CONT:[TID]:<ExtContAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ExtContAid|External Control Access Identifier. The address of the external control for which attributes are to be retrieved. ExtContAid is the AID ExtControlRngAid and is listable and rangeable. ExtContAid must not be null.

##### Syntax: ```RTRV-ATTR-ENV:[TID]:<EnvAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EnvAid|Environmental Access Identifier. The address of the environmental input contact for which attributes are to be retrieved. EnvAid is the AID EnvRngAid and is listable and rangeable. EnvAid must not be null.

##### Syntax: ```RTRV-ATU:[TID]:<AtuAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AtuAid|ADSL Terminal Unit Access Identifier. The address of the ATU from where the data is retrieved. AtuAid is the AID TermUnitAid and is listable. AtuAid must not be null.

##### Syntax: ```RTRV-AVO:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Analog Video Overlay Port Access Identifer. The address of the AVO port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortNtwkRngAid. OntPortAid must not be null.

##### Syntax: ```RTRV-BAR:[TID]:<BarSessAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
BarSessAid|This AID refers to a BAR session that has been activated with the OPR-BAR command. BarSessAid is of type BarSession. BarSessAid must not be null.

##### Syntax: ```RTRV-BERTSTAT-T1:[TID]:<Ds1Aid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|DS1 Port AID where to start the test. Only DS1 AIDs on DS1-12 PWE and T1-8 PWE are supported. Ds1Aid is the AID TwentyFourPortAid. Ds1Aid must not be null.

##### Syntax: ```RTRV-BW-PROV:[TID]:<EpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EpAid|Endpoint Access Identifier. This identifies the entity for which provisioned bandwidth information is to be retrieved. This command is not supported for physical ports on GE-2P equipment. EpAid is the AID EpRngAid. EpAid must not be null.

##### Syntax: ```RTRV-BWC:[TID]:<BwcAid>:[CTAG]:::[INTERNAL=<INTERNAL>]; ```

##### Parameters
Attribute | Description
|---
BwcAid|Bandwidth Constraint Access Identifier. Identifies the Bandwidth Constraint to be operated upon. BwcAid is the AID BwcRngAid and is listable and rangeable. BwcAid must not be null.
INTERNAL|INTERNAL is of type BwcInternalTypes and is listable. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-BWCLINK:[TID]:<LinkBwcAid>:[CTAG]:::[INTERNAL=<INTERNAL>]; ```

##### Parameters
Attribute | Description
|---
LinkBwcAid|Link Bandwidth Constraint Access Identifier. Identifies the Link Bandwidth Constraint to be operated upon. LinkBwcAid is the AID BwclinkId2 and is listable and rangeable. LinkBwcAid must not be null.
INTERNAL|Internal BWC Type. INTERNAL is of type BwcInternalTypes and is listable. A null value defaults to "NONE".

##### Syntax: ```RTRV-CFG-ONT:[TID]:<CfgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
CfgAid|Aid of ONT configuration file. CfgAid is the AID OntId1. CfgAid must not be null.

##### Syntax: ```RTRV-COND-<OCN>:[TID]:<OcNAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Port Access Identifier. The address of the OCn port for which conditions are being retrieved. OcNAid is the AID FourPortLuAndRapRngAid and is listable and rangeable. OcNAid must not be null.

##### Syntax: ```RTRV-COND-<STSN>:[TID]:<StsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path for which conditions are being retrieved. StsAid is the AID StsRngAid and is listable and rangeable. StsAid must not be null.

##### Syntax: ```RTRV-COND-ACO:[TID]:<NodeAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
NodeAid|Alarm Cutoff Access Identifier. The address of the alarm cutoff for which conditions are being retrieved. NodeAid is the AID NodeAid and is listable. NodeAid must not be null.

##### Syntax: ```RTRV-COND-ADSL:[TID]:<AdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AdslAid|ADSL Port Access Identifier. The address of the ADSL port for which conditions are being retrieved. AdslAid is the AID TwentyFourPortLuRngAid and is listable and rangeable. AdslAid must not be null.

##### Syntax: ```RTRV-COND-AP:[TID]:<ApAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID ApId and is listable and rangeable. ApAid must not be null.

##### Syntax: ```RTRV-COND-BWCLINK:[TID]:<LinkBwcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkBwcAid|Access Identifier. The address of the Link Bandwidth Constraint for which conditions are being retrieved. LinkBwcAid is the AID LinkBwcRngAid and is listable and rangeable. LinkBwcAid must not be null.

##### Syntax: ```RTRV-COND-EC1:[TID]:<Ec1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|Access Identifier. The address of the EC1 port for which conditions are being retrieved. Ec1Aid is the AID TwelvePortLuRngAid and is listable and rangeable. Ec1Aid must not be null.

##### Syntax: ```RTRV-COND-ENV:[TID]:<EnvAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EnvAid|Environmental Access Identifier. The address of the environmental input contact for which conditions are being retrieved. EnvAid is the AID EnvRngAid and is listable and rangeable. EnvAid must not be null.

##### Syntax: ```RTRV-COND-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the equipment for which conditions are being retrieved. EqptAid is the AID EquipmentId1 and is listable and rangeable. EqptAid must not be null.

##### Syntax: ```RTRV-COND-ERPS:[TID]:<ErpsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|ERPS Domain Identifier. ErpsAid is the AID ErpsId and is listable and rangeable. ErpsAid must not be null.

##### Syntax: ```RTRV-COND-ETH:[TID]:<EthAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EthAid|Ethernet Access Identifier. EthAid is the AID TwelvePortLuRngAid and is listable and rangeable. EthAid must not be null.

##### Syntax: ```RTRV-COND-GR303:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|GR303 Data Links Access Identifier. The address of the GR303 EOC/TMC data links for which conditions are being retrieved. DataLinkSwAid is the AID IgLinkSwRngAid and is listable and rangeable. DataLinkSwAid must not be null.

##### Syntax: ```RTRV-COND-GRPXDSL:[TID]:<src>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
src|src is the AID DslGrpAid and is listable. src must not be null.

##### Syntax: ```RTRV-COND-H248:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|The AID of the target H248 IG. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-COND-HDSL:[TID]:<HdslRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslRngAid|HDSL Port Access Identifier. The address of the HDSL port for which conditions are being retrieved. HdslRngAid is the AID SixPortLuRngAid and is listable and rangeable. HdslRngAid must not be null.

##### Syntax: ```RTRV-COND-IMA:[TID]:<ImaAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. The address of the IMA Group for which conditions are being retrieved. ImaAid is the AID ImaRngAid and is listable and rangeable. ImaAid must not be null.

##### Syntax: ```RTRV-COND-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|LAG Identifier. LinkAggAid is the AID LagId and is listable and rangeable. LinkAggAid must not be null.

##### Syntax: ```RTRV-COND-LOG:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the log are located for which conditions are being retrieved. ShelfAid is the AID ShelfAid and is listable and rangeable. ShelfAid must not be null.

##### Syntax: ```RTRV-COND-LSWPORT:[TID]:<LSwitchPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LSwitchPortAid|Logical Switch Port Access Identifier. LSwitchPortAid is the AID LSwitchPortRngAid. LSwitchPortAid must not be null.

##### Syntax: ```RTRV-COND-ONT:[TID]:<OntAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntAid|Access Identifier of an ONT. OntAid is the AID OntRngAid and is listable and rangeable. OntAid must not be null.

##### Syntax: ```RTRV-COND-PON:[TID]:<PonAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PonAid|The Access Identifier of a PON port. PonAid is the AID FourPortLuRngAid and is listable and rangeable. PonAid must not be null.

##### Syntax: ```RTRV-COND-PP:[TID]:<PpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpAid|Pseudo-Port Access Identifier. The address of the pseudo-port for which conditions are being retrieved. PpAid is the AID PpRngAid and is listable and rangeable. PpAid must not be null.

##### Syntax: ```RTRV-COND-PPL:[TID]:<PplAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PplAid|Path Protection LayerIdentifier. The address of the STS1 path for which conditions are being retrieved. PplAid is the AID PplId1 and is listable and rangeable. PplAid must not be null.

##### Syntax: ```RTRV-COND-PW:[TID]:<PwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PwAid|PwAid is the AID PwRangeAid and is listable and rangeable. PwAid must not be null.

##### Syntax: ```RTRV-COND-SECU:[TID]:<SecuAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SecuAid|The condition may be raised on an AMP slot, or against the system. SecuAid is the AID SecurityId and is listable. SecuAid must not be null.

##### Syntax: ```RTRV-COND-SHELF:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. ShelfAid is the AID ShelfAid. ShelfAid must not be null.

##### Syntax: ```RTRV-COND-SIPVCG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-COND-T0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Port Access Identifier. The address of the T0 port for which conditions are being retrieved. T0Aid is the AID TwentyFourPortLuRngAid and is listable and rangeable. T0Aid must not be null.

##### Syntax: ```RTRV-COND-T1:[TID]:<Ds1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port for which conditions are being retrieved. Ds1Aid is the AID TwelvePortLuRngAid and is listable and rangeable. Ds1Aid must not be null.

##### Syntax: ```RTRV-COND-T1TG:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|T1TG Data Links Access Identifier. The address of the T1TG EOC/TMC data links for which conditions are being retrieved. DataLinkSwAid is the AID IgLinkSwRngAid and is listable and rangeable. DataLinkSwAid must not be null.

##### Syntax: ```RTRV-COND-T3:[TID]:<Ds3Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port for which conditions are being retrieved. Ds3Aid is the AID T3RngAid and is listable and rangeable. Ds3Aid must not be null.

##### Syntax: ```RTRV-COND-TDMGW:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgRngAid. IgAid must not be null.

##### Syntax: ```RTRV-COND-TMG:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the timing is located for which conditions are being retrieved. ShelfAid is the AID ShelfAid and is listable and rangeable. ShelfAid must not be null.

##### Syntax: ```RTRV-COND-VCG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Access Identifier of the VCG. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-COND-VRP:[TID]:<VrpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrpAid|Video Return Path Access Identifer. VrpAid is the AID VrpNtwkRngAid and is listable and rangeable. VrpAid must not be null.

##### Syntax: ```RTRV-COND-XDSL:[TID]:<DSLAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DSLAID|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DSLAID is the AID TwentyFourPortRngAid. DSLAID must not be null.

##### Syntax: ```RTRV-CRS-<STSN>:[TID]:<StsAid>:[CTAG]:::[[PATH=<PATH>,][CONSTAT=<CONSTAT>,][HOPS=<HOPS>,][SCOPE=<SCOPE>,][INTERNAL=<INTERNAL>]]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of an STS path which is one of the endpoints in the cross-connect (either full or intermediate). Note: ranging across an entire shelf (N4-5-ALL, for example) is not supported). StsAid is the AID StsCrsRngAid and is listable and rangeable. StsAid must not be null.
PATH|Path. Protection path of the cross-connect being retrieved. PATH is of type Path. A null value is equivalent to "ALL".
CONSTAT|Connection Status. If present in the request, this parameter will limit the retrieval to cross connects having a connection status among those specified. CONSTAT is of type ConnectionStatus and is listable. A null value is equivalent to "ALL".
HOPS|Hops. If set to Y, this parameter indicates that all the intermediate cross-connects between the source and destination endpoints should be returned. If set to N, only the endpoints are shown. HOPS is of type BoolYN. A null value defaults to "N".
SCOPE|Scope of retrieval. This will indicate how far to trace the cross-connect. SCOPE is of type Scope. A null value defaults to "SHELF".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the retrieval of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. A null value defaults to "NONE".

##### Syntax: ```RTRV-CRS-DCC:[TID]:<CrsDccAid>:[CTAG]:::[[PATH=<PATH>,][CONSTAT=<CONSTAT>,][HOPS=<HOPS>,][SCOPE=<SCOPE>]]; ```

##### Parameters
Attribute | Description
|---
CrsDccAid|DCC Access Identifier. The address of an SDCC which is one of the endpoints in the cross-connect (either full or intermediate). SDCC denotes a section DCC. LDCC denotes a line DCC. LDCC(1-3) denotes one byte in the line DCC overhead CrsDccAid is the AID DccRngAid and is listable and rangeable. CrsDccAid must not be null.
PATH|Path. Protection path of the cross-connect being retrieved. PATH is of type Path. A null value is equivalent to "ALL".
CONSTAT|Connection Status. If present in the request, this parameter will limit the retrieval to cross connects having a connection status among those specified. CONSTAT is of type ConnectionStatus and is listable. A null value is equivalent to "ALL".
HOPS|Hops. If set to Y, this parameter indicates that all the intermediate cross-connects between the source and destination endpoints should be returned. If set to N, only the endpoints are shown. HOPS is of type BoolYN. A null value defaults to "N".
SCOPE|Scope of retrieval. This will indicate how far to trace the cross-connect. SCOPE is of type Scope. A null value defaults to "SHELF".

##### Syntax: ```RTRV-CRS-T0:[TID]:<Ds0Aid>:[CTAG]:::[IGS=<IGS>]; ```

##### Parameters
Attribute | Description
|---
Ds0Aid|DS0 Access Identifier. The address of a DS0 facility which is one of the endpoints in the cross-connect. Ds0Aid is the AID CrsT0RngAid and is listable and rangeable. Ds0Aid must not be null.
IGS|Interface GroupS. This parameter specifies whether the TDM transport interface groups through which the connection passes should be listed. IGS is of type BoolYN. A null value defaults to "N".

##### Syntax: ```RTRV-CRS-T1:[TID]:<Ds1Aid>:[CTAG]::[]:[[PATH=<PATH>,][BWC=<BWC>,][APP=<APP>,][CONSTAT=<CONSTAT>,][HOPS=<HOPS>,][SCOPE=<SCOPE>,][INTERNAL=<INTERNAL>]]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Access Identifier. The address of an T1 facility which is one of the endpoints in the cross-connect (either full or intermediate). Note: ranging across an entire shelf (N4-5-ALL, for example) is not supported). Ds1Aid is the AID T1CrsRngAid and is listable and rangeable. Ds1Aid must not be null.
PATH|Path. Protection path of the cross-connect being retrieved. PATH is of type Path. A null value is equivalent to "ALL".
BWC|Bandwidth Constraint. If present in the request, this parameter will limit the retrieval to cross connects using a bandwidth constraint among those specified. BWC is the AID BwcAid and is listable. A null value is equivalent to "ALL".
APP|Application Id. If present in the request, this parameter will limit the retrieval to cross connects using a traffic profile having an Application Id among those specified. APP is of type ApplicationId and is listable. A null value is equivalent to "ALL".
CONSTAT|Connection Status. If present in the request, this parameter will limit the retrieval to cross connects having a connection status among those specified. CONSTAT is of type ConnectionStatus and is listable. A null value is equivalent to "ALL".
HOPS|Hops. If set to Y, this parameter indicates that all the intermediate cross-connects between the source and destination endpoints should be returned. If set to N, only the endpoints are shown. HOPS is of type BoolYN. A null value defaults to "N".
SCOPE|Scope of retrieval. This will indicate how far to trace the cross-connect. SCOPE is of type Scope. A null value defaults to "SHELF".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the retrieval of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. A null value defaults to "NONE".

##### Syntax: ```RTRV-CRS-VC:[TID]:<VcAid>:[CTAG]::[]:[[TRFPROF=<TRFPROF>,][BCKPROF=<BCKPROF>,][PATH=<PATH>,][PC=<PC>,][BWC=<BWC>,][APP=<APP>,][CONSTAT=<CONSTAT>,][PPL=<PPL>,][PPLORIGIN=<PPLORIGIN>,][HOPS=<HOPS>,][SCOPE=<SCOPE>,][INTERNAL=<INTERNAL>]]; ```

##### Parameters
Attribute | Description
|---
VcAid|Virtual Circuit (VC) Access Identifier. The address of any point along the connection to be retrieved. It need not be just an endpoint Note: ranging across an entire shelf (N4-5-ALL, for example) is not currently supported). VcAid is the AID VcId8 and is listable and rangeable. VcAid must not be null.
TRFPROF|Traffic Profile. If present in the request, this parameter will limit the retrieval to cross connects using a traffic profile among those specified. TRFPROF is the AID TrfId and is listable. A null value is equivalent to "ALL".
BCKPROF|Backward Traffic Profile. If present in the request, this parameter will limit the retrieval to cross connects using a backward traffic profile among those specified. BCKPROF is the AID TrfId and is listable. A null value is equivalent to "ALL".
PATH|Path. Protection path of the cross-connect being retrieved. PATH is of type Path. A null value is equivalent to "ALL".
PC|Protection Class. If present in the request, this parameter will limit the retrieval to cross connects matching the requested Class. PC is of type ProtClass and is listable. A null value is equivalent to "ALL".
BWC|Bandwidth Constraint. If present in the request, this parameter will limit the retrieval to cross connects using a bandwidth constraint among those specified. BWC is the AID BwcAid and is listable. A null value is equivalent to "ALL".
APP|Application Id. If present in the request, this parameter will limit the retrieval to cross connects using a traffic profile having an Application Id among those specified. APP is of type ApplicationId and is listable. A null value is equivalent to "ALL".
CONSTAT|Connection Status. If present in the request, this parameter will limit the retrieval to cross connects having a connection status among those specified. CONSTAT is of type ConnectionStatus and is listable. A null value is equivalent to "ALL".
PPL|Path Protection Label. If present in the request, this parameter will limit the retrieval to cross connects with a PPL among those specified. PPL is the AID PplId1 and is listable. A null value is equivalent to "ALL".
PPLORIGIN|Path Protection Label Origination Shelf. If present in the request, this parameter will limit the retrieval to cross connects with a PPL originating on the given shelves. PPLORIGIN is the AID ShelfAid and is listable. A null value is equivalent to "ALL".
HOPS|Hops. If set to Y, this parameter indicates that all the intermediate cross-connects between the source and destination endpoints should be returned. If set to N, only the endpoints are shown. HOPS is of type BoolYN. A null value defaults to "N".
SCOPE|Scope of retrieval. This will indicate how far to trace the cross-connect. SCOPE is of type Scope. A null value defaults to "SHELF".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the retrieval of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. A null value defaults to "NONE".

##### Syntax: ```RTRV-CRS-VIDVC:[TID]:<VcAid>:[CTAG]:::IRCAID=<IrcAid>,[[TRFPROF=<TRFPROF>,][BCKPROF=<BCKPROF>,][PATH=<PATH>,][BWC=<BWC>,][APP=<APP>,][CONSTAT=<CONSTAT>,][INTERNAL=<INTERNAL>,][IP=<IP>]]; ```

##### Parameters
Attribute | Description
|---
VcAid|Virtual Circuit (VC) Access Identifier. The address of a terminating endpoint of the cross-connect to be retrieved. VcAid is the AID VidvcId4 and is listable and rangeable. VcAid must not be null.
IrcAid|The slot addres of the IRC. IrcAid is the AID SlotLuAid. IrcAid must not be null.
TRFPROF|Traffic Profile. If present in the request, this parameter will limit the retrieval to cross connects using a traffic profile among those specified. TRFPROF is the AID TrfId and is listable. A null value is equivalent to "ALL".
BCKPROF|Backward Traffic Profile. If present in the request, this parameter will limit the retrieval to cross connects using a backward traffic profile among those specified. BCKPROF is the AID TrfId and is listable. A null value is equivalent to "ALL".
PATH|Path. Protection path of the cross-connect being retrieved. PATH is of type Path. A null value is equivalent to "ALL".
BWC|Bandwidth Constraint. If present in the request, this parameter will limit the retrieval to cross connects using a bandwidth constraint among those specified. BWC is the AID BwcAid and is listable. A null value is equivalent to "ALL".
APP|Application Id. If present in the request, this parameter will limit the retrieval to cross connects using a traffic profile having an Application Id among those specified. APP is of type ApplicationId and is listable. A null value is equivalent to "ALL".
CONSTAT|Connection Status. If present in the request, this parameter will limit the retrieval to cross connects having a connection status among those specified. CONSTAT is of type ConnectionStatus and is listable. A null value is equivalent to "ALL".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the retrieval of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. A null value defaults to "NONE".
IP|IP Address. If present in the request, this parameter will limit the retrieval to cross connects using an IP Address among those specified. IP is the AID IpAid and is listable. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-CRS-VP:[TID]:<VpAid>:[CTAG]::[]:[[TRFPROF=<TRFPROF>,][BCKPROF=<BCKPROF>,][PATH=<PATH>,][PC=<PC>,][BWC=<BWC>,][APP=<APP>,][CONSTAT=<CONSTAT>,][PPL=<PPL>,][PPLORIGIN=<PPLORIGIN>,][HOPS=<HOPS>,][SCOPE=<SCOPE>,][INTERNAL=<INTERNAL>]]; ```

##### Parameters
Attribute | Description
|---
VpAid|Virtual Path (VP) Access Identifier. The address of an virtual path which is one of the endpoints in the cross-connect (either full or intermediate). Note: ranging across an entire shelf (N4-5-ALL, for example) is not supported). VpAid is the AID VpRngAid and is listable and rangeable. VpAid must not be null.
TRFPROF|Traffic Profile. If present in the request, this parameter will limit the retrieval to cross connects using a traffic profile among those specified. TRFPROF is the AID TrfId and is listable. A null value is equivalent to "ALL".
BCKPROF|Backward Traffic Profile. If present in the request, this parameter will limit the retrieval to cross connects using a backward traffic profile among those specified. BCKPROF is the AID TrfId and is listable. A null value is equivalent to "ALL".
PATH|Path. Protection path of the cross-connect being retrieved. PATH is of type Path. A null value is equivalent to "ALL".
PC|Protection Class. If present in the request, this parameter will limit the retrieval to cross connects matching the requested Class (Bridged or Unbridged). PC is of type ProtClass and is listable. A null value is equivalent to "ALL".
BWC|Bandwidth Constraint. If present in the request, this parameter will limit the retrieval to cross connects using a bandwidth constraint among those specified. BWC is the AID BwcAid and is listable. A null value is equivalent to "ALL".
APP|Application Id. If present in the request, this parameter will limit the retrieval to cross connects using a traffic profile having an Application Id among those specified. APP is of type ApplicationId and is listable. A null value is equivalent to "ALL".
CONSTAT|Connection Status. If present in the request, this parameter will limit the retrieval to cross connects having a connection status among those specified. CONSTAT is of type ConnectionStatus and is listable. A null value is equivalent to "ALL".
PPL|Path Protection Label. If present in the request, this parameter will limit the retrieval to cross connects with a PPL among those specified. PPL is the AID PplId1 and is listable. A null value is equivalent to "ALL".
PPLORIGIN|Path Protection Label Origination Shelf. If present in the request, this parameter will limit the retrieval to cross connects with a PPL originating on the given shelf. PPLORIGIN is the AID ShelfAid and is listable. A null value is equivalent to "ALL".
HOPS|Hops. If set to Y, this parameter indicates that all the intermediate cross-connects between the source and destination endpoints should be returned. If set to N, only the endpoints are shown. HOPS is of type BoolYN. A null value defaults to "N".
SCOPE|Scope of retrieval. This will indicate how far to trace the cross-connect. SCOPE is of type Scope. A null value defaults to "SHELF".
INTERNAL|Internal Cross Connects. If present, this parameter specifies the retrieval of otherwise hidden cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. A null value defaults to "NONE".

##### Syntax: ```RTRV-CSTAT-ADSL:[TID]:<AdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
AdslAid|ADSL Port Access Identifier. The address of the ADSL port being retrieved. AdslAid is the AID TwentyFourPortLuNtwkRngAid and is listable and rangeable. AdslAid must not be null.

##### Syntax: ```RTRV-CSTAT-ERPS:[TID]:<ErpsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|ErpsAid is the AID ErpsId. ErpsAid must not be null.

##### Syntax: ```RTRV-CSTAT-GRPXDSL:[TID]:<GroupAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GroupAid is the AID DslGrpAid and is listable and rangeable. GroupAid must not be null.

##### Syntax: ```RTRV-CSTAT-HDSL:[TID]:<HdslRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslRngAid|HDSL Port Access Identifier. The address of the HDSL port being retrieved. HdslRngAid is the AID SixPortLuNtwkRngAid and is listable and rangeable. HdslRngAid must not be null.

##### Syntax: ```RTRV-CSTAT-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|LinkAggAid is the AID LagId and is listable and rangeable. LinkAggAid must not be null.

##### Syntax: ```RTRV-CSTAT-SIPT0:[TID]:<SipT0Aid>:[CTAG]:::[SRVST=<SRVST>]; ```

##### Parameters
Attribute | Description
|---
SipT0Aid|The AID of a SIPT0 line. SipT0Aid is the AID SipT0PortRngAid and is listable and rangeable. SipT0Aid must not be null.
SRVST|Server Status. This can be supplied on input to filter the responses. SRVST is of type SipT0ServiceState and is listable. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-CSTAT-T0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Access Identifier. The address of the T0 for which the call status is being retrieved. T0Aid is the AID TwentyFourPortLuAid and is listable and rangeable. T0Aid must not be null.

##### Syntax: ```RTRV-CSTAT-VC:[TID]:<VcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VcAid|Virtual Circuit (VC) Access Identifier. The address of the virtual circuit for which the call statistics are to be retrieved. VcAid is the AID VcId11. VcAid must not be null.

##### Syntax: ```RTRV-CSTAT-VEP:[TID]:<VepAid>:[CTAG]:::[SRVST=<SRVST>]; ```

##### Parameters
Attribute | Description
|---
VepAid|VepAid is the AID VepStatRngAid. VepAid must not be null.
SRVST|Server Status. This can be supplied on input to filter the responses. SRVST is of type SipT0ServiceState and is listable. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-CSTAT-VIRTIF:[TID]:<VIRTIFAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VIRTIFAID|VIRTIFAID is the AID VirtIfRGAid. VIRTIFAID must not be null.

##### Syntax: ```RTRV-CSTAT-VP:[TID]:<VpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VpAid|Virtual Path (VP) Access Identifier. The address of the virtual path for which the call statistics are to be retrieved. VpAid is the AID VpAid. VpAid must not be null.

##### Syntax: ```RTRV-CSTAT-XDSL:[TID]:<DslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DslAid is the AID TwentyFourPortRngAid and is listable and rangeable. DslAid must not be null.

##### Syntax: ```RTRV-CVIDREG:[TID]:<CVidRegAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
CVidRegAid|CVID Registration Table Entry Access Identifier. CVidRegAid is the AID CvidregId and is listable and rangeable. CVidRegAid must not be null.

##### Syntax: ```RTRV-DHCP-LEASE:[TID]:<MACAID>:[CTAG]:::[[RTRAID=<RTRAID>,][IP=<IP>,][VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][SLOT=<SLOT>,][PORT=<PORT>]]; ```

##### Parameters
Attribute | Description
|---
MACAID|MACAID is the AID MacRngAid and is listable and rangeable. MACAID must not be null.
RTRAID|RTRAID is the AID RouterAid. A null value is equivalent to "ALL".
IP|The IP address this host is using. IP is the AID IpAid. A null value is equivalent to "ALL".
VLAN|VLAN is the AID IfId1. A null value is equivalent to "ALL".
BRIDGE|BRIDGE is the AID BridgeProvAid. A null value is equivalent to "ALL".
SLOT|SLOT is the AID SlotLuAid. A null value is equivalent to "ALL".
PORT|The request may be filtered to a specific port. PORT is the AID LeaseId1. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-DHCP-OUI:[TID]:<OUIAID>:[CTAG]:::RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
OUIAID|OUIAID is the AID OuiAidRng. OUIAID must not be null.
RTRAID|RTRAID is the AID SlotLuAid. RTRAID must not be null.

##### Syntax: ```RTRV-DHCPSVR:[TID]:<IP>:[CTAG]:::RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
IP|IP Address of the DHCP Server IP is the AID. IP is the AID IpRngAid and is listable. IP must not be null.
RTRAID|RTRAID is the AID RouterAid. RTRAID must not be null.

##### Syntax: ```RTRV-DLPROF:[TID]:<DLProfileAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DLProfileAid|Data Link Profile Access Identifier. The address of the GR-303 data link profile entity. DLProfileAid is the AID DLProfileAid and is listable. DLProfileAid must not be null.

##### Syntax: ```RTRV-DLSTAT-GR303:[TID]:<IgLinkAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgLinkAid|Data Link Access Identifier. The address of the GR303 interface group or a specific data link within the interface for which the status is to be returned. IgLinkAid is the AID IgLinkRngAid and is listable and rangeable. IgLinkAid must not be null.

##### Syntax: ```RTRV-DLSTAT-T1TG:[TID]:<IgLinkAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgLinkAid|Data Link Access Identifier. The address of the T1 Transport interface group or a specific data link within the interface for which status is being returned. IgLinkAid is the AID IgLinkRngAid and is listable and rangeable. IgLinkAid must not be null.

##### Syntax: ```RTRV-EC1:[TID]:<EcaAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EcaAid|Access Identifier. The address of the EC1 being retrieved. EcaAid is the AID TwelvePortLuNtwkRngAid and is listable and rangeable. EcaAid must not be null.

##### Syntax: ```RTRV-EOAM-CFG:[TID]::[CTAG]:::[DETAILS=<DETAILS>]; ```

##### Parameters
Attribute | Description
|---
DETAILS|DETAILS is of type BoolYN. A null value defaults to "N".

##### Syntax: ```RTRV-EOAM-DRMEP:[TID]:<MEGAID>:[CTAG]:::[[RMEPID=<RMEPID>,][RMACADDR=<RMACADDR>,][LOCALMEP=<LOCALMEP>]]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid. MEGAID must not be null.
RMEPID|RMEPID is of type OneTo8191OrAll. A null value defaults to "ALL".
RMACADDR|RMACADDR is the AID DrmepId1. A null value defaults to "ALL".
LOCALMEP|LOCALMEP is the AID DrmepId2. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-EOAM-FMP:[TID]:<FMPAID>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
FMPAID|FMPAID is the AID EthOamFmpRngAid. FMPAID must not be null.

##### Syntax: ```RTRV-EOAM-LPBK:[TID]:<MEGAID>:[CTAG]:::[SOURCE=<SOURCE>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|The MEG defines the scope of the loopback test. The test will only occur among the MEPS within this MEG. MEGAID is the AID MegAid. MEGAID must not be null.
SOURCE|The endpont to be used as the Loopback source. Can be an explicitly-defined MEP Id, an ONT Ethernet port, or an ONT Gateway. All are in the scope of the MEG. SOURCE is the AID LtraceId3. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-EOAM-LTRACE:[TID]:<MEGAID>:[CTAG]:::[[SOURCE=<SOURCE>,][TRANSID=<TRANSID>,][HISTORY=<HISTORY>]]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid. MEGAID must not be null.
SOURCE|SOURCE is the AID LtraceId3. A null value is equivalent to "ALL".
TRANSID|TRANSID is of type OneTo64K. A null value is equivalent to "ALL".
HISTORY|HISTORY is of type BoolYN. A null value defaults to "N".

##### Syntax: ```RTRV-EOAM-MEG:[TID]:<MEGAID>:[CTAG]:::[[MEGNAME=<MEGNAME>,][VLAN=<VLAN>,][LEVEL=<LEVEL>,][MEGIDFMT=<MEGIDFMT>,][CCMINT=<CCMINT>,][AUTODISC=<AUTODISC>,][AUTODISCTMO=<AUTODISCTMO>,][ALMTIME=<ALMTIME>,][ALMCLRTIME=<ALMCLRTIME>]]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegRngAid. MEGAID must not be null.
MEGNAME|MEGNAME is a String. A null value is equivalent to "ALL".
VLAN|VLAN is the AID VlanIndexAid. A null value is equivalent to "ALL".
LEVEL|LEVEL is of type ZeroTo7. A null value is equivalent to "ALL".
MEGIDFMT|MEGIDFMT is of type BoolYN. A null value is equivalent to "ALL".
CCMINT|CCMINT is of type CcmInterval. A null value is equivalent to "ALL".
AUTODISC|AUTODISC is of type BoolYN. A null value is equivalent to "ALL".
AUTODISCTMO|AUTODISCTMO is of type ThrityFiveTo100. A null value is equivalent to "ALL".
ALMTIME|ALMTIME is of type AlmTimeRng. A null value is equivalent to "ALL".
ALMCLRTIME|ALMCLRTIME is of type AlmClrTimeRng. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-EOAM-MEP:[TID]:<MEPAID>:[CTAG]:::[[IFAID=<IFAID>,][DETAILS=<DETAILS>]]; ```

##### Parameters
Attribute | Description
|---
MEPAID|MEPAID is the AID EthOamMepRngAid. MEPAID must not be null.
IFAID|IFAID is the AID MepId1. A null value is equivalent to "ALL".
DETAILS|DETAILS is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-EOAM-MIP:[TID]:<MIPAID>:[CTAG]:::[MEGAID=<MEGAID>]; ```

##### Parameters
Attribute | Description
|---
MIPAID|MIPAID is the AID OntPortRngAid. MIPAID must not be null.
MEGAID|MEGAID is the AID MegAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-EOAM-RMEP:[TID]:<RMEPAID>:[CTAG]:::[RMEPIDLIST=<RMEPIDLIST>]; ```

##### Parameters
Attribute | Description
|---
RMEPAID|RMEPAID is the AID EthOamMepRngAid. RMEPAID must not be null.
RMEPIDLIST|RMEPIDLIST is of type OneTo8191 and is listable. A null value defaults to "ALL".

##### Syntax: ```RTRV-EQPT:[TID]:<EqptAid>:[CTAG]::[<TYPE>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the equipment being retrieved. EqptAid is the AID EquipmentId7 and is listable and rangeable. EqptAid must not be null.
TYPE|If specified, only retrieve Equipment of the given type(s). TYPE is of type EqptTypeProv and is listable. A null value defaults to "ALL TYPES".

##### Syntax: ```RTRV-ERPS:[TID]:<ErpsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsId1 and is listable and rangeable. ErpsAid must not be null.

##### Syntax: ```RTRV-ETH:[TID]:<EthPortAid>:[CTAG]:::[[AHDISCENABLE=<AHDISCENABLE>,][AHLPBKACCEPT=<AHLPBKACCEPT>]]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Access Identifier. EthPortAid is the AID TwelvePortLuNtwkRngAid and is listable and rangeable. EthPortAid must not be null.
AHDISCENABLE|AHDISCENABLE is of type BoolYN. A null value is equivalent to "ALL".
AHLPBKACCEPT|AHLPBKACCEPT is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ETH-ACL:[TID]:<EthPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|Ethernet Port Ranging Access Identifier. EthPortAid is the AID TwelvePortLuRngAid and is listable and rangeable. EthPortAid must not be null.

##### Syntax: ```RTRV-EXT-CONT:[TID]:<ExtContAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ExtContAid|External Control Access Identifier. The address of the external control being retrieved. ExtContAid is the AID ExtControlRngAid and is listable and rangeable. ExtContAid must not be null.

##### Syntax: ```RTRV-FFP-<OCN>:[TID]:<OcNAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OcNAid|Port Access Identifier. The address of the working or protection OCn port being retrieved. OcNAid is the AID FourPortLuAndRapNtwkRngAid and is listable and rangeable. OcNAid must not be null.

##### Syntax: ```RTRV-FPACC:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the front panel is connected. ShelfAid is the AID ShelfAid and is listable and rangeable. ShelfAid must not be null.

##### Syntax: ```RTRV-FTP:[TID]:<FTPAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
FTPAID|FTP server AID. FTPAID is the AID FtpId and is listable and rangeable. FTPAID must not be null.

##### Syntax: ```RTRV-GOS-<OCN>:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the OC12 Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service path parameters are to be retrieved. A null value retrieves both. Only one set of section parameters are maintained. They are retrieved in association with the near end. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-<STSN>:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the STS Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service parameters are being retrieved. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-ADSL:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the ADSL Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service parameters are being retrieved. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-AP:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. This parameter indicates whether the near end or far end PM threshold values are being provisioned. LOCN is of type Location. A null value is equivalent to "ALL".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-GOS-EC1:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the EC1 Grade of Service table entry. GosAid is the AID GosAllAid. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-ETH:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. This parameter indicates the location, in reference to the entity identified by the ONT Ethernet Port. (Only NEND is supported.) LOCN is of type Location and can be one of the following values: "NEND". A null value is equivalent to "ALL".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. TMPER is of type PMPeriod. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-GOS-GRPXDSL:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the GRPXDSL Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service parameters are being retrieved. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-HDSL:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the T1 Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service parameters are being retrieved. A null value retrieves both. LOCN is of type Location. A null value defaults to "both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "both".

##### Syntax: ```RTRV-GOS-IMA:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Group Grade of Service table entry. GosAid is the AID GosAllAid. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-IMALINK:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the IMA Link Grade of Service table entry. GosAid is the AID GosAllAid. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-ONT:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|LOCN is of type Location. A null value is equivalent to "ALL".
TMPER|TMPER is of type PMPeriod. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-GOS-PW:[TID]:<GosAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
GosAid|PW Grade of Service Aid pattern. GosAid is the AID GosAllAid. GosAid must not be null.

##### Syntax: ```RTRV-GOS-T1:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the T1 Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service parameters are being retrieved. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-T3:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the T3 Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service parameters are being retrieved. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GOS-XDSL:[TID]:<GosAid>:[CTAG]::[<LOCN>],[<TMPER>]; ```

##### Parameters
Attribute | Description
|---
GosAid|Grade of Service Access Identifier. The address of the XDSL Grade of Service table entry. GosAid is the AID GosAllAid and is listable and rangeable. GosAid must not be null.
LOCN|Location. Indicates whether the near end or far end grade of service parameters are being retrieved. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".

##### Syntax: ```RTRV-GR303:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|GR303 Interface Group Access Identifier. The address of the GR-303 Interface Group being retrieved. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-GR8:[TID]:<SlotIgRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SlotIgRngAid|GR8 Interface Group Access Identifier. The address of the GR-8 Interface Group being retrieved. SlotIgRngAid is the AID SlotIgRngAid. SlotIgRngAid must not be null.

##### Syntax: ```RTRV-GRPXDSL:[TID]:<GroupAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GroupAid|Access Identifier of the Group. GroupAid is the AID GrpdslId1 and is listable and rangeable. GroupAid must not be null.

##### Syntax: ```RTRV-GW-VOIP:[TID]:<VOIPGWAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VOIPGWAID|AID of the VoIP Gateway. VOIPGWAID is the AID VoIPGWONTAid. VOIPGWAID must not be null.

##### Syntax: ```RTRV-H248:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Address of the H.248 IG being retrieved. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-HDR:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-HDSL:[TID]:<HdslAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port being retrieved. HdslAid is the AID SixPortLuNtwkRngAid and is listable and rangeable. HdslAid must not be null.

##### Syntax: ```RTRV-HTU:[TID]:<HtuAid>:[CTAG]::<LOCN>; ```

##### Parameters
Attribute | Description
|---
HtuAid|HDSL Terminal Unit Access Identifier. The address of the HTU from where the data is retrieved. HtuAid is the AID SixPortLuRngAid and is listable and rangeable. HtuAid must not be null.
LOCN|LOCatioN. Near or Far End. LOCN is of type Location. LOCN must not be null.

##### Syntax: ```RTRV-IFCONFIG:[TID]:<IfConfigAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IfConfigAid|Interface Configuration Access Identifier. The address of an interface configuration which is being retrieved IfConfigAid is the AID IfConfigAid and is listable. IfConfigAid must not be null.

##### Syntax: ```RTRV-IG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Interface Group Id IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-IG-CRV:[TID]:<CrvAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
CrvAid|Call Reference Value Access Identifier. The address of the call reference value in a GR303 interface group which is being retrieved. CrvAid is the AID CrvRngAid and is listable and rangeable. CrvAid must not be null.

##### Syntax: ```RTRV-IG-CSHELF:[TID]:<IgAid>:[CTAG]::[<SHELF>]; ```

##### Parameters
Attribute | Description
|---
IgAid|The Interface Group AID. IgAid is the AID IgRngAid. IgAid must not be null.
SHELF|An associated shelf. If omitted, this is interpreted as "all associated shelves". SHELF is the AID ShelfAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-IG-DS1:[TID]:<IgDs1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgDs1Aid|Interface Group DS1 Access Identifier. The address of the DS1 Line Termination in a GR-303 interface group being retrieved. IgDs1Aid is the AID IgDs1RngAid and is listable and rangeable. IgDs1Aid must not be null.

##### Syntax: ```RTRV-IG-VDS1:[TID]:<IgDs1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgDs1Aid|Interface Group DS1 Access Identifier. The address of the DS1 Line Termination in a VCG interface group being retrieved. IgDs1Aid is the AID IgDs1RngAid and is listable and rangeable. IgDs1Aid must not be null.

##### Syntax: ```RTRV-IG-VSP:[TID]:<IgVspAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgVspAid|The address of the VSP Termination in a VCG interface group being retrieved. IgVspAid is the AID VspId and is listable and rangeable. IgVspAid must not be null.

##### Syntax: ```RTRV-IGMP:[TID]:<IrcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IrcAid|IP Route processor Card Access IDentifier. IrcAid is the AID IgmpId and is listable. IrcAid must not be null.

##### Syntax: ```RTRV-IGMP-JOIN:[TID]:<IP>:[CTAG]:::IRCAID=<IRCAID>,[L2IFAID=<L2IFAID>]; ```

##### Parameters
Attribute | Description
|---
IP|IP address of the EPG channel or the Multicast IP address for video. IP is the AID IpRngAid and is listable. IP must not be null.
IRCAID|IRCAID is the AID SlotLuAid. IRCAID must not be null.
L2IFAID|L2IFAID is the AID JoinId. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-IMA:[TID]:<ImaAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA AID. This is the address of the IMA Interface Group that is being created. The slot number of this AID must be that of the T1 lines which are to be included in the group. ImaAid is the AID ImaRngAid and is listable and rangeable. ImaAid must not be null.

##### Syntax: ```RTRV-IP-HOST:[TID]:<IP>:[CTAG]:::[[RTRAID=<RTRAID>,][MAC=<MAC>,][L2IFAID=<L2IFAID>,][VLAN=<VLAN>,][BRIDGE=<BRIDGE>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP is the AID IpRngAid. IP must not be null. IP can be set to "ALL".
RTRAID|RTRAID is the AID RouterAid. A null value defaults to "ALL".
MAC|MAC is the AID MacAid. A null value defaults to "ALL".
L2IFAID|L2IFAID is the AID HostId3. A null value defaults to "ALL".
VLAN|VLAN is the AID IfId1. A null value is equivalent to "ALL".
BRIDGE|BRIDGE is the AID BridgeProvAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-IP-HOSTID:[TID]:<IPHostIdAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
IPHostIdAid|IP HostId AID on 8/12-port line-unit only. IPHostIdAid is the AID IPHostIdRngAid and is listable and rangeable. IPHostIdAid must not be null.

##### Syntax: ```RTRV-IP-IF:[TID]:<IP>:[CTAG]:::[[L2IFAID=<L2IFAID>,][RTRAID=<RTRAID>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP is the AID IpRngAid. IP must not be null. IP can be set to "ALL".
L2IFAID|L2IFAID is the AID IpIfAid. A null value is equivalent to "ALL".
RTRAID|RTRAID is the AID RouterAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-IP-ROUTE:[TID]:<IPMASK>:[CTAG]:::RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
IPMASK|IPMASK is the AID IpMaskAid. IPMASK must not be null.
RTRAID|RTRAID is the AID RouteId. RTRAID must not be null.

##### Syntax: ```RTRV-IPIF-PORT:[TID]:<IP>:[CTAG]:::[INTERFACE=<INTERFACE>],RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
IP|IP Address IP is the AID IpRngAid. IP must not be null.
INTERFACE|Interface to create the association with the IP address. Examples of this interfaces are Virtual Bridge, Virtual Router VC Endpoint and VLAN. INTERFACE is the AID IpIfPortAid. A null value defaults to "ALL".
RTRAID|Router Access Identifier - Address of the Virtual Router. RTRAID is the AID VrAid. RTRAID must not be null.

##### Syntax: ```RTRV-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 12 groups are supported on a single slot, and up to 4 on a single VB. LinkAggAid is the AID LagId1 and is listable and rangeable. LinkAggAid must not be null.

##### Syntax: ```RTRV-LINE-TONES:[TID]:<DslAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
DslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. DslAid is the AID TwentyFourPortRngAid and is listable and rangeable. DslAid must not be null.

##### Syntax: ```RTRV-LINK:[TID]:<DataLinkAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkAid|Data Link Access Identifier. The address of a Data Link within an internal interface within the C7 network which is being retrieved. DataLinkAid is the AID DataLinkRngAid and is listable and rangeable. DataLinkAid must not be null.

##### Syntax: ```RTRV-LOG:[TID]:<LogAid>:[CTAG]::<LOGNM>; ```

##### Parameters
Attribute | Description
|---
LogAid|Log Access Identifier. The address of the log entry to be retrieved. The log index can be a maximum of 500 for the Alarm log, and 300 for other logs. LogAid is the AID LogRngAid. LogAid must not be null.
LOGNM|Log Name. The name of the log being retrieved. LOGNM is of type LogName and can be one of the following values: "ALM". LOGNM must not be null.

##### Syntax: ```RTRV-LSWITCH:[TID]:<LSwitchAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LSwitchAid|Logical Switch Access Identifier. LSwitchAid is the AID LSwitchRngAid and is listable and rangeable. LSwitchAid must not be null.

##### Syntax: ```RTRV-LSWITCH-PORT:[TID]:<LSwitchPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LSwitchPortAid|Logical Switch Port Access Identifier. LSwitchPortAid is the AID LSwitchPortRngAid and is listable and rangeable. LSwitchPortAid must not be null.

##### Syntax: ```RTRV-MACHOST:[TID]:<MACAID>:[CTAG]:::VLAN=<VLAN>,[[BRIDGE=<BRIDGE>,][L2IFAID=<L2IFAID>,][STATIC=<STATIC>]]; ```

##### Parameters
Attribute | Description
|---
MACAID|MAC Address, unique within a VLAN. MACAID is the AID MacRngAid and is listable. MACAID must not be null.
VLAN|VLAN is the AID MachostId2. VLAN must not be null.
BRIDGE|Bridge is a required parameter left optional for CMS compatibility with older C7 releases. BRIDGE is the AID BridgeProvAid. A null value is equivalent to "ALL".
L2IFAID|Layer 2 Access Identifier. This is the port address or the VC Aid on which the host can be found. This parameter is mandatory when BRIDGE equals to LOCAL for locating the bridge. L2IFAID is the AID MachostId. A null value is equivalent to "ALL".
STATIC|Indicates whether the MACHOST entry was STATICally provisioned or dynamically learned. STATIC is of type BoolYN. A null value defaults to "N".

##### Syntax: ```RTRV-NETYPE:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-NODE:[TID]:<NodeAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
NodeAid|Node Access Identifier. The node identifier used to identify the node. NodeAid is the AID NodeId and is listable and rangeable. NodeAid must not be null. NodeAid can be set to "ALL".

##### Syntax: ```RTRV-NTWK-CNFG:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-ONT:[TID]:<OntAid>:[CTAG]:::[[REGID=<REGID>,][ONTPROF=<ONTPROF>,][DETAILS=<DETAILS>]]; ```

##### Parameters
Attribute | Description
|---
OntAid|Optical Network Termination Access ID. OntAid is the AID OntNtwkRngAid and is listable and rangeable. OntAid must not be null.
REGID|If specified, only retrieve ONTs with the given REGID(s). REGID is a String and is listable. A null value is equivalent to "ALL".
ONTPROF|ONTPROF is the AID OntId2 and is listable. A null value is equivalent to "ALL".
DETAILS|Additional ONT info will be displayed only if DETAILS=Y is included. DETAILS is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-ONT-QUAR:[TID]:<QuarOntAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
QuarOntAid|QuarOntAid is the AID QuarOntAid2. QuarOntAid must not be null.

##### Syntax: ```RTRV-ONT-UA:[TID]:<PonRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PonRngAid|The PON Port Access Identifier. PonRngAid is the AID FourPortLuNtwkRngAid and is listable and rangeable. PonRngAid must not be null.

##### Syntax: ```RTRV-PM-<OCN>:[TID]:<OcNAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
OcNAid|OCn Line Access Identifier. The address of the OCn line which the monitored parameter values are requested. OcNAid is the AID FourPortLuAndRapAid and is listable. OcNAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeOCn. A null value defaults to "retrieving".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by STS12. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-<STSN>:[TID]:<StsAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
StsAid|STS Path Access Identifier. The address of the STS path which the monitored parameter values are requested. StsAid is the AID StsAid and is listable. StsAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeSts. A null value defaults to "retrieving".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by STS1 facility. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-ADSL:[TID]:<AdslAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
AdslAid|ADSL Access Identifier. The address of the ADSL ports which the monitored parameter values are requested. AdslAid is the AID TwentyFourPortLuAid and is listable. AdslAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeAdsl. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by ADSL port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-AP:[TID]:<ApAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
ApAid|ApAid is the AID AtmRscPortAid and is listable. ApAid must not be null.
MONTYPE|Monitored Type. This parameter indicates the monitored type which is being retrieved, such as IV-IMA, SES-IMA, etc. MONTYPE is of type MonitorTypeAp. A null value defaults to "retrieving all".
LOCN|LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value is equivalent to "ALL".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-EC1:[TID]:<Ec1Aid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
Ec1Aid|EC1 Access Identifier. The address of the EC1 ports having the monitored parameter values retrieved. Ec1Aid is the AID TwelvePortLuAid and is listable. Ec1Aid must not be null.
MONTYPE|Monitored Type. This parameter indicates the monitored type which is being retrieved, such as ES-L, SES-L, etc. MONTYPE is of type MonitorTypeEc1. A null value defaults to "retrieving all".
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-ERPS:[TID]:<ErpsAid>:[CTAG]::[<MONTYPE>],,,,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsAid. ErpsAid must not be null.
MONTYPE|Monitored Type. This parameter indicates the monitored type which is being retrieved. MONTYPE is of type MonitorTypeErps. A null value is equivalent to "ALL".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value is equivalent to "ALL".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value is equivalent to "ALL".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "ALL".

##### Syntax: ```RTRV-PM-ETH:[TID]:<EthPortAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
EthPortAid|ONT Ethernet Port Access Identifier. The address of the GPON ONT Ethernet Port for which the monitored parameter values are requested. EthPortAid is the AID EthId2 and is listable. EthPortAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeOntEth. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by T1 port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-GRPXDSL:[TID]:<GroupAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GRPXDSL Access Identifier. The address of the GRPXDSL ports which the monitored parameter values are requested. GroupAid is the AID DslGrpAid. GroupAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeGrpXdsl. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by ADSL port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-HDSL:[TID]:<HdslAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
HdslAid|HDSL Port Access Identifier. The address of the HDSL port which the monitored parameter values are requested. HdslAid is the AID SixPortLuAid and is listable. HdslAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeHdsl. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by HDSL port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-IMA:[TID]:<ImaAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
ImaAid|IMA Group Access Identifier. The address of the IMA group which the monitored parameter values retrieved. ImaAid is the AID ImaGrpAid and is listable. ImaAid must not be null.
MONTYPE|Monitored Type. This parameter indicates the monitored type which is being retrieved, such as GR-FC, GR-UAS-IMA, etc. MONTYPE is of type MonitorTypeIma. A null value defaults to "retrieving all".
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-IMALINK:[TID]:<ImaLinkAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
ImaLinkAid|IMA Link Access Identifier. The address of the IMA Link having the monitored parameter values retrieved. ImaLinkAid is the AID SixPortLuAid and is listable. ImaLinkAid must not be null.
MONTYPE|Monitored Type. This parameter indicates the monitored type which is being retrieved, such as IV-IMA, SES-IMA, etc. MONTYPE is of type MonitorTypeImaLink. A null value defaults to "retrieving all".
LOCN|Location. Indicates whether the near end or far end Path PM registers are to be edited. Section PM registers are only kept in association with the near end. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the period of time that the PM threshold values apply to. Currently 15-MIN and 1-DAY period are supported. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-ONT:[TID]:<OntAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
OntAid|ONT Access Identifier. The address of the GPON ONT for which the monitored parameter values are requested. OntAid is the AID OntAid and is listable. OntAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeOnt. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by T1 port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-PW:[TID]:<PwAid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
PwAid|PW Access Identifier. The address of the PW object which the monitored parameter values retrieved. PwAid is the AID PwAid and is listable. PwAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. MONTYPE is of type MonitorTypePw. A null value is equivalent to "ALL".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by PW. LOCN is of type Location. A null value is equivalent to "ALL".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. TMPER is of type PMPeriod. A null value is equivalent to "ALL".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value is equivalent to "ALL".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-PM-T1:[TID]:<Ds1Aid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port which the monitored parameter values are requested. Ds1Aid is the AID TwelvePortLuAid and is listable. Ds1Aid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeT1. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by T1 port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-T3:[TID]:<Ds3Aid>:[CTAG]::[<MONTYPE>],,[<LOCN>],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port which the monitored parameter values are requested. Ds3Aid is the AID T3Aid and is listable. Ds3Aid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeT3. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by T3 port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored unless TMPER is specified as 1-DAY. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PM-VIDCHAN:[TID]:<IpAid>:[CTAG]::[<MONTYPE>],,,,[<TMPER>],[<MONDAT>],[<MONTM>]:RTRAID=<RTRAID>; ```

##### Parameters
Attribute | Description
|---
IpAid|IpAid is the AID IpAid and is listable. IpAid must not be null.
MONTYPE|MONTYPE is of type MonitorTypeVidChan. A null value defaults to "ALL".
TMPER|TMPER is of type PMPeriod. A null value defaults to "ALL".
MONDAT|MONDAT is a Date. A null value defaults to "ALL".
MONTM|MONTM is a Time. A null value defaults to "ALL".
RTRAID|RTRAID is the AID SlotLuAid. RTRAID must not be null.

##### Syntax: ```RTRV-PM-XDSL:[TID]:<DslAid>:[CTAG]::[<MONTYPE>],,[<LOCN >],,[<TMPER>],[<MONDAT>],[<MONTM>]; ```

##### Parameters
Attribute | Description
|---
DslAid|XDSL Access Identifier. The address of the XDSL ports which the monitored parameter values are requested. DslAid is the AID TwentyFourPortAid and is listable. DslAid must not be null.
MONTYPE|Monitored Type. This specifies the type of monitored parameter for which a value is requested. A null value retrieves all. MONTYPE is of type MonitorTypeXdsl. A null value defaults to "retrieving all".
LOCN|Location. This parameter indicates the location, in reference to the entity identified by ADSL port. Thus, "near end" refers to PM values obtained at the identified entity, and "far end" refers to PM values obtained at a distant entity that is connected to the identified entity. A null value retrieves both. LOCN is of type Location. A null value defaults to "retrieving both".
TMPER|Time Period. This indicates the length of the accumulation time period to which the retrieved parameters apply. Currently 15-MIN and 1-DAY periods are supported. A null value retrieves both. TMPER is of type PMPeriod. A null value defaults to "retrieving both".
MONDAT|Monitored Date (MM-DD). This parameter identifies the beginning of the PM period. It is ignored if TMPER is specified as 15-MIN. MONDAT is a Date. A null value defaults to "retrieving all".
MONTM|Monitored Time (HH-MM). This parameter identifies the beginning time of day of the requested PM period. It is ignored if TMPER is specified as 1-DAY. MONTM is a Time. A null value defaults to "retrieving all".

##### Syntax: ```RTRV-PON:[TID]:<PonRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PonRngAid|The PON Port Access Identifier. PonRngAid is the AID FourPortLuNtwkRngAid and is listable and rangeable. PonRngAid must not be null.

##### Syntax: ```RTRV-PP:[TID]:<PPAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PPAid|Pseudo-port Access Identifier. PPAid is the AID PpRngAid. PPAid must not be null.

##### Syntax: ```RTRV-PPL:[TID]:<PplAid>:[CTAG]::[PPLORIGIN=<PPLORIGIN>]; ```

##### Parameters
Attribute | Description
|---
PplAid|The Path Protection Label in question. PplAid is the AID PplRngAid and is listable and rangeable. PplAid must not be null.
PPLORIGIN|The shelf originating the PPL PPLORIGIN is the AID ShelfAid and is listable. A null value defaults to "ALL".

##### Syntax: ```RTRV-PPPOEAC:[TID]:<MAC>:[CTAG]:::SCOPE=<SCOPE>,[[VLAN=<VLAN>,][L2IFAID=<L2IFAID>]]; ```

##### Parameters
Attribute | Description
|---
MAC|MAC Address : This is the Ethernet Address of the AC as learned from the PPPoE Discovery packet MAC is the AID MacRngAid and is listable. MAC must not be null.
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1. SCOPE must not be null.
VLAN|The request may be filtered to a specific VLAN. VLAN is the AID VlanIndexAid. A null value is equivalent to "ALL".
L2IFAID|The request can be filtered on Layer 2 Interface Access Identifier.
This can be one of the following :

- subscriber port on which this Host was discovered

OR

- AID of the remote endpoint (on an access LU card) of the subscriber VC L2IFAID is the AID PppoehostId1. A null value is equivalent to "ALL".


##### Syntax: ```RTRV-PPPOEHOST:[TID]:<MACAID>:[CTAG]:::[PPPENCAP=<PPPENCAP>],SCOPE=<SCOPE>,[[VLAN=<VLAN>,][L2IFAID=<L2IFAID>]]; ```

##### Parameters
Attribute | Description
|---
MACAID|This is the Ethernet Address of the Host as learned from the PPPoE Discovery packet MACAID is the AID MacRngAid and is listable. MACAID must not be null.
PPPENCAP|Filter on PPP Encapsulation Type. PPPENCAP is of type PppEncapsulation. A null value is equivalent to "ALL".
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1. SCOPE must not be null.
VLAN|The request may be filtered to a specific VLAN. VLAN is the AID VlanIndexAid. A null value is equivalent to "ALL".
L2IFAID|Layer 2 Interface Access Identifier L2IFAID is the AID PppoehostId1. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-PPPOESESS:[TID]:<MACAID>:[CTAG]::[<ACSESS>]:[PPPENCAP=<PPPENCAP>],SCOPE=<SCOPE>,[[VLAN=<VLAN>,][HOSTMAC=<HOSTMAC>,][L2IFAID=<L2IFAID>]]; ```

##### Parameters
Attribute | Description
|---
MACAID|MACAID is the AID MacRngAid and is listable. MACAID must not be null.
ACSESS|The Session Id is a 16 bit number produced by the AC during the discovery phase. If MAC Address is set to ALL, AC Sess should be set to NULL. ACSESS is a Integer. A null value is equivalent to "ALL".
PPPENCAP|Filter on PPP Encapsulation Type. PPPENCAP is of type PppEncapsulation. A null value is equivalent to "ALL".
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1. SCOPE must not be null.
VLAN|The request may be filtered to a specific VLAN. VLAN is the AID VlanIndexAid. A null value is equivalent to "ALL".
HOSTMAC|HOSTMAC is the AID MacAid. A null value is equivalent to "ALL".
L2IFAID|Layer 2 Interface Access Identifier - This can be one of the following : - On input, this can be a subscriber port or a GE2p physical port. On output, this is the port on which the Host was discovered OR - AID of the remote endpoint (on an access LU card) of the subscriber VC L2IFAID is the AID PppoehostId1. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-PROF-ACS:[TID]:<ACSPROFAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ACSPROFAID|The ACSProf Access Identifier. ACSPROFAID is the AID AcsId. ACSPROFAID must not be null.

##### Syntax: ```RTRV-PROF-ETH:[TID]:<EthProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EthProfAid|Ethernet Profile Access Identifier. EthProfAid is the AID EthProfRngAid and is listable and rangeable. EthProfAid must not be null.

##### Syntax: ```RTRV-PROF-ETHBW:[TID]:<ProfileId>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ProfileId|This identifies which profile is being operated on. ProfileId is the AID EthbwId2 and is listable and rangeable. ProfileId must not be null.

##### Syntax: ```RTRV-PROF-MATCHLIST:[TID]:<MatchListAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
MatchListAid|A unique network wide ID. MatchListAid is the AID MatchlistId and is listable and rangeable. MatchListAid must not be null.

##### Syntax: ```RTRV-PROF-MATCHRULE:[TID]:<RuleAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
RuleAid|A C7 Network unique number identifying the rule. RuleAid is the AID MatchruleId1 and is listable and rangeable. RuleAid must not be null.

##### Syntax: ```RTRV-PROF-MCAST:[TID]:<McastProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
McastProfAid|McastProfAid is the AID McastId and is listable and rangeable. McastProfAid must not be null.

##### Syntax: ```RTRV-PROF-MCASTRANGE:[TID]:<McastRangeProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
McastRangeProfAid|Mcast Range Profile AID. McastRangeProfAid is the AID McastrangeId. McastRangeProfAid must not be null.

##### Syntax: ```RTRV-PROF-MVR:[TID]:<MvrProfAid>:[CTAG]:::[VLAN=<VLAN>]; ```

##### Parameters
Attribute | Description
|---
MvrProfAid|Multicast VLAN Registration Profile Index AID. MvrProfAid is the AID MvrId and is listable and rangeable. MvrProfAid must not be null.
VLAN|VLANs associated with a MVR profile. VLAN is the AID VlanIndexAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-PROF-ONT:[TID]:<OntProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntProfAid|The access identifier(s) of profiles to retrieve. OntProfAid is the AID OntId3 and is listable and rangeable. OntProfAid must not be null.

##### Syntax: ```RTRV-PROF-SIPDIAL:[TID]:<SipDialAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SipDialAid|System scoped Dial Plan for SIP Gateways. SipDialAid is the AID SipdialId. SipDialAid must not be null.

##### Syntax: ```RTRV-PROF-SIPSVC:[TID]:<SipSvcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SipSvcAid|System scoped SIP Profile SipSvcAid is the AID SipsvcId. SipSvcAid must not be null.

##### Syntax: ```RTRV-PROF-TRF:[TID]:<TrfProfAid>:[CTAG]:::[INTERNAL=<INTERNAL>]; ```

##### Parameters
Attribute | Description
|---
TrfProfAid|Traffic Profile Access Identifier. The address of a specific entry in Traffic Profile table to be retrieved. TrfProfAid is the AID TrfId1 and is listable and rangeable. TrfProfAid must not be null.
INTERNAL|Traffic profiles for Internal Cross Connects. If present, this parameter specifies the retrieval of otherwise hidden traffic profiles used for cross connects created internally by the C7. It is intended for use only by system experts or C7 support personnel. INTERNAL is of type InternalCrsTypes and is listable. A null value defaults to "NONE".

##### Syntax: ```RTRV-PW:[TID]:<PwAid>:[CTAG]:::[DETAILS=<DETAILS>]; ```

##### Parameters
Attribute | Description
|---
PwAid|PW Aid pattern. PwAid is the AID PwId and is listable and rangeable. PwAid must not be null.
DETAILS|DETAILS is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-RADIUS:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-RFVID:[TID]:<OntPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|Rf-Video Port Access Identifer. The address of the RFVID port. (The ONT port number must be equal to 1.) OntPortAid is the AID OntPortNtwkRngAid. OntPortAid must not be null.

##### Syntax: ```RTRV-RMTDEV:[TID]:<RmtDevAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
RmtDevAid|Remote Device Access Identifier. RmtDevAid is the AID RmtDevAid. RmtDevAid must not be null.

##### Syntax: ```RTRV-RMTDEV-DISC:[TID]:<RmtDevPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
RmtDevPortAid|The port on which the remote device has been detected. RmtDevPortAid is the AID RmtDevDiscRngAid. RmtDevPortAid must not be null.

##### Syntax: ```RTRV-SERIAL:[TID]:<SerialAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SerialAid|Serial Port Access Identifier. The address of the serial port for which is being retrieved. SerialAid is the AID SerialPort and is listable. SerialAid must not be null.

##### Syntax: ```RTRV-SFP:[TID]:<PortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PortAid|This is the AID of a port equipped with an SFP. Currently this means a GE port of a GE-2P card, or an OLTG PON port. PortAid is the AID SfpId3 and is listable and rangeable. PortAid must not be null.

##### Syntax: ```RTRV-SHELF:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the data is to be retrieved from. ShelfAid is the AID ShelfId and is listable and rangeable. ShelfAid must not be null. ShelfAid can be set to "ALL".

##### Syntax: ```RTRV-SIP:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Access Identifier for the SIP Group. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-SIP-DNSSRV:[TID]:<IGAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IGAID|IG AID. IGAID is the AID IgAid. IGAID must not be null.

##### Syntax: ```RTRV-SIPT0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0Aid is the AID SipT0PortNtwkRngAid. T0Aid must not be null.

##### Syntax: ```RTRV-SIPVCG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Ig Number within a shelf. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-SNMP:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-SNMP-ACL:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-SNMP-TRAP:[TID]:<TrapAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
TrapAid|Trap Access Identifier. The address of the trap to be retrieved. TrapAid is the AID TrapAid. TrapAid must not be null.

##### Syntax: ```RTRV-SSH:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-STAT-CHAN:[TID]:<IP>:[CTAG]:::LOC=<LOC>; ```

##### Parameters
Attribute | Description
|---
IP|Multicast Channel IP address. IP is the AID IpAid. IP must not be null.
LOC|Location of the Multicast Channel statistics. LOC is the AID SourceId. LOC must not be null.

##### Syntax: ```RTRV-STAT-DHCPL2RELAY:[TID]:<VlanAid>:[CTAG]:::[[BRIDGE=<BRIDGE>,][L2IFAID=<L2IFAID>]]; ```

##### Parameters
Attribute | Description
|---
VlanAid|VlanAid is the AID PacketVlanRngAid and is listable and rangeable. VlanAid must not be null.
BRIDGE|BRIDGE will default to ALL unless L2IFAID is specified. In that case, only BRIDGE=LOCAL results are returned for that EXA LU slot, and so BRIDGE in that case defaults to LOCAL. BRIDGE is the AID BridgeRtrvAid. A null value is equivalent to "ALL".
L2IFAID|L2IFAID is required if Bridge=Local. This must be the address of an EXA Slot.
If L2IFAID is specified, only BRIDGE=LOCAL responses are returned for that slot. L2IFAID is the AID SlotLuAid. A null value is equivalent to "ALL".


##### Syntax: ```RTRV-STAT-ERPS:[TID]:<ErpsAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
ErpsAid|The aid of ERPS domain. ErpsAid is the AID ErpsId. ErpsAid must not be null.

##### Syntax: ```RTRV-STAT-ETH:[TID]:<EthAid>:[CTAG]:::[[LPBKSTATE=<lpbkstate>,][RFC2544LPBKVLANS=<atmTrfProfProvAid>]]; ```

##### Parameters
Attribute | Description
|---
EthAid|Ethernet Access Identifier. Note that the AID with suffix of ALL is not applicable for BR/RG. EthAid is the AID EthId8 and is listable and rangeable. EthAid must not be null.
lpbkstate|lpbkstate is a String. A null value is equivalent to "ALL".
atmTrfProfProvAid|atmTrfProfProvAid is the AID AtmTrfProfProvAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-STAT-GRPXDSL:[TID]:<GroupAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
GroupAid|GroupAid is the AID DslGrpAid and is listable and rangeable. GroupAid must not be null.

##### Syntax: ```RTRV-STAT-HPNA:[TID]:<OntEthPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntEthPortAid|Access identifier for HPNA performance statistics on any HPNA supported ETH port on the ONT. OntEthPortAid is the AID OntPortRngAid and is listable and rangeable. OntEthPortAid must not be null.

##### Syntax: ```RTRV-STAT-IP:[TID]:<PpRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpRngAid|Pseudoport Access Identifier on an IRC or Ge-2p PpRngAid is the AID Pp1RngAid and is listable and rangeable. PpRngAid must not be null.

##### Syntax: ```RTRV-STAT-LAG:[TID]:<LinkAggAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
LinkAggAid|A unique AID identifying a group. Up to 64 groups are supported on a single shelf. LinkAggAid is the AID LagId and is listable and rangeable. LinkAggAid must not be null.

##### Syntax: ```RTRV-STAT-MEP:[TID]:<MEPAID>:[CTAG]:::[IFAID=<IFAID>]; ```

##### Parameters
Attribute | Description
|---
MEPAID|MEPAID is the AID EthOamMepRngAid. MEPAID must not be null.
IFAID|IFAID is the AID MepId1. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-STAT-MEPFRAMEDELAY:[TID]:<MEGAID>:[CTAG]:::[MEP=<MEP>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid. MEGAID must not be null.
MEP|MEP is the AID LtraceId3. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-STAT-MEPFRAMELOSS:[TID]:<MEGAID>:[CTAG]:::[MEP=<MEP>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid. MEGAID must not be null.
MEP|MEP is the AID LtraceId3. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-STAT-MIP:[TID]:<MEGAID>:[CTAG]:::[MIP=<MIP>]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid. MEGAID must not be null.
MIP|MIP is the AID OntPortAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-STAT-NDP:[TID]:<VlanAid>:[CTAG]:::[[BRIDGE=<BRIDGE>,][L2IFAID=<L2IFAID>]]; ```

##### Parameters
Attribute | Description
|---
VlanAid|VlanAid is the AID PacketVlanRngAid and is listable and rangeable. VlanAid must not be null.
BRIDGE|BRIDGE will default to ALL unless L2IFAID is specified. In that case, only BRIDGE=LOCAL results are returned for that EXA LU slot, and so BRIDGE in that case defaults to LOCAL. BRIDGE is the AID BridgeRtrvAid. A null value is equivalent to "ALL".
L2IFAID|L2IFAID is required if Bridge=Local. This must be the address of an EXA Slot.
If L2IFAID is specified, only BRIDGE=LOCAL responses are returned for that slot. L2IFAID is the AID SlotLuAid. A null value is equivalent to "ALL".


##### Syntax: ```RTRV-STAT-PPPOA:[TID]:<Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Aid|Aid is the AID PppoaId1 and is listable. Aid must not be null.

##### Syntax: ```RTRV-STAT-PPPOE:[TID]:<Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Aid|Aid is the AID PppoaId1 and is listable. Aid must not be null.

##### Syntax: ```RTRV-STAT-PPPOEAC:[TID]:<MACAID>:[CTAG]:::SCOPE=<SCOPE>; ```

##### Parameters
Attribute | Description
|---
MACAID|This is the Ethernet Address of the AC as learned from the PPPoE Discovery packet MACAID is the AID MacRngAid and is listable. MACAID must not be null.
SCOPE|This parameter specifies the target of the command, a Virtual Bridge or VDSL slot. SCOPE is the AID PppoaId1. SCOPE must not be null.

##### Syntax: ```RTRV-STAT-PW:[TID]:<PwAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
PwAid|PW identifier. ONT Pw Aid not supported. PwAid is the AID PwAid. PwAid must not be null.

##### Syntax: ```RTRV-STAT-RFR:[TID]:<OntRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
OntRngAid|OntRngAid is the AID OntRngAid and is listable and rangeable. OntRngAid must not be null.

##### Syntax: ```RTRV-STAT-SIPT0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0Aid is the AID SipT0PortNtwkRngAid. T0Aid must not be null.

##### Syntax: ```RTRV-STAT-UDP:[TID]:<PpRngAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
PpRngAid|Pseudoport Access Identifier on an IRC or Ge-2p PpRngAid is the AID Pp1RngAid and is listable and rangeable. PpRngAid must not be null.

##### Syntax: ```RTRV-STAT-VEP:[TID]:<VepAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VepAid|VepAid is the AID VepStatRngAid. VepAid must not be null.

##### Syntax: ```RTRV-STAT-VID:[TID]:<VidStatAid>:[CTAG]:::[[VLAN=<VLAN>,][CHAN=<CHAN>,][ADDR=<ADDR>]]; ```

##### Parameters
Attribute | Description
|---
VidStatAid|Target address - may be a slot or port on an EXA capable line unit. VidStatAid is the AID Vid2. VidStatAid must not be null.
VLAN|The request may be filtered for a specific VLAN. VLAN is the AID VlanIndexAid. A null value is equivalent to "ALL".
CHAN|The request may be filtered for a specific Channel. CHAN is the AID IpAid. A null value is equivalent to "ALL".
ADDR|When targetting a RAP slot only, this address may be supplied to filter responses corresponding to an EXA Capable Line Unit or an ERPS or LAG. ADDR is the AID Vid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-STATUS:[TID]:<MsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
MsAid|Maintenance Slot Access Identifier. The address of the Maintenance Slot where the user's session is to be retrieved. MsAid is the AID MsAllAid and is listable. MsAid must not be null.

##### Syntax: ```RTRV-STP-GROUP:[TID]:<StpGroupAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
StpGroupAid|Spanning Tree Protocol Range Group - used to retrieve a range of spanning tree protocol groups in the system. StpGroupAid is the AID StpGroupRngAid. StpGroupAid must not be null.

##### Syntax: ```RTRV-SUBIF-BINDING:[TID]:<PHYSLOC>:[CTAG]:::[[RTRAID=<RTRAID>,][IP=<IP>]]; ```

##### Parameters
Attribute | Description
|---
PHYSLOC|Physical Location Access Identifier - specifies the subscriber location scope. This AID can be ALL, Node, Shelf, Slot or Port or a range of the above AIDs. PHYSLOC is the AID SubIfBindingRng and is listable. PHYSLOC must not be null.
RTRAID|This is the IRC slot location. RTRAID is the AID SlotLuAid. A null value defaults to "ALL".
IP|IP is the AID IpAid. A null value defaults to "ALL".

##### Syntax: ```RTRV-SYS:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-SYS-SECU:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-T0:[TID]:<T0Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Port Access Identifier. The access identifier of the T0 port being retrieved. T0Aid is the AID TwentyFourPortLuNtwkRngAid and is listable and rangeable. T0Aid must not be null.

##### Syntax: ```RTRV-T1:[TID]:<Ds1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds1Aid|T1 Port Access Identifier. The address of the T1 port being retrieved. Ds1Aid is the AID TwelvePortLuNtwkRngAid and is listable and rangeable. Ds1Aid must not be null.

##### Syntax: ```RTRV-T1TG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|Interface Group AID. This parameter specifies the interface group for which the data is to be retrieved. It may represent either the subscriber-facing (IDT) or network-facing (RT) interface group. IgAid is the AID IgRngAid. IgAid must not be null.

##### Syntax: ```RTRV-T3:[TID]:<Ds3Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Ds3Aid|T3 Port Access Identifier. The address of the T3 port being retrieved. Ds3Aid is the AID T3NtwkRngAid and is listable and rangeable. Ds3Aid must not be null.

##### Syntax: ```RTRV-TDMGW:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|IgAid is the AID IgRngAid. IgAid must not be null.

##### Syntax: ```RTRV-TGRP:[TID]:<MsAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
MsAid|Maintenance Slot Access Identifier. The address of the maintenance slot which controls the test bus. MsAid is the AID MsAid and is listable. MsAid must not be null.

##### Syntax: ```RTRV-TMG:[TID]:<ShelfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
ShelfAid|Shelf Access Identifier. The address of the shelf where the timing is to be retrieved. ShelfAid is the AID ShelfAid and is listable. ShelfAid must not be null.

##### Syntax: ```RTRV-TMPLT-ADSL:[TID]:<DslProfAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DslProfAid|DslProfAid is the AID DslProfAllAid and is listable and rangeable. DslProfAid must not be null.

##### Syntax: ```RTRV-TMPLT-PW:[TID]:<PwTmpltAid>:[CTAG]:::; ```

##### Parameters
Attribute | Description
|---
PwTmpltAid|PW template Aid pattern. PwTmpltAid is the AID PwTmpltRngAid. PwTmpltAid must not be null.

##### Syntax: ```RTRV-TMPLT-SECU:[TID]:<SecuTmpltAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
SecuTmpltAid|This is the Access Identifier of the Security Template. SecuTmpltAid is the AID SecuTmpltAllAid and is listable and rangeable. SecuTmpltAid must not be null.

##### Syntax: ```RTRV-TMPLT-VLANIF:[TID]:<VlanIfTmpltAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VlanIfTmpltAid|VlanIfTmpltAid is the AID VlanIfTmpltRngAid. VlanIfTmpltAid must not be null.

##### Syntax: ```RTRV-TMPLT-XDSL:[TID]:<XdslTmpltAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
XdslTmpltAid|DSL Configuration Template Number XdslTmpltAid is the AID DslProfAllAid. XdslTmpltAid must not be null.

##### Syntax: ```RTRV-TRAF:[TID]:<IgAid>:[CTAG]::[<CSHELF>]:[RESET=<RESET>]; ```

##### Parameters
Attribute | Description
|---
IgAid|Interface group Aid of the Interface Group for which traffic statistics are being requested. IgAid is the AID IgAid and is listable and rangeable. IgAid must not be null.
CSHELF|Address of a concentration shelf from which to retrieve call statistics. If not provided, statistics for the IG are returned. (see ENT-IG-CSHELF) CSHELF is the AID ShelfAid. A null value is equivalent to "ALL".
RESET|This parameter indicates that the counters should be reset immediately after the data returned by the reply has been retrieved. RESET is of type BoolYN. A null value defaults to "N".

##### Syntax: ```RTRV-USER-ACL:[TID]::[CTAG]; ```


##### Syntax: ```RTRV-USER-SECU:[TID]:<UID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
UID|User Identifier. The user's identifier for session to be cancelled. It is a non-confidential identifier that uniquely determines a user. The user's identifier is any combination of alphanumeric characters 4 to 10 characters long and is case-sensitive. A value of ALL is allowed for retrieving all users. UID is the AID UserAllAid. UID must not be null.

##### Syntax: ```RTRV-VB:[TID]:<VbAid>:[CTAG]:::[[OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>]]; ```

##### Parameters
Attribute | Description
|---
VbAid|VbAid is the AID VbRngAid and is listable and rangeable. VbAid must not be null.
OPTION82|This parameter is deprecated after release 7.2. This can be supplied as an optional request filter. OPTION82 is of type Option82. A null value defaults to "ALL".
L2RLYMODE|This parameter is deprecated after release 7.2. This can be supplied as an optional request filter. L2RLYMODE is of type DhcpL2RelayMode. A null value defaults to "ALL".

##### Syntax: ```RTRV-VBPORT:[TID]:<VbPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|Virtual Bridge Port Aid - This identifies either physical port or VC endpoint associated with the Virtual Bridge. VbPortAid is the AID VirtualBridgePortId7 and is listable and rangeable. VbPortAid must not be null.

##### Syntax: ```RTRV-VCG:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|The address of the Voice Concentration Group(s) to retrieve. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-VCGLINK:[TID]:<IgAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
IgAid|The address of the Voice Concentration Group. IgAid is the AID IgRngAid and is listable and rangeable. IgAid must not be null.

##### Syntax: ```RTRV-VDS1:[TID]:<Vds1Aid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
Vds1Aid|Virtual DS1 Location. Vds1Aid is the AID Vds1NtwkRngAid and is listable and rangeable. Vds1Aid must not be null.

##### Syntax: ```RTRV-VEP:[TID]:<VepAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VepAid|Voice Endpoint AID of POTs port on ONT or C7 Line Unit VepAid is the AID VepRngAid and is listable and rangeable. VepAid must not be null.

##### Syntax: ```RTRV-VID-CHAN:[TID]:<IP>:[CTAG]:::[[VP=<VP>,][VC=<VC>,][TRFPROF=<TRFPROF>,][TYPE=<TYPE>,][DESC=<DESC>,][DETAILS=<DETAILS>]]; ```

##### Parameters
Attribute | Description
|---
IP|IP is the AID IpRngAid. IP must not be null.
VP|The VP number associated with the video transport VCs to deliver this channel to the different shelves. When specified here, this parameter acts as a filter to only return channels with the specified VP. VP is of type VPRange. A null value is equivalent to "ALL".
VC|The VC number associated with the video transport VCs to deliver this channel to the different shelves. When specified here, this parameter acts as a filter to only return channels with the specified VC. VC is of type VCRange. A null value is equivalent to "ALL".
TRFPROF|Traffic Profile. This parameter identifies which Traffic Profile which is being used by the channel. When specified here, this parameter acts as a filter to only return channels with the specified TRFPROF. TRFPROF is the AID AtmTrfProfProvAid. A null value is equivalent to "ALL".
TYPE|Video Channel Type. This is applicable for AVT Model channels only. TYPE is of type ChannelType and is listable. A null value is equivalent to "ALL".
DESC|Channel description. The description can be up to 40 characters in length for VCVT Model channels and upto 31 characters in length for AVT Model Channels. DESC is a String. A null value is equivalent to "ALL".
DETAILS|The COUNT parameter will be displayed only if DETAILS=Y is included. DETAILS is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-VID-FILTER:[TID]:<VidSrcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source Index AID. VidSrcAid is the AID VidSrcAid. VidSrcAid must not be null.

##### Syntax: ```RTRV-VID-IRCLOC:[TID]:<VidServAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VidServAid|Video Service Access Identifier. The AID of the Video Service that contains the IRC. VidServAid is the AID VidServRngAid. VidServAid must not be null.

##### Syntax: ```RTRV-VID-SOURCE:[TID]:<VidSrcAid>:[CTAG]:::[DETAILS=<DETAILS>]; ```

##### Parameters
Attribute | Description
|---
VidSrcAid|Video Source Index AID or ALL. VidSrcAid is the AID SourceId1. VidSrcAid must not be null.
DETAILS|Details Flag. The allocated and used bandwidth on the VB Video source slots are displayed only if DETAILS=Y is included. DETAILS is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-VID-SUB:[TID]:<VidSubAid>:[CTAG]:::RTRAID=<RTRAID>,[[SCOPE=<SCOPE>,][CHANIP=<CHANIP>,][STBIP=<STBIP>]]; ```

##### Parameters
Attribute | Description
|---
VidSubAid|Video Subscriber Access Identifier - The port or channel to which subscribers are connected. Usually an ADSL Channel or ONT (or vdsl in the future) port. VidSubAid is the AID SubId2. VidSubAid must not be null.
RTRAID|RTRAID - Location of IRC to handle the command RTRAID is the AID SlotLuAid. RTRAID must not be null.
SCOPE|This flag allows the user to view only the fixed rate ports, only the variable rate ports or all the ports. SCOPE is of type VideoBwcScope and is listable. A null value defaults to "ALL".
CHANIP|IP Address of the channel flowing to the port. This can be supplied to filter the request. CHANIP is the AID IpAid. A null value is equivalent to "ALL".
STBIP|Ip address of the STB on the port. This can be supplied to filter the request. STBIP is the AID IpAid. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-VID-SVC:[TID]:<VidSvcAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VidSvcAid|Video Service Access Identifier. VidSvcAid is the AID VidSvcRngAid. VidSvcAid must not be null.

##### Syntax: ```RTRV-VIRT-IF:[TID]:<VIRTIFAID>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VIRTIFAID|VIRTIFAID is the AID VirtIfRngAid. VIRTIFAID must not be null.

##### Syntax: ```RTRV-VLAN:[TID]:<VlanAid>:[CTAG]:::[[OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>,][NUMPRIO=<NUMPRIO>,][DHCPLOCK=<DHCPLOCK>,][MFF=<MFF>]]; ```

##### Parameters
Attribute | Description
|---
VlanAid|VlanAid is the AID VlanId1 and is listable and rangeable. VlanAid must not be null.
OPTION82|This can be supplied as an optional request filter. Not supported for now. OPTION82 is of type Option82. A null value is equivalent to "ALL".
L2RLYMODE|DHCP L2 Relay Mode. Not supported for now. L2RLYMODE is of type DhcpL2RelayMode. A null value is equivalent to "ALL".
NUMPRIO|Not supported for now. NUMPRIO is of type NumPrioRange. A null value is equivalent to "ALL".
DHCPLOCK|Not supported for now. DHCPLOCK is of type BoolYN. A null value is equivalent to "ALL".
MFF|Not supported for now. MFF is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-VLAN-IF:[TID]:<IfRngAid>:[CTAG]:::[[VLAN=<VLAN>,][BRIDGE=<BRIDGE>,][DETAILS=<DETAILS>]]; ```

##### Parameters
Attribute | Description
|---
IfRngAid|Ranged retrievals are shelf-based, although an AID of �ALL� is accepted for backward compatibility. If IfRngAid=ALL, then the BRIDGE is used to scope the request. IfRngAid is the AID IfId9 and is listable and rangeable. IfRngAid must not be null.
VLAN|Packet VLAN Access Identifier. Only VLAN number AID is allowed since R7.0. If the parameter is not specified but the retrieval is ranged on a remote shelf(remote w/r to the specified BRIDGE=VB), the command will be rejected. VLAN is the AID IfId1. A null value is equivalent to "ALL".
BRIDGE|VB Access Identifier. To control the scope of retrievals, there are several rules governing how BRIDGE is used :
for retrievals scoped under a slot, BRIDGE=ALL will include results with BRIDGE on remote shelves
for retrievals spanning slots, using BRIDGE=ALL will return only interfaces having a BRIDGE matching the shelf the requested IfRngAid
for retrievals spanning shelves, the BRIDGE is used to scope the retrieval to the shelf of the BRIDGE.
if IfRngAid=ALL, then BRIDGE=LOCAL is not supported
BRIDGE is the AID IfId10. A null value is equivalent to "ALL".
DETAILS|The VBPort Aid and ATM(cross-connect) parameters will be displayed only if DETAILS=Y is included. DETAILS is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```RTRV-VLAN-PORT:[TID]:<VLanPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VLanPortAid|VLAN port Access Identifier. VLanPortAid is the AID VLanPortRngAid and is listable and rangeable. VLanPortAid must not be null.

##### Syntax: ```RTRV-VLAN-VBPORT:[TID]:<VbPortAid>:[CTAG]:::[[VLAN=<VLAN>,][OPT82ACT=<OPT82ACT>]]; ```

##### Parameters
Attribute | Description
|---
VbPortAid|VbPortAid is the AID VirtualBridgePortId7 and is listable and rangeable. VbPortAid must not be null.
VLAN|Packet Vlan address for optional request filtering. VLAN is the AID PacketVlanAid. A null value defaults to "ALL".
OPT82ACT|Not supported in release 6.0. This can be supplied as an optional request filter. OPT82ACT is of type Option82Action. A null value defaults to "ALL".

##### Syntax: ```RTRV-VODCLNT:[TID]:<IpAid>:[CTAG]:::IRCAID=<IRCAID>; ```

##### Parameters
Attribute | Description
|---
IpAid|IP Address. The IP address of the VOD client. IpAid is the AID IpRngAid and is listable. IpAid must not be null.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid. IRCAID must not be null.

##### Syntax: ```RTRV-VODDSTLU:[TID]:<EqptAid>:[CTAG]:::IRCAID=<IRCAID>; ```

##### Parameters
Attribute | Description
|---
EqptAid|VOD Destination LU Access Identifier. The address of the VOD Destination Line Unit. EqptAid is the AID EquipmentId2 and is listable and rangeable. EqptAid must not be null.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid. IRCAID must not be null.

##### Syntax: ```RTRV-VODFLOW:[TID]:<VodFlowId>:[CTAG]:::IRCAID=<IRCAID>; ```

##### Parameters
Attribute | Description
|---
VodFlowId|VOD Flow Access Identifier. Number of the VOD flow. VodFlowId is the AID VodFlowRngAid and is listable and rangeable. VodFlowId must not be null.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid. IRCAID must not be null.

##### Syntax: ```RTRV-VODSRCLU:[TID]:<EqptAid>:[CTAG]:::IRCAID=<IRCAID>; ```

##### Parameters
Attribute | Description
|---
EqptAid|VOD Source LU Access Identifier. The address of the VOD Source Line Unit. EqptAid is the AID VodsrcluId1 and is listable and rangeable. EqptAid must not be null.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid. IRCAID must not be null.

##### Syntax: ```RTRV-VODSVR:[TID]:<IpAid>:[CTAG]:::IRCAID=<IRCAID>; ```

##### Parameters
Attribute | Description
|---
IpAid|IP Address. The IP address of the VOD server. IpAid is the AID IpRngAid and is listable. IpAid must not be null.
IRCAID|IRC AID. The address of the IRC. IRCAID is the AID SlotLuAid. IRCAID must not be null.

##### Syntax: ```RTRV-VR:[TID]:<VrAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrAid|Virtual Router Access Identifier. VrAid is the AID VrRngAid and is listable and rangeable. VrAid must not be null.

##### Syntax: ```RTRV-VRP:[TID]:<VrpAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrpAid|Video Return Path Access Identifier. VrpAid is the AID VrpNtwkRngAid and is listable and rangeable. VrpAid must not be null.

##### Syntax: ```RTRV-VRPORT:[TID]:<VrPortAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VrPortAid|Virtual Router Port Access Identifier. VrPortAid is the AID VirtualRouterPortId1 and is listable and rangeable. VrPortAid must not be null.

##### Syntax: ```RTRV-VSP:[TID]:<VspAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VspAid|Access Identifier of the VSP port. VspAid is the AID VspPortNtwkRngAid. VspAid must not be null.

##### Syntax: ```RTRV-VTI:[TID]:<VtiAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
VtiAid|VTI Access Identifier VtiAid is the AID VtiRngAid and is listable and rangeable. VtiAid must not be null.

##### Syntax: ```RTRV-XDSL:[TID]:<XdslAid>:[CTAG]:::[DETAILS=<DETAILS>]; ```

##### Parameters
Attribute | Description
|---
XdslAid|There are 24 ports on all DSL line units. This AID uniquely identifies which DSL port is to be acted upon. XdslAid is the AID TwentyFourPortRngAid and is listable and rangeable. XdslAid must not be null.
DETAILS|This is a retrieve control parameter which allows the caller to request both basic and advanced parameters at the same time. DETAILS is of type BoolYN. A null value defaults to "N".

##### Syntax: ```RTRV-XLAN:[TID]:<XLanAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
XLanAid|Extended LAN Access Identifier. XLanAid is the AID XLanRngAid and is listable and rangeable. XLanAid must not be null.

##### Syntax: ```RTRV-XTU:[TID]:<XtuAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
XtuAid|XDSL Terminal Unit Access Identifier. The address of the XTU from where the data is retrieved. XtuAid is the AID TermUnitAid and is listable. XtuAid must not be null.

##### Syntax: ```SET-ACO:[TID]:<NodeAid>:[CTAG]::<ACOMODE>; ```

##### Parameters
Attribute | Description
|---
NodeAid|Alarm Cutoff Access Identifier. The address of the alarm cutoff being set. NodeAid is the AID NodeAid.
ACOMODE|Alarm Cutoff Mode. This parameter indicates the mode of alarm cutoff operation. ACOMODE is of type AlarmCutoffMode.

##### Syntax: ```SET-ATTR-CONT:[TID]:<ExtContAid>:[CTAG]::[<CONTTYPE>],[<POL>]; ```

##### Parameters
Attribute | Description
|---
ExtContAid|External Control Access Identifier. The address of the external control for which attributes are being set. ExtContAid is the AID ExtControlAid.
CONTTYPE|Condition Type. The parameter indicates which condition type should be associated with the external control. If parameter is not entered, then value does not change from current values. CONTTYPE is of type ContType.
POL|Polarity. This parameter indicates whether the OPR-EXT-CONT command closes the control or opens it. If parameter is not entered, then value is not changed. The initial value is OPRISCLOSED. POL is of type ContPolarity.

##### Syntax: ```SET-ATTR-ENV:[TID]:<EnvAid>:[CTAG]::[<NTFCNCDE>],[<ALMTYPE>],[<ALMMSG>],[<POL>]; ```

##### Parameters
Attribute | Description
|---
EnvAid|Environmental Access Identifier. The address of the environmental input contact. EnvAid is the AID EnvAid.
NTFCNCDE|Notification Code. This parameter indicate the notification code which should be used when the specified condition is raised. If parameter is not entered, then value does not change from current values. NTFCNCDE is of type NotificationRtrv.
ALMTYPE|Alarm Type. This parameter indicate the type of the alarm which should be generated when the status points are not normal. If parameter is not entered, then value does not change from current values. ALMTYPE is of type CondTypeEnvAlm.
ALMMSG|Alarm Message. This parameter identifies the textual string whcih will be included in any notification messages for this environmental input contact. If parameter is not entered, then value does not change from current values. Note: This value is limited to 11 characters and output will be trunctated to this length. ALMMSG is a String.
POL|Polarity. This parameter indicates if the status points are normally open or normally closed. POL is of type EnvPolarity.

##### Syntax: ```SW-DX-EQPT:[TID]:<EqptAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. The address of the duplex equipment which is currently carrying the load. EqptAid is the AID SlotCsAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced switch even if otherwise prohibited. INCL is of type BoolYN. The default value is "N".

##### Syntax: ```SW-DX-GR303:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|Data Link Access Identifier. The address of the EOC/TMC which is to be switched. DataLinkSwAid is the AID IgLinkSwAid.

##### Syntax: ```SW-DX-T1TG:[TID]:<DataLinkSwAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
DataLinkSwAid|Data Link Access Identifier. The address of the EOC/TMC which is to be switched. DataLinkSwAid is the AID IgLinkSwAid.

##### Syntax: ```SW-TOPROTN-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Protecting Access Identifier. The address of the working equipment unit which is currently active and is to transfer its load to the protection unit. EqptAid is the AID SlotLuAid.

##### Syntax: ```SW-TOWKG-EQPT:[TID]:<EqptAid>:[CTAG]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Protection Access Identifier. The address of the protection equipment unit which is currently active and is to transfer its load back to the unit that normally carries the load. EqptAid is the AID SlotLuAid.

##### Syntax: ```SW-VOICE-SVC:[TID]:<EqptAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
EqptAid|Equipment Access Identifier. EqptAid is the AID SlotLuAid.
INCL|INCLusive. This parameter provides a way for the user to request a forced switch even if otherwise prohibited. INCL is of type BoolYN.

##### Syntax: ```TRACE-IP-HOST:[TID]:<RTRAID>:[CTAG]:::IP=<IP>,[[NPROBES=<NPROBES>,][WAITTIME=<WAITTIME>,][INTERVAL=<INTERVAL>,][MAXFAILS=<MAXFAILS>,][FIRSTHOP=<FIRSTHOP>,][MAXHOP=<MAXHOP>,][PROTOCOL=<PROTOCOL>,][UDPPORT=<UDPPORT>]]; ```

##### Parameters
Attribute | Description
|---
RTRAID|The address of the IRC, Ge-2p, Virtual Router, H.248 IG, or VSP Port. RTRAID is the AID HostId1. RTRAID must not be null.
IP|IP Address. The IP address of the destination. IP is the AID IpAid. IP must not be null.
NPROBES|Number of Probes. The number of probes to issue at each hop. NPROBES must be between 1 and 10. NPROBES is a Integer. A null value defaults to "3".
WAITTIME|Wait Time. The number of seconds to wait for a response to a probe. WAITTIME must be between 1 and 30. WAITTIME is a Integer. A null value defaults to "5".
INTERVAL|Interval. The number of seconds to wait between sending probes. INTERVAL must be between 0 and 30. INTERVAL is a Integer. A null value defaults to "0".
MAXFAILS|Maximum Failures. The number of probe failures before advancing to the next hop. This is handy when specifying a large number of NPROBES to help avoid long timeout periods for unresponsive hosts. MAXFAILS must be between 0 and 30. MAXFAILS is a Integer. A null value defaults to "3".
FIRSTHOP|First Hop. The number of the initial hop value. No processing will occur for those intermediate hops less than FIRSTHOP away. FIRSTHOP must be between 1 and 255 and less than or equal to MAXHOP. FIRSTHOP is a Integer. A null value defaults to "1".
MAXHOP|Maximum Hops. The maximum number of hops before the operation will cease. MAXHOP must be between 1 and 255 and greater than or equal to FIRSTHOP. MAXHOP is a Integer. A null value defaults to "10".
PROTOCOL|Protocol. The protocol of the probe packets. Currently only UDP is supported. PROTOCOL is of type TracerouteProtocol. A null value defaults to "UDP".
UDPPORT|The base port used in UDP probe packets. This parameter only applies when the PROTOCOL is UDP. Traceroute assumes that nothing is listening on UDP ports (UDPPORT+(HOP-1)*NPROBES) to (UDPPORT+(HOP*NPROBE)-1) at the destination host, so that an ICMP PORT_UNREACHABLE message will be returned to terminate the route tracing. If something is listening on a port in the default range, this option can be used to select an unused port range. HOP is defined as the number of hops between the source and the destination. UDPPORT is of type UdpPort. A null value defaults to "33434".

##### Syntax: ```TST-EOAM-LPBK:[TID]:<MEGAID>:[CTAG]:::[[SOURCE=<SOURCE>,][DEST=<DEST>,][PDUCOUNT=<PDUCOUNT>,][PRIO=<PRIO>,][DROPELIG=<DROPELIG>,][DATA=<DATA>,][DATALEN=<DATALEN>]]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid. MEGAID must not be null.
SOURCE|SOURCE is the AID LtraceId3. A null value is equivalent to "ALL".
DEST|DEST is the AID LtraceId1. A null value is equivalent to "ALL".
PDUCOUNT|PDUCOUNT is of type OneTo1024. A null value defaults to "1".
PRIO|PRIO is of type LBPrio. A null value defaults to "USEMEP".
DROPELIG|DROPELIG is of type BoolYN. A null value defaults to "N".
DATA|DATA is a String. A null value defaults to "01020304".
DATALEN|DATALEN is of type ZeroTo1400. A null value defaults to "1".

##### Syntax: ```TST-EOAM-LTRACE:[TID]:<MEGAID>:[CTAG]:::[[SOURCE=<SOURCE>,][DEST=<DEST>,][MAXHOPS=<MAXHOPS>]]; ```

##### Parameters
Attribute | Description
|---
MEGAID|MEGAID is the AID MegAid. MEGAID must not be null.
SOURCE|SOURCE is the AID LtraceId. A null value is equivalent to "ALL".
DEST|DEST is the AID LtraceId1. A null value is equivalent to "ALL".
MAXHOPS|MAXHOPS is of type OneTo99. A null value is equivalent to "ALL".

##### Syntax: ```TST-ITACC-MET:[TID]:<T0Aid>:[CTAG]::<TAP>:[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
T0Aid|T0 Port Access Identifier. The address of the T0 port which is to be tested. T0Aid is the AID TwentyFourPortLuAid. T0Aid must not be null.
TAP|Test Access Path (TAP) Identifier. The test access path selected. This is an optional parameter. If the parameter is provided and the request TAP is not available, the command will be rejected. If the TAP is not provided, then the C7 will assign the TAP for the test. TAP is the AID TapAid. TAP must not be null.
INCL|Inclusive. Specifying INCL=Y will force the test to be performed regardless of Off-Hook status. INCL is of type BoolYN. A null value is equivalent to "ALL".

##### Syntax: ```TST-ONT-MET:[TID]:<OntPortAid>:[CTAG]:::[INCL=<INCL>]; ```

##### Parameters
Attribute | Description
|---
OntPortAid|T0 Port Access Identifier. The address of the ONT T0 port which is to be tested. OntPortAid is the AID OntPortAid and is listable. OntPortAid must not be null.
INCL|Inclusive. Specifying INCL=Y will force the test to be performed regardless of Off-Hook status. INCL is of type BoolYN. A null value defaults to "N".
