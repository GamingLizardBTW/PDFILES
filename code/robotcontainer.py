#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import logging
log = logging.Logger('P212-robot')
import wpilib
import commands2
from commands2.button import Trigger
from constants import OP
#from wpilib import XboxController
from wpilib import PS5Controller
from constants import ELEC

# Subsystems
import subsystems.FirstMotorSubsystem
import subsystems.SecondMotorSubsystem

# Commands
from commands.FirstMotorCommands import ForwardSpin, ReverseSpin, StopSpin
from commands.SecondMotorCommands import TriggerSpin


class RobotContainer:

    def __init__(self):
        # Controllers
        #self.Xbox = commands2.button.CommandXboxController(OP.joystick_port)
        self.PS5 = PS5Controller(OP.joystick_port)
        
        # Subsystems
        self.firstmotorsub = subsystems.FirstMotorSubsystem.FirstMotorSubsystemClass()
        self.secondmotorsub = subsystems.SecondMotorSubsystem.SecondMotorSubsystemClass()

        # Set default command for second motor (trigger-controlled)
        self.secondmotorsub.setDefaultCommand(
            TriggerSpin(self.secondmotorsub, self.PS5)
        )

        # Configure buttons for first motor
        self.configureButtonBindings()

    def configureButtonBindings(self):
        # Xbox controller example bindings (commented)
        # self.Xbox.leftBumper().onTrue(ForwardSpin(self.motorsub))
        # self.Xbox.leftBumper().onFalse(StopSpin(self.motorsub))
        # self.Xbox.rightBumper().onTrue(ReverseSpin(self.motorsub))
        # self.Xbox.rightBumper().onFalse(StopSpin(self.motorsub))
        
        # PS5 controller bindings
        # L1 button: first motor forward
        Trigger(lambda: self.PS5.getL1Button()).onTrue(ForwardSpin(self.firstmotorsub))
        Trigger(lambda: self.PS5.getL1Button()).onFalse(StopSpin(self.firstmotorsub))

        # R1 button: first motor reverse
        Trigger(lambda: self.PS5.getR1Button()).onTrue(ReverseSpin(self.firstmotorsub))
        Trigger(lambda: self.PS5.getR1Button()).onFalse(StopSpin(self.firstmotorsub))

        # Example for other buttons (X) if needed
        # Trigger(lambda: self.PS5.getCrossButton()).onTrue(SomeCommand(...))

    def all_subsystems(self):
        """
        Return every attribute of this RobotContainer which is an instance of
        a commands2.Subsystem subclass.
        """
        subsystems_list = []
        for attribute_name in dir(self):
            attribute = getattr(self, attribute_name)
            if isinstance(attribute, commands2.Subsystem):
                subsystems_list.append(attribute)
        return subsystems_list

    def get_autonomous_command(self):
        pass
