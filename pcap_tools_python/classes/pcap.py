class Pcap:

    Path = ""
    Magic = ""
    TimeIsNanoSeconds = True
    MajorVersion = 0
    MinorVersion = 0
    Reserved1 = 0
    Reserved2 = 0
    SnapLen = 0
    FCS = 0
    F_header = False
    LinkType = 0

    def __init__(self, pcapPath):
        self.Path = pcapPath
