##deleteUI window ##

########Script Starts########
import maya.cmds as cmds
import os
import inspect 
import ar
reload(ar)

import colorPatch
import arArmAlignPatch
import arBindJntPatch
reload(arBindJntPatch)

######getting an image location######
inspect.getfile( inspect.currentframe() ) 
home = inspect.getfile( inspect.currentframe() )  

######image location#######
home = home[0:-14]
img = "%s/skeleton.jpg" %home    
print img

#self.numFingers = 4
#self.thumbYN = 'No'

class arExecute:
    def __init__(self):
            self.autoRigExecute = ar.Auto_Rig()
            self.stretchArm = 'False'
            self.stretchLeg = 'False'
            self.fkSpline = 'True'
            self.ikSpine = 'False'
            self.isTail = 'False'
            self.isHair = 'False'
            self.twistArm = 'False'
            
            self.thumbYN = 'No'
            self.numFingers = 4
             
            ############################################################	
            if cmds.window('autoRigUI', exists = True):
                    cmds.deleteUI('autoRigUI')
            
            ############################################################

            ##################
            ######################################
            autoRigGUI = cmds.window("autoRigUI", title = "auto Rig UI")
    
            form = cmds.formLayout(numberOfDivisions=100)
            
            ###attach image###
            pic = cmds.columnLayout()
            cmds.picture( image=img, enable = False )
            cmds.setParent('..')
    
            ###components###
            #layoutSpine = cmds.rowLayout( numberOfColumns=3, columnWidth3=(80, 75, 75), columnAlign=(1, 'right'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
            layoutSpine = cmds.columnLayout()
            #cmds.text('Spine')
            cmds.radioCollection()
            self.radioButtonFK = cmds.radioButton( label='FK Spine' , sl = True)
            self.radioButtonIK = cmds.radioButton( label='Stretch IK Spine')
            cmds.setParent('..')
            
            cmds.radioCollection()
            layoutArm = cmds.columnLayout( )
            self.radioButtonRegularFKIK = cmds.radioButton( label = 'Just FKIK Arm', sl = True)
            self.radiobuttonStretchArm = cmds.radioButton( label = 'Stretch Arm')
            self.radioButtonTwistArm = cmds.radioButton( label='Twist Arm')
            cmds.setParent('..')
            
            layoutThumb = cmds.rowLayout(numberOfColumns=1)
            self.checkBoxThumb = cmds.checkBox(label = 'Thumb', v = True)
            cmds.setParent('..')
            
            layoutFingers = cmds.rowColumnLayout(numberOfColumns=1)
            cmds.text(label='Number of Fingers')
            cmds.rowLayout(numberOfColumns=2)
            self.intFieldFinger = cmds.intField( minValue=1, maxValue=4, value=4, w = 15 )
            self.sliderFinger = cmds.intSlider( min=1, max=4, value=4, dc = self.fingerSlider) 
            cmds.setParent('..')
            cmds.setParent('..')
            
            layoutStretchLeg = cmds.rowLayout( numberOfColumns=1)
            self.checkBoxStretchLeg = cmds.checkBox( label='Stretch Leg')
            cmds.setParent('..')
            
            layoutTail = cmds.rowLayout( numberOfColumns=1)
            self.checkBoxTail = cmds.checkBox( label='Tail')
            cmds.setParent('..')
    
            layoutHair = cmds.rowLayout( numberOfColumns=1)
            self.checkBoxHair = cmds.checkBox( label='Hair')
            cmds.setParent('..')
            
            layoutButtons = cmds.columnLayout(adj=True)
            cmds.button(en = 1, l = 'Create', c = self.createJoint)
            cmds.button(en = 1, l = 'Confirm Joint', c = self.confirmJoint)
            cmds.button(en = 1, l = 'Make Controllers', c = self.confirmCTRL)
            cmds.setParent('..')
            
            cmds.formLayout( form, edit=True, attachForm=[(pic, 'top', 0)] ) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutButtons, 'top', 380),(layoutButtons, 'left', 556)]) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutSpine, 'top', 240),(layoutSpine, 'left', 370)]) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutArm, 'top', 150),(layoutArm, 'left', 450)]) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutThumb, 'top', 390),(layoutThumb, 'left', 150)]) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutFingers, 'top', 410),(layoutFingers, 'left', 120)]) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutStretchLeg, 'top', 420),(layoutStretchLeg, 'left', 400)]) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutTail, 'top', 300),(layoutTail, 'left', 130)]) 
            cmds.formLayout( form, edit=True, attachForm=[(layoutHair, 'top', 15),(layoutHair, 'left', 270)]) 
            
            cmds.showWindow(autoRigGUI)

    def createJoint(self, *arg):
            ##Thumb YN##
            thumbStatus = cmds.checkBox(self.checkBoxThumb, v = True,q = True)
            print 'Thumb stateus = %s' %thumbStatus
            if thumbStatus == True:
                    self.thumbYN = 'Yes'
            elif thumbStatus == False:
                    self.thumbYN = 'No'
            print self.thumbYN
            
            ###NO Fingers##
            self.numFingers = cmds.intField(self.intFieldFinger, q = True, v = True)
            
            #self.autoRigExecute.placeRootJoints()
            #self.autoRigExecute.placeSpineJoints()
            #self.autoRigExecute.placeLegJoints()
            #self.autoRigExecute.placeArmJoints()
            self.autoRigExecute.placeJoints()
            self.autoRigExecute.placeFingerJoints(self.numFingers, self.thumbYN)
            
            self.isTail = cmds.checkBox(self.checkBoxTail, v = True,q = True)
            if self.isTail == True:
                    self.autoRigExecute.placeTailJoints()	
            
            self.isHair = cmds.checkBox(self.checkBoxHair, v = True,q = True)
            if self.isHair == True:
                    self.autoRigExecute.Hair_Joints()	
    
    def confirmJoint(self, *arg):
            thumbStatus = cmds.checkBox(self.checkBoxThumb, v = True,q = True)
            print 'Thumb stateus = %s' %thumbStatus
            if thumbStatus == True:
                    self.thumbYN = 'Yes'
            elif thumbStatus == False:
                    self.thumbYN = 'No'
            print self.thumbYN
    
            ###NO Fingers##
            self.numFingers = cmds.intField(self.intFieldFinger, q = True, v = True)
            
            self.autoRigExecute.confirmJoints(self.numFingers, self.thumbYN)
            self.autoRigExecute.orientJoints(self.numFingers, self.thumbYN)
    
            self.isTail = cmds.checkBox(self.checkBoxTail, v = True,q = True)
            if self.isTail == True:
                    self.autoRigExecute.tailConfirm()	
    
            self.isHair = cmds.checkBox(self.checkBoxHair, v = True,q = True)
            if self.isHair == True:
                    self.autoRigExecute.Hair_Confirm()	
                    
    def confirmCTRL(self, *arg):
            thumbStatus = cmds.checkBox(self.checkBoxThumb, v = True,q = True)
            print 'Thumb stateus = %s' %thumbStatus
            if thumbStatus == True:
                    self.thumbYN = 'Yes'
            elif thumbStatus == False:
                    self.thumbYN = 'No'
            print self.thumbYN
    
            ###NO Fingers##
            self.numFingers = cmds.intField(self.intFieldFinger, q = True, v = True)
            
            self.autoRigExecute.makeControllers()
            self.autoRigExecute.legSetting()
            self.autoRigExecute.fkLegSetting()
            self.autoRigExecute.spineSetting()
            self.twistArm = cmds.radioButton(self.radioButtonTwistArm, sl = True,q = True) 
            self.autoRigExecute.armSetting(self.twistArm)
            self.autoRigExecute.fingerSetting(self.numFingers, self.thumbYN)
            self.autoRigExecute.parenting()
                    
            self.stretchArm = cmds.radioButton(self.radiobuttonStretchArm, sl = True,q = True)
            if self.stretchArm == True:
                    self.autoRigExecute.bendyArm()
                    self.autoRigExecute.stretchIkArm()
                    #self.autoRigExecute.individualStretchArm()
            
            
            self.stretchLeg = cmds.checkBox(self.checkBoxStretchLeg, v = True,q = True)
            if self.stretchLeg == True:
                    self.autoRigExecute.bendyLeg()
                    self.autoRigExecute.stretchIkLeg()
    
            
            ##HeadWorld##
            self.autoRigExecute.head_Orientation_Setting()
            
            ##Stretch Spine##
            self.fkSpline = cmds.radioButton(self.radioButtonFK, q = True, sl = True)
            self.ikSpine = cmds.radioButton(self.radioButtonIK, q = True, sl = True)
            if self.ikSpine == True:
                    self.autoRigExecute.stretchIkSpine()
    
            ##Tail##
            self.isTail = cmds.checkBox(self.checkBoxTail, v = True,q = True)
            if self.isTail == True:
                    self.autoRigExecute.fkTailSetup()	
                    self.autoRigExecute.ikTailSetup()	
                    self.autoRigExecute.fkikTailSetup()
    
            ##Hair##
            self.isHair = cmds.checkBox(self.checkBoxHair, v = True,q = True)
            if self.isHair == True:
                    self.autoRigExecute.FK_Hair_Settup()	
                    self.autoRigExecute.IK_Hair_Settup()	
                    self.autoRigExecute.FKIK_Hair_Settup()
                    
            ##Twist Arm##
            if self.twistArm == True:
                    self.autoRigExecute.twistArm(self.stretchArm)		
                    cmds.select(cl = True)
            
            ##colorPatch
            colorPatch.colorPatch()
            
            ##arm align patch
            arArmAlignPatch.armAlignPatch()
            
            ##bind joint patch
            #arBindJntPatch.createBindJoints()
    
    def fingerSlider(self):
            sliderVal = cmds.intSlider(fingerSlider, v = True, q = True)
            cmds.intField(self.intFieldFinger, e = True, v = sliderVal)
                

x = arExecute()
