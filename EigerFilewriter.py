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
## ON : ready
## FAULT : error
## MOVING : acquire
## OFF : disabled
## UNKNOWN : Not known

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
        self.attr_Mode_read = ''
        self.attr_TransferMode_read = ''
        self.attr_ImagesPerFile_read = 0
        self.attr_ImageNbStart_read = 0
        self.attr_FilenamePattern_read = ''
        self.attr_CompressionEnabled_read = 0
        self.attr_FilewriterState_read = ''
        self.attr_BufferFree_read = 0
        self.attr_FilewriterError_read = ['']
        #----- PROTECTED REGION ID(EigerFilewriter.init_device) ENABLED START -----#

        connected = 0
        try:
            self.dev = PyTango.DeviceProxy(self.EigerDevice)
            connected = 1
        except:
            self.set_state(PyTango.DevState.FAULT)
            self.set_status("Not able to create proxy EigerDevice")

        if connected:
            prop = self.dev.get_property(['Host'])
            host = prop['Host'][0]              
            prop = self.dev.get_property(['APIVersion'])
            api_version = prop['APIVersion'][0]
            nums = api_version.split(".")
            if int(nums[1]) > 2:
                port_nb = -1
            else:
                prop = self.dev.get_property(['PortNb'])
                port_nb = prop['PortNb'][0]  
                
            self.filewriter = EigerFileWriter(host, port_nb, api_version)

            self.set_state(PyTango.DevState.ON)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(EigerFilewriter.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.always_executed_hook

    #-----------------------------------------------------------------------------
    #    EigerFilewriter read/write attribute methods
    #-----------------------------------------------------------------------------
    
    def read_Mode(self, attr):
        self.debug_stream("In read_Mode()")
        #----- PROTECTED REGION ID(EigerFilewriter.Mode_read) ENABLED START -----#
        self.attr_Mode_read = self.filewriter.mode

        attr.set_value(self.attr_Mode_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.Mode_read
        
    def write_Mode(self, attr):
        self.debug_stream("In write_Mode()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerFilewriter.Mode_write) ENABLED START -----#
        
        self.filewriter.mode = data

        #----- PROTECTED REGION END -----#	//	EigerFilewriter.Mode_write
        
    def read_TransferMode(self, attr):
        self.debug_stream("In read_TransferMode()")
        #----- PROTECTED REGION ID(EigerFilewriter.TransferMode_read) ENABLED START -----#

        self.attr_TransferMode_read = self.filewriter.transfer_mode

        attr.set_value(self.attr_TransferMode_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.TransferMode_read
        
    def write_TransferMode(self, attr):
        self.debug_stream("In write_TransferMode()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerFilewriter.TransferMode_write) ENABLED START -----#
        self.filewriter.transfer_mode = data
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.TransferMode_write
        
    def read_ImagesPerFile(self, attr):
        self.debug_stream("In read_ImagesPerFile()")
        #----- PROTECTED REGION ID(EigerFilewriter.ImagesPerFile_read) ENABLED START -----#

        self.attr_ImagesPerFile_read = self.filewriter.images_per_file

        attr.set_value(self.attr_ImagesPerFile_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.ImagesPerFile_read
        
    def write_ImagesPerFile(self, attr):
        self.debug_stream("In write_ImagesPerFile()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerFilewriter.ImagesPerFile_write) ENABLED START -----#
    
        self.filewriter.images_per_file = data
    
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.ImagesPerFile_write
        
    def read_ImageNbStart(self, attr):
        self.debug_stream("In read_ImageNbStart()")
        #----- PROTECTED REGION ID(EigerFilewriter.ImageNbStart_read) ENABLED START -----#
        self.attr_ImageNbStart_read = self.filewriter.image_nr_start

        attr.set_value(self.attr_ImageNbStart_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.ImageNbStart_read
        
    def write_ImageNbStart(self, attr):
        self.debug_stream("In write_ImageNbStart()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerFilewriter.ImageNbStart_write) ENABLED START -----#
        self.filewriter.image_nr_start = data

        #----- PROTECTED REGION END -----#	//	EigerFilewriter.ImageNbStart_write
        
    def read_FilenamePattern(self, attr):
        self.debug_stream("In read_FilenamePattern()")
        #----- PROTECTED REGION ID(EigerFilewriter.FilenamePattern_read) ENABLED START -----#
        pattern = self.filewriter.filename_pattern
        self.attr_FilenamePattern_read = pattern

        attr.set_value(self.attr_FilenamePattern_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.FilenamePattern_read
        
    def write_FilenamePattern(self, attr):
        self.debug_stream("In write_FilenamePattern()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerFilewriter.FilenamePattern_write) ENABLED START -----#
               
        data = data
        self.filewriter.filename_pattern = data

        #----- PROTECTED REGION END -----#	//	EigerFilewriter.FilenamePattern_write
        
    def read_CompressionEnabled(self, attr):
        self.debug_stream("In read_CompressionEnabled()")
        #----- PROTECTED REGION ID(EigerFilewriter.CompressionEnabled_read) ENABLED START -----#
        if self.filewriter.compression_enabled == True:
            self.attr_CompressionEnabled_read = 1
        else:
            self.attr_CompressionEnabled_read = 0
            
        attr.set_value(self.attr_CompressionEnabled_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.CompressionEnabled_read
        
    def write_CompressionEnabled(self, attr):
        self.debug_stream("In write_CompressionEnabled()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerFilewriter.CompressionEnabled_write) ENABLED START -----#
                
        if data == 0:
            self.filewriter.compression_enabled = False
        else:
            self.filewriter.compression_enabled = True


        #----- PROTECTED REGION END -----#	//	EigerFilewriter.CompressionEnabled_write
        
    def read_FilewriterState(self, attr):
        self.debug_stream("In read_FilewriterState()")
        #----- PROTECTED REGION ID(EigerFilewriter.FilewriterState_read) ENABLED START -----#
        self.attr_FilewriterState_read = self.filewriter.status

        attr.set_value(self.attr_FilewriterState_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.FilewriterState_read
        
    def read_BufferFree(self, attr):
        self.debug_stream("In read_BufferFree()")
        #----- PROTECTED REGION ID(EigerFilewriter.BufferFree_read) ENABLED START -----#

        self.attr_BufferFree_read = self.filewriter.buffer_free
        attr.set_value(self.attr_BufferFree_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.BufferFree_read
        
    def read_FilewriterError(self, attr):
        self.debug_stream("In read_FilewriterError()")
        #----- PROTECTED REGION ID(EigerFilewriter.FilewriterError_read) ENABLED START -----#
        self.attr_FilewriterError_read = self.filewriter.error
        attr.set_value(self.attr_FilewriterError_read)
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.FilewriterError_read
        
    
    
        #----- PROTECTED REGION ID(EigerFilewriter.initialize_dynamic_attributes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.initialize_dynamic_attributes
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(EigerFilewriter.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerFilewriter.read_attr_hardware


    #-----------------------------------------------------------------------------
    #    EigerFilewriter command methods
    #-----------------------------------------------------------------------------
    
    def dev_state(self):
        """ This command gets the device state (stored in its device_state data member) and returns it to the caller.
        
        :param : none
        :type: PyTango.DevVoid
        :return: Device state
        :rtype: PyTango.CmdArgType.DevState """
        self.debug_stream("In dev_state()")
        argout = PyTango.DevState.UNKNOWN
        #----- PROTECTED REGION ID(EigerFilewriter.State) ENABLED START -----#
    
        rstate = self.filewriter.get_status()

        if rstate == "disabled":
            self.set_state(PyTango.DevState.OFF) 
        elif rstate == "ready":
            self.set_state(PyTango.DevState.ON)
        elif rstate == "acquire":
            self.set_state(PyTango.DevState.MOVING)
        elif rstate =="error":
            self.set_state(PyTango.DevState.FAULT)
        else:
            self.set_state(PyTango.DevState.UNKNOWN)
 

        #----- PROTECTED REGION END -----#	//	EigerFilewriter.State
        if argout != PyTango.DevState.ALARM:
            PyTango.Device_4Impl.dev_state(self)
        return self.get_state()
        
    def dev_status(self):
        """ This command gets the device status (stored in its device_status data member) and returns it to the caller.
        
        :param : none
        :type: PyTango.DevVoid
        :return: Device status
        :rtype: PyTango.ConstDevString """
        self.debug_stream("In dev_status()")
        argout = ''
        #----- PROTECTED REGION ID(EigerFilewriter.Status) ENABLED START -----#
        
        self.argout = str(self.filewriter.get_status())

        #----- PROTECTED REGION END -----#	//	EigerFilewriter.Status
        self.set_status(self.argout)
        self.__status = PyTango.Device_4Impl.dev_status(self)
        return self.__status
        
    def Clear(self):
        """ Drops all data (image data and directories) on the DCU.
        
        :param : 
        :type: PyTango.DevVoid
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In Clear()")
        #----- PROTECTED REGION ID(EigerFilewriter.Clear) ENABLED START -----#
        
        self.filewriter.clear()

        #----- PROTECTED REGION END -----#	//	EigerFilewriter.Clear
        
    def InitializeFilewriter(self):
        """ Resets the filewriter to its original state.
        
        :param : 
        :type: PyTango.DevVoid
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In InitializeFilewriter()")
        #----- PROTECTED REGION ID(EigerFilewriter.InitializeFilewriter) ENABLED START -----#

        self.filewriter.initialize()

        #----- PROTECTED REGION END -----#	//	EigerFilewriter.InitializeFilewriter
        

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
        'Clear':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'InitializeFilewriter':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'Mode':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Operation mode, can be enabled or disabled.",
            } ],
        'TransferMode':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Transfer mode. Currently only http is supported.",
            } ],
        'ImagesPerFile':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'min value': "1",
                'description': "Number of images stored in a single data file.",
            } ],
        'ImageNbStart':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "image_nr_low metadata parameter in the first HDF5 data file",
            } ],
        'FilenamePattern':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "The file naming pattern.",
            } ],
        'CompressionEnabled':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "True if the LZ4 data compression is enabled, False otherwise.",
            } ],
        'FilewriterState':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "The filewriter`s status. The status can be one of disabled,\nready, acquire, and error.",
            } ],
        'BufferFree':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "kB",
                'description': "Remaining buffer space in KB",
            } ],
        'FilewriterError':
            [[PyTango.DevString,
            PyTango.SPECTRUM,
            PyTango.READ, 10],
            {
                'description': "list of status parameters causing error state.",
            } ],
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
