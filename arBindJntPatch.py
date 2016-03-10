import maya.cmds as cmds

def createBindJoints():
    a1 = [u'Jaw', u'Head', u'NeckBase', u'R_Scapula', u'L_Scapula', u'Spine4', u'Spine3', u'Spine2', u'Root', u'Spine1', u'L_Hip', u'R_Hip', u'L_Knee', u'R_Knee', u'L_Ankle', u'R_Ankle', u'L_Ball', u'R_Ball'] 
    a2 = [u'L_Thumb2', u'L_Thumb1', u'L_Index3', u'L_Index2', u'L_Index1', u'L_Index0', u'L_Middle3', u'L_Middle2', u'L_Middle1', u'L_Middle0', u'L_Ring3', u'L_Ring2', u'L_Ring1', u'L_Ring0', u'L_Thumb0', u'R_Thumb2', u'R_Thumb1', u'R_Thumb0', u'R_Index3', u'R_Index2', u'R_Index1', u'R_Index0', u'R_Middle3', u'R_Middle2', u'R_Middle1', u'R_Middle0', u'R_Ring3', u'R_Ring2', u'R_Ring1', u'R_Ring0']
    a3 = [u'L_Bendy_Shoulder', u'L_Bendy_Shoulder_Bendy2', u'L_Bendy_Shoulder_Bendy4', u'L_Bendy_Elbow', u'L_Bendy_Elbow_Bendy2', u'L_Bendy_Elbow_Bendy4', u'L_Wrist', u'R_Bendy_Shoulder', u'R_Bendy_Shoulder_Bendy2', u'R_Bendy_Shoulder_Bendy4', u'R_Bendy_Elbow', u'R_Bendy_Elbow_Bendy2', u'R_Bendy_Elbow_Bendy3', u'R_Bendy_Elbow_Bendy5', u'R_Wrist'] 
    
    jnts = a1 + a2 + a3
    
    print jnts
    cmds.joint(n = 'abc', p = [0,0,0])
    for jnt in jnts:
        print jnt
        newJnt = cmds.joint(n = jnt + '_bnd_jnt', p = [0,0,0])
        cmds.select(jnt, r = True)
        cmds.select(newJnt, tgl = True)
        cmds.parentConstraint(mo = False, weight = 1)
        cmds.select(cl = True)
