import maya.cmds as cmds
import armSetup
reload(armSetup)

def armSetupRun():
    cmds.file(new = True, f = True)
    cmds.window( width=150 )
    cmds.columnLayout( adjustableColumn=True )
    cmds.button( label='Create Locator', command = armSetup.createLocator )
    cmds.button( label='Confirm Joints', command = armSetup.confirmJoints )
    cmds.button( label='Mirror Joints', command = armSetup.mirrorJoints )
    cmds.button( label='Arm setup', command = armSetup.armSetup )
    cmds.showWindow()