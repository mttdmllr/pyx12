######################################################################
# Copyright (c) 2001-2004 Kalamazoo Community Mental Health Services,
#   John Holland <jholland@kazoocmh.org> <john@zoner.org>
# All rights reserved.
#
# This software is licensed as described in the file LICENSE.txt, which
# you should have received as part of this distribution.
#
######################################################################

#    $Id$

"""pyx12 package exception classes.
"""

class XML_Reader_Error(Exception):
    """Class for XML Reader errors."""

class x12Error(Exception):
    """Base class for X12N format errors."""

#class ISAError(x12Error):
#    """Errors in the ISA or IEA segements."""

class GSError(x12Error):
    """Errors in the GS or GE segements."""

#class STError(x12Error):
#    """Errors in the ST or SE segements."""

#class WEDIError(Exception):
#    """Base class for WEDI errors in this module."""

#class WEDI1Error(WEDIError): pass
#class WEDI2Error(WEDIError): pass
#class WEDI3Error(WEDIError): pass
#class WEDI4Error(WEDIError): pass
#class WEDI5Error(WEDIError): pass
#class WEDI6Error(WEDIError): pass

class EngineError(Exception): 
    """Base class for translation engine errors."""

#class HL_Loop_Pop(EngineError):
#    """Pop a HL level"""

class IterOutOfBounds(Exception):
    """Iterator is out of bounds"""

class IterDone(Exception):
    """Iterator is Complete"""
        
