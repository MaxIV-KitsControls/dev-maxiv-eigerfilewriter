#!/usr/bin/env python
# -*- coding:utf-8 -*- 


##############################################################################
## license :
##============================================================================
##
## File :        EigerFilewriter.py
## 
## Project :     Eiger Filewriter
##
## This file is part of Tango device class.
## 
## Tango is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Tango is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Tango.  If not, see <http://www.gnu.org/licenses/>.
## 
##
## $Author :      tnunez$
##
## $Revision :    $
##
## $Date :        $
##
## $HeadUrl :     $
##============================================================================
##            This file is generated by POGO
##    (Program Obviously used to Generate tango Object)
##
##        (c) - Software Engineering Group - ESRF
##############################################################################

"""Filewriter for the Eiger detector"""

__all__ = ["EigerFilewriter", "EigerFilewriterClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(EigerFilewriter.additionnal_import) ENABLED START -----#

from dectris_eiger.filewriter import EigerFileWriter

#----- PROTECTED REGION END -----#	//	EigerFilewriter.additionnal_import

## Device States Description
## ON : 
## FAULT : 
## MOVING : 

class EigerFilewriter (PyTango.Device_4Impl):

    #--------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(EigerFilewriter.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	EigerFilewriter.global_variables

    def __init__(self,cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        EigerFilewriter.init_device(self)
        #----- PROTECTED REGION ID(EigerFilewriter.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(EigerFilewriter.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        #----- PROTECTED REGION ID(EigerFilewriter.init_device) ENABLED START -----#

        self.dev = PyTango.DeviceProxy(self.EigerDevice)
        host = self.dev.get_property(['Host'])
        port_nb = self.dev.get_property(['PortNb'])
        api_version = self.dev.get_property(['APIVersion'])
        self.filewriter = EigerFileWriter(host, port_nb, api_version)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(EigerFilewriter.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.always_executed_hook

    #-----------------------------------------------------------------------------
    #    EigerFilewriter read/write attribute methods
    #-----------------------------------------------------------------------------
    
    
    
        #----- PROTECTED REGION ID(EigerFilewriter.initialize_dynamic_attributes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.initialize_dynamic_attributes
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(EigerFilewriter.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.read_attr_hardware


    #-----------------------------------------------------------------------------
    #    EigerFilewriter command methods
    #-----------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(EigerFilewriter.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	EigerFilewriter.programmer_methods

class EigerFilewriterClass(PyTango.DeviceClass):
    #--------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(EigerFilewriter.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	EigerFilewriter.global_class_variables

    def dyn_attr(self, dev_list):
        """Invoked to create dynamic attributes for the given devices.
        Default implementation calls
        :meth:`EigerFilewriter.initialize_dynamic_attributes` for each device
    
        :param dev_list: list of devices
        :type dev_list: :class:`PyTango.DeviceImpl`"""
    
        for dev in dev_list:
            try:
                dev.initialize_dynamic_attributes()
            except:
                import traceback
                dev.warn_stream("Failed to initialize dynamic attributes")
                dev.debug_stream("Details: " + traceback.format_exc())
        #----- PROTECTED REGION ID(EigerFilewriter.dyn_attr) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.dyn_attr

    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        'EigerDevice':
            [PyTango.DevString,
            "Name of the Tango Device of the EigerDectris class to connect to",
            [] ],
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(EigerFilewriterClass,EigerFilewriter,'EigerFilewriter')
        #----- PROTECTED REGION ID(EigerFilewriter.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed,e:
        print '-------> Received a DevFailed exception:',e
    except Exception,e:
        print '-------> An unforeseen exception occured....',e

if __name__ == '__main__':
    main()
