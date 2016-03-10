import maya.cmds as cmds
import controller as ct
import partDic
reload(ct)
import poleVector
reload(poleVector)

armSet = partDic.armSet
lrPrefix = ['l_', 'r_']

def createController(name):
    cmds.createNode('transform', n = '%s_grp' %name)
    cmds.circle(n = name)
    cmds.select(name, r = True)
    cmds.select('%s_grp' %name, tgl = True)
    cmds.parent()
    
def createLocator(*arg):
        #- create locator in default position
        
    for oneSet in armSet:
        if cmds.objExists('%s_loc' %oneSet[0]):
            cmds.delete('%s_loc' %oneSet[0])
        cmds.spaceLocator(n = '%s_loc' %oneSet[0])
        cmds.xform('%s_loc' %oneSet[0], t = oneSet[1])

       
def confirmJoints(*arg):
        
    #- draw joints in locator position      
    cmds.select(cl = True) 
    for oneSet in armSet :
        jointPos = cmds.xform('%s_loc' %oneSet[0], t = True, q = True, ws = True)
        cmds.joint(n = 'l_%s_jnt' %oneSet[0], p = jointPos)
        
        #- orient joint
        cmds.joint('l_shoulder_jnt', e = True, oj = 'xzy', secondaryAxisOrient = 'yup', ch = True, zso = True)
        
    for oneSet in armSet :
        cmds.delete('%s_loc' %oneSet[0])
                
def mirrorJoints(*arg):
        
    #-mirroring joints
    cmds.select(cl = True)
    cmds.joint(n = 'root_jnt')
    cmds.select('l_shoulder_jnt', r = True)
    cmds.select('root_jnt', tgl = True)
    cmds.parent()
    
    cmds.select('l_shoulder_jnt', r = True)
    cmds.mirrorJoint(mirrorYZ = True, mirrorBehavior  = True, searchReplace =  ['l_', 'r_'])
    
    cmds.select('l_shoulder_jnt', 'r_shoulder_jnt')
    cmds.parent(w = True)
    
    cmds.delete('root_jnt')

def armSetup(*arg):
    fkArmSetup()
    ikArmSetup()
    fkikCombine()

def fkArmSetup():

    #- fk arm setup
    cmds.select(cl = True)
    for lr in lrPrefix:
            cmds.select('%sshoulder_jnt' %lr, r = True)
            cmds.duplicate(rr = True, n = '%sfk_shoulder_jnt' %lr)          
            armChild = cmds.listRelatives('%sfk_shoulder_jnt' %lr, ad = True, f = True)
            print armChild
            
            cmds.rename(armChild[0], '%sfk_wrist_jnt' %lr )
            cmds.rename(armChild[1], '%sfk_elbow_jnt' %lr )                 
    
            for oneset in armSet:
                    if lr == 'l_':
                            cntColor = 6
                    else:
                            cntColor = 12
                    cnt = ct.circleController('%sfk_%s_cnt' %(lr, oneset[0]), 'yz', 2, cntColor, ['tr', 'sc', 'vi'])
                    cmds.select('%s%s_jnt' %(lr, oneset[0]), r = True)
                    cmds.select('%s_grp' %cnt, tgl = True)
                    cmds.pointConstraint(mo = False, weight = 1)
                    cmds.orientConstraint(mo = False, weight = 1)
                    cmds.delete('%s_grp_pointConstraint1' %cnt)
                    cmds.delete('%s_grp_orientConstraint1' %cnt)            
            
                    #- constrain joints
                    cmds.select(cnt, r = True)
                    cmds.select('%sfk_%s_jnt' %(lr, oneset[0]), tgl = True)
                    cmds.orientConstraint(mo = False, weight = 1)
    
            #- parent controls
            cmds.select('%sfk_wrist_cnt_grp' %lr, r = True)
            cmds.select('%sfk_elbow_cnt' %lr, tgl = True)
            cmds.parent()   

            cmds.select('%sfk_elbow_cnt_grp' %lr, r = True)
            cmds.select('%sfk_shoulder_cnt' %lr, tgl = True)
            cmds.parent()                   

def ikArmSetup():
    #- fk arm setup
    
    cmds.select(cl = True)
    for lr in lrPrefix:
        cmds.select('%sshoulder_jnt' %lr, r = True)
        cmds.duplicate(rr = True, n = '%sik_shoulder_jnt' %lr)          
        armChild = cmds.listRelatives('%sik_shoulder_jnt' %lr, ad = True, f = True)
        print armChild
        
        cmds.rename(armChild[0], '%sik_wrist_jnt' %lr )
        cmds.rename(armChild[1], '%sik_elbow_jnt' %lr ) 
        
        if lr == 'l_':
                cntColor = 6
        else:
                cntColor = 12
        ct.boxController('%sarm_ik_cnt' %lr, cntColor, ['sc', 'vi'])
        ct.arrowController('%sarm_polevector_cnt' %lr, cntColor, ['ro', 'sc', 'vi'])

        cmds.select('%sik_wrist_jnt' %lr, r = True)
        cmds.select('%sarm_ik_cnt_grp' %lr, tgl = True)
        cmds.pointConstraint(mo = False, weight = 1)
        cmds.orientConstraint(mo = False, weight = 1)
        cmds.delete('%sarm_ik_cnt_grp_pointConstraint1' %lr)
        cmds.delete('%sarm_ik_cnt_grp_orientConstraint1' %lr)
        
        cmds.select('%sik_shoulder_jnt.rotatePivot' %lr, r = True)
        cmds.select('%sik_wrist_jnt.rotatePivot' %lr, add = True)
        cmds.ikHandle(n = '%sarm_ikHandle' %lr, sol = 'ikRPsolver')             
        
        cmds.select('%sarm_ikHandle' %lr, r = True)
        cmds.select('%sarm_ik_cnt' %lr, tgl = True)
        cmds.parent()
        
        polVecPos = poleVector.getPolVectorPos('%sik_shoulder_jnt' %lr, '%sik_elbow_jnt' %lr, '%sik_wrist_jnt' %lr, 1)
        cmds.select('%sarm_polevector_cnt_grp' %lr, r = True)
        cmds.move(polVecPos[0], polVecPos[1], polVecPos[2])
        
        cmds.select('%sarm_polevector_cnt' %lr, r = True)
        cmds.select('%sarm_ikHandle' %lr, tgl = True)
        cmds.poleVectorConstraint(weight = 1)

def fkikCombine():
    #fkik arm combine
    
    cmds.select(cl = True)
    
    for lr in lrPrefix:
        # creating extra Control
        if lr == 'l_':
                cntColor = 6
        else:
                cntColor = 12
        ct.extraController('%sarm_extra_cnt' %lr, cntColor, ['tr', 'ro', 'sc', 'vi'])
        
        #- add Extra attributes
        cmds.addAttr('%sarm_extra_cnt' %lr, ln = 'FKIK', at = 'double', min = 0, max = 1)
        cmds.setAttr('%sarm_extra_cnt.FKIK' %lr, e = True, keyable = True)              
        
        cmds.select('%sarm_extra_cnt_grp' %lr, tgl = True)
        cmds.parent()
        cmds.select('%sarm_extra_cnt_grp' %lr, r = True)
        extraCntPos = cmds.xform('%swrist_jnt' %lr, t = True, q = True, ws = True)
        cmds.move(extraCntPos[0], extraCntPos[1], extraCntPos[2] -2)

        cmds.select('%swrist_jnt' %lr, r = True)
        cmds.select('%sarm_extra_cnt_grp' %lr, tgl = True)
        cmds.parentConstraint(mo = True, weight = 1)    
        
        #- rotate
        cmds.shadingNode('blendColors', n = '%sFKIK_Arm_Mux' %lr, asUtility = True)
        cmds.connectAttr('%sarm_extra_cnt.FKIK' %lr, '%sFKIK_Arm_Mux.blender' %lr, f = True)

        cmds.setAttr('%sFKIK_Arm_Mux.color1R' %lr, 1)
        cmds.setAttr('%sFKIK_Arm_Mux.color2R' %lr, 0)
        cmds.setAttr('%sFKIK_Arm_Mux.color1G' %lr, 0)
        cmds.setAttr('%sFKIK_Arm_Mux.color2G' %lr, 1)

        for oneSet  in armSet:
                cmds.select('%sfk_%s_jnt' %(lr, oneSet[0]), r = True)
                cmds.select('%s%s_jnt' %(lr, oneSet[0]), tgl = True)
                cmds.orientConstraint(mo = False, weight =1)

                cmds.select('%sik_%s_jnt' %(lr, oneSet[0]), r = True)
                cmds.select('%s%s_jnt' %(lr, oneSet[0]), tgl = True)
                cmds.orientConstraint(mo = False, weight =1)
                
                cmds.connectAttr('%sFKIK_Arm_Mux.outputR' %lr, '%s%s_jnt_orientConstraint1.%sik_%s_jntW1' %(lr, oneSet[0], lr, oneSet[0]))
                cmds.connectAttr('%sFKIK_Arm_Mux.outputG' %lr, '%s%s_jnt_orientConstraint1.%sfk_%s_jntW0' %(lr, oneSet[0], lr, oneSet[0]))
                
        cmds.connectAttr('%sFKIK_Arm_Mux.outputG' %lr, '%sfk_shoulder_cnt_grp.visibility' %lr)
        cmds.connectAttr('%sFKIK_Arm_Mux.outputR' %lr, '%sarm_ik_cnt_grp.visibility' %lr)
        cmds.connectAttr('%sFKIK_Arm_Mux.outputR' %lr, '%sarm_polevector_cnt_grp.visibility' %lr)       
        
        cmds.setAttr('%sfk_shoulder_jnt.visibility' %lr, 0)
        cmds.setAttr('%sik_shoulder_jnt.visibility' %lr, 0)             
        
        cmds.createNode('transform', n = '%sfkik_arm_jnt_grp' %lr)
        
        cmds.select('%sfk_shoulder_jnt' %lr, r = True)
        cmds.select('%sik_shoulder_jnt' %lr, add = True)
        cmds.select('%sfkik_arm_jnt_grp' %lr, tgl = True)
        cmds.parent()
                
                        
                        